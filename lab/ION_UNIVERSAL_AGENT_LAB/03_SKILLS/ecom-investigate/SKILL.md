# ecom-investigate

Purpose: prove root cause before proposing a repair.

## Rules
1. Load current project context.
2. Identify exact owner, source truth, current SHA and evidence.
3. Reproduce or prove the defect READONLY when possible.
4. Classify: SOURCE / GENERATED / RUNTIME / STATE / I18N / RESPONSIVE / INTEGRATION / EXTERNAL.
5. Search existing debt and prior fixes before creating new work.
6. Do not patch during investigation.
7. Output: FACTS, ROOT_CAUSE, AFFECTED_OWNER, RISK, PROPOSED_NEXT_ACTION, EVIDENCE_REFS.
8. If root cause is not proven, return BLOCK_UNPROVEN_ROOT_CAUSE.
