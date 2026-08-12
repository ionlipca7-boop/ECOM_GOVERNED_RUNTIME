# PHASE 0 — READONLY INVENTORY MATRIX V1

Status: ACTIVE

Goal: establish what already exists before installing or duplicating anything.

| Area | Known existing source | Initial disposition | Required verification |
|---|---|---|---|
| Production ECOM OS | D:\ECOM_OS_PRO_LOCAL_OPERATOR_BUILD | KEEP / CANONICAL | current owners, registries, browser contracts, coordinator pointers |
| Knowledge memory | D:\ECOM_KNOWLEDGE_LAB | REUSE READONLY | IWE guard, vault, dashboard, Obsidian map, current coverage |
| Governed runtime | D:\ECOM_GOVERNED_RUNTIME | REUSE | runtime/governance/tools vs production owners |
| Local assistant | D:\ION_LOCAL_ASSISTANT_REPO | AUDIT / REUSE PARTS | duplicate capabilities, Windows helpers, dashboard, safety |
| Codex workspace | D:\ECOM_OS_V7_3C_CODEX_WORKSPACE | REUSE AS REVIEWER INPUT | exact current purpose and isolation |
| Photo worker | D:\ECOM_PHOTO_WORKER | REUSE OWNER | photo/design responsibilities and interface |
| Marketplace/browser tooling | ECOM OS V7 + existing browser profiles | REUSE / NO SECOND OWNER | current browser owner, persistent-session options, QA hooks |
| gstack reference | garrytan/gstack | ADAPT CONCEPTS | skills, browser daemon, design review, QA, context, learn, guard |
| Agent communication | Coordinator Inbox + handoffs | UPGRADE | mailbox, ACK, cursor, lease, task state |
| Model layer | not yet selected | MISSING / DEFER | local-first provider evaluation after core |
| Safe AI Gate | debt/architecture only | BUILD LATER | allowlist, PII/secrets, tool approval, audit |

## Classification vocabulary
- KEEP: canonical existing owner; do not replace.
- REUSE: connect to existing component.
- ADAPT: borrow mechanism but implement to ECOM governance.
- MISSING: justified new component.
- DO_NOT_DUPLICATE: creating a second owner would be an architectural defect.

## Phase 0 exit criteria
1. Every relevant Windows root classified.
2. Existing owner/component overlap documented.
3. Lab-only capabilities separated from production capabilities.
4. No production write performed.
5. Exact Phase 1 Windows skeleton confirmed before materialization.
