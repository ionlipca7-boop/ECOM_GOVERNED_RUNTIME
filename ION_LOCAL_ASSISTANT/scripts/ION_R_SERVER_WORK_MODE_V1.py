import subprocess, datetime, pathlib, json, hashlib, sys

MARKER = "# ION_SERVER_AUTO_SAFE_V1"
ROOT = pathlib.Path(r"D:\ECOM_GOVERNED_RUNTIME")
SERVER_BLOCKS = ROOT / "ION_LOCAL_ASSISTANT" / "storage" / "server_blocks"
REGISTRY = SERVER_BLOCKS / "registry.json"
REPORT = ROOT / "ION_LOCAL_ASSISTANT" / "storage" / "reports" / "r_server_work_mode_last_output.txt"
SSH = [
    "ssh",
    "-i", r"C:\Users\Ion Lipca\.ssh\ecom_os_v3_server_ed25519",
    "-o", "IdentitiesOnly=yes",
    "-o", "BatchMode=yes",
    "-o", "ConnectTimeout=10",
    "-o", "StrictHostKeyChecking=yes",
    "ionlipca7@34.29.150.106",
    "bash -s",
]

HARD_BLOCK = [
    "rm -rf",
    "sudo ",
    "reboot",
    "shutdown",
    "mkfs",
    "dd if=",
    "git push",
    ".env",
    "storage/secrets",
    "EBAY_ACCESS_TOKEN",
    "EBAY_REFRESH_TOKEN",
    "CLIENT_SECRET",
    "PASSWORD",
    "TOKEN=",
    "SECRET=",
    "curl -X POST",
    "curl -X PUT",
    "curl -X DELETE",
]

REQUIRED_TEXT = [
    MARKER,
    "MODE: READ_ONLY_NO_WRITE_NO_LIVE",
    "NO_WRITE_NO_DELETE_NO_CLEANUP_NO_EBAY_LIVE",
]

def set_clip(text: str) -> None:
    subprocess.run(
        ["powershell", "-NoProfile", "-Command", "Set-Clipboard -Value ([Console]::In.ReadToEnd())"],
        input=text,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

def fail(reason: str, extra: str = "") -> int:
    result = "\r\n".join([
        "=== ION R SERVER WORK MODE OUTPUT V3 ===",
        "MODE=STABLE_BLOCK_LIBRARY_ONLY",
        "DECISION=BLOCKED_R_STABLE_LIBRARY_CHECK_FAILED",
        "REASON=" + reason,
        extra,
    ]).strip() + "\r\n"
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(result, encoding="utf-8")
    set_clip(result)
    print(result)
    return 2

def main() -> int:
    print("=== ION R SERVER WORK MODE V3 ===")
    print("MODE=STABLE_BLOCK_LIBRARY_ONLY")
    print("REGISTRY=" + str(REGISTRY))

    if not REGISTRY.exists():
        return fail("registry_missing", str(REGISTRY))

    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8", errors="replace"))
    except Exception as exc:
        return fail("registry_json_error", repr(exc))

    block_id = registry.get("default_block_id")
    blocks = registry.get("blocks") or {}
    block = blocks.get(block_id) or {}
    rel_path = block.get("path")

    if not block_id or not rel_path:
        return fail("default_block_or_path_missing", "block_id=" + str(block_id) + " path=" + str(rel_path))

    block_path = (ROOT / rel_path.replace("/", "\\")).resolve()
    current_dir = (SERVER_BLOCKS / "current").resolve()

    if current_dir not in block_path.parents:
        return fail("block_path_not_under_current_allowlist", str(block_path))

    if not block_path.exists():
        return fail("block_file_missing", str(block_path))

    text = block_path.read_text(encoding="utf-8", errors="replace")
    text = text.replace(chr(0xFEFF), "").replace("я╗┐", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n").lstrip()

    if not text.startswith(MARKER):
        return fail("marker_missing_or_not_first_line", block_id)

    missing = [x for x in REQUIRED_TEXT if x not in text]
    if missing:
        return fail("required_readonly_text_missing", ",".join(missing))

    bad = [x for x in HARD_BLOCK if x.lower() in text.lower()]
    if bad:
        return fail("hard_block_pattern_detected", ",".join(bad))

    sha1 = hashlib.sha1(text.encode("utf-8", errors="replace")).hexdigest()
    print("BLOCK_ID=" + str(block_id))
    print("BLOCK_PATH=" + str(block_path))
    print("BLOCK_SHA1=" + sha1)
    print("AUTO_EXEC_START")

    data = text.encode("utf-8", errors="replace").replace(b"\xef\xbb\xbf", b"").replace(b"\r\n", b"\n").replace(b"\r", b"\n")

    try:
        proc = subprocess.run(SSH, input=data, capture_output=True, timeout=240)
        stdout = (proc.stdout or b"").decode("utf-8", errors="replace")
        stderr = (proc.stderr or b"").decode("utf-8", errors="replace")
        decision = "PASS_R_STABLE_BLOCK_SERVER_OUTPUT_COPIED" if proc.returncode == 0 else "BLOCKED_SSH_OR_REMOTE_ERROR"
        returncode_line = "RETURN_CODE=" + str(proc.returncode)
    except Exception as exc:
        stdout = ""
        stderr = repr(exc)
        decision = "BLOCKED_R_STABLE_BLOCK_EXCEPTION"
        returncode_line = "RETURN_CODE=EXCEPTION"

    result = "\r\n".join([
        "=== ION R SERVER WORK MODE OUTPUT V3 ===",
        "UTC=" + datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "MODE=STABLE_BLOCK_LIBRARY_ONLY",
        "BLOCK_ID=" + str(block_id),
        "BLOCK_SHA1=" + sha1,
        returncode_line,
        "",
        stdout,
        stderr,
        "",
        "DECISION=" + decision,
    ]).strip() + "\r\n"

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(result, encoding="utf-8")
    set_clip(result)
    print(result)
    print("AUTO_EXEC_DONE_COPIED_TO_CLIPBOARD=1")
    return 0 if decision.startswith("PASS_") else 2

if __name__ == "__main__":
    sys.exit(main())
