# ECOM OS V7.3C — локальное интеграционное ядро

Текущий режим: `local_dry_integration_core`.

Это не live runtime. Панель и contracts связывают Telegram, Browser, Shared Case JSON, будущий Server brain и agent placeholders без Telegram patch, без eBay, без записи на сервер и без секретов.

## Роли системы

- Telegram = главный пульт Ion. Сейчас описан dry-контракт кнопок, live bot не патчится.
- Browser = локальное рабочее окно оператора. Здесь Ion заполняет черновик кейса и собирает Case JSON.
- Shared Case JSON = мост между Telegram, Browser и будущим Server runtime.
- Server = будущий мозг, исполнитель и agent chain. Сейчас только bridge targets и placeholders.
- GitHub = память и source of truth для контрактов, карт и checkpoint-архивов.
- Secrets = только через локальный protected `.env`, не через Git и не через browser output.

## Безопасность

Закрыто в текущем режиме:

- live Telegram patch;
- eBay publish/revise/delete;
- запись на сервер;
- server restart;
- delete/cleanup;
- commit/push;
- чтение или печать реальных токенов;
- показ секретов в браузере.

Live Telegram/eBay/server режим можно обсуждать только после отдельных gates:

1. `LOCAL_SECRETS_INSTALL_APPROVED`
2. `SERVER_BRIDGE_ACTIVATION_APPROVED`
3. `LIVE_TELEGRAM_OR_EBAY_GATE_APPROVED`

## Секреты

Codex не читает и не обрабатывает реальные токены.

Будущий локальный файл секретов:

```text
D:\ECOM_OS_LOCAL_SECRETS\.env.ecom.local
```

Этот файл устанавливается вручную позже и не должен попадать в Git. Серверный export секретов — отдельный approved gate. Dashboard никогда не должен показывать секреты.

Пример без значений хранится в:

```text
.env.example
```

## Запуск dashboard

Из корня проекта:

```powershell
runtime_skeleton\start_dashboard.bat
```

URL:

```text
http://127.0.0.1:8730/runtime_skeleton/_output/index.html
```

Чтобы остановить локальный сервер, вернитесь в CMD-окно с dashboard и нажмите `CTRL+C`.

## Проверка без live-действий

```powershell
runtime_skeleton\verify_local.bat
```

Скрипт может запускать только:

- `python runtime_skeleton\validator.py`
- `python runtime_skeleton\app.py`
- `py -m py_compile runtime_skeleton\app.py runtime_skeleton\contract_loader.py runtime_skeleton\validator.py`
- `git diff --check`
- `git status --short`

Он не коммитит, не пушит, не удаляет, не вызывает сервер, Telegram, eBay и не читает секреты.

## Кнопки оператора

- `Главная` — возвращает панель к стартовому маршруту 01 и не меняет данные маршрутов.
- `Назад` — возвращает к предыдущему выбранному маршруту из локальной истории UI.
- `Стоп` — ставит только локальное UI-состояние остановки. После reload dashboard снова работает.

## Как проверить один продукт через маршрут 01

1. Откройте dashboard.
2. Выберите `01 Новый продукт`.
3. В блоке `Операторский ввод` заполните:
   - ссылку поставщика;
   - название товара;
   - текст товара;
   - фото/файлы/заметки;
   - чек/закупку;
   - цену закупки;
   - цену продажи;
   - количество;
   - доставку;
   - комментарий Ion;
   - следующее действие.
4. Нажмите `Сохранить черновик`.
5. Нажмите `Собрать карточку`.
6. Нажмите `Экспорт JSON`.
7. Проверьте, что Case JSON содержит `route_id`, `case_namespace`, `operator_inputs`, `server_bridge_status`, `assigned_agent`, `history` и `safety_locks`.

Черновики хранятся в `localStorage` по `route_id`: маршрут 01 не перезаписывает маршрут 02.

## Контракты интеграции

Новые dry contracts:

- `runtime_skeleton/contracts/case_schema_v1.json`
- `runtime_skeleton/contracts/telegram_routes_v1.json`
- `runtime_skeleton/contracts/agent_map_v1.json`
- `runtime_skeleton/contracts/server_import_map_v1.json`
- `runtime_skeleton/contracts/server_capability_map_v1.json`
- `runtime_skeleton/contracts/server_bridge_v1.json`
- `runtime_skeleton/contracts/server_required_exports_v1.json`
- `runtime_skeleton/contracts/integration_manifest_v1.json`
- `runtime_skeleton/contracts/secret_requirements_v1.json`
- `runtime_skeleton/contracts/local_env_bridge_v1.json`

Главная цепочка:

```text
Telegram button
→ route_id
→ Browser panel
→ Shared Case JSON
→ Server bridge target
→ Agent placeholder
→ Report/checkpoint
→ Approval gate
```

## Что должно случиться позже

- Утвердить server bridge activation.
- Вручную установить локальные секреты в protected `.env`.
- Экспортировать серверные entrypoints через отдельный gate.
- Только после approval gate разрешить Telegram/eBay live actions.

До этого момента проект остаётся локальным dry integration core.
