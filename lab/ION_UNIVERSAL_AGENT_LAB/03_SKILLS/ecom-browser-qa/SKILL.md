# ecom-browser-qa

Purpose: verify a candidate in a real browser against contracts and actual state transitions.

## Required checks
- exact screen and candidate identity
- control visibility and disabled reasons
- click -> handler -> state/API outcome
- navigation continuity
- no duplicate semantic actions
- negative/empty/error contexts
- no save/publish/live marketplace side effect unless separately approved
- before/after evidence

Output PASS only when observed behavior matches the screen contract. Structural/static success alone is insufficient.
