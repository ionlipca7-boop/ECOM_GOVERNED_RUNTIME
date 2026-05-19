from pathlib import Path
import json
from datetime import datetime
import argparse

PROJECT_KEYWORDS = {
    'ecom': ['ebay', 'shop', 'listing', 'inventory', 'offer'],
    'photos': ['photo', 'image', 'screenshot', 'camera'],
    'code': ['src', 'node_modules', '.git', 'package.json', 'requirements.txt'],
    'documents': ['invoice', 'rechnung', 'tax', 'report'],
}


def detect_project_type(path):
    score = {}
    text = str(path).lower()

    for category, keywords in PROJECT_KEYWORDS.items():
        score[category] = sum(1 for kw in keywords if kw in text)

    best = max(score, key=score.get)

    if score[best] == 0:
        return 'unknown'

    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)
    args = parser.parse_args()

    root = Path(args.path)

    report = {
        'generated_at': datetime.now().isoformat(),
        'root': str(root),
        'mode': 'DRY_RUN_ONLY',
        'projects': []
    }

    for path in root.iterdir():
        if path.is_dir():
            project_type = detect_project_type(path)

            report['projects'].append({
                'folder': str(path),
                'detected_type': project_type,
            })

    out = Path(__file__).resolve().parent.parent / 'storage' / 'reports'
    out.mkdir(parents=True, exist_ok=True)

    output_file = out / 'project_detector_report.json'

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print('PROJECT DETECTOR COMPLETE')
    print(output_file)


if __name__ == '__main__':
    main()
