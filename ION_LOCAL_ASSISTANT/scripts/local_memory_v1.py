from pathlib import Path
from datetime import datetime
import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--note', required=True)
    args = parser.parse_args()

    base = Path(__file__).resolve().parent.parent
    memory_dir = base / 'storage' / 'memory'
    memory_dir.mkdir(parents=True, exist_ok=True)

    memory_file = memory_dir / 'local_memory_log.json'

    data = []

    if memory_file.exists():
        try:
            data = json.loads(memory_file.read_text(encoding='utf-8'))
        except Exception:
            data = []

    entry = {
        'created_at': datetime.now().isoformat(),
        'note': args.note,
        'mode': 'DRY_RUN_ONLY'
    }

    data.append(entry)

    with open(memory_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print('ПАМЯТЬ ОБНОВЛЕНА')
    print(memory_file)


if __name__ == '__main__':
    main()
