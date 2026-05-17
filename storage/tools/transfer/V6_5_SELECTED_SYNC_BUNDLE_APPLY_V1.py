#!/usr/bin/env python3
import json
import pathlib
import datetime

ROOT = pathlib.Path('/home/ionlipca7/ecom_governed_runtime')
ACTIVE_ROOT = pathlib.Path('/home/ionlipca7/runtime_eco_v1')
TS = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
OUT = ROOT / 'storage' / 'state_control' / f'V6_5_SELECTED_SYNC_BUNDLE_APPLY_RESULT_{TS}.json'

FILES = {
 'storage/memory/archive/ECOM_OS_V3_MASTER_PLAN_V6_5_COMPANY_OS_20260517T163000Z/00_MANIFEST_RU.md': '''# ECOM OS V3 MASTER PLAN V6.5 MANIFEST
Status: PASS_APPROVED_BY_ION_FOR_ARCHIVE
Updated UTC: 20260517T163000Z
Mode: SERVER_SYNCED_MEMORY_COPY

V6.5 = ECOM Company Operating System.
GitHub remains canonical source of truth.
Server clean root receives selected memory/contracts only.
Runtime activation is separate.
''',
 'storage/memory/archive/ECOM_OS_V3_MASTER_PLAN_V6_5_COMPANY_OS_20260517T163000Z/01_MASTER_PLAN_V6_5_COMPANY_OS_RU.md': '''# ECOM OS V3 MASTER PLAN V6.5 COMPANY OS
Status: SERVER_SYNCED_MEMORY_COPY

Core concept:
Ion = director.
Telegram = director cockpit.
GitHub = memory and rules.
Server = runtime office.
Agents = departments.
Master Product = main product object.
Listing Studio = listing production.
Decision Inbox = action cards.
Marketplace Guard = safety layer.
Stock Finance = stock and margin.
Teacher Memory = learning loop.
''',
 'storage/memory/archive/ECOM_OS_V3_MASTER_PLAN_V6_5_COMPANY_OS_20260517T163000Z/02_ROADMAP_TO_FINISH_STOP_V6_5_RU.md': '''# ECOM OS V3 ROADMAP TO FINISH STOP V6.5
Status: SERVER_SYNCED_MEMORY_COPY

Route: A -> B -> FINISH -> STOP.
No parallel branches.

Phases:
1 Telegram Cockpit foundation.
2 Master Product Registry.
3 Product Intake Pipeline.
4 Listing Studio.
5 Marketplace Guard.
6 Stock Finance Ledger.
7 Orders Returns Customers.
8 Performance Lifecycle.
9 Research Ideas.
10 Decision Inbox and Briefing.
11 Teacher Memory.
12 Transfer Restore.
''',
 'storage/memory/archive/ECOM_OS_V3_MASTER_PLAN_V6_5_COMPANY_OS_20260517T163000Z/03_PASS_NOT_PASS_LEDGER_V6_5_RU.md': '''# ECOM OS V3 PASS NOT PASS LEDGER V6.5
Status: SERVER_SYNCED_MEMORY_COPY

PASS:
- V6.5 architecture approved.
- Telegram recovered earlier.
- Safety gates preserved.
- GitHub first route confirmed.

NOT PASS:
- runtime V6.5 activation.
- active bot migration.
- full agent runtime code.
- server candidate bridge.

Current server step:
selected memory and contract sync to clean root only.
''',
 'storage/memory/archive/ECOM_OS_V3_MASTER_PLAN_V6_5_COMPANY_OS_20260517T163000Z/04_NEXT_CHAT_FRONT_V6_5_RU.txt': '''ION / E1 NEXT CHAT FRONT V6.5
Work in Russian.
GitHub first.
Server is runtime layer.
Current route: V6.5 selected sync to clean root completed or pending verification.
No runtime activation without gate.
''',
 'storage/memory/archive/ECOM_OS_V3_MASTER_PLAN_V6_5_COMPANY_OS_20260517T163000Z/06_CODE_AGENT_BRIEF_V6_5_RU.md': '''# CODE AGENT BRIEF V6.5
Status: SERVER_SYNCED_MEMORY_COPY

Code-agent may help with static review, dry samples, validators, candidate code and transfer plans.
Server activation requires separate gate.
''',
 'storage/architecture/master_product/MASTER_PRODUCT_REGISTRY_V6_5_SCHEMA_RU.md': '''# MASTER PRODUCT REGISTRY V6.5 SCHEMA
Status: SERVER_SYNCED_CONTRACT_COPY

Master Product fields:
product_id, status, source, evidence, product_passport, item_variations, listing_angles, linked_listings, marketplace_relations, stock_ledger_ref, finance_ref, performance_memory, risk_blocker_layer.
''',
 'storage/contracts/master_product/MASTER_PRODUCT_OBJECT_CONTRACT_V1_RU.md': '''# MASTER PRODUCT OBJECT CONTRACT V1
Status: SERVER_SYNCED_CONTRACT_COPY

Required:
product_id, product_status, source, evidence, product_passport, item_variations array, listing_angles array, linked_listings array, marketplace_relations array, stock_ledger_ref, finance_ref, performance_memory, risk_blocker_layer.
''',
 'storage/contracts/master_product/ITEM_VARIATION_CONTRACT_V1_RU.md': '''# ITEM VARIATION CONTRACT V1
Status: SERVER_SYNCED_CONTRACT_COPY

Variation fields:
variation_id, status, variation_type, names, attributes, sku, photos, price, stock, marketplace_refs, risk_blocker_layer.
''',
 'storage/contracts/master_product/LISTING_ANGLE_CONTRACT_V1_RU.md': '''# LISTING ANGLE CONTRACT V1
Status: SERVER_SYNCED_CONTRACT_COPY

Listing angle fields:
listing_angle_id, status, buyer_intent, target_customer, seo_keywords, aeo_keywords, title_strategy, html_strategy, photo_strategy, duplicate_guard, marketplace_refs, risk_blocker_layer.
''',
 'storage/contracts/master_product/MASTER_PRODUCT_PASS_CRITERIA_V1_RU.md': '''# MASTER PRODUCT PASS CRITERIA V1
Status: SERVER_SYNCED_CONTRACT_COPY

PASS if required Master Product, variation, listing angle and safety fields exist and no runtime action is performed by the object layer.
''',
 'storage/contracts/agents/AGENT_REGISTRY_V6_5_RU.md': '''# AGENT REGISTRY V6.5
Status: SERVER_SYNCED_CONTRACT_COPY

Agents:
01 Master Product Registry Agent
02 Product Intake Pipeline Agent
03 Listing Studio Agent
04 Marketplace Guard Agent
05 Stock Finance Agent
06 Decision Inbox Agent
07 Orders Returns Customer Agent
08 Performance Lifecycle Agent
09 Research Ideas Agent pending
10 Teacher Memory Agent
11 Archivist Checkpoint Agent
12 Transfer Restore Agent
''',
 'storage/contracts/agents/MASTER_PRODUCT_REGISTRY_AGENT_CONTRACT_V6_5_RU.md': '''# MASTER PRODUCT REGISTRY AGENT CONTRACT V6.5
Mission: create and maintain Master Product records.
PASS: stable product_id, evidence, variations, listing angles, links, stock refs, risk layer.
''',
 'storage/contracts/agents/PRODUCT_INTAKE_PIPELINE_AGENT_CONTRACT_V6_5_RU.md': '''# PRODUCT INTAKE PIPELINE AGENT CONTRACT V6.5
Mission: prepare product inputs for Master Product Registry.
PASS: intake packet, missing fields, evidence refs, new/existing proposal, decision card.
''',
 'storage/contracts/agents/LISTING_STUDIO_AGENT_CONTRACT_V6_5_RU.md': '''# LISTING STUDIO AGENT CONTRACT V6.5
Mission: create listing draft packet from Master Product.
PASS: passport, German title, German HTML, item specifics, photo order, draft packet.
''',
 'storage/contracts/agents/MARKETPLACE_GUARD_AGENT_CONTRACT_V6_5_RU.md': '''# MARKETPLACE GUARD AGENT CONTRACT V6.5
Mission: check listing draft before external channel activation.
PASS: category, specifics, duplicate field, payload completeness, risk result, operator card.
''',
 'storage/contracts/agents/STOCK_FINANCE_AGENT_CONTRACT_V6_5_RU.md': '''# STOCK FINANCE AGENT CONTRACT V6.5
Mission: track stock, costs, fees, margin and profit.
PASS: stock event schema, stock calculation, cost, fee, margin, conflict warning.
''',
 'storage/contracts/agents/DECISION_INBOX_AGENT_CONTRACT_V6_5_RU.md': '''# DECISION INBOX AGENT CONTRACT V6.5
Mission: collect agent action cards for Ion.
PASS: inbox item schema, states, product link, agent source, decision history, Russian text.
''',
 'storage/contracts/agents/ORDERS_RETURNS_CUSTOMER_AGENT_CONTRACT_V6_5_RU.md': '''# ORDERS RETURNS CUSTOMER AGENT CONTRACT V6.5
Mission: prepare customer service decisions and German reply drafts.
PASS: order event, return event, buyer draft, German template support, decision card.
''',
 'storage/contracts/agents/PERFORMANCE_LIFECYCLE_AGENT_CONTRACT_V6_5_RU.md': '''# PERFORMANCE LIFECYCLE AGENT CONTRACT V6.5
Mission: observe listing lifecycle and propose improvements.
PASS: day signals, metrics fields, proposal states, product link, listing link, decision card.
''',
 'storage/contracts/agents/TEACHER_MEMORY_AGENT_CONTRACT_V6_5_RU.md': '''# TEACHER MEMORY AGENT CONTRACT V6.5
Mission: record lessons and governance proposals.
PASS: lesson schema, source reference, pass/block type, proposal field, governance card.
''',
 'storage/contracts/agents/ARCHIVIST_CHECKPOINT_AGENT_CONTRACT_V6_5_RU.md': '''# ARCHIVIST CHECKPOINT AGENT CONTRACT V6.5
Mission: record PASS, BLOCK, STOP and route transitions.
PASS: checkpoint schema, status, next action, changed files, references, no private values.
''',
 'storage/contracts/agents/TRANSFER_RESTORE_AGENT_CONTRACT_V6_5_RU.md': '''# TRANSFER RESTORE AGENT CONTRACT V6.5
Mission: prepare selected file transfer and restore plans.
PASS: source paths, target root, selected file list, precheck, postcheck, rollback note.
''',
 'storage/samples/master_product/MASTER_PRODUCT_DRY_SAMPLE_OBJECT_V1.json': '''{
  "status": "DRY_SAMPLE_OBJECT_NO_RUNTIME",
  "updated_utc": "20260517T194500Z",
  "mode": "GITHUB_FIRST_NO_SERVER_NO_RUNTIME_NO_PRIVATE_VALUES",
  "product_id": "mp_20260517_usb_tester_sample_001",
  "product_status": "draft",
  "source": {"source_type": "manual_sample", "source_url": "", "source_platform": "manual", "source_ref": "dry_sample_only"},
  "evidence": {"raw_inputs": [], "photos": [], "receipts": [], "operator_notes": ["Dry sample object for V6.5 validation."], "audit_files": []},
  "product_passport": {"name_ru": "Тестовый USB измеритель", "name_de": "USB Messgeraet Testmuster", "brand": "", "model": "", "category_hint": "electronics_accessory", "key_features": ["dry sample"], "technical_specs": {}, "included_items": [], "warnings": []},
  "item_variations": [{"variation_id": "var_001", "status": "draft", "variation_type": "bundle", "variation_name_ru": "Один товар", "variation_name_de": "Einzelartikel", "attributes": {}, "sku": "DRY-SAMPLE-USB-TESTER-001", "photos": [], "price": {"currency": "EUR", "amount": null}, "stock": {"quantity_total": null, "quantity_available": null, "quantity_reserved": 0}, "marketplace_refs": [], "risk_blocker_layer": {"risk_status": "clear", "risks": [], "blockers": []}}],
  "listing_angles": [{"listing_angle_id": "angle_001", "status": "draft", "angle_name_ru": "Базовый технический листинг", "angle_name_de": "Technisches Basisangebot", "buyer_intent": "technical accessory", "target_customer": "general buyer", "seo_keywords": [], "aeo_keywords": [], "title_strategy": {"main_title_de": "", "title_variants": []}, "html_strategy": {"main_message_ru": "", "main_message_de": "", "sections": []}, "photo_strategy": {"main_photo_rule": "clean product photo only", "photo_order": [], "variant_photo_rules": []}, "duplicate_guard": {"status": "not_checked", "reason": "dry sample only"}, "marketplace_refs": [], "risk_blocker_layer": {"risk_status": "clear", "risks": [], "blockers": []}}],
  "linked_listings": [], "marketplace_relations": [], "stock_ledger_ref": "", "finance_ref": "", "performance_memory": [],
  "risk_blocker_layer": {"risk_status": "clear", "risks": [], "blockers": [], "last_check_utc": "20260517T194500Z"}
}
''',
 'storage/validators/master_product/MASTER_PRODUCT_DRY_VALIDATOR_PLAN_V1_RU.md': '''# MASTER PRODUCT DRY VALIDATOR PLAN V1
Status: SERVER_SYNCED_VALIDATOR_PLAN_COPY

Required top-level fields:
status, updated_utc, mode, product_id, product_status, source, evidence, product_passport, item_variations, listing_angles, linked_listings, marketplace_relations, stock_ledger_ref, finance_ref, performance_memory, risk_blocker_layer.
PASS: fields exist, arrays are arrays, risk layer exists, no runtime activation fields.
''',
 'storage/transfer/V6_5_SELECTED_FILE_MANIFEST_RU.md': '''# V6.5 SELECTED FILE MANIFEST
Status: SERVER_SYNCED_TRANSFER_MANIFEST_COPY
Target clean root: /home/ionlipca7/ecom_governed_runtime
Active root not touched: /home/ionlipca7/runtime_eco_v1
Selected file count expected by bundle: 29.
''',
 'storage/transfer/V6_5_GITHUB_TO_SERVER_TRANSFER_PLAN_RU.md': '''# V6.5 GITHUB TO SERVER TRANSFER PLAN
Status: SERVER_SYNCED_TRANSFER_PLAN_COPY
Method: selected file sync only.
No bulk restore. No blind pull. No active bot root change. Runtime activation is separate.
''',
 'storage/transfer/V6_5_SERVER_PRETRANSFER_BLACK_WINDOW_CHECK_RU.md': '''# V6.5 SERVER PRETRANSFER BLACK WINDOW CHECK
Status: SERVER_SYNCED_CHECK_COPY
Use black-window checks before transfer. Verify clean root, active root, process path, selected files, and safety gates.
''',
 'storage/route/V6_5_CURRENT_BUILD_STATUS_AND_NEXT_STEPS_RU.md': '''# V6.5 CURRENT BUILD STATUS AND NEXT STEPS
Status: SERVER_SYNCED_ROUTE_COPY
PASS: V6.5 contracts and dry sample selected for clean root sync.
NEXT: verify selected sync, create clean-root V6.5 server pointer, then build candidate runtime bridge later.
'''
}

def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if not ACTIVE_ROOT.exists():
        decision = 'STOP_ACTIVE_ROOT_MISSING'
        written = []
    else:
        written = []
        for rel, content in FILES.items():
            path = ROOT / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content.rstrip() + '\n', encoding='utf-8')
            written.append(rel)
        decision = 'PASS_BUNDLE_APPLY_COMPLETE'
    present = [p for p in FILES if (ROOT / p).exists()]
    missing = [p for p in FILES if not (ROOT / p).exists()]
    audit = {
        'status': 'V6_5_SELECTED_SYNC_BUNDLE_APPLY_RESULT',
        'updated_utc': TS,
        'mode': 'OFFLINE_BUNDLE_SELECTED_FILES_ONLY_NO_RUNTIME',
        'target_root': str(ROOT),
        'active_root_not_touched': str(ACTIVE_ROOT),
        'selected_count': len(FILES),
        'written_count': len(written),
        'present_count': len(present),
        'missing_count': len(missing),
        'missing': missing,
        'safety': {
            'git_pull_performed': False,
            'bot_restarted': False,
            'active_root_changed': False,
            'runtime_activated': False
        },
        'decision': decision if not missing else 'PARTIAL_BUNDLE_APPLY_REVIEW_REQUIRED',
        'next_allowed_action': 'VERIFY_SELECTED_SYNC_THEN_CREATE_SERVER_V6_5_POINTER_NO_RUNTIME' if not missing and decision == 'PASS_BUNDLE_APPLY_COMPLETE' else 'STOP_REVIEW_BUNDLE_APPLY'
    }
    OUT.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding='utf-8')
    print('V6_5_SELECTED_SYNC_BUNDLE_APPLY_RESULT')
    print('OUT=' + str(OUT))
    print('SELECTED_COUNT=' + str(len(FILES)))
    print('WRITTEN_COUNT=' + str(len(written)))
    print('PRESENT_COUNT=' + str(len(present)))
    print('MISSING_COUNT=' + str(len(missing)))
    print('DECISION=' + audit['decision'])
    print('---- JSON ----')
    print(OUT.read_text(encoding='utf-8', errors='replace')[:16000])

if __name__ == '__main__':
    main()
