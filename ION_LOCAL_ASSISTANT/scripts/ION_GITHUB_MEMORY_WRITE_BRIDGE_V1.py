from pathlib import Path
from datetime import datetime, timezone
import subprocess
import json
import os
import sys

ROOT = Path(r"D:\ECOM_GOVERNED_RUNTIME")
os.chdir(str(ROOT))

ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

archive_dir = ROOT / "storage" / "memory" / "archive"
control_dir = ROOT / "storage" / "control_room"
report_dir = ROOT / "storage" / "state_control"

archive_dir.mkdir(parents=True, exist_ok=True)
control_dir.mkdir(parents=True, exist_ok=True)
report_dir.mkdir(parents=True, exist_ok=True)

archive = archive_dir / ("GITHUB_MEMORY_BRIDGE_ARCHIVE_" + ts + ".txt")
pointer = control_dir / "GITHUB_MEMORY_BRIDGE_LATEST_POINTER.json"
report = report_dir / ("GITHUB_MEMORY_WRITE_BRIDGE_RUN_" + ts + ".txt")

def log(x):
    with report.open("a", encoding="utf-8") as f:
        f.write(str(x) + "\n")

def run(cmd):
    p = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace")
    log("$ " + " ".join(cmd))
    if p.stdout:
        log(p.stdout.rstrip())
    if p.stderr:
        log(p.stderr.rstrip())
    log("RETURN_CODE=" + str(p.returncode))
    return p

def finish(code):
    text = report.read_text(encoding="utf-8", errors="replace") if report.exists() else ""
    print(text)
    try:
        subprocess.run(["clip"], input=report.read_text(encoding="utf-8", errors="replace"), text=True, encoding="utf-8", errors="replace", check=False)
    except Exception:
        pass
    print("RESULT_COPIED_TO_CLIPBOARD")
    print("FILE=" + str(report))
    sys.exit(code)

report.write_text("STEP=ION_GITHUB_MEMORY_WRITE_BRIDGE_V1\nUTC=" + ts + "\n", encoding="utf-8")

clip_p = subprocess.run(["powershell", "-NoProfile", "-Command", "Get-Clipboard -Raw"], capture_output=True, text=True, encoding="utf-8", errors="replace")
clip = clip_p.stdout

if "ION_GITHUB_MEMORY_WRITE_V1" not in clip:
    log("STATUS=BLOCK_MISSING_MARKER_ION_GITHUB_MEMORY_WRITE_V1")
    finish(1)

staged = run(["git", "diff", "--cached", "--name-only"])
if staged.stdout.strip():
    log("STATUS=BLOCK_EXISTING_STAGED_FILES_CLEAR_STAGE_FIRST")
    finish(1)

archive.write_text(clip, encoding="utf-8")

pointer.write_text(json.dumps({
    "status": "PASS_GITHUB_MEMORY_BRIDGE_ARCHIVE_WRITTEN",
    "updated_utc": ts,
    "archive": "storage/memory/archive/" + archive.name,
    "mode": "LOCAL_WINDOWS_GITHUB_WRITE_BRIDGE",
    "next_safe_action": "VERIFY_GITHUB_MEMORY_ARCHIVE_IN_GITHUB"
}, indent=2, ensure_ascii=False), encoding="utf-8")

log("ARCHIVE=" + str(archive))
log("POINTER=" + str(pointer))

run(["git", "add", "--", str(archive), str(pointer)])
run(["git", "diff", "--cached", "--name-status"])

commit = run(["git", "commit", "-m", "archive GitHub memory bridge " + ts])
if commit.returncode != 0:
    log("STATUS=BLOCK_GIT_COMMIT_FAILED")
    finish(1)

push = run(["git", "push", "origin", "main"])
if push.returncode != 0:
    log("STATUS=BLOCK_GIT_PUSH_FAILED")
    finish(1)

log("STATUS=PASS_GITHUB_MEMORY_WRITE_BRIDGE_PUSHED_TO_GITHUB")
finish(0)