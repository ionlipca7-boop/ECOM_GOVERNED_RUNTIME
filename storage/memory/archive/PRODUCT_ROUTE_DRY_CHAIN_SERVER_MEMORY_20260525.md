# PRODUCT ROUTE DRY CHAIN SERVER MEMORY — 2026-05-25

## A = Archive purpose

This is a GitHub memory checkpoint for the server-side work completed in the ECOM OS V3 / V6.5 project.

GitHub did not have the new server dry-chain files. GitHub had 0/13 of the requested dry-chain files on branch `main`.

Because the GitHub chat cannot see the server, this archive records the full server-side logic, decisions, statuses, blockers, and next steps as memory.

This is not a production/live checkpoint. This is a dry/no-active-write checkpoint.

## B = Source of truth

Current source of truth: server clean root.

Server clean root:

`/home/ionlipca7/ecom_governed_runtime`

Legacy/live root:

`/home/ionlipca7/runtime_eco_v1`

GitHub role at this moment:

`ARCHIVE / MEMORY / SKELETON`, not current runtime truth.

Server Direct Eyes status from server-side chat:

`PASS / READONLY`

## C = Safety rules used during server work

The server-side chat followed these hard rules:

* no active bot write unless explicitly approved;
* no Telegram send;
* no restart;
* no eBay live;
* no publish;
* no revise;
* no delete;
* no cleanup;
* no secret print;
* no supplier photo download;
* no server git push;
* all new work was dry/candidate/checkpoint only.

## D = Product route decision

Three product lines were separated.

### PRIMARY product route

`mp_20260524_aliexpress_1005007495085039_dry_001`

Source key:

`aliexpress:1005007495085039`

Role:

`PRIMARY_REAL_PRODUCT_CANDIDATE`

This is the product route selected for continuing the V6.5 project.

### Cockpit donor / old UI binding

`aliexpress:1005005252938636`

Role:

`COCKPIT_UI_DONOR_REFERENCE`

This key was found as the old hardcoded cockpit/UI binding. It must not be active.

### Old donor / history route

`aliexpress:1005005210545584`

Role:

`OLD_DONOR_HISTORY`

This key exists in older current pointer/history. It must not be active.

### Sample skeleton product

`mp_20260517_usb_tester_sample_001`

Role:

`V6_5_DRY_AGENT_SAMPLE_ONLY`

Used only for earlier V6.5 dry agent skeleton tests. It must not be treated as real active product.

## E = Why product boundary was needed

The project had mixed product traces:

* old active pointer: `aliexpress:1005005210545584`;
* old cockpit/UI trace: `aliexpress:1005005252938636`;
* new real dry product route: `aliexpress:1005007495085039`.

Server-side decision:

Do not hard-replace randomly.

Instead, introduce a route boundary:

`PRODUCT_ROUTE_CONTEXT_V1`

All future cockpit, listing, photo, Telegram, HTML shop, and marketplace dry work should read product identity from route context instead of hardcoded old product keys.

## F = Completed server-side dry chain

The following dry chain was completed on server side.

### 1. Product route context

Status:

`PASS_STATIC_VALIDATE_PRODUCT_ROUTE_CONTEXT_V1_CANDIDATE_NO_ACTIVE_WRITE`

Purpose:

Create a candidate product route context that defines primary, donor, old, and sample routes.

Primary:

`aliexpress:1005007495085039`

Donors:

`aliexpress:1005005252938636`

`aliexpress:1005005210545584`

Sample:

`mp_20260517_usb_tester_sample_001`

No active bot write. No restart. No eBay/live.

### 2. Dry product passport

Initial validation had a false BLOCK because the validator used raw `False` safety flags inside `all(checks.values())`.

That was corrected.

Final status:

`PASS_FIX_STATIC_VALIDATE_DRY_PRODUCT_PASSPORT_FROM_PRODUCT_ROUTE_CONTEXT_V1_NO_ACTIVE_WRITE`

Purpose:

Build a dry product passport from `PRODUCT_ROUTE_CONTEXT_V1`.

### 3. Dry listing context

Status:

`PASS_BUILD_DRY_LISTING_CONTEXT_FROM_DRY_PRODUCT_PASSPORT_NO_ACTIVE_WRITE`

Purpose:

Create dry listing context for the primary product only.

Listing route:

`PRIMARY_PRODUCT_ONLY`

Marketplace mode:

`EBAY_DRY_CONTEXT_ONLY`

No publish. No revise. No live.

### 4. Dry photo plan

Status:

`PASS_BUILD_DRY_PHOTO_PLAN_FROM_LISTING_CONTEXT_NO_ACTIVE_WRITE`

Photo policy:

* listing photos must be own/generated/operator-uploaded only;
* supplier photos are reference only;
* supplier photo download is forbidden;
* photo TTL is 12 hours;
* cleanup gate remains closed until explicit approval.

No photo cleanup was done.

### 5. Dry HTML shop button map

Status:

`PASS_BUILD_DRY_HTML_SHOP_BUTTON_MAP_FROM_LISTING_AND_PHOTO_PLAN_NO_ACTIVE_WRITE`

Purpose:

Prepare dry buyer-facing HTML shop button map.

Important policy:

* button map only;
* no live listing edit;
* no eBay publish;
* no external redirect tracking;
* no product key mixing;
* future related products must have their own product IDs and boundaries.

### 6. Dry Telegram review card

Status:

`PASS_BUILD_DRY_TELEGRAM_REVIEW_CARD_FROM_ROUTE_LISTING_PHOTO_HTML_NO_ACTIVE_WRITE`

Purpose:

Prepare a dry Telegram review card for the operator.

Important:

* Telegram message was not sent;
* active bot was not touched;
* restart was not done.

Dry buttons prepared conceptually:

1. Confirm primary route.
2. Request missing product fields.
3. Prepare own/generated photos later.
4. Preview HTML shop buttons.
5. STOP without live.

### 7. Dry cockpit rebind candidate diff

Status:

`PASS_BUILD_DRY_COCKPIT_REBIND_CANDIDATE_DIFF_NO_ACTIVE_WRITE`

Server audit found:

* existing target files: 11;
* old cockpit key occurrences: 26.

Old cockpit key:

`aliexpress:1005005252938636`

Correct future pattern:

Do not directly hard-replace every string.

Instead use a product route resolver candidate that reads:

`PRODUCT_ROUTE_CONTEXT_V1`

The resolver candidate was designed as:

`product_route_context_resolver_candidate_v1.py`

No active bot files were modified.

### 8. Cockpit rebind approval packet

Status:

`PASS_CREATE_COCKPIT_REBIND_PATCH_APPROVAL_PACKET_NO_ACTIVE_WRITE`

Purpose:

Prepare approval packet for future cockpit rebind.

Approval needed later:

`APPROVE_COCKPIT_REBIND_PATCH_NO_ACTIVE_WRITE`

This does not apply the patch. It only records the approval requirement.

### 9. Final dry-chain checkpoint

Status:

`PASS_PRODUCT_ROUTE_DRY_CHAIN_FINAL_CHECKPOINT_NO_ACTIVE_WRITE`

Purpose:

Close the dry chain and record it as a final server checkpoint.

Completed chain:

1. Product route context.
2. Dry product passport.
3. Dry listing context.
4. Dry photo plan.
5. Dry HTML shop buttons.
6. Dry Telegram review card.
7. Dry cockpit rebind candidate.
8. Cockpit rebind approval packet.

No active write. No restart. No eBay/live. No delete/cleanup.

### 10. Production approval roadmap

Status:

`PASS_CREATE_PRODUCT_ROUTE_PRODUCTION_APPROVAL_ROADMAP_NO_ACTIVE_WRITE`

Purpose:

Define future approvals before any real active/production step.

Roadmap phases:

1. GitHub archive check.
2. Cockpit rebind approval.
3. Active bot patch candidate diff.
4. Active bot write no restart.
5. Restart gate.
6. Telegram smoke test.
7. Product data completion.
8. Own/generated photos.
9. Marketplace/eBay dry preflight.
10. Live/eBay only by explicit future approval.

All active gates remain closed.

### 11. Operator missing fields packet

Status:

`PASS_CREATE_OPERATOR_MISSING_FIELDS_PACKET_NO_ACTIVE_WRITE`

Purpose:

Because AliExpress readonly fetch is blocked, the project needs operator/manual product evidence.

Needed fields:

1. Product name in simple human terms.
2. Exact variant: color, size, model, quantity, set, plug type if relevant.
3. Five main features.
4. Package included.
5. Buy cost.
6. Shipping cost and time.
7. Target sale price.
8. Condition.
9. Country/item location.
10. Return policy.
11. Photo plan: own/generated/operator uploaded.

## G = Known blockers

### Blocker 1: AliExpress readonly fetch

Status:

`BLOCKED_READONLY_URL_FETCH_EMPTY_OR_FAILED`

Known cause:

AliExpress returned redirect loop / 302 issue during readonly fetch.

Effect:

Real product data extraction cannot rely only on automated server fetch.

Resolution path:

Use operator evidence/manual product fields first, then later investigate safe fetch improvement.

### Blocker 2: GitHub missing server dry-chain files

GitHub check found:

`0/13 files present`

Meaning:

GitHub does not yet have the new server dry-chain checkpoint files.

Resolution path:

Archive this memory checkpoint first, then later archive exact files if a safe transfer method exists.

### Blocker 3: Cockpit old hardcoded key

Old key:

`aliexpress:1005005252938636`

Found:

11 target files, 26 occurrences.

Resolution path:

Future patch must rebind cockpit to `PRODUCT_ROUTE_CONTEXT_V1`, not direct string replacement.

### Blocker 4: Active Telegram/cockpit not patched yet

Telegram card is dry only. Cockpit rebind is candidate only.

No active Telegram send happened.

No restart happened.

### Blocker 5: Photo cleanup not done

Photo TTL policy exists: 12 hours.

Cleanup gate remains closed.

No delete/cleanup performed.

## H = Telegram status

Telegram/V6.5 layer is not considered broken.

Known server state:

* `python_bot_count: 1`;
* Telegram V6.5 smoke test previously PASS;
* Decision Inbox Telegram runtime ready;
* Scheduled briefing runtime ready.

Current product route work did not modify active Telegram bot.

Future Telegram work requires approvals:

1. cockpit rebind approval;
2. active bot patch candidate diff;
3. active bot write no restart approval;
4. restart gate approval;
5. Telegram smoke test.

## I = Agents / skeleton status

V6.5 skeleton has dry/static agents already validated earlier:

* Master Product Registry Agent;
* Product Intake Pipeline Agent;
* Listing Studio Agent;
* Marketplace Guard Agent;
* Stock Finance Agent;
* Decision Inbox Agent;
* Orders/Returns/Customer Agent;
* Performance Lifecycle Agent;
* Teacher Memory Agent;
* Archivist Checkpoint Agent;
* Telegram Decision Inbox Adapter;
* Scheduled Briefing Adapter.

Many earlier agents used sample product:

`mp_20260517_usb_tester_sample_001`

Current real product route is now:

`mp_20260524_aliexpress_1005007495085039_dry_001`

Future work should connect real product route into the agent layer without mixing it with sample product.

## J = Legacy / donor policy

Legacy/live root:

`/home/ionlipca7/runtime_eco_v1`

Role:

Donor/history only.

Do not activate old eBay/live scripts from legacy.

Do not cleanup/delete legacy until explicit future approval.

Do not mix legacy product keys with current primary route.

## K = Server files created or referenced

These server files were created/referenced during dry chain, but GitHub chat may not have their content:

* `storage/runtime_bridge/candidates/PRODUCT_ROUTE_CONTEXT_V1_CANDIDATE_NO_ACTIVE_WRITE.json`
* `storage/runtime_bridge/candidates/DRY_PRODUCT_PASSPORT_FROM_PRODUCT_ROUTE_CONTEXT_V1.json`
* `storage/runtime_bridge/candidates/DRY_LISTING_CONTEXT_FROM_PRODUCT_PASSPORT_V1.json`
* `storage/runtime_bridge/candidates/DRY_PHOTO_PLAN_FROM_LISTING_CONTEXT_V1.json`
* `storage/runtime_bridge/candidates/DRY_HTML_SHOP_BUTTON_MAP_FROM_LISTING_AND_PHOTO_PLAN_V1.json`
* `storage/runtime_bridge/candidates/DRY_TELEGRAM_REVIEW_CARD_FROM_ROUTE_LISTING_PHOTO_HTML_V1.json`
* `storage/runtime_bridge/candidates/DRY_COCKPIT_REBIND_CANDIDATE_DIFF_NO_ACTIVE_WRITE.json`
* `storage/runtime_bridge/candidates/product_route_context_resolver_candidate_v1.py`
* `storage/state_control/DRY_COCKPIT_REBIND_CANDIDATE_DIFF_NO_ACTIVE_WRITE.diff`
* `storage/approval/COCKPIT_REBIND_PATCH_APPROVAL_PACKET_NO_ACTIVE_WRITE_RU.md`
* `storage/memory/archive/PRODUCT_ROUTE_DRY_CHAIN_FINAL_CHECKPOINT_20260525T065733Z.json`
* `storage/memory/archive/PRODUCT_ROUTE_DRY_CHAIN_FRONT_20260525T065733Z.txt`
* `storage/control_room/PRODUCT_ROUTE_DRY_CHAIN_FINAL_CHECKPOINT_POINTER.json`
* `storage/runtime_bridge/candidates/PRODUCT_ROUTE_PRODUCTION_APPROVAL_ROADMAP_V1.json`
* `storage/approval/PRODUCT_ROUTE_PRODUCTION_APPROVAL_ROADMAP_RU.md`
* `storage/control_room/PRODUCT_ROUTE_PRODUCTION_APPROVAL_ROADMAP_POINTER.json`
* `storage/decision_inbox/OPERATOR_MISSING_FIELDS_PRIMARY_PRODUCT_1005007495085039_V1.json`
* `storage/control_room/OPERATOR_MISSING_FIELDS_PRIMARY_PRODUCT_POINTER.json`

## L = Current next safe action

Current safe next action:

`WAIT_OPERATOR_PRODUCT_FIELDS_OR_GITHUB_ARCHIVE_RESULT`

Meaning:

Either wait for GitHub archive confirmation, or continue filling missing product fields from operator/manual evidence.

## M = What must not be done yet

Do not:

* apply cockpit rebind to active bot;
* restart Telegram bot;
* send Telegram review card;
* publish/revise eBay listing;
* perform eBay live action;
* delete or cleanup files/photos;
* print secrets;
* use old donor products as active;
* treat sample product as real listing product.

## N = Suggested next commit result

After saving this file, respond:

A = archive memory PASS/BLOCK
B = file created path
C = commit sha if committed
D = safety checks
E = next step for server-side chat
FINISH = exact status

FINISH value should be:

`GITHUB_MEMORY_ARCHIVE_PRODUCT_ROUTE_DRY_CHAIN_SERVER_MEMORY_SAVED_NO_SERVER_ACCESS_NO_LIVE_NO_RESTART_NO_EBAY`
