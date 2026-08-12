# ION UNIVERSAL AGENT LAB — MASTER ARCHITECTURE R1

Status: DESIGN/ISOLATED_BUILD
Production integration: FORBIDDEN until acceptance
Purpose: combine ECOM OS governance, Knowledge Lab/IWE memory, gstack-inspired skills, browser/design QA, multi-agent coordination, local AI and optional cloud models into one isolated laboratory next to the production project.

## Core rule

Build the complete system beside production first. Production ECOM OS remains source/canonical truth and is read-only from the lab until a separately approved integration stage.

## What already exists and must be reused

- ECOM OS multi-chat owner model: Coordinator + owner workers + shared inbox + handoffs + ACK/SHA/cursors.
- ECOM Knowledge Lab: Obsidian visual knowledge vault, browser dashboard, IWE graph/search mirror, READONLY guard.
- ECOM governed runtime: Product Vault, Product Intake, Binary Bridge, lifecycle, registry, STOP_SAFE, approval gates.
- V7 MCP connector: bounded read/write and binary bridge access.
- gstack-derived concepts: SKILL routing, plan/design review, investigate-first, browser QA, context save/restore, learn, cross-model critique.
- Candidate future orchestration layer: local multi-agent runtime, A2A/MCP separation, local Ollama and optional cloud models through a safe gate.

## Target architecture

Operator/Phone/ChatGPT
  -> ION CONTROL PLANE
  -> Context Loader
  -> Memory Router
  -> Skill Router
  -> Coordinator/Orchestrator
  -> specialist workers
  -> Browser/Design Guardian
  -> Independent Critic
  -> Approval Gate
  -> existing governed executors only
  -> verify/readback
  -> learning/debt/memory

## Isolation boundary

LAB may read exported/mirrored project truth.
LAB may create its own candidates, reports, screenshots, plans, indexes and agent state.
LAB must not directly modify canonical ECOM OS, marketplace state, Product Vault canonical data, active browser route, registry owner state or production Git branch.

Any future production change must go through:
LAB candidate -> tests -> adversarial QA -> operator review -> exact integration package -> governed owner -> readback -> acceptance/freeze.

## Major subsystems

### 1. CONTROL PLANE
One dashboard/status surface for operator and Coordinator. Shows agents, tasks, blockers, approvals, memory freshness, browser health, current candidate and production readback.

### 2. KNOWLEDGE/MEMORY PLANE
- source export/mirror
- Obsidian knowledge vault
- IWE graph/search
- structured current context packets
- decisions/debts/learnings
- context save/restore
- provenance + SHA + timestamps

### 3. SKILL PLANE
Machine-readable skills with owner, inputs, outputs, allowed tools, forbidden writes, stop conditions and acceptance rules.
Initial skills:
- ecom-context-load
- ecom-ui-canon
- ecom-workflow-map
- ecom-screen-contract
- ecom-design-consultation
- ecom-design-review
- ecom-responsive-qa
- ecom-browser-qa
- ecom-investigate
- ecom-cross-model-review
- ecom-context-save
- ecom-context-restore
- ecom-learn
- ecom-health
- ecom-security-review

### 4. ORCHESTRATION PLANE
Coordinator/manager selects skills and agents, preserves owner boundaries and serializes writes. Agent-to-agent communication is via durable mailbox/task records, not implicit chat assumptions.

Required primitives:
SEND, INBOX, ACK, CURSOR, TASK, LEASE, BLOCKER, RESULT, CHALLENGE, APPROVAL, CANCEL, STATUS.

### 5. SAFE AI GATE
All external/local model calls pass through one policy layer. Responsibilities:
- model allowlist
- secret/PII redaction
- project-scope filter
- prompt provenance
- tool permission profile
- output validation
- audit log
- optional budget/quota rules

Local/offline model is default candidate; cloud models are optional specialists.

### 6. BROWSER + DESIGN GUARDIAN
One canonical UI logic model, not free-form redesign.
Maintains:
- UX workflow map
- screen contracts
- design tokens/system
- control map and handler map
- responsive breakpoints
- visual checkpoints
- interaction regression suite
- cross-screen/global header/i18n/currency/shop invariants

Designer may create A/B/C candidate architectures in the lab. Guardian rejects any candidate that changes business semantics or removes required workflow.

### 7. TEST/QA PLANE
Static -> schema -> unit -> generated candidate -> browser click/state/API -> negative contexts -> responsive -> i18n/currency/shop/role -> adversarial critic -> operator visual review when needed.

### 8. MEMORY/LEARNING LOOP
Every completed cycle emits structured records:
intent, evidence, decision, result, failure, repair, accepted pattern, rejected pattern, debt, next trigger.
Learning is advisory until promoted to canon by governance.

## Build phases

PHASE 0 — inventory and source-truth map.
PHASE 1 — isolated folder skeleton + manifests.
PHASE 2 — memory adapters to existing Knowledge Lab/IWE READONLY guard.
PHASE 3 — context packet + skill registry + workflow/screen contracts.
PHASE 4 — UI Design Factory: A/B/C candidate generation + scoring.
PHASE 5 — persistent browser QA adapter + responsive/visual checkpoints.
PHASE 6 — local agent orchestrator/mailbox + owner leases.
PHASE 7 — SAFE AI GATE + local model provider.
PHASE 8 — independent multi-model/cross-model critic.
PHASE 9 — full lab E2E: Home -> New/Variants -> Studio -> Home using non-live fixtures.
PHASE 10 — failure/recovery/rollback tests.
PHASE 11 — operator acceptance of lab system.
PHASE 12 — bounded production integration package only after approval.

## Definition of LAB COMPLETE

LAB_COMPLETE requires:
- no production writes during lab build
- deterministic context restore
- durable agent mailbox/ACK/cursor
- no duplicate owners
- UI candidate can be generated and retested without touching active UI
- browser/design guardian catches intentional regressions
- local memory search returns provenance-backed answers
- orchestrator survives restart and resumes pending work
- local/default model path works without paid cloud dependency
- cloud provider path is optional and gated
- full audit log
- rollback/recovery evidence
- one-click Windows startup plan
- operator can run primarily from phone while Windows host executes tools

## Final product name
Working name: ION UNIVERSAL AGENT LAB / ECOM FACTORY LAB.
It is a reusable platform for ECOM OS first and future projects later.