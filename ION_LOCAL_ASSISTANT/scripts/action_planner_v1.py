from pathlib import Path
from datetime import datetime
import argparse
import json

BLOCKED_WORDS = ['delete', 'remove', 'publish', 'send', 'token', '.env', 'secret', 'server']
REVIEW_WORDS = ['move', 'rename', 'replace', 'overwrite', 'cleanup']


def plan_action(text):
    t = text.lower()

    if any(word in t for word in BLOCKED_WORDS):
        return {
            'decision': 'BLOCKED_OR_APPROVAL_REQUIRED',
            'reason': 'Действие содержит высокий риск. Нужен отдельный approval и проверка.',
            'allowed_now': False,
        }

    if any(word in t for word in REVIEW_WORDS):
        return {
            'decision': 'REVIEW_REQUIRED',
            'reason': 'Действие может менять файлы. Сначала нужен dry-run отчёт.',
            'allowed_now': False,
        }

    return {
        'decision': 'DRAFT_ALLOWED',
        'reason': 'Можно подготовить черновик или отчёт. Изменения не выполняются.',
        'allowed_now': True,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', required=True)
    args = parser.parse_args()

    result = plan_action(args.task)

    report = {
        'generated_at': datetime.now().isoformat(),
        'mode': 'DRY_RUN_ONLY',
        'task': args.task,
        'plan': result,
        'next_step': 'Показать отчёт оператору и ждать решения.'
    }

    out_dir = Path(__file__).resolve().parent.parent / 'storage' / 'reports'
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / 'action_planner_v1.json'

    with open(out, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print('ПЛАН ДЕЙСТВИЯ ГОТОВ')
    print(result['decision'])
    print(out)


if __name__ == '__main__':
    main()
