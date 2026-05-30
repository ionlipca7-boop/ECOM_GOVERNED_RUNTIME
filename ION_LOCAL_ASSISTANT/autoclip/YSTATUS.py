from pathlib import Path
import subprocess
import datetime

ROOT = Path(r"D:\ECOM_GOVERNED_RUNTIME")
OUT = ROOT / "storage" / "state_control" / "ION_AUTOCLIP_YSTATUS_LATEST.txt"

def run(cmd, cwd=ROOT, timeout=20):
    try:
        p = subprocess.run(cmd, cwd=str(cwd), shell=True, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()
    except Exception as e:
        return 999, "", repr(e)

def one(cmd, default=""):
    rc, out, err = run(cmd)
    if rc == 0 and out:
        return out.splitlines()[0].strip()
    return default

def count_dirty():
    rc, out, err = run("git status --porcelain")
    if rc != 0:
        return "UNKNOWN"
    if not out.strip():
        return "0"
    return str(len([x for x in out.splitlines() if x.strip()]))

def status_line(name, value):
    value = "" if value is None else str(value)
    value = value.replace("\r", " ").replace("\n", " ")[:500]
    return f"{name}={value}"

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("ION_AUTO:ECOM_WORKSPACE_STATUS_V2")
    lines.append(status_line("UTC", datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")))
    lines.append(status_line("LOCAL_WORKSPACE", "PASS" if ROOT.exists() else "BLOCK"))
    lines.append(status_line("ROOT", ROOT))
    lines.append(status_line("SERVER_MARKER_EXPECTED", "ION_AUTO:SERVER_READONLY_STATUS_V1"))
    lines.append(status_line("SERVER_DIRECT_EYES_CHATGPT", "CHECK_IN_CHAT"))

    rc, out, err = run("git rev-parse --is-inside-work-tree")
    lines.append(status_line("GIT_LOCAL", "PASS" if rc == 0 else "BLOCK"))
    lines.append(status_line("GIT_BRANCH", one("git branch --show-current", "UNKNOWN")))
    lines.append(status_line("GIT_HEAD", one("git rev-parse --short HEAD", "UNKNOWN")))
    lines.append(status_line("GIT_LAST_COMMIT", one("git log -1 --pretty=%s", "UNKNOWN")))
    lines.append(status_line("GIT_DIRTY_COUNT", count_dirty()))

    rc, out, err = run("git remote get-url origin")
    lines.append(status_line("GIT_REMOTE_ORIGIN", out if rc == 0 else "BLOCK"))

    rc, out, err = run("git ls-remote --heads origin")
    lines.append(status_line("GITHUB_REMOTE_READ", "PASS" if rc == 0 else "BLOCK"))

    rc, out, err = run("gh auth status")
    lines.append(status_line("GH_AUTH", "PASS" if rc == 0 else "BLOCK_OR_NOT_INSTALLED"))

    ngrok_json = ROOT / "NGROK_EYES_TUNNELS.json"
    lines.append(status_line("NGROK_TUNNELS_FILE", "PRESENT" if ngrok_json.exists() else "MISSING"))

    lines.append(status_line("CURRENT_CONFIRMED_POINTER", "R100_TELEGRAM_V72_NEW_PRODUCT_INTAKE_RECEIPT_FIX_VERIFIED_POINTER"))
    lines.append(status_line("NEXT", "CONTINUE_FROM_VERIFIED_NEW_PRODUCT_CASE_TO_PRODUCT_NORMALIZATION_OR_DRAFT_GATE_NO_EBAY"))
    lines.append(status_line("NO_EBAY_LIVE", "true"))
    lines.append(status_line("NO_SERVER_WRITE", "true"))
    lines.append(status_line("NO_GIT_PUSH", "true"))

    text = "\r\n".join(lines) + "\r\n"
    OUT.write_text(text, encoding="utf-8")

    clip = subprocess.run("clip", input=text, text=True, shell=True)
    print(text, end="")
    print(status_line("COPIED_TO_CLIPBOARD", "true" if clip.returncode == 0 else "false"))
    print(status_line("OUT", OUT))

if __name__ == "__main__":
    main()
