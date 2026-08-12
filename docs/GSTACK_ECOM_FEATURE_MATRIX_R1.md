# GSTACK -> ECOM OS FEATURE MATRIX R1

STATUS=READONLY_COMPARISON

| gstack mechanism | ECOM current state | Decision |
|---|---|---|
| Specialist skills | Roles/contracts exist, but no unified skill registry/runtime | ADOPT as ECOM skill layer |
| Autoplan chained review | Coordinator + plans exist, not one reusable pipeline | ADOPT as ecom-autoplan |
| Investigate before fix | STOP_SAFE / evidence-first exists informally and in contracts | FORMALIZE as ecom-investigate |
| Persistent browser | ECOM has single-browser law and browser profiles, but no universal skill-facing daemon contract | ADAPT into existing browser owner; no second browser |
| Browser QA | Existing route/browser tests are fragmented by owner | ADOPT as reusable owner-aware ecom-browser-qa |
| Design review | Home/Route01/02/03 visual QA exists; no universal design controller | ADOPT owner-aware design-review |
| Design shotgun | No universal governed multi-variant UI design exploration | DEFER; use only in isolated candidate space |
| Design consultation | Design rules exist across project/history | ADOPT as plan-only skill, no active UI write |
| Codex second opinion | Codex workspace/audits already exist | FORMALIZE REVIEW/CHALLENGE/CONSULT interface |
| context-save/restore | Many CURRENT pointers/handoffs exist, but fragmented | ADOPT unified context packet over current pointers |
| learn | Debts, reports and idea queue exist | ADAPT into provenance-linked accepted learning records |
| gbrain | ECOM has knowledge/memory ambitions and canonical reports | ADAPT later; do not introduce second truth store |
| careful/freeze/guard | ECOM has STOP_SAFE, file leases, owner locks | KEEP ECOM law; expose as skills/policies |
| health | Many status files/tests exist | ADOPT unified health aggregator |
| benchmark | No universal orchestration/browser latency baseline | ADOPT |
| security review | Governance strong; hostile-web prompt-injection boundary not yet universal | ADOPT for browser/source-research agents |
| ship/land/deploy | ECOM controlled activation differs from normal SaaS release | DO NOT COPY; map to Coordinator acceptance + governed activation |
| telemetry | Not required for ECOM factory core | DO NOT ADOPT by default |
| automatic background update | Conflicts with controlled Windows/runtime expectations | DO NOT ADOPT |

## Highest-value first wave

1. context-load
2. investigate
3. design-review
4. responsive-qa
5. browser-qa
6. cross-model-review
7. context-save/restore
8. learn/debt-register
9. health
10. security-review

## Key architectural conclusion

ECOM is not missing most domain logic. It is missing a stable composition layer that turns the existing contracts, owners, reports, browser paths, Product Vault and QA rules into reusable, machine-routable skills.
