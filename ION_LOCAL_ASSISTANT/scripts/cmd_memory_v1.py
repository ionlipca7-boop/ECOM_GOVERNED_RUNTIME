from pathlib import Path
from datetime import datetime
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='ION CMD memory layer.')
    parser.add_argument('--input', required=True, help='Текст CMD/output/log')
    args = parser.parse_args()

    base = Path(__file__).resolve().parent.parent
    memory_dir = base / 'storage' / 'memory'
    memory_dir.mkdir(parents=True, exist_ok=True)

    memory_file = memory_dir / 'cmd_memory_v1.json'

    data = []

    if memory_file.exists():
        try:
            data = json.loads(memory_file.read_text(encoding='utf-8'))
        except Exception:
            data = []

    entry = {
        'created_at': datetime.now().isoformat(),
        'type': 'CMD_OUTPUT',
        'content_preview': args.input[:1000],
        'mode': 'DRY_RUN_ONLY'
    }

    data.append(entry)

    memory_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

    print('CMD ПАМЯТЬ ОБНОВЛЕНА')
    print(memory_file)


if __name__ == '__main__':
    main()
