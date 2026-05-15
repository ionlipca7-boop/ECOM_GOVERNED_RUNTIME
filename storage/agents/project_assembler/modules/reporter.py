from pathlib import Path
import json


def write_json(workspace: Path, name: str, data):
    path = workspace / name
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    return str(path)


def write_text(workspace: Path, name: str, text: str):
    path = workspace / name
    path.write_text(text, encoding='utf-8')
    return str(path)
