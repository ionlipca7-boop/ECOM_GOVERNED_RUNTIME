from pathlib import Path
from datetime import datetime
import argparse
import json


def load_json(path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding='utf-8'))
        except Exception:
            return default
    return default


def main():
    parser = argparse.ArgumentParser(description='ION task queue. DRY_RUN_ONLY.')
    parser.add_argument('--add', help='Добавить задачу в очередь')
    parser.add_argument('--list', action='store_true', help='Показать очередь')
    parser.add_argument('--done', type=int, help='Отметить задачу выполненной по номеру')
    args = parser.parse_args()

    base = Path(__file__).resolve().parent.parent
    state_dir = base / 'storage' / 'state'
    state_dir.mkdir(parents=True, exist_ok=True)
    queue_file = state_dir / 'task_queue_v1.json'

    queue = load_json(queue_file, [])

    if args.add:
        queue.append({
            'id': len(queue) + 1,
            'created_at': datetime.now().isoformat(),
            'task': args.add,
            'status': 'OPEN',
            'mode': 'DRY_RUN_ONLY'
        })

    if args.done is not None:
        for item in queue:
            if item.get('id') == args.done:
                item['status'] = 'DONE'
                item['done_at'] = datetime.now().isoformat()

    queue_file.write_text(json.dumps(queue, indent=2, ensure_ascii=False), encoding='utf-8')

    print('ОЧЕРЕДЬ ЗАДАЧ')
    for item in queue:
        print(f"[{item.get('id')}] {item.get('status')} - {item.get('task')}")
    print(queue_file)


if __name__ == '__main__':
    main()
