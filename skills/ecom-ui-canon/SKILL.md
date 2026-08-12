---
name: ecom-ui-canon
version: 1.0.0
mode: readonly
purpose: Compile the current ECOM OS UI/business truth into one machine-readable design canon before any design generation or repair.
---

# ECOM UI CANON

## Mandatory rule
Do not design, repair, simplify, remove, merge, or add any UI control before this skill has produced a current canon packet from verified project sources.

## Inputs
Read from the existing ECOM OS project only:
- root governance
- current Coordinator Inbox
- current master/control/stage pointers
- current Primary4 source SHAs
- current screen ownership contracts
- current Product Vault/context contracts
- current i18n/currency/shop/role contracts
- current browser/single-shell contracts
- current debt/defect registers
- current operator screenshot/video evidence when available

## Forbidden
- no active UI write
- no marketplace write
- no eBay write
- no Save/Publish/Revise/Delete
- no second browser owner
- no second navigation/state/i18n/currency/shop owner
- no invention of business truth when a source is missing

## Procedure
1. Verify project root and current Coordinator pointer.
2. Verify current source SHAs for HOME, ROUTE01, ROUTE02, ROUTE03 and shared/global owners.
3. Extract global invariants.
4. Extract the real operator workflow between screens.
5. Inventory each screen's controls and classify each as AUTO, MANUAL, DIRTY_ONLY, CONDITIONAL, or READONLY.
6. Map each control to its real owner, handler/API/state when evidence exists.
7. Mark any unbound control as DISABLED_WITH_REASON or debt; never pretend it works.
8. Extract Product Vault/product context rules.
9. Extract language/currency/shop/role independence rules.
10. Extract responsive widths and known visual defects.
11. Extract frozen-proven-good blocks that must not be redesigned without evidence.
12. Produce ECOM_UI_CANON_V1 JSON conforming to schemas/ecom_ui_canon_schema_v1.json.
13. Produce a human-readable summary with conflicts, missing evidence and blockers.

## Conflict law
When sources disagree:
- current explicit operator decision wins over older project records;
- current root governance and current Coordinator authority beat stale reports;
- current physical source/readback beats stale generated documentation;
- unresolved conflict becomes BLOCKED_CANON_CONFLICT, never guessed.

## Output status
READY only if the canon is sufficient to design without guessing business semantics.
Otherwise output DRAFT with exact missing evidence.

## Handoff
READY → ecom-workflow-map and ecom-screen-contract.
DRAFT/BLOCKED → investigation/debt registration; no candidate design generation.
