# SERVER EYES NGROK ONE-BUTTON CHECKPOINT

Date: 2026-05-25
Mode: read-only server visibility checkpoint

## Result

Server Direct Eyes via NGROK was verified in a server-only ChatGPT chat.

Final server-only verdict:

PASS_READONLY_NGROK_SERVER_ACCESS_VERIFIED_THIS_CHAT_USABLE_NO_WRITE_NO_RESTART_NO_DELETE_NO_CLEANUP_NO_EBAY_NO_LIVE

## Working model

A single local Windows helper named START_ECOM_EYES_ALL is the preferred user-facing entry point.

It starts the local Server Eyes bridge, waits for the local MCP bridge, then starts NGROK forwarding for the ChatGPT MCP app named ECOM Server Direct Eyes NGROK.

The older helper attempts are deprecated. They should be moved to OLD_ECOM_BUTTONS_DO_NOT_USE after one clean final test.

The internal Server Eyes Bridge component remains required and must not be deleted.

## Confirmed server read-only state

server_health_readonly PASS:

- mode READONLY
- runtime roots exist
- Python 3.11.2
- Git 2.39.5

read_current_pointers PASS:

- CURRENT_BRIDGE_STATE PASS
- CURRENT_POINTER PASS_NEW_CHAT_TRANSITION_ARCHIVE_POINTER_V1
- SERVER_V6_5_CURRENT_STEP_POINTER PASS_SERVER_V6_5_STATIC_BRIDGE_CHECKPOINT_READY
- SERVER_V6_5_RUNTIME_CURRENT_POINTER PASS_V6_5_RUNTIME_ACTIVATION_CHECKPOINT_READY
- REAL_PRODUCT_EXTERNAL_READONLY_FETCH_POINTER_V6_5 remains BLOCKED_READONLY_URL_FETCH_EMPTY_OR_FAILED

read_latest_reports PASS.

## Remaining blocker

The remaining V6.5 blocker is the real product external read-only fetch / AliExpress redirect loop.

Before retrying that work, search existing archive, GitHub, and server read-only records for prior workaround.

## Safety gates

- live closed
- marketplace and eBay write closed
- restart closed
- cleanup/delete/move closed
- secret print forbidden

## Two-chat workflow

If GitHub and Server Direct Eyes are not exposed in the same chat:

1. Use server-only chat for Direct Eyes NGROK read-only checks.
2. Paste the server report into GitHub/archive chat.
3. Archive only confirmed state to GitHub.

## Final verdict

A = NGROK read-only server visibility PASS
B = one-button helper PASS created
C = GitHub and Server same-chat still not guaranteed
D = V6.5 ready for read-only continuation only
FINISH = PASS_SERVER_EYES_NGROK_ONE_BUTTON_CHECKPOINT
