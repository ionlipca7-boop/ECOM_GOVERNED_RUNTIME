from pathlib import Path
import shutil
import json
from datetime import datetime

TOOLS = {
    'ollama': shutil.which('ollama'),
    'python': shutil.which('python'),
    'git': shutil.which('git'),
}

report = {
    'generated_at': datetime.now().isoformat(),
    'mode': 'DRY_RUN_ONLY',
    'future_ai_layer_status': {},
}

for tool, path in TOOLS.items():
    report['future_ai_layer_status'][tool] = {
        'installed': bool(path),
        'path': path,
    }

base = Path(__file__).resolve().parent.parent / 'storage' / 'reports'
base.mkdir(parents=True, exist_ok=True)

out = base / 'ai_layer_check_v1.json'

with open(out, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print('AI LAYER CHECK COMPLETE')
print(out)
