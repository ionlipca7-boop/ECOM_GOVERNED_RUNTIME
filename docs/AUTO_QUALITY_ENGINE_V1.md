# AUTO_QUALITY_ENGINE_V1

## Цель
Сделать систему, которая не просто публикует товар, а автоматически улучшает листинг до уровня лучше конкурентов.

## Рабочий порядок блоков

### 1. Product Intake
Вход из Telegram, компьютера или файла: фото, ссылка, название, цена, заметки оператора.

### 2. Product Detection
Определить бренд, модель, тип товара, категорию, базовые характеристики.

### 3. Competitor Intelligence
Найти похожие и идентичные товары на eBay и других источниках. Собрать titles, prices, photos, item specifics, descriptions, delivery/trust patterns.

### 4. Multi-Agent Analysis
Минимум 3 роли:
- Analyst: собирает факты и структуру рынка.
- Optimizer: предлагает лучший title, specifics, description, photo order.
- Critic: проверяет слабые места, риск ошибок, SEO и конкурентность.

### 5. Quality Scoring
Оценить listing по шкале:
- photos
- first photo
- title SEO
- item specifics
- description
- price
- shipping/payment clarity
- trust
- promoted listing readiness

### 6. Auto Improvement Plan
Сформировать dry plan: что изменить, почему, риск, expected benefit.

### 7. Approval Gate
Показать оператору в Telegram: old vs new, score before/after, approve/reject.

### 8. Controlled Execute
Только после approval: token guard, readonly verify, exact executor path check, one revise/publish.

### 9. Verify
Readonly verify after action: inventory, offer, image count, price, category, title, specifics.

### 10. Learning Loop
Собирать performance: views, watchers, sales, stale days, failed patterns. Предлагать refresh/revise/replace.

## Приоритет внедрения
1. Competitor Intelligence Engine
2. Quality Scoring Engine
3. SEO Title Engine
4. Item Specifics Engine
5. HTML Description Engine
6. Photo Ranking Engine
7. Telegram Approval Dashboard
8. Learning Loop
9. n8n Orchestration

## Safety
- No live action without approval.
- No old executors.
- Dry first, live only after gate.
- Readonly verify before and after live action.
- One route only: A -> B -> FINISH -> STOP.
- Phone phase = planning/audit only.

## Source principles checked
- eBay photo guidance: best first photo, high quality, neutral background.
- eBay listing best practices: searchable title, detailed description, competitive price, right category.
- eBay item specifics: more complete specifics improve buyer matching and filters.
- Promoted listings should come after listing quality is strong.
