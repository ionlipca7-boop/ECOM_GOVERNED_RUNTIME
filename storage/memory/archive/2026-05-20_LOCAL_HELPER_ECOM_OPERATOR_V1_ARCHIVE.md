# Local Helper ECOM Operator V1 — session archive

Date: 2026-05-20

## Final status

```text
LOCAL HELPER OPERATOR V1 = PASS / FINISH
SERVER ADAPTER FRONT = READY
NEXT_ALLOWED_ACTION = server_readonly_status_adapter_v1
```

## Final pointer state

```text
current_layer = local_helper_ecom_operator_bridge_complete_v1
next_allowed_action = resume_ecom_project_with_local_helper_readonly_operator_v1
status = PASS
mode = LOCAL_SAFE_OPERATOR_READ_ONLY
```

## Commits completed

```text
4a341bb Add local helper ECOM operator bridge v1
d8371a1 Mark local helper ECOM operator bridge complete
6d43909 Fix final local helper menu launcher
```

## How to start the helper

```cmd
cd /d D:\ECOM_GOVERNED_RUNTIME
START_ION_HELPER_V2.cmd
```

Desktop launcher also exists locally: `ION_HELPER_V2_START.cmd`.

## Final menu

```text
[1] PREVIEW / ПРЕВЬЮ  - буфер в Блокнот
[2] RUN / ЗАПУСК      - pending CMD после safety-check
[3] REPORT / ОТЧЁТ    - последний approve-run report
[4] AI / ИИ           - проверить Ollama / Python / Git
[5] REPORTS / ОТЧЁТЫ  - открыть папку reports
[6] GIT               - read-only git status
[7] EXIT / ВЫХОД
[8] ECOM              - статус ECOM проекта read-only
[9] OPERATOR          - статус для ChatGPT
```

Final manual UI test: menu opened, all items were visible, pressing `7` returned to CMD with `ION HELPER V2 CLOSED`.

## Working workflow

```text
ChatGPT gives one gray CMD block.
User pastes into Windows CMD.
CMD creates a report.
CMD copies report to clipboard.
User presses Ctrl+V in ChatGPT.
ChatGPT gives the next safe step.
```

## Confirmed capabilities

```text
clipboard preview = PASS
manual approve-run = PASS
safety block = PASS
one-enter approve runner = PASS
ECOM read-only status button = PASS
operator prompt button = PASS
GitHub sync / commit / push / verify = PASS
server adapter front plan = PASS
```

## Safety gates

Allowed now: read, scan, report, preview, approve, safe run, copy report to clipboard.

Blocked until explicit gate: cleanup, delete, runtime cleanup, extra Git staging, live marketplace actions, server write actions, private config output, server Git push.

## Server adapter front

Prepared but not executed on server.

```text
SERVER_ADAPTER_FRONT_V1 = PASS
MODE = PLAN_ONLY_NO_SERVER_WRITE
NEXT_ALLOWED_ACTION = server_readonly_status_adapter_v1
```

Next server check should verify runtime folder, legacy runtime folder, tmux bot session, project pointer, state files, reports, Git status, and last Git commit. Server mode starts read-only.

## Lessons for future projects

1. Do not paste multiline Python into Windows CMD.
2. Avoid PowerShell here-strings inside normal CMD paste.
3. Prefer short one-line commands or plain CMD report blocks.
4. Every step should create a report and copy it to clipboard.
5. Do not open interactive menus inside long CMD blocks.
6. Use `choice /c 123456789` for menu selection.
7. Avoid `>` in menu text unless escaped.
8. Before committing: stage exact files, inspect diff, run `git diff --check`, and compile-check Python when relevant.
9. Runtime reports and checkpoints remain local unless separately approved.
10. Server helper must be separate Bash/tmux adapter.
11. Ollama/Llama can become a future local AI layer, but the current helper works without it.

## Remaining local items

Local reports, checkpoints, old test bridge files, backup pointer files, and older audit/quarantine/state files remain untracked. Do not clean them without a cleanup gate.

## Next session

Start helper, press `9`, paste output to ChatGPT, then continue with `server_readonly_status_adapter_v1`.
