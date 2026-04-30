# REUSE_AND_UPGRADE_AUDIT_V1

## Вывод
Лучший путь: не строить всё с нуля. В старом MVP уже есть нужные зачатки. Их надо перенести в governed runtime и улучшить.

## Existing blocks to reuse

### 1. Photo Engine
Found in old MVP state_control:
- finish_c_photo_engine_v1.json
- prepare_photo_engine_* files
- photo_engine smart/design rules

Use for:
- image intake
- image safety checks
- photo count rules
- future first-photo ranking
- photo improvement pipeline

Upgrade needed:
- choose best first photo
- rank photos by marketplace quality
- reject weak/duplicate/low-trust photos
- support 3-9 images baseline and future 12/24 where allowed

### 2. Listing Engine
Found:
- prepare_listing_engine_block_d_v1.json
- start_d_listing_engine_entry_v1.json

Use for:
- title generation
- German listing structure
- description generation

Upgrade needed:
- competitor-aware title generator
- keyword scoring
- HTML cleanup
- no raw broken HTML in live listing

### 3. Price Research
Found:
- prepare_price_research_v1.json
- price_research_read_only_v1.json
- start_e_price_research_entry_v1.json

Use for:
- competitor price range
- buy/sell margin logic
- pricing recommendations

Upgrade needed:
- sold-item logic
- active vs sold separation
- shipping-inclusive price comparison
- ad/promoted rate suggestion after quality score

### 4. Competitor Review
Found:
- run_save_adapter_001_competitor_review_v1.py
- adapter_001_competitor_review_v1.json

Use for:
- first version of Competitor Intelligence Engine

Upgrade needed:
- generic product input
- eBay search/sold data
- competitor title/photo/specifics extraction
- structured scoring

### 5. Controlled Runtime / Safety
Existing governed route is now proven:
- token refresh
- publish proof route
- photos-only revise
- readonly verify
- STOP_SAFE philosophy

Use for all future live actions.

## Best implementation order
1. Move existing analysis blocks into governed runtime docs/tools.
2. Build dry competitor_intelligence_engine_v1.
3. Build quality_scoring_engine_v1.
4. Build seo_title_engine_v1.
5. Build item_specifics_engine_v1.
6. Build html_description_engine_v1.
7. Build photo_ranking_engine_v1.
8. Build telegram_review_packet_v1.
9. Only then build controlled live revise integration.

## Internet-checked principles
- Inventory API update is complete replacement: always GET current item, merge, then PUT.
- Image URLs must be HTTPS and image list is part of product data.
- Item specifics/aspects are important and should use Taxonomy API/category norms.
- Description supports basic HTML only, no active content.
- Listing quality must be improved before promoted listing/ad strategy.

## Next safe build target
competitor_intelligence_engine_v1

Mode:
- read-only
- dry output JSON
- no live API action
- reusable for Telegram and PC workflows
