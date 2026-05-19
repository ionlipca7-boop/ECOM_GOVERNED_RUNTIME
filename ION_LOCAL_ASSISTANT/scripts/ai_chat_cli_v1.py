from datetime import datetime
from pathlib import Path
import json

WELCOME = '''
======================================
ION ЛОКАЛЬНЫЙ AI ПОМОЩНИК
РЕЖИМ: GOVERNED / DRY RUN
======================================
Напиши команду или вопрос.
Для выхода напиши: exit
'''


def generate_response(user_input):
    text = user_input.lower()

    if 'очист' in text or 'удал' in text:
        return {
            'risk': 'HIGH',
            'answer': 'Обнаружено потенциально опасное действие. Сначала нужен dry-run отчёт и approval.'
        }

    if 'фото' in text:
        return {
            'risk': 'LOW',
            'answer': 'Могу подготовить dry-run анализ фотографий и группировку.'
        }

    if 'лог' in text or 'ошиб' in text:
        return {
            'risk': 'LOW',
            'answer': 'Могу помочь проанализировать лог и подготовить summary.'
        }

    return {
        'risk': 'LOW',
        'answer': 'Команда получена. Могу подготовить безопасный план действий или отчёт.'
    }


def save_memory(question, answer):
    base = Path(__file__).resolve().parent.parent
    memory_dir = base / 'storage' / 'memory'
    memory_dir.mkdir(parents=True, exist_ok=True)

    memory_file = memory_dir / 'ai_chat_history_v1.json'

    data = []

    if memory_file.exists():
        try:
            data = json.loads(memory_file.read_text(encoding='utf-8'))
        except Exception:
            data = []

    data.append({
        'time': datetime.now().isoformat(),
        'question': question,
        'answer': answer,
    })

    memory_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')


print(WELCOME)

while True:
    user_input = input('ION > ')

    if user_input.strip().lower() == 'exit':
        print('ЗАВЕРШЕНИЕ AI ПОМОЩНИКА')
        break

    result = generate_response(user_input)

    print('\nКратко:')
    print(result['answer'])
    print('Риск:', result['risk'])
    print('Подтверждение нужно:', 'ДА' if result['risk'] != 'LOW' else 'НЕТ')
    print()

    save_memory(user_input, result)
