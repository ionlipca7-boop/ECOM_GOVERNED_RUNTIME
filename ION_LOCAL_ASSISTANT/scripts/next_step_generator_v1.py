from pathlib import Path
from datetime import datetime
import json

base = Path(__file__).resolve().parent.parent
report_dir = base / 'storage' / 'reports'
report_dir.mkdir(parents=True, exist_ok=True)

summary = {
    'generated_at': datetime.now().isoformat(),
    'mode': 'DRY_RUN_ONLY',
    'recommended_next_steps': [
        'Проверить последние отчёты',
        'Проверить duplicate groups',
        'Проверить большие файлы',
        'Сделать dry-run cleanup plan',
        'Показать отчёт оператору',
        'Ждать approval перед любыми изменениями'
    ]
}

out = report_dir / 'next_step_generator_v1.json'
out.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8')

print('СЛЕДУЮЩИЕ ШАГИ СГЕНЕРИРОВАНЫ')
print(out)
