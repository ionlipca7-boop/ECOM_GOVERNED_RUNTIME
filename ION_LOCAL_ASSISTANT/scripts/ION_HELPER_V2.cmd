@echo off
setlocal
chcp 65001 >nul
:menu
cd /d D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT
cls
echo ======================================
echo        ION HELPER FINAL LOCAL CONTROL
echo        SAFE OPERATOR / RU MODE
echo ======================================
echo.
echo [1] PREVIEW        - clipboard CMD to Notepad
echo [2] RUN SAFE CMD   - pending CMD after safety-check
echo [3] LAST REPORT    - show/copy approve-run report
echo [4] AI CHECK       - Ollama / Python / Git
echo [5] REPORTS        - open reports folder
echo [6] GIT            - local git read-only report
echo [7] CMD MODE       - return to black window, no close
echo [8] ECOM           - ECOM status read-only
echo [9] OPERATOR       - full operator report for ChatGPT
echo [S] SERVER         - server status read-only
echo [R] AUTO WATCH     - clipboard hub: server/local safe markers
echo [P] PHOTOS         - photos/images read-only audit
echo [F] FILES          - files/materials read-only audit
echo [C] COMPUTER       - computer order read-only audit
echo [A] ARCHIVE        - archive/checkpoint read-only plan
echo [T] TELEGRAM HOLD  - future only, no computer access
echo [H] HEALTH         - helper health read-only
echo [X] EXIT           - close helper menu
echo.
choice /c 123456789SPFCATHXR /n
if errorlevel 18 goto serverrclip
if errorlevel 17 goto end
if errorlevel 16 goto health
if errorlevel 15 goto telegram
if errorlevel 14 goto archive
if errorlevel 13 goto computer
if errorlevel 12 goto files
if errorlevel 11 goto photos
if errorlevel 10 goto serverstatus
if errorlevel 9 goto operator
if errorlevel 8 goto ecom
if errorlevel 7 goto cmdmode
if errorlevel 6 goto gitstatus
if errorlevel 5 goto reports
if errorlevel 4 goto ai
if errorlevel 3 goto report
if errorlevel 2 goto approve
if errorlevel 1 goto preview
goto menu
:preview
cd /d D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT
py scripts\clipboard_cmd_preview_v1.py
pause
goto menu
:approve
cd /d D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT
py scripts\approve_run_pending_cmd_v1.py
pause
goto menu
:report
cd /d D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT
if exist storage\reports\approve_run_pending_cmd_v1.json (
type storage\reports\approve_run_pending_cmd_v1.json
type storage\reports\approve_run_pending_cmd_v1.json | clip
echo COPIED_TO_CLIPBOARD=1
) else (
echo No approve-run report found.
)
pause
goto menu
:ai
cd /d D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT
if not exist storage\reports mkdir storage\reports
py scripts\ai_layer_check_v1.py > storage\reports\ai_local_check_v1.txt 2>&1
type storage\reports\ai_local_check_v1.txt
type storage\reports\ai_local_check_v1.txt | clip
echo COPIED_TO_CLIPBOARD=1
pause
goto menu
:reports
cd /d D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT
if not exist storage\reports mkdir storage\reports
start "" storage\reports
goto menu
:gitstatus
cd /d D:\ECOM_GOVERNED_RUNTIME
echo ION GIT READONLY STATUS V1>ION_LOCAL_ASSISTANT\storage\reports\git_readonly_status_v1.txt
git status --short >>ION_LOCAL_ASSISTANT\storage\reports\git_readonly_status_v1.txt 2>&1
echo.>>ION_LOCAL_ASSISTANT\storage\reports\git_readonly_status_v1.txt
git log -1 --oneline >>ION_LOCAL_ASSISTANT\storage\reports\git_readonly_status_v1.txt 2>&1
type ION_LOCAL_ASSISTANT\storage\reports\git_readonly_status_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\git_readonly_status_v1.txt | clip
echo COPIED_TO_CLIPBOARD=1
pause
goto menu
:ecom
cd /d D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT
call scripts\ecom_status_bridge_simple_v1.cmd
goto menu
:operator
cd /d D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT
call scripts\ecom_operator_prompt_v1.cmd
goto menu
:serverstatus
cd /d D:\ECOM_GOVERNED_RUNTIME
call ION_LOCAL_ASSISTANT\scripts\server_status_readonly_v2.cmd
pause
goto menu
:photos
cd /d D:\ECOM_GOVERNED_RUNTIME
call ION_LOCAL_ASSISTANT\scripts\photos_readonly_audit_v1.cmd
goto menu
:files
cd /d D:\ECOM_GOVERNED_RUNTIME
call ION_LOCAL_ASSISTANT\scripts\files_materials_readonly_audit_v1.cmd
goto menu
:computer
cd /d D:\ECOM_GOVERNED_RUNTIME
call ION_LOCAL_ASSISTANT\scripts\computer_order_readonly_audit_v1.cmd
goto menu
:archive
cd /d D:\ECOM_GOVERNED_RUNTIME
call ION_LOCAL_ASSISTANT\scripts\archive_checkpoint_readonly_plan_v1.cmd
goto menu
:telegram
cd /d D:\ECOM_GOVERNED_RUNTIME
call ION_LOCAL_ASSISTANT\scripts\telegram_hold_readonly_v1.cmd
goto menu
:health
cd /d D:\ECOM_GOVERNED_RUNTIME
call ION_LOCAL_ASSISTANT\scripts\helper_health_readonly_v1.cmd
goto menu
:cmdmode
cd /d D:\ECOM_GOVERNED_RUNTIME
echo ION HELPER MENU PAUSED. You are back in black CMD window.
echo To open menu again type: START_ION_HELPER_V2.cmd
exit /b 0
:end
echo ION HELPER MENU CLOSED
exit /b 0

:serverrclip
call D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\scripts\ION_SERVER_AUTO_CLIP_WATCH_V2.cmd
goto cmdmode
