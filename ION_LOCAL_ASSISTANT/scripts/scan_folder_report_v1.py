import argparse
import hashlib
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp', '.tif', '.tiff'}
DOC_EXTENSIONS = {'.pdf', '.doc', '.docx', '.xls', '.xlsx', '.csv', '.txt', '.md'}
ARCHIVE_EXTENSIONS = {'.zip', '.rar', '.7z', '.tar', '.gz'}
DEFAULT_LARGE_FILE_MB = 100


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def classify_file(path):
    ext = path.suffix.lower()
    if ext in IMAGE_EXTENSIONS:
        return 'image'
    if ext in DOC_EXTENSIONS:
        return 'document'
    if ext in ARCHIVE_EXTENSIONS:
        return 'archive'
    if ext in {'.mp4', '.mov', '.avi', '.mkv'}:
        return 'video'
    if ext in {'.mp3', '.wav', '.m4a'}:
        return 'audio'
    return 'other'


def is_empty_dir(path):
    try:
        return path.is_dir() and not any(path.iterdir())
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(description='ION Local Assistant V1 folder scanner. DRY_RUN_ONLY.')
    parser.add_argument('--path', required=True, help='Folder to scan')
    parser.add_argument('--large-mb', type=int, default=DEFAULT_LARGE_FILE_MB, help='Large file threshold in MB')
    args = parser.parse_args()

    root = Path(args.path)

    if not root.exists():
        print('ERROR: path does not exist')
        return

    if not root.is_dir():
        print('ERROR: path is not a folder')
        return

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_dir = Path(__file__).resolve().parent.parent / 'storage' / 'reports'
    report_dir.mkdir(parents=True, exist_ok=True)

    files = []
    errors = []
    duplicates = defaultdict(list)
    extension_stats = defaultdict(int)
    class_stats = defaultdict(int)
    large_files = []
    image_files = []
    empty_folders = []
    total_size = 0
    large_threshold = args.large_mb * 1024 * 1024

    for path in root.rglob('*'):
        if path.is_dir() and is_empty_dir(path):
            empty_folders.append(str(path))
            continue

        if path.is_file():
            try:
                size = path.stat().st_size
                ext = path.suffix.lower()
                file_class = classify_file(path)
                file_hash = sha256_file(path)

                item = {
                    'path': str(path),
                    'name': path.name,
                    'size': size,
                    'size_mb': round(size / 1024 / 1024, 2),
                    'extension': ext,
                    'class': file_class,
                    'sha256': file_hash,
                }

                files.append(item)
                duplicates[file_hash].append(str(path))
                extension_stats[ext or '[no_extension]'] += 1
                class_stats[file_class] += 1
                total_size += size

                if size >= large_threshold:
                    large_files.append(item)

                if file_class == 'image':
                    image_files.append(item)

            except Exception as e:
                errors.append({'path': str(path), 'error': str(e)})

    duplicate_groups = {k: v for k, v in duplicates.items() if len(v) > 1}

    quarantine_candidates = []
    for hash_value, paths in duplicate_groups.items():
        quarantine_candidates.append({
            'reason': 'duplicate_group',
            'sha256': hash_value,
            'keep_first_candidate': paths[0],
            'duplicate_candidates': paths[1:],
            'note': 'DRY_RUN_ONLY: no file moved or deleted.'
        })

    report = {
        'assistant': 'ION_LOCAL_ASSISTANT',
        'version': 'V1',
        'mode': 'DRY_RUN_ONLY',
        'scan_root': str(root),
        'generated_at': timestamp,
        'large_file_threshold_mb': args.large_mb,
        'summary': {
            'total_files': len(files),
            'total_size_bytes': total_size,
            'total_size_mb': round(total_size / 1024 / 1024, 2),
            'duplicate_groups': len(duplicate_groups),
            'large_files': len(large_files),
            'image_files': len(image_files),
            'empty_folders': len(empty_folders),
            'errors': len(errors),
        },
        'extensions': dict(sorted(extension_stats.items())),
        'classes': dict(sorted(class_stats.items())),
        'large_files': large_files,
        'empty_folders': empty_folders,
        'duplicate_groups': duplicate_groups,
        'quarantine_candidates': quarantine_candidates,
        'errors': errors,
        'files': files,
    }

    json_path = report_dir / f'{timestamp}_folder_scan_v1.json'
    txt_path = report_dir / f'{timestamp}_folder_scan_v1.txt'

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('ION LOCAL ASSISTANT REPORT V1\n')
        f.write('MODE: DRY_RUN_ONLY\n')
        f.write(f'SCAN ROOT: {root}\n')
        f.write(f'TOTAL FILES: {len(files)}\n')
        f.write(f'TOTAL SIZE MB: {round(total_size / 1024 / 1024, 2)}\n')
        f.write(f'DUPLICATE GROUPS: {len(duplicate_groups)}\n')
        f.write(f'LARGE FILES: {len(large_files)}\n')
        f.write(f'IMAGE FILES: {len(image_files)}\n')
        f.write(f'EMPTY FOLDERS: {len(empty_folders)}\n')
        f.write(f'ERRORS: {len(errors)}\n')
        f.write('\nEXTENSIONS:\n')
        for ext, count in sorted(extension_stats.items()):
            f.write(f'  {ext}: {count}\n')
        f.write('\nCLASSES:\n')
        for cls, count in sorted(class_stats.items()):
            f.write(f'  {cls}: {count}\n')
        f.write('\nTOP LARGE FILES:\n')
        for item in sorted(large_files, key=lambda x: x['size'], reverse=True)[:20]:
            f.write(f"  {item['size_mb']} MB | {item['path']}\n")
        f.write('\nQUARANTINE CANDIDATES:\n')
        for item in quarantine_candidates[:20]:
            f.write(f"  duplicate candidates: {len(item['duplicate_candidates'])} | keep: {item['keep_first_candidate']}\n")

    print('SCAN COMPLETE V1')
    print('MODE: DRY_RUN_ONLY')
    print(json_path)
    print(txt_path)


if __name__ == '__main__':
    main()
