# ION UNIVERSAL AGENT LAB — ORCHESTRATOR CONTRACT V1

## Purpose
Coordinate specialist agents without creating a second governance system.

## Core loop
REQUEST -> CLASSIFY -> LOAD CONTEXT -> OWNER RESOLUTION -> TASK PACKAGE -> WORKER -> EVIDENCE -> CRITIC -> DISPOSITION -> REPORT -> NEXT SAFE TASK.

## Required controls
- message_id
- from_owner
- to_owner
- task_id
- cursor
- ack
- lease
- dependency list
- risk class
- evidence refs
- disposition

## Rules
1. One task has one accountable owner.
2. Cross-owner defects are routed, never silently repaired by the wrong worker.
3. Workers may continue non-blocked owner-safe backlog while one dependency waits.
4. No production write without an explicit governed integration package and project approval gate.
5. Duplicate requests must be deduplicated by task identity + evidence hash.
6. Stale context must fail closed and request refresh.
7. The Coordinator remains final cross-owner disposition authority for ECOM OS integration.

## Initial runtime mode
READONLY_LAB_ORCHESTRATION_ONLY.

## Future adapters
- MCP for tools
- mailbox/relay for agent messages
- A2A-compatible transport candidate
- local model runner candidate
- cloud model adapters behind Safe AI Gate
