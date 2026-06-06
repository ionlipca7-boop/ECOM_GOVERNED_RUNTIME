# ECOM OS MEMORY V2 — POLICY

## Read order
1. First read Memory V2.
2. If missing info, read old archive/reference.
3. If old info is still useful, summarize into V2.
4. Do not rewrite/delete old archives.
5. Latest pointer must point to one current real checkpoint.

## Required paths
storage/memory_v2/current/
storage/memory_v2/archive/
storage/memory_v2/policy/
storage/control_room/ECOM_OS_MEMORY_V2_LATEST_POINTER.json

## Safety rules
No false PASS.
No eBay live/publish/revise/delete without separate explicit gate.
No server delete/cleanup without separate explicit gate.
No restart without separate explicit gate.
No secrets/tokens/env print.
No blind GitHub commit/push.
Always staged review before commit.
Legacy root /home/ionlipca7/runtime_eco_v1 is protected and must not be modified.

## Approval scope
APPROVE_SERVER_CREATE_MEMORY_V2_FILES_LOCAL_NO_COMMIT_NO_PUSH allows creating only Memory V2 checkpoint, policy and pointer.
It does not allow commit, push, delete, eBay write, restart, cleanup or secrets print.
