from pathlib import Path
from datetime import datetime
import argparse
import json

HIGH_RISK_WORDS = [
    'delete',
    'remove',
    'format',
    'drop',
    'publish',
    'secret',
    'token',
    '.env'
]

MEDIUM_RISK_WORDS = [
    'move',
    'rename',
    'replace',
    'overwrite'
]


def calculate_risk(text):
    t = text.lower()

    for word in HIGH_RISK_WORDS:
        if word in t:
            return 'HIGH'

    for word in MEDIUM_RISK_WORDS:
        if word in t:
            return 'MEDIUM'

    return 'LOW'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', required=True)
    args = parser.parse_args()

    risk = calculate_risk(args.text)

    report = {
        'generated_at': datetime.now().isoformat(),
        'mode': 'DRY_RUN_ONLY',
        'input': args.text,
        'risk_level': risk,
    }

    out_dir = Path(__file__).resolve().parent.parent / 'storage' / 'reports'
    out_dir.mkdir(parents=True, exist_ok=True)

    out_file = out_dir / 'risk_score_v1.json'

    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print('ОЦЕНКА РИСКА ГОТОВА')
    print('УРОВЕНЬ:', risk)
    print(out_file)


if __name__ == '__main__':
    main()
