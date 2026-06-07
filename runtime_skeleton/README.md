# ECOM OS V7.3C Local Runtime Skeleton

Минимальная локальная панель для просмотра и проверки контрактов V7.3C.

## Запуск

```powershell
python runtime_skeleton/app.py
```

Локальный адрес:

```text
http://localhost:8000
```

Сервер слушает только `127.0.0.1`, не требует интернета, токенов, Telegram,
eBay или marketplace API.

## Что делает

- читает контракты из `storage/contracts/v7_3c/`;
- показывает 8 route buttons;
- отображает route card/details;
- показывает inputs, outputs, agents, blocks, handoffs и rules;
- валидирует JSON-контракты;
- пишет локальный отчёт в `runtime_skeleton/_output/validation_report.json`.

## Отдельная проверка

```powershell
python runtime_skeleton/validator.py
```
