# TOP_SELLER_PERFORMANCE_INTELLIGENCE_V1

## Purpose
This document captures important marketplace-performance ideas for future agents/helpers.

The system must learn from sellers and listings that already have strong sales history.

## Core insight
For eBay and similar marketplaces, do not only analyze product text.
Analyze performance signals:
- sold count
- sales history
- listing age
- quantity strategy
- restocking behavior
- seller trust
- photo quality
- item specifics density
- shipping/returns clarity
- price position
- description quality

## Important rule
Preserve strong listings when possible.

Do not blindly delete and recreate listings, because successful listings may have valuable sales history.
Prefer:
- controlled revise
- refresh
- quantity restock
- photo/title/specifics improvement
- keep listing authority when useful

## Target sellers to analyze
Future competitor agents should prioritize:
- sellers/listings with 100+ sold
- sellers/listings with 500+ sold
- sellers/listings with 1000+ sold
- multi-quantity listings
- long-living listings
- listings that appear high in search repeatedly

## What to extract from top sellers
For each strong listing:
- title structure
- title keywords
- first photo style
- photo count
- item specifics/aspects
- price
- shipping model
- return policy style
- description structure
- quantity sold
- visible sales history
- seller rating/trust
- promoted/sponsored visibility if detectable

## Agent roles

### Market Analyst
Finds high-performing listings and records objective facts.

### SEO Optimizer
Extracts title, keyword, and structure patterns.

### Photo Critic
Evaluates first photo, image order, trust feeling, and visual quality.

### Listing Critic
Finds missing specifics, weak descriptions, category risks, and buyer trust gaps.

### Strategy Agent
Decides whether to improve, refresh, restock, promote, or replace.

## How this connects to our project
This feeds:
- Competitor Intelligence Engine
- Quality Scoring Engine
- SEO Title Engine
- Photo Ranking Engine
- Item Specifics Engine
- Performance Intelligence Engine
- Learning Loop Engine

## Future output
Create:
- top_seller_pattern_dataset_v1.json
- sales_history_pattern_analysis_v1.json
- listing_authority_preservation_rules_v1.json
- performance_based_revise_recommendations_v1.json

## Safety
Read-only analysis first.
No live revise/publish/delete without approval gate.
