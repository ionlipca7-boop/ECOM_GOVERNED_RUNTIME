# 2026-05-20 — Local Helper STOP addendum: UI/path issue

## Stop reason

The operator asked to stop for today after discovering one more UI/path issue in the local helper.

## What is already saved and verified

Previously saved GitHub state:

```text
LOCAL HELPER OPERATOR V1 = PASS / FINISH
SERVER ADAPTER FRONT = READY
NEXT_ALLOWED_ACTION = server_readonly_status_adapter_v1
```

Main commits already pushed:

```text
4a341bb Add local helper ECOM operator bridge v1
d8371a1 Mark local helper ECOM operator bridge complete
6d43909 Fix final local helper menu launcher
4847cd2 Archive local helper operator V1 session
```

The archive file created earlier:

```text
storage/memory/archive/2026-05-20_LOCAL_HELPER_ECOM_OPERATOR_V1_ARCHIVE.md
```

## New problem discovered after the archive

The helper was opened again from the launcher / Desktop path.

Observed behavior:

```text
[4] AI initially failed with:
C:\Python314\python.exe: can't open file 'D:\ECOM_GOVERNED_RUNTIME\scripts\ai_layer_check_v1.py'
```

Root cause:

```text
The menu was running from the wrong working directory.
It searched D:\ECOM_GOVERNED_RUNTIME\scripts\...
instead of D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\scripts\...
```

A local repair was then performed to use absolute paths inside the helper menu and launchers.

Local audit after repair showed:

```text
MENU_ITEMS = PASS
CHOICE_CHECK = PASS
REQUIRED_FILES = PASS
ROOT_LAUNCHER = PASS
DESKTOP_LAUNCHER = PASS
DECISION = HELPER_ABSOLUTE_PATHS_REPAIRED_TEST_REQUIRED
```

Manual test after local path repair:

```text
[4] AI / ИИ worked.
AI LAYER CHECK COMPLETE
Report path: D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\storage\reports\ai_layer_check_v1.json
```

## Remaining issue at stop

Operator then reported that the black CMD window / menu did not fully close in the expected way.

Observed screen showed:

```text
Выбери действие: 7
ION HELPER V2 CLOSED
```

Meaning: the helper script did execute exit logic, but the CMD window remained visible / returned to prompt. This may be normal when launched from an already-open CMD, but needs tomorrow's verification from the real Desktop launcher and root launcher.

## Important current risk

The local absolute-path repair was performed after the last code commit. It may not yet be committed/pushed as code.

Do not assume repository code equals current local repaired code until verified with:

```cmd
git status --short
git diff -- ION_LOCAL_ASSISTANT/scripts/ION_HELPER_V2.cmd START_ION_HELPER_V2.cmd
```

## Tomorrow next allowed route

Start with read-only/local verification, not new build.

Recommended next action:

```text
local_helper_ui_path_exit_audit_v1
```

Checklist:

```text
1. Verify git status and local diffs.
2. Inspect ION_HELPER_V2.cmd working-directory lines.
3. Inspect START_ION_HELPER_V2.cmd and Desktop launcher content.
4. Test launch from root launcher.
5. Test launch from Desktop launcher.
6. Clarify expected close behavior:
   - if launched from existing CMD, returning to prompt is acceptable;
   - if launched by double-click, window should close after 7.
7. Only after PASS, commit/push the absolute-path UI fix if needed.
```

## Rules for tomorrow

```text
No cleanup/delete.
No server write.
No eBay live action.
No extra git add until diff is inspected.
No auto-open menu inside long CMD block.
Manual UI tests only.
Every diagnostic block must create a report and copy it to clipboard.
```

## Server adapter remains next after helper UI is stable

After local helper UI is fully stable and saved, continue with:

```text
server_readonly_status_adapter_v1
```

Server remains read-only first.
