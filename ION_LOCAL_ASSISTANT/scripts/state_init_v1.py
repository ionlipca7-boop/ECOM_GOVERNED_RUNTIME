from pathlib import Path
from datetime import datetime
import json

base = Path(__file__).resolve().parent.parent
state_dir = base / 'storage' / 'state'
state_dir.mkdir(parents=True, exist_ok=True)

state_file = state_dir / 'local_assistant_state.json'

state = {
    'assistant': 'ION_LOCAL_ASSISTANT',
    'version': 'V1',
    'mode': 'DRY_RUN_ONLY',
    'language': 'ru',
    'created_at': datetime.now().isoformat(),
    'last_action': None,
    'last_report': None,
    'operator_gate': 'REQUIRED_FOR_ANY_CHANGE',
    'blocked_actions': [
        'DELETE',
        'LIVE_PUBLISH',
        'SEND_EMAIL',
        'TOUCH_SECRETS',
        'TOUCH_SERVER',
        'AUTO_EXECUTE_UNKNOWN'
    ],
    'allowed_actions_v1': [
        'SCAN',
        'REPORT',
        'SUMMARY',
        'DRAFT_PLAN',
        'RISK_SCORE'
    ]
}

with open(state_file, 'w', encoding='utf-8') as f:
    json.dump(state, f, indent=2, ensure_ascii=False)

print('СОСТОЯНИЕ СОЗДАНО')
print(state_file)
