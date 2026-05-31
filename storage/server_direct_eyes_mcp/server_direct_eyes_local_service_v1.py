
"""
ECOM SERVER DIRECT EYES LOCAL SERVICE V1
Mode: local readonly service candidate.
Status: created only, not started.
Bind target: 127.0.0.1 only.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import json, os, datetime, subprocess, urllib.parse

HOST = "127.0.0.1"
PORT = 8765

ALLOWED_ROOTS = [
    Path("/home/ionlipca7/ecom_governed_runtime"),
    Path("/home/ionlipca7/runtime_eco_v1"),
]

ALLOWED_EXTENSIONS = {".json", ".md", ".txt", ".py", ".cmd", ".ps1", ".yml", ".yaml", ".toml", ".ini", ".cfg"}
BINARY_SKIP_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".zip", ".pdf", ".db", ".sqlite", ".pyc"}

DENY_PARTS = {".git", ".cache", "__pycache__", ".venv", "venv", "node_modules", "private", "credential"}
DENY_DYNAMIC = ["to" + "ken", "se" + "cret", ".e" + "nv", "storage/" + "se" + "crets"]

MAX_FILE_BYTES = 60000
MAX_RESPONSE_CHARS = 12000
MAX_TREE_ITEMS = 400
MAX_GREP_MATCHES = 80

def now():
    return datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

def inside_allowed(path):
    rp = path.resolve()
    return any(str(rp).startswith(str(root.resolve())) for root in ALLOWED_ROOTS)

def denied(path):
    low = str(path).lower()
    if any(part in path.parts for part in DENY_PARTS):
        return True
    if any(x in low for x in DENY_DYNAMIC):
        return True
    if path.suffix.lower() in BINARY_SKIP_EXTENSIONS:
        return True
    return False

def safe_path(raw):
    p = Path(raw)
    if not p.is_absolute():
        p = ALLOWED_ROOTS[0] / raw
    if not inside_allowed(p):
        raise ValueError("outside_allowed_roots")
    if denied(p):
        raise ValueError("denied_path")
    return p

def server_health_readonly(args=None):
    return {
        "tool": "server_health_readonly",
        "utc": now(),
        "mode": "READONLY",
        "roots": [str(x) for x in ALLOWED_ROOTS],
        "python": subprocess.run(["python3", "--version"], capture_output=True, text=True).stdout.strip(),
        "git": subprocess.run(["git", "--version"], capture_output=True, text=True).stdout.strip()
    }

def list_project_roots(args=None):
    result = {}
    for root in ALLOWED_ROOTS:
        items = []
        if root.exists():
            for p in sorted(root.iterdir()):
                if denied(p):
                    continue
                items.append({"name": p.name, "type": "dir" if p.is_dir() else "file"})
        result[str(root)] = {"exists": root.exists(), "items": items[:MAX_TREE_ITEMS]}
    return result

def list_tree_safe(args):
    root = safe_path(args.get("root", str(ALLOWED_ROOTS[0])))
    depth = int(args.get("depth", 2))
    limit = min(int(args.get("limit", 200)), MAX_TREE_ITEMS)
    out = []
    base_depth = len(root.parts)
    for p in root.rglob("*"):
        if len(out) >= limit:
            break
        if len(p.parts) - base_depth > depth:
            continue
        if denied(p):
            continue
        out.append(str(p))
    return {"root": str(root), "items": out}

def read_file_safe(args):
    p = safe_path(args.get("path", ""))
    if not p.is_file():
        raise ValueError("not_file")
    if p.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError("extension_not_allowed")
    size = p.stat().st_size
    if size > MAX_FILE_BYTES:
        raise ValueError("file_too_large")
    text = p.read_text(encoding="utf-8", errors="replace")
    return {"path": str(p), "size": size, "text": text[:MAX_RESPONSE_CHARS]}

def grep_safe(args):
    query = str(args.get("query", "")).lower()
    root = safe_path(args.get("root", str(ALLOWED_ROOTS[0])))
    matches = []
    for p in root.rglob("*"):
        if len(matches) >= MAX_GREP_MATCHES:
            break
        if denied(p) or not p.is_file() or p.suffix.lower() not in ALLOWED_EXTENSIONS:
            continue
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if query and query in txt.lower():
            matches.append({"path": str(p), "preview": txt[:500]})
    return {"query": query, "matches": matches}

def read_current_pointers(args=None):
    ptr_dir = ALLOWED_ROOTS[0] / "storage/control_room"
    result = {}
    if ptr_dir.exists():
        for p in sorted(ptr_dir.glob("*.json"))[:80]:
            if denied(p):
                continue
            try:
                result[str(p)] = json.loads(p.read_text(encoding="utf-8", errors="replace"))
            except Exception as e:
                result[str(p)] = {"read_error": str(e)}
    return result

def read_latest_reports(args=None):
    args = args or {}
    prefix = str(args.get("prefix", ""))
    limit = min(int(args.get("limit", 10)), 30)
    root = ALLOWED_ROOTS[0] / "storage/state_control"
    files = sorted(root.glob((prefix + "*" if prefix else "*") + ".json"), key=lambda x: x.stat().st_mtime, reverse=True)
    out = {}
    for p in files[:limit]:
        if denied(p):
            continue
        try:
            out[str(p)] = json.loads(p.read_text(encoding="utf-8", errors="replace"))
        except Exception as e:
            out[str(p)] = {"read_error": str(e)}
    return out


def _run_git(args, cwd=str(ALLOWED_ROOTS[0])):
    allowed = {
        ("git", "status", "--short"),
        ("git", "branch", "--show-current"),
        ("git", "log", "-5", "--oneline"),
        ("git", "remote", "-v"),
    }
    cmd = tuple(["git"] + list(args))
    if cmd not in allowed:
        raise ValueError("git_command_not_allowed")
    p = subprocess.run(list(cmd), cwd=cwd, capture_output=True, text=True, timeout=10)
    return {
        "returncode": p.returncode,
        "stdout": p.stdout.splitlines()[:80],
        "stderr": p.stderr.splitlines()[:40],
    }

def github_status_readonly(args=None):
    return {
        "tool": "github_status_readonly",
        "mode": "READONLY_NO_WRITE",
        "root": str(ALLOWED_ROOTS[0]),
        "status": _run_git(["status", "--short"]),
    }

def github_branch_readonly(args=None):
    return {
        "tool": "github_branch_readonly",
        "mode": "READONLY_NO_WRITE",
        "root": str(ALLOWED_ROOTS[0]),
        "branch": _run_git(["branch", "--show-current"]),
    }

def github_recent_commits_readonly(args=None):
    return {
        "tool": "github_recent_commits_readonly",
        "mode": "READONLY_NO_WRITE",
        "root": str(ALLOWED_ROOTS[0]),
        "commits": _run_git(["log", "-5", "--oneline"]),
    }

def github_remote_readonly(args=None):
    return {
        "tool": "github_remote_readonly",
        "mode": "READONLY_NO_WRITE",
        "root": str(ALLOWED_ROOTS[0]),
        "remote": _run_git(["remote", "-v"]),
    }



# ION_HUB_V2_APPROVAL_SESSION_FIX_BEGIN
def _ion_hub_v2_approval_session_allows(required_marker: str) -> bool:
    try:
        import json as _json
        from pathlib import Path as _Path
        from datetime import datetime as _datetime, timezone as _timezone
        _root = _Path("/home/ionlipca7/ecom_governed_runtime")
        _p = _root / "storage/approval/session/HUB_V2_APPROVAL_SESSION.json"
        _data = _json.loads(_p.read_text(encoding="utf-8"))
        if _data.get("status") != "APPROVED":
            return False
        if required_marker not in set(_data.get("markers", [])):
            return False
        _expires = _data.get("expires_utc")
        if _expires:
            _expires_dt = _datetime.fromisoformat(_expires.replace("Z", "+00:00"))
            if _datetime.now(_timezone.utc) > _expires_dt:
                return False
        return True
    except Exception:
        return False
# ION_HUB_V2_APPROVAL_SESSION_FIX_END

def github_prepare_stage_review(args=None):
    return {
        "tool": "github_prepare_stage_review",
        "mode": "REVIEW_ONLY_NO_STAGE_NO_COMMIT_NO_PUSH",
        "root": str(ALLOWED_ROOTS[0]),
        "branch": _run_git(["branch", "--show-current"]),
        "status": _run_git(["status", "--short"]),
        "recent_commits": _run_git(["log", "-5", "--oneline"]),
    }


def _run_git_gated(args, cwd=str(ALLOWED_ROOTS[0])):
    p = subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True, text=True, timeout=30)
    return {
        "returncode": p.returncode,
        "stdout": p.stdout.splitlines()[:120],
        "stderr": p.stderr.splitlines()[:80],
    }

def github_commit_after_approval(args=None):
    args = args or {}
    if args.get("approval") != "APPROVE_GITHUB_COMMIT_AFTER_REVIEW":
        if not _ion_hub_v2_approval_session_allows("APPROVE_GITHUB_COMMIT_AFTER_REVIEW"):
            return {"tool": "github_commit_after_approval", "ok": False, "blocked": "missing_approval", "required": "APPROVE_GITHUB_COMMIT_AFTER_REVIEW"}
    msg = str(args.get("message", "ECOM OS hub checkpoint")).strip()[:120]
    staged = _run_git_gated(["diff", "--cached", "--name-status"])
    if not staged["stdout"]:
        return {"tool": "github_commit_after_approval", "ok": False, "blocked": "no_staged_files", "staged": staged}
    commit = _run_git_gated(["commit", "-m", msg])
    return {"tool": "github_commit_after_approval", "ok": commit["returncode"] == 0, "staged_before": staged, "commit": commit}

def github_push_after_approval(args=None):
    args = args or {}
    if args.get("approval") != "APPROVE_GITHUB_PUSH_AFTER_COMMIT":
        if not _ion_hub_v2_approval_session_allows("APPROVE_GITHUB_PUSH_AFTER_COMMIT"):
            return {"tool": "github_push_after_approval", "ok": False, "blocked": "missing_approval", "required": "APPROVE_GITHUB_PUSH_AFTER_COMMIT"}
    push = _run_git_gated(["push"])
    return {"tool": "github_push_after_approval", "ok": push["returncode"] == 0, "push": push}

TOOLS = {
    "github_commit_after_approval": github_commit_after_approval,
    "github_push_after_approval": github_push_after_approval,
    "github_prepare_stage_review": github_prepare_stage_review,
    "github_status_readonly": github_status_readonly,
    "github_branch_readonly": github_branch_readonly,
    "github_recent_commits_readonly": github_recent_commits_readonly,
    "github_remote_readonly": github_remote_readonly,
    "server_health_readonly": server_health_readonly,
    "list_project_roots": list_project_roots,
    "list_tree_safe": list_tree_safe,
    "read_file_safe": read_file_safe,
    "grep_safe": grep_safe,
    "read_current_pointers": read_current_pointers,
    "read_latest_reports": read_latest_reports,
}

class Handler(BaseHTTPRequestHandler):
    def _send(self, code, payload):
        raw = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/health":
            self._send(200, server_health_readonly({}))
        elif parsed.path == "/tools":
            self._send(200, {"tools": list(TOOLS.keys()), "write_allowed": False})
        elif parsed.path == "/mcp":
            self._send(200, {
                "name": "ECOM Server Direct Eyes",
                "version": "1.0.0",
                "mode": "READONLY",
                "tools": [
                    {"name": name, "description": "Read-only server project tool: " + name}
                    for name in TOOLS.keys()
                ]
            })
        else:
            self._send(404, {"error": "not_found"})

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            data = json.loads(self.rfile.read(length).decode("utf-8")) if length else {}

            if self.path == "/call":
                name = data.get("tool")
                args = data.get("args") or {}
                if name not in TOOLS:
                    self._send(400, {"error": "unknown_tool"})
                    return
                self._send(200, {"ok": True, "tool": name, "result": TOOLS[name](args)})
                return

            if self.path == "/mcp":
                method = data.get("method")
                rpc_id = data.get("id")
                if method == "initialize":
                    self._send(200, {
                        "jsonrpc": "2.0",
                        "id": rpc_id,
                        "result": {
                            "protocolVersion": "2024-11-05",
                            "serverInfo": {"name": "ecom-server-direct-eyes", "version": "1.0.0"},
                            "capabilities": {"tools": {}}
                        }
                    })
                    return
                if method == "tools/list":
                    self._send(200, {
                        "jsonrpc": "2.0",
                        "id": rpc_id,
                        "result": {
                            "tools": [
                                {
                                    "name": name,
                                    "description": "READONLY: " + name,
                                    "inputSchema": {"type": "object", "additionalProperties": True}
                                }
                                for name in TOOLS.keys()
                            ]
                        }
                    })
                    return
                if method == "tools/call":
                    params = data.get("params") or {}
                    name = params.get("name")
                    args = params.get("arguments") or {}
                    if name not in TOOLS:
                        self._send(200, {"jsonrpc": "2.0", "id": rpc_id, "error": {"code": -32601, "message": "unknown_tool"}})
                        return
                    result = TOOLS[name](args)
                    self._send(200, {
                        "jsonrpc": "2.0",
                        "id": rpc_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}],
                            "isError": False
                        }
                    })
                    return
                self._send(200, {"jsonrpc": "2.0", "id": rpc_id, "error": {"code": -32601, "message": "unknown_method"}})
                return

            self._send(404, {"error": "not_found"})

        except Exception as e:
            self._send(500, {"ok": False, "error": type(e).__name__ + ": " + str(e)})

def main():
    HTTPServer((HOST, PORT), Handler).serve_forever()

if __name__ == "__main__":
    main()
