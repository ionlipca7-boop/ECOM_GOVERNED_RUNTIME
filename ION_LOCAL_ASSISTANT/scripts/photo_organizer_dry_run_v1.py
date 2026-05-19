from pathlib import Path
from collections import defaultdict
from datetime import datetime
import argparse
import json

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)
    args = parser.parse_args()

    root = Path(args.path)

    groups = defaultdict(list)

    for path in root.rglob('*'):
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
            groups[path.parent.name].append(str(path))

    report = {
        'generated_at': datetime.now().isoformat(),
        'mode': 'DRY_RUN_ONLY',
        'root': str(root),
        'photo_groups': dict(groups),
    }

    out_dir = Path(__file__).resolve().parent.parent / 'storage' / 'reports'
    out_dir.mkdir(parents=True, exist_ok=True)

    out = out_dir / 'photo_organizer_dry_run_v1.json'

    with open(out, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print('PHOTO ORGANIZER COMPLETE')
    print(out)


if __name__ == '__main__':
    main()
