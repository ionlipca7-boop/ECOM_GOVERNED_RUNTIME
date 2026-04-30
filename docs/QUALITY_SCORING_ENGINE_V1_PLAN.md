# QUALITY_SCORING_ENGINE_V1_PLAN

## Goal
Create a read-only scoring engine that evaluates listing quality before any publish/revise action.

## Why
The system can now publish/revise safely. The next level is to automatically decide whether a listing is strong enough to compete.

## Multi-source principles checked
- eBay Inventory API: createOrReplaceInventoryItem is complete replacement. Future revise must always use GET current -> merge -> PUT.
- eBay Inventory API: imageUrls must be HTTPS; up to 24 pictures may be allowed in many categories, but baseline remains controlled.
- eBay Inventory API: product.description supports only basic HTML and forbids active content.
- eBay Taxonomy/API guidance: category aspects/item specifics are required or recommended and should be category-aware.
- Seller best practices: clear photos, strong first photo, detailed description, competitive price, searchable title.
- Additional seller sources also support: more high-quality photos and clear white/neutral backgrounds improve buyer trust and listing quality.

## Current baseline
Minimum safe baseline:
- photos: 3-9
- title exists
- category valid
- price valid
- policies present
- readonly verify pass

Future quality baseline:
- photos target: 8-12 where possible
- first photo should be clean, product-focused, high contrast, no messy background
- item specifics should be category-complete
- title should include brand + model + product type + core keywords
- description should be clean German HTML with sections
- price should be competitor-aware

## Score model 0-100

### 1. Photos: 20
- 0-5: at least 3 images
- 0-5: target 8-12 images where possible
- 0-5: first image quality
- 0-5: no duplicate/weak/misleading images

### 2. Title SEO: 15
- brand/model present
- product type present
- buyer keywords present
- no keyword spam
- readable German marketplace title

### 3. Item specifics/aspects: 20
- required aspects present
- recommended aspects present
- brand/model/type/MPN/EAN logic handled
- category norms checked

### 4. Description/HTML: 15
- clean basic HTML only
- no raw/broken HTML
- sections: overview, features, specs, compatibility, package, shipping/returns note
- German commercial tone

### 5. Price competitiveness: 10
- market price range checked
- shipping-inclusive comparison
- margin logic
- not blindly cheapest

### 6. Shipping/payment/trust clarity: 10
- policy IDs present
- buyer-facing delivery clarity
- returns clarity
- trust signals

### 7. Promotion readiness: 5
- ads only after quality pass
- recommended ad rate based on margin and competition

### 8. Critic risk score: 5
- detects missing/unsafe claims
- detects weak first photo
- detects category mismatch
- detects overpromising

## Output JSON
quality_scoring_engine_v1.json:
- status
- sku/listing_id/offer_id
- score_total
- score_breakdown
- pass_threshold
- blocking_gaps
- improvement_plan
- critic_notes
- next_allowed_action

## Thresholds
- 0-59: BLOCKED_LOW_QUALITY
- 60-74: NEEDS_IMPROVEMENT_DRY_PLAN
- 75-89: READY_FOR_OPERATOR_REVIEW
- 90-100: STRONG_LISTING_READY

## Reuse
Use old MVP blocks:
- photo engine
- listing engine
- price research
- competitor review

Use governed runtime for:
- state_control outputs
- approval gates
- token guard only for future live actions
- readonly verify

## Next build target
Create dry skeleton later:
- storage/tools/quality_scoring_engine_v1.py
- storage/state_control/quality_scoring_engine_v1.json

No live actions in v1.
