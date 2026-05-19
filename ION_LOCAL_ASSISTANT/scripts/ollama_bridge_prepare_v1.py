from pathlib import Path
from datetime import datetime
import json
import shutil

report = {
    'generated_at': datetime.now().isoformat(),
    'mode': 'PREPARE_ONLY',
    'ollama_detected': bool(shutil.which('ollama')),
    'recommended_models': [
        'llama3',
        'mistral',
        'phi3'
    ],
    'future_usage': [
        'local summaries',
        'command explanation',
        'workflow help',
        'project memory assistance'
    ],
    'note': 'AI layer is not active by default.'
}

out_dir = Path(__file__).resolve().parent.parent / 'storage' / 'reports'
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / 'ollama_bridge_prepare_v1.json'

with open(out, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print('OLLAMA PREPARE REPORT CREATED')
print(out)
