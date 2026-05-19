# ION Local Assistant

Локальный диспетчер порядка для Windows.

## Статус

`V0 / DRY_RUN_ONLY / Windows-first`

## Цель

Создать бесплатного локального помощника под контролем оператора ION.

Помощник должен помогать с:

- сканированием папок;
- поиском дубликатов;
- сортировкой фото и документов;
- подготовкой отчётов;
- подготовкой безопасных CMD-действий;
- чтением логов и выводов команд;
- подготовкой текста для ChatGPT.

## Жёсткое правило V0

На этапе V0 помощник ничего не удаляет, не публикует, не отправляет и не меняет в live-системах.

Разрешено только:

- READ;
- SCAN;
- REPORT;
- DRAFT;
- QUARANTINE_PLAN.

## Запрещено в V0

- delete files;
- move important folders;
- send email;
- publish/revise eBay;
- touch secrets;
- touch server;
- run unknown scripts;
- modify production project files.

## Структура

```text
ION_LOCAL_ASSISTANT/
  README.md
  SPEC.md
  SAFETY_RULES.md
  ROADMAP.md
  scripts/
    README.md
  src/
    README.md
  storage/
    README.md
```

## Следующий шаг

Подготовить первый локальный Windows dry-run сканер:

```text
scan_folder_report_v0.py
```

Он должен создать отчёт, но ничего не удалять.