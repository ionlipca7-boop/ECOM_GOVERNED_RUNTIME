import subprocess
from pathlib import Path
from datetime import datetime


def get_clipboard_text():
    ps = subprocess.run(
        ["powershell", "-NoProfile", "-Command", "Get-Clipboard"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    return ps.stdout.strip()


def main():
    text = get_clipboard_text()

    base = Path(__file__).resolve().parent.parent
    pending_dir = base / "storage" / "pending_cmd"
    pending_dir.mkdir(parents=True, exist_ok=True)

    out_file = pending_dir / "last_cmd_from_chatgpt.txt"
    out_file.write_text(text, encoding="utf-8")

    print("======================================")
    print("ION CMD PREVIEW")
    print("РЕЖИМ: ТОЛЬКО ПРОСМОТР")
    print("======================================")
    print()
    print("CMD-блок из буфера сохранён:")
    print(out_file)
    print()
    print("Файл сейчас откроется в Блокноте для проверки.")
    print("Автоматический запуск НЕ выполняется.")

    subprocess.Popen(["notepad", str(out_file)])


if __name__ == "__main__":
    main()
