from pathlib import Path
from datetime import datetime
import argparse
import json

ERROR_WORDS = ['error', 'failed', 'exception', 'traceback', 'fatal']
WARNING_WORDS = ['warning', 'warn', 'attention']
SUCCESS_WORDS = ['success', 'complete', 'done', 'ok', 'passed']


def classify_line(text):
    t = text.lower()

    if any(word in t for word in ERROR_WORDS):
        return 'ERROR'

    if any(word in t for word in WARNING_WORDS):
        return 'WARNING'

    if any(word in t for word in SUCCESS_WORDS):
        return 'SUCCESS'

    return 'INFO'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    args = parser.parse_args()

    log_path = Path(args.file)

    if not log_path.exists():
        print('ФАЙЛ НЕ НАЙДЕН')
        return

    lines = log_path.read_text(encoding='utf-8', errors='replace').splitlines()

    summary = {
        'generated_at': datetime.now().isoformat(),
        'source_file': str(log_path),
        'mode': 'DRY_RUN_ONLY',
        'counts': {
            'ERROR': 0,
            'WARNING': 0,
            'SUCCESS': 0,
            'INFO': 0,
        },
        'important_lines': [],
        'next_action_draft': None,
    }

    for line in lines:
        level = classify_line(line)
        summary['counts'][level] += 1

        if level != 'INFO':
            summary['important_lines'].append({
                'level': level,
                'text': line[:500]
            })

    if summary['counts']['ERROR'] > 0:
        summary['next_action_draft'] = 'ПРОВЕРИТЬ ОШИБКИ И НЕ ЗАПУСКАТЬ LIVE ДЕЙСТВИЯ'
    elif summary['counts']['WARNING'] > 0:
        summary['next_action_draft'] = 'ПРОВЕРИТЬ WARNING ПЕРЕД ПРОДОЛЖЕНИЕМ'
    else:
        summary['next_action_draft'] = 'КРИТИЧЕСКИХ ПРОБЛЕМ НЕ ОБНАРУЖЕНО'

    out_dir = Path(__file__).resolve().parent.parent / 'storage' / 'reports'
    out_dir.mkdir(parents=True, exist_ok=True)

    out_file = out_dir / 'log_summary_v1.json'

    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print('АНАЛИЗ ЛОГА ЗАВЕРШЁН')
    print(out_file)


if __name__ == '__main__':
    main()
