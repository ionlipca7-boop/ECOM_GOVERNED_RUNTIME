# ION LOCAL ASSISTANT UPGRADE BACKLOG

## Цель

Перед установкой на Windows зафиксировать, какие апгрейды можно добавить дальше без хаоса.

## Priority 1

### 1. CMD / LOG WATCHER

Задача:

- читать вывод CMD;
- искать ERROR / WARNING / SUCCESS;
- делать summary;
- предлагать следующий шаг.

Статус:

```text
PARTLY_STARTED
```

### 2. SMART CLEANUP PLANNER

Задача:

- искать дубликаты;
- искать большие файлы;
- искать пустые папки;
- искать старые downloads;
- строить quarantine plan.

Правило:

```text
NO_DELETE_BY_DEFAULT
```

### 3. PHOTO WORKSPACE

Задача:

- группировка фото;
- поиск дублей;
- поиск похожих фото в будущем;
- подготовка eBay photo report.

### 4. ECOM WORKSPACE MODE

Задача:

- понимать product folders;
- понимать listing assets;
- понимать reports;
- понимать photo pipeline;
- помогать готовить eBay work пакет.

## Priority 2

### 5. LOCAL AI LAYER

Инструменты:

- Ollama;
- локальная модель;
- позже Open Interpreter local mode.

Задача:

- русский диалог;
- объяснение ошибок;
- анализ логов;
- локальная project memory.

### 6. LOCAL KNOWLEDGE BASE

Задача:

- хранить правила проекта;
- хранить ошибки;
- хранить решения;
- искать по локальной памяти.

### 7. DASHBOARD V2

Задача:

- кнопки;
- просмотр отчётов;
- просмотр задач;
- просмотр памяти;
- запуск безопасных действий.

## Priority 3

### 8. VOICE MODE

Задача:

- голосовая команда;
- голосовой ответ;
- локальный диктант.

### 9. BROWSER HELPER

Задача:

- открывать нужные страницы;
- собирать информацию;
- делать отчёт;
- без автопокупок и без автопубликации.

### 10. LOCAL AGENT TEAM

Будущий слой:

- File Agent;
- Photo Agent;
- Report Agent;
- ECOM Agent;
- CMD Agent.

Только после стабильного core.
