# ION SAFE AI GATE — CONTRACT V1

## Goal
All external or optional AI providers must pass through one safety and capability boundary before receiving project context or tool access.

## Default policy
DENY_BY_DEFAULT.

## Pipeline
REQUEST -> PROVIDER CLASSIFY -> CONTEXT MINIMIZE -> SECRET/PII FILTER -> TOOL ALLOWLIST -> RISK SCORE -> EXECUTION MODE -> AUDIT LOG -> RESULT VALIDATION.

## Provider classes
- LOCAL_TRUSTED: local models and local deterministic tools.
- CONNECTED_REVIEWER: remote model with bounded readonly context.
- CONNECTED_WORKER: remote model with explicit bounded tools and approval.
- BLOCKED: provider or request not satisfying policy.

## Hard rules
- no raw secrets;
- no cookies/session tokens;
- no unrestricted filesystem;
- no unrestricted browser profile;
- no marketplace purchase/send/publish/refund by default;
- no canonical project write from external model;
- evidence and provider identity logged;
- project context is minimized per task.

## Initial mode
READONLY_DESIGN_AND_REVIEW_PREPARATION.
