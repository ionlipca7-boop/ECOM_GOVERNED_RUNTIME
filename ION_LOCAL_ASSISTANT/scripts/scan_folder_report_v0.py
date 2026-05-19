import argparse
import hashlib
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)
    args = parser.parse_args()

    root = Path(args.path)

    if not root.exists():
        print('ERROR: path does not exist')
        return

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    report_dir = Path(__file__).resolve().parent.parent / 'storage' / 'reports'
    report_dir.mkdir(parents=True, exist_ok=True)

    files = []
    duplicates = defaultdict(list)
    extension_stats = defaultdict(int)
    total_size = 0

    for path in root.rglob('*'):
        if path.is_file():
            try:
                size = path.stat().st_size
                file_hash = sha256_file(path)

                files.append({
                    'path': str(path),
                    'size': size,
                    'extension': path.suffix.lower(),
                    'sha256': file_hash,
                })

                duplicates[file_hash].append(str(path))
                extension_stats[path.suffix.lower()] += 1
                total_size += size

            except Exception as e:
                files.append({
                    'path': str(path),
                    'error': str(e),
                })

    duplicate_groups = {
        k: v for k, v in duplicates.items() if len(v) > 1
    }

    report = {
        'scan_root': str(root),
        'generated_at': timestamp,
        'total_files': len(files),
        'total_size_bytes': total_size,
        'extensions': dict(extension_stats),
        'duplicate_groups': duplicate_groups,
        'files': files,
        'mode': 'DRY_RUN_ONLY'
    }

    json_path = report_dir / f'{timestamp}_folder_scan.json'
    txt_path = report_dir / f'{timestamp}_folder_scan.txt'

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('ION LOCAL ASSISTANT REPORT\n')
        f.write(f'SCAN ROOT: {root}\n')
        f.write(f'TOTAL FILES: {len(files)}\n')
        f.write(f'DUPLICATE GROUPS: {len(duplicate_groups)}\n')
        f.write(f'TOTAL SIZE BYTES: {total_size}\n')

    print('SCAN COMPLETE')
    print(json_path)
    print(txt_path)


if __name__ == '__main__':
    main()
