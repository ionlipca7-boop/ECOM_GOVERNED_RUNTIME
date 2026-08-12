# ECOM BROWSER GUARDIAN — CONTRACT V1

## Mission
Keep the ECOM OS browser coherent while allowing candidate redesigns to be explored safely outside production.

## Inputs
- project context packet
- workflow map
- screen contracts
- UI canon
- current candidate source SHA
- generated candidate SHA
- viewport matrix
- screenshots
- control/handler map

## Required checks
1. Logic preservation.
2. No duplicate action semantics.
3. AUTO vs MANUAL correctness.
4. Owner boundaries.
5. Responsive widths: 700, 820, 960, 1200, 1500, 1648.
6. RU/DE/EN/RO projection parity.
7. Language independent from currency/shop/role.
8. Empty/error/loading/dirty states.
9. Cross-screen navigation and active product context.
10. Before/after visual evidence.

## Candidate policy
A/B/C redesigns are allowed only inside Browser Lab. Production source stays untouched until an integration package is approved.

## Acceptance
DESIGN_PASS alone is insufficient.
Required chain:
DESIGN -> LOGIC_GUARD -> BROWSER_QA -> RESPONSIVE_QA -> CROSS_SCREEN_QA -> INDEPENDENT_CRITIC -> OPERATOR_REVIEW -> INTEGRATION_PACKAGE.
