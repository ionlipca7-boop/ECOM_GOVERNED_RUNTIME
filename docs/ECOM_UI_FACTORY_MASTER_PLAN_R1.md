# ECOM UI FACTORY MASTER PLAN R1

Status: PREPARATION_ACTIVE
Mode: GITHUB_FIRST / WINDOWS_LATER / NO_ACTIVE_UI_WRITE
Branch: feat/ecom-factory-gstack-r1

## 1. Goal
Build one governed ECOM UI Factory that can understand the whole ECOM OS project, propose a better browser/interface architecture, generate bounded design candidates, test them in the real browser, compare them against project logic, and only then hand an accepted candidate to the existing integration owner.

The factory is not a second ECOM OS. It must reuse current owners, current Product Vault, current browser/runtime, current governance, current i18n, current marketplace executors and current approval gates.

## 2. Non-negotiable invariants
- SECOND_PRODUCT_VAULT=false
- SECOND_COORDINATOR=false
- SECOND_BROWSER_OWNER=false
- SECOND_NAVIGATION_OWNER=false
- SECOND_I18N_OWNER=false
- SECOND_CURRENCY_OWNER=false
- SECOND_SHOP_OWNER=false
- SECOND_MARKETPLACE_EXECUTOR=false
- ACTIVE_UI_WRITE=false until explicit integration approval
- MARKETPLACE_WRITE=false during design/build/QA
- EBAY_WRITE=0 during design/build/QA
- SAVE_PUBLISH_REVISE_DELETE=false during design/build/QA
- SOURCE_OF_TRUTH=existing ECOM OS canon + operator decisions

## 3. Target operating model
Operator intent
→ Context Loader
→ Canon Extractor
→ Workflow Mapper
→ UX Architect
→ Design System Builder
→ Candidate Generator
→ Critic / Adversarial Reviewer
→ Browser QA
→ Responsive QA
→ Functional State QA
→ Cross-screen regression QA
→ Candidate score
→ Operator review only for mature finalists
→ Existing integration owner
→ Real browser readback
→ Freeze / rollback / debt registration

## 4. Required project memory packet
Every design run must load one immutable context packet containing at minimum:
- current project root and branch/ref
- current Coordinator Inbox pointer
- global operator rules
- active Product Vault/context rules
- screen ownership map
- route-to-route workflow map
- AUTO vs MANUAL rules
- current language/currency/shop/role rules
- current browser entrypoint and single-browser invariant
- active screen source SHAs
- known debts and known frozen-good blocks
- screenshot/video evidence refs when available
- forbidden actions and write boundaries

No design generation starts if the context packet is incomplete or stale.

## 5. ECOM Design Canon
Create one machine-readable design canon, not free-form taste.

Required canon sections:
1. Information architecture
2. Screen hierarchy
3. Navigation laws
4. Product context visibility
5. Primary action law
6. AUTO/MANUAL visibility law
7. Control density law
8. Empty-state law
9. Error/warning/state presentation
10. Product card law
11. Media/photo presentation law
12. Responsive law
13. Typography/spacing/grid tokens
14. RU/DE/EN/RO text behavior
15. EUR/USD/GBP/RON independence from language
16. Shop/store/marketplace identity separation
17. Accessibility basics
18. No-fake-control rule
19. No-duplicate-action rule
20. One-owner-per-control rule

## 6. Screen contracts
Each screen gets a SCREEN_CONTRACT generated from the canon and existing business logic.

Minimum fields:
- screen_id
- owner
- purpose
- entry conditions
- exit/continuation actions
- required panels
- optional panels
- prohibited panels
- control inventory
- control→handler/API/state binding
- AUTO controls
- MANUAL controls
- dirty-only controls
- conditional retry controls
- empty states
- blocked states
- responsive breakpoints
- language/currency/shop/role expectations
- product context expectations
- visual acceptance rules
- regression dependencies

Initial target screens:
- HOME
- NEW_PRODUCT / Route01
- VARIANTS / Route02
- LISTING_STUDIO / Route03

## 7. Design Factory roles
### A. Context Loader
Reads canon, pointers, current SHAs, owners and debts. Readonly only.

### B. Workflow Mapper
Builds a graph of operator jobs and route transitions. Detects unnecessary clicks, duplicated decisions and dead ends.

### C. UX Architect
Produces information architecture and screen structure without changing business semantics.

### D. Design System Builder
Creates reusable tokens/components/layout rules. Must not invent a second state owner.

### E. Candidate Generator
Produces 2–3 isolated candidate directions. Never writes active UI.

### F. Design Critic
Scores hierarchy, clarity, density, trust, consistency, mobile/tablet behavior and operator effort.

### G. Logic Guardian
Rejects a visually attractive candidate if it changes workflow semantics, owner boundaries or approval gates.

### H. Browser QA
Runs real clicks/state checks in the existing browser/runtime where available.

### I. Responsive Guardian
Checks at minimum 700/820/960/1200/1500/1648 widths.

### J. Cross-screen Regression Guardian
Checks that a change in one screen does not break shared header/nav/i18n/currency/shop/product context or neighboring screens.

### K. Independent Reviewer
Second-model/adversarial pass; no implementation authority.

## 8. Candidate lifecycle
D0 DISCOVER
D1 CANONIZE
D2 MAP_WORKFLOW
D3 DEFINE_SCREEN_CONTRACTS
D4 DESIGN_SYSTEM
D5 GENERATE_A_B_C
D6 STATIC_REVIEW
D7 INTERACTIVE_PROTOTYPE
D8 BROWSER_QA
D9 RESPONSIVE_QA
D10 CROSS_SCREEN_QA
D11 ADVERSARIAL_REVIEW
D12 OPERATOR_FINALIST_REVIEW
D13 INTEGRATION_PACKAGE
D14 GOVERNED_INTEGRATION
D15 POST_INTEGRATION_BROWSER_READBACK
D16 FROZEN_PROVEN_GOOD

A candidate cannot skip stages.

## 9. Candidate scoring
Score 0–10 per dimension:
- workflow correctness
- operator click economy
- primary-action clarity
- information hierarchy
- visual consistency
- responsive behavior
- state/error clarity
- product-context clarity
- language robustness
- accessibility basics
- owner/binding correctness
- regression safety

Hard FAIL regardless of score if:
- business semantics changed without approval
- duplicate state owner introduced
- hidden marketplace/live write path introduced
- required control disappears
- fake/unbound control appears
- responsive overflow/clipping exists at supported widths
- language/currency coupling appears
- Product Vault context is ambiguous

## 10. Visual checkpoint package
Every accepted checkpoint stores:
- source SHA(s)
- generated SHA(s)
- design canon version
- screen contract version
- viewport
- screenshot ref
- DOM/control inventory
- handler/state map
- language
- currency
- shop/store context
- role context
- product_key/context state
- QA result
- known exceptions

This allows exact before/after regression detection.

## 11. Windows strategy
Do not copy upstream gstack setup blindly.

Windows target:
- native Windows-first wrappers
- existing V7 connector for project reads/writes
- existing 127.0.0.1:8765 browser/runtime as the single operator browser
- no second active browser owner
- optional persistent browser-control helper only if it attaches safely to the existing browser architecture
- Git Bash/MSYS dependency avoided where practical
- PowerShell/CMD-compatible bootstrap
- exact path and SHA checks before any local write

## 12. gstack mechanisms to adapt
KEEP/ADAPT:
- design-consultation concept
- plan-design-review concept
- design-review iterative visual QA
- qa / qa-only methodology
- investigate-before-fix
- context-save / context-restore
- learn / persistent lessons
- codex second-opinion pattern
- browser persistent-state principles
- careful/freeze/guard concepts

DO NOT COPY AS-IS:
- a second browser owner
- direct autonomous ship/deploy semantics
- ungoverned writes
- upstream project assumptions
- macOS-specific setup flow
- any skill that bypasses ECOM approval or owner boundaries

## 13. Implementation phases
### PHASE 0 — Baseline capture
Read current ECOM canon, active screen SHAs, owners, browser rules and known debts. No writes to Windows.

### PHASE 1 — Canon compiler
Implement ecom-context-load + ecom-ui-canon. Output readonly JSON/MD packets.

### PHASE 2 — Workflow graph
Implement ecom-workflow-map. Build route/action/state graph and click-economy report.

### PHASE 3 — Screen contracts
Generate contracts for Home, Route01, Route02, Route03 from current truth.

### PHASE 4 — Design system
Create design tokens, component grammar, spacing/grid/type/state rules and reusable layout constraints.

### PHASE 5 — Design consultation
Generate 2–3 isolated browser architecture directions. No active integration.

### PHASE 6 — Candidate prototype
Build clickable isolated candidate(s) backed by mocked/read-only data where needed.

### PHASE 7 — Design + logic review
Run design critic and logic guardian. Reject any semantic drift.

### PHASE 8 — Browser QA
Use real browser where safely available; click/state/API/readback, no marketplace writes.

### PHASE 9 — Responsive QA
Run all supported widths and long-string stress cases.

### PHASE 10 — Cross-screen regression
Verify shared header/nav/i18n/currency/shop/role/product context.

### PHASE 11 — Independent review
Codex/second reviewer challenge against omissions and accidental simplification.

### PHASE 12 — Operator finalist review
Show only mature candidates with comparison: current vs A/B/C, score, click count, regressions, risks.

### PHASE 13 — Integration package
Prepare exact paths, SHA guards, tests, rollback, owner handoff. Still no integration without approval.

### PHASE 14 — Governed Windows integration
Existing owner applies accepted package through current governance.

### PHASE 15 — Post-integration guardian
Continuously compare current browser against frozen screen contracts/checkpoints after future changes.

## 14. First implementation order
1. ecom-context-load
2. ecom-ui-canon
3. ecom-workflow-map
4. ecom-screen-contract
5. ecom-design-consultation
6. ecom-design-review
7. ecom-logic-guardian
8. ecom-browser-qa
9. ecom-responsive-qa
10. ecom-cross-screen-qa
11. ecom-cross-model-review
12. ecom-context-save / restore
13. ecom-learn
14. ecom-health
15. ecom-ui-guardian orchestration

## 15. Finish definition
The project reaches ECOM_UI_FACTORY_R1_COMPLETE only when:
- the full canon can be compiled from project truth;
- every Primary4 screen has a machine-readable contract;
- the factory can produce isolated alternative design candidates;
- design candidates are checked against business semantics automatically;
- browser/responsive/cross-screen QA is repeatable;
- visual checkpoints can detect regressions;
- an accepted candidate can be handed to existing integration owner with exact SHA/rollback package;
- future UI changes can be checked by the Guardian without redesigning everything from scratch.
