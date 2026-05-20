import json
import subprocess
from datetime import datetime
from pathlib import Path

BLOCKED_WORDS = [
    "delete", "del ", "erase", "remove", "rmdir", "rd ",
    "publish", "revise", "send", "token", ".env", "secret",
    "server", "ssh", "scp", "git push", "git add", "git commit"
]

REVIEW_WORDS = [
    "move", "rename", "replace", "overwrite", "cleanup", "copy"
]

def main():
    base = Path(__file__).resolve().parent.parent
    repo_root = base.parent
    pending = base / "storage" / "pending_cmd" / "last_cmd_from_chatgpt.txt"
    reports = base / "storage" / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    report_file = reports / "approve_run_pending_cmd_v1.json"

    if not pending.exists():
        result = {
            "generated_at": datetime.now().isoformat(),
            "mode": "MANUAL_APPROVE_RUN",
            "decision": "BLOCKED",
            "reason": "pending command file not found",
            "pending_file": str(pending)
        }
        report_file.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print("BLOCKED: pending command file not found")
        print(report_file)
        return 1

    cmd = pending.read_text(encoding="utf-8", errors="replace").strip()
    lower = cmd.lower()

    decision = "APPROVED_TO_RUN"
    allowed_now = True
    reason = "Manual approval runner. Command passed basic safety check."

    if not cmd:
        decision = "BLOCKED"
        allowed_now = False
        reason = "Empty pending command."

    if allowed_now and any(word in lower for word in BLOCKED_WORDS):
        decision = "BLOCKED_OR_APPROVAL_REQUIRED"
        allowed_now = False
        reason = "High-risk word detected. Manual runner refuses this command."

    if allowed_now and any(word in lower for word in REVIEW_WORDS):
        decision = "REVIEW_REQUIRED"
        allowed_now = False
        reason = "File-changing word detected. Dry-run report required first."

    result = {
        "generated_at": datetime.now().isoformat(),
        "mode": "MANUAL_APPROVE_RUN",
        "pending_file": str(pending),
        "command": cmd,
        "decision": decision,
        "allowed_now": allowed_now,
        "reason": reason,
        "returncode": None,
        "stdout": "",
        "stderr": ""
    }

    if not allowed_now:
        report_file.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(decision)
        print(reason)
        print(report_file)
        return 2

    print("================================")
    print("ION APPROVE RUN PENDING CMD V1")
    print("MODE: MANUAL_APPROVED")
    print("================================")
    print("COMMAND:")
    print(cmd)
    print()

    run = subprocess.run(
        cmd,
        shell=True,
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    result["returncode"] = run.returncode
    result["stdout"] = run.stdout
    result["stderr"] = run.stderr

    report_file.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print("RETURN CODE:", run.returncode)
    print("STDOUT:")
    print(run.stdout)
    print("STDERR:")
    print(run.stderr)
    print("REPORT:")
    print(report_file)

    return run.returncode

if __name__ == "__main__":
    raise SystemExit(main())
