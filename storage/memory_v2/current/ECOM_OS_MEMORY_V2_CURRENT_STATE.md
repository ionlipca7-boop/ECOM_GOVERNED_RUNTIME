# ECOM OS MEMORY V2 — CURRENT STATE

Status date: 2026-06-06
Operator: Ion

## Architecture
GitHub = long-term memory / source of truth.
Server = runtime / working place / eyes.
Windows = local operator + standalone AutoClip.
Old memory/archive = read-only reference.
New memory = ECOM_OS_MEMORY_V2.

## Runtime
Active server runtime:
/home/ionlipca7/ecom_governed_runtime

Legacy protected root:
/home/ionlipca7/runtime_eco_v1

Legacy root must not be modified.

## Confirmed checkpoint
AUTOCLIP_V1_DONE=PASS
RUN_TASK_FIX_DONE=PASS
GITHUB_ACCESS=PASS
MEMORY_V2_POLICY_READY=PASS
FULL_MEMORY_V2_FILE_CREATED=YES

## Standalone AutoClip V1
Windows root:
D:\ECOM_STANDALONE_AUTOCLIP

Confirmed:
ION_CLIP:HEALTH=PASS
ION_CLIP:STATUS=PASS
ION_CLIP:RUN_TASK=PASS
SSH=OK
CLIPBOARD=OK
BLACK_WINDOW_OUTPUT=PASS
OLD_HELPER_TOUCHED=NO
OLD_R_TOUCHED=NO

RUN_TASK fixed:
RUN_TASK_CONTRACT_FIXED=PASS
PASS_ONLY_ON_EXIT0=PASS
DONE_MARKER_REQUIRED=PASS
REPORT_LINES_NOT_EXECUTED_AS_CMD=PASS
CLIPBOARD_OUTPUT=PASS
TASK_PRIORITY_PS1_FIRST=PASS
CURRENT_TASK_PS1_ONLY=PASS
OLD_TASKS_MOVED_TO_QUARANTINE=PASS

## Protected old helper/R
Do not touch:
D:\ECOM_GOVERNED_RUNTIME\START_HELPER_MENU_ONLY.cmd
ION_SERVER_AUTO_CLIP_WATCH_V2.ps1
ION_R_SERVER_WORK_MODE_V1.py
old R button
old marker ION_AUTO:SERVER_READONLY_STATUS_V1

## GitHub
Repo:
ionlipca7-boop/ECOM_GOVERNED_RUNTIME

GitHub auth:
permission_admin=true
permission_push=true
permission_pull=true

## Repo warning
Repo has many modified/untracked files.
Do not commit/push blindly.
Do staged review first.
Do not delete old archives.

## Next allowed action
Verify these Memory V2 files.
Then prepare staged review.
No commit/push until Ion approval.
