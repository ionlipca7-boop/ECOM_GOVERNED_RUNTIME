# GSTACK -> ECOM FACTORY ADOPTION R1

STATUS=PREPARED_IN_GITHUB_BRANCH_ONLY
BRANCH=feat/ecom-factory-gstack-r1
WINDOWS_ACTIVE_INTEGRATION=NOT_STARTED
LIVE_MARKETPLACE_ACTIONS=DISABLED

## 1. Goal

Build the missing ECOM OS "collector/factory" layer: one governed orchestrator that loads current project/product context, routes work through specialist roles, preserves decisions and learnings, runs design/engineering/QA/adversarial review chains, and returns one controlled result to the operator.

This is an adaptation, not a blind copy of gstack. No third-party source code is copied by this document. gstack is treated as an external reference architecture.

## 2. External reference: gstack mechanisms worth adopting

Verified from garrytan/gstack current source and AGENTS documentation:

- specialist SKILL.md roles rather than one giant prompt;
- autoplan-style chained review;
- investigate-before-fix discipline;
- QA in a real persistent Chromium browser;
- design review with screenshot -> issue -> fix -> reverify loop;
- design consultation / design variants / HTML design roles;
- Codex as an independent second opinion/challenge/review path;
- context-save / context-restore;
- learn / persistent project learnings;
- gbrain-style cross-session knowledge retrieval;
- careful/freeze/guard safety layers;
- health / benchmark / security review;
- persistent localhost browser daemon with state, health check and authentication;
- Windows-safe test subset exists, but native PowerShell setup is not yet the upstream default; upstream setup currently expects Git Bash/MSYS on Windows.

## 3. What ECOM OS already has

Do not duplicate these owners.

Existing architecture already provides:

- Root governance and one canonical order authority;
- central Coordinator + Second Coordinator / adversarial QA;
- one owner per functional domain and file lease rules;
- STOP_SAFE philosophy;
- READONLY before/after verification;
- approval gates for risky actions;
- Product Identity Resolver;
- Product Vault Builder/Foundation;
- Product Intake Coordinator;
- Binary Bridge;
- Product Lifecycle runtime;
- Marketplace Gateway / source adapters;
- Listing Studio;
- eBay DOM safe core;
- single-browser/single-shell UI direction;
- continuous team orchestration contracts;
- request disposition queue;
- debt / idea capture and canonicalization rules;
- existing Auto Quality Engine concept with Analyst / Optimizer / Critic roles;
- Windows local assistant plans for Browser Helper, Local Knowledge Base, Dashboard and Local Agent Team.

## 4. Real gap

The missing layer is not another Product Vault, another browser, another coordinator or another marketplace executor.

The missing layer is a universal governed orchestration runtime that composes existing owners into repeatable skills and preserves the evidence/learning between runs.

Working name:

ECOM_FACTORY_ORCHESTRATOR_V1

## 5. Target architecture

Operator / ChatGPT / local UI
-> Context Loader
-> Canonical Router
-> Specialist Skill Graph
-> Existing Owner Adapters
-> Evidence Collector
-> Independent Critic / Second Model Gate
-> QA / Browser Verification
-> Approval Gate where required
-> Existing governed executor only
-> Readback
-> Learning / Debt / Decision Recorder

Important invariant:

ORCHESTRATOR_CALLS_OWNERS=true
ORCHESTRATOR_DOES_NOT_REIMPLEMENT_OWNERS=true

## 6. Core modules to add

### A. Context Loader

Input:
- project root;
- current Coordinator Inbox;
- current Master Report;
- Product Vault/product_key when product-bound;
- case_id / listing intent when applicable;
- current owner locks;
- current debt / idea queue;
- current browser/screen state pointers.

Output:
- one bounded immutable context packet with source hashes.

### B. Skill Registry

Each skill must declare:
- skill_id;
- purpose;
- inputs;
- allowed owners/tools;
- forbidden actions;
- risk level;
- read/write mode;
- evidence required;
- acceptance tests;
- stop conditions;
- next allowed skills.

### C. Orchestration Graph

Initial universal graph:

INTENT
-> CONTEXT_LOAD
-> DUPLICATE/CANON_CHECK
-> PLAN_REVIEW
-> OWNER_ROUTING
-> INVESTIGATE
-> IMPLEMENT_OR_DRY_PLAN
-> INDEPENDENT_REVIEW
-> QA
-> REVERIFY
-> RECORD_LEARNING/DEBT
-> COORDINATOR_HANDOFF

For risky actions insert OPERATOR_APPROVAL before EXECUTE.

### D. Persistent Browser Adapter

Do NOT create a second production browser owner.

Adopt the useful gstack properties inside the existing ECOM single-browser law:
- persistent browser state;
- health/liveness check;
- deterministic browser owner;
- fast repeated commands;
- screenshot + DOM evidence;
- current URL/tab/session tracking;
- auth/token boundary;
- no secret/cookie values in logs;
- prompt-injection / hostile-page boundary for agent-consumed web content;
- operator handoff for CAPTCHA/login when required.

Target must remain compatible with the existing ECOM browser at 127.0.0.1:8765 and existing browser-profile ownership. No second uncontrolled Chromium daemon may become canonical.

### E. Design Controller

Create skills over the existing UI owner model, not a second UI.

Required workflow:
1. load exact screen owner + current source SHA;
2. render same-shell screen;
3. inspect desktop and tablet/mobile-safe widths required by ECOM contracts;
4. capture visual evidence;
5. score layout, hierarchy, spacing, typography, overflow, language/currency consistency, controls, errors and responsiveness;
6. classify each finding OWNER_LOCAL / SHARED / EXTERNAL;
7. owner-local fix only when permitted;
8. regenerate successor;
9. screenshot/readback re-test;
10. Second Coordinator adversarial QA;
11. freeze only after full acceptance.

### F. Investigator

Rule:
NO_FIX_WITHOUT_REPRODUCTION_OR_EVIDENCE=true

Required output:
- symptom;
- reproduction;
- observed evidence;
- likely root cause;
- alternative hypotheses;
- owner;
- affected paths;
- risk;
- smallest repair;
- regression tests.

### G. Cross-model Critic

Use current ChatGPT/Codex/GitHub-connected capabilities as available.

Modes:
- REVIEW;
- CHALLENGE;
- CONSULT.

The critic is read-only by default and cannot approve its own proposed change.

### H. Knowledge / Learning Store

Do not create ungoverned memory.

Persist only structured, provenance-linked records:
- problem;
- evidence;
- attempted solution;
- result;
- reusable rule;
- owner;
- affected products/routes;
- source hashes;
- accepted/rejected/deferred status;
- supersession pointer.

Integrate with existing ECOM idea/debt/canonical memory cycle.

### I. Context Save / Restore

One resumable packet must contain:
- current order/inbox SHA;
- project root;
- branch/SHA when Git is involved;
- active product/case/listing context;
- owner leases;
- completed evidence;
- remaining blockers/debts;
- exact next safe action.

### J. Health / Benchmark / Security Skills

Health:
- registries;
- imports;
- tests;
- route build;
- browser liveness;
- stale pointers;
- duplicated owners;
- missing contracts;
- broken generated artifacts.

Benchmark:
- browser interaction latency;
- screen build latency;
- context-load latency;
- test duration;
- repeated agent task duration.

Security:
- localhost-only control surfaces;
- auth on browser-mutating commands;
- no secret values in logs;
- prompt-injection boundary for external pages;
- no marketplace write without governed approval;
- no uncontrolled shell/destructive command path.

## 7. Initial ECOM skill set

1. ecom-context-load
2. ecom-autoplan
3. ecom-investigate
4. ecom-design-review
5. ecom-responsive-qa
6. ecom-browser-qa
7. ecom-product-intake-review
8. ecom-product-vault-audit
9. ecom-listing-quality-review
10. ecom-marketplace-source-research
11. ecom-cross-model-review
12. ecom-health
13. ecom-security-review
14. ecom-context-save
15. ecom-context-restore
16. ecom-learn
17. ecom-debt-register
18. ecom-release-readiness

## 8. Windows strategy

ECOM must remain Windows-first.

Do not make upstream gstack Git Bash/MSYS assumptions part of the canonical runtime.

Implement native Windows adapters where practical:
- PowerShell/CMD launch compatibility;
- Windows path normalization;
- health checks instead of PID-only assumptions;
- explicit UTF-8 handling;
- no Unix-only find/sed/awk requirement in core ECOM skills;
- Playwright/Chromium compatibility verified on Windows;
- source state kept under the existing ECOM project root;
- no hidden auto-start background services unless separately approved.

## 9. Migration law

Phase 0: READONLY inventory and architecture comparison.
Phase 1: GitHub-only skill/contracts prototype.
Phase 2: static tests and fixtures.
Phase 3: local Windows READONLY context-loader + skill-router acceptance.
Phase 4: browser adapter READONLY acceptance in existing single-browser architecture.
Phase 5: design-review + responsive QA pilot on one already-owned screen.
Phase 6: cross-model critic and learning/context save/restore.
Phase 7: coordinator integration.
Phase 8: controlled owner-local write pilots.
Phase 9: broader adoption only after unrelated-screen/product acceptance.

## 10. Non-negotiable safety

SECOND_PRODUCT_VAULT=false
SECOND_COORDINATOR=false
SECOND_BROWSER_OWNER=false
SECOND_UI=false
SECOND_MARKETPLACE_EXECUTOR=false
SILENT_PUBLISH=false
SILENT_SEND=false
SILENT_DELETE=false
SILENT_FINANCE_WRITE=false
BYPASS_APPROVAL=false

Every new skill and adapter must prove that it calls the existing canonical owner or remains READONLY.

## 11. Immediate next build package

PACK EFACT-R1-A — READONLY FOUNDATION

Deliverables:
- exact ECOM current owner inventory;
- gstack -> ECOM feature mapping;
- ECOM skill registry schema;
- context packet schema;
- orchestration run schema;
- learning record schema;
- Windows compatibility matrix;
- no active runtime changes.

PACK EFACT-R1-B — GITHUB PROTOTYPE

Deliverables:
- skills/ecom-context-load/SKILL.md;
- skills/ecom-investigate/SKILL.md;
- skills/ecom-design-review/SKILL.md;
- skills/ecom-responsive-qa/SKILL.md;
- skills/ecom-cross-model-review/SKILL.md;
- skills/ecom-context-save/SKILL.md;
- skills/ecom-context-restore/SKILL.md;
- skills/ecom-learn/SKILL.md;
- schemas + fixtures + static validator.

Only after the Coordinator/governance layer accepts the package should it be copied or adapted into the active Windows runtime.
