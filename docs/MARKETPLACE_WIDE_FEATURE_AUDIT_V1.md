# MARKETPLACE_WIDE_FEATURE_AUDIT_V1

## Goal
Expand ECOM OS beyond eBay thinking. Use best marketplace patterns from eBay, Amazon, Walmart, Etsy, Shopify, and Google Merchant Center to design reusable listing-quality blocks.

## Core universal principle
A strong marketplace listing is not only a title and photo. It is a full product detail system:
- search relevance
- conversion trust
- structured attributes
- image quality
- price competitiveness
- fulfillment clarity
- reviews/performance
- ads readiness
- policy compliance

## eBay patterns to support
- Category correctness
- Item specifics / aspects
- 1+ image required, multiple high-quality photos recommended
- Up to 12/24 photos depending route/category
- Accurate item description
- Clean basic HTML only
- Promoted Listings only after quality is good
- Revise safety: GET current -> merge -> PUT because inventory update can replace complete item data

Needed blocks:
- ebay_aspects_engine_v1
- ebay_photo_policy_checker_v1
- ebay_html_cleaner_v1
- ebay_promoted_listing_advisor_v1

## Amazon patterns to support
- Shared catalog / ASIN logic
- Strong title
- 3+ bullet points minimum for advertising readiness
- High-quality images
- Product description
- Relevant search terms / backend keywords
- A+ Content where eligible
- Featured Offer / Prime / reviews / in-stock status affect ad readiness

Needed blocks:
- amazon_catalog_match_engine_v1
- amazon_bullet_points_engine_v1
- amazon_backend_keywords_engine_v1
- amazon_a_plus_content_planner_v1
- amazon_ad_readiness_checker_v1

## Walmart patterns to support
- Listing Quality Score as a formal model
- Content quality: item name, description, key features, images
- Offer/price/shipping-related quality
- Ratings/reviews and seller performance signals

Needed blocks:
- walmart_listing_quality_score_adapter_v1
- universal_listing_quality_score_v1

## Etsy patterns to support
- Attributes act like search signals
- Tags are separate search opportunities
- First photo matters
- Title should be clear and readable, not overloaded
- Description and shop trust/brand story matter

Needed blocks:
- etsy_tags_engine_v1
- etsy_attributes_engine_v1
- etsy_story_description_engine_v1

## Shopify / own-store patterns to support
- Unique product descriptions, not manufacturer copy
- Product category/taxonomy
- Media, variants, metafields
- SEO title/meta description/URL handle
- Search engine listing preview
- Structured product data/schema
- Product page speed/mobile clarity

Needed blocks:
- shopify_seo_meta_engine_v1
- product_schema_engine_v1
- unique_description_engine_v1
- image_alt_text_engine_v1
- variant_metafields_engine_v1

## Google Merchant Center patterns to support
- Product data feed quality
- Product status/issues monitoring
- Title, description, image link, GTIN/brand/MPN, availability, price
- Feed diagnostics and product issue export

Needed blocks:
- google_merchant_feed_quality_checker_v1
- product_identifier_resolver_v1
- feed_diagnostics_monitor_v1

## Universal blocks to add to ECOM OS

### 1. marketplace_profile_engine_v1
Determines rules per marketplace: eBay/Amazon/Walmart/Etsy/Shopify/Google.

### 2. product_identity_engine_v1
Resolves brand, model, GTIN/EAN/UPC, MPN, ASIN where applicable.

### 3. universal_attribute_engine_v1
Maps item specifics/aspects/attributes/metafields across marketplaces.

### 4. universal_photo_engine_v2
Photo count, first photo, clean background, no duplicates, alt text, marketplace policy checks.

### 5. universal_copy_engine_v1
Generates title, bullets, description, HTML/A+ content style, marketplace-specific structure.

### 6. universal_quality_score_v1
Scoring model based on marketplace-specific weights.

### 7. ad_readiness_engine_v1
Ads only after listing quality pass. Marketplace-specific ad readiness checks.

### 8. learning_loop_engine_v1
Tracks views, clicks, watchers, sales, conversion, stale days, ad spend, score changes.

## Best build order
1. marketplace_profile_engine_v1
2. product_identity_engine_v1
3. competitor_intelligence_engine_v1
4. universal_quality_score_v1
5. universal_attribute_engine_v1
6. universal_photo_engine_v2
7. universal_copy_engine_v1
8. ad_readiness_engine_v1
9. telegram_approval_dashboard_v1
10. learning_loop_engine_v1

## Current project comparison
Already exists or partial:
- controlled eBay publish/revise
- token guard
- Telegram runtime
- photo engine beginnings
- listing engine beginnings
- price research
- competitor review beginnings
- state_control gates

Missing:
- marketplace profiles
- universal attribute mapping
- Amazon catalog/ASIN logic
- Amazon bullets/backend keywords/A+ planner
- Walmart listing quality adapter
- Etsy tags/attributes engine
- Shopify SEO/meta/schema engine
- Google Merchant feed diagnostics
- unified ad readiness
- unified learning loop

## Safety
Phone phase: docs/plans only.
Server phase later: read-only modules first.
No live publish/revise/delete without approval gate and readonly verify.
