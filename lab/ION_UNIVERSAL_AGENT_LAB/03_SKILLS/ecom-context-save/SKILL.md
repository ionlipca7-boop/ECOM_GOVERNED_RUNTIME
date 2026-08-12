# ecom-context-save

Purpose: create a deterministic resumable checkpoint.

Capture current goal, exact refs/SHAs, owner, completed work, open debts, blockers, leases, artifacts, browser evidence, next safe actions and approval state. Never copy secrets. Write only to LAB memory/checkpoint storage. Mark resume_safe=true only after all required refs exist and no unresolved write lease ambiguity remains.
