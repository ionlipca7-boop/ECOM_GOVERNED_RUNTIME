# COMPETITOR_INTELLIGENCE_ENGINE_V1_PLAN

## Цель
Создать read-only engine, который по входному товару собирает конкурентов, анализирует качество их листингов и готовит улучшения для нашего dry revise plan.

## Reuse из старого проекта
Найдено в старом MVP:
- run_save_adapter_001_competitor_review_v1.py
- storage/exports/adapter_001_competitor_review_v1.json
- price research blocks
- photo engine blocks
- listing engine state blocks

Вывод: строить не с нуля. Переносить идеи в governed runtime и делать универсальный v1.

## External checks
Проверено по eBay docs и seller guidance:
- Inventory update через createOrReplaceInventoryItem = complete replacement, значит live revise должен быть GET current -> merge -> PUT.
- product.imageUrls требуют HTTPS; eBay позволяет много фото, но наш baseline остается 3-9 до следующего стандарта.
- Taxonomy API getItemAspectsForCategory нужен для required/recommended aspects.
- Description supports basic HTML only; no active content.
- Listing quality first, promoted ads after quality score.

## Input
- product_name
- brand/model if known
- category_id
- marketplace
- our current listing snapshot
- optional operator notes/photo URLs

## Data to collect per competitor
- item_id / URL
- title
- price
- shipping cost / delivery promise
- photo count
- first photo style
- item specifics / aspects
- description structure
- seller trust signals
- promoted/sponsored visibility if detectable
- sold/completed signal where available

## Agent roles

### Analyst
Collects factual market data.

### Optimizer
Builds better title, specifics, photo order, description, price/ad suggestions.

### Critic
Challenges weak claims, detects missing aspects, checks against eBay rules and competitor quality.

## Output JSON
competitor_intelligence_engine_v1.json:
- status
- input_product
- competitors[]
- market_price_range
- keyword_map
- photo_patterns
- required_aspects
- recommended_aspects
- quality_gaps
- suggested_improvements
- critic_notes
- next_allowed_action

## Scoring
Score 0-100:
- title SEO: 15
- item specifics: 20
- photos: 20
- description: 15
- price: 10
- shipping/payment clarity: 10
- trust/commercial quality: 10

## Safety
- read-only only
- no live revise
- no publish
- no delete
- output dry JSON only
- approval required before any future live action

## Next implementation step
Create governed runtime skeleton:
- storage/tools/competitor_intelligence_engine_v1.py
- storage/state_control/competitor_intelligence_engine_v1.json

Mode for first version:
- input via JSON/manual links
- web/eBay source data can be pasted or collected later
- no live eBay writes
