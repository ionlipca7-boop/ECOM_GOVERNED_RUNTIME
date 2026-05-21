@echo off
setlocal
chcp 65001 >nul
:menu
cd /d D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT
cls
echo ======================================
echo        ION HELPER V2
echo        LOCAL SAFE OPERATOR / RU MODE
echo ======================================
echo.
echo [1] PREVIEW / ПРЕВЬЮ  - буфер в Блокнот
echo [2] RUN / ЗАПУСК      - pending CMD после safety-check
echo [3] REPORT / ОТЧЁТ    - последний approve-run report
echo [4] AI / ИИ           - проверить Ollama / Python / Git
echo [5] REPORTS / ОТЧЁТЫ  - открыть папку reports
echo [6] GIT               - read-only git status
echo [7] EXIT / ВЫХОД
echo [8] ECOM              - статус ECOM проекта read-only
echo [9] OPERATOR          - статус для ChatGPT
echo [S] SERVER            - server status read-only
echo.
choice /c 123456789S /n /m "Выбери действие: "
if errorlevel 10 goto serverstatus
if errorlevel 9 goto operator
if errorlevel 8 goto ecom
if errorlevel 7 goto end
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
if exist storage\reports\approve_run_pending_cmd_v1.json (type storage\reports\approve_run_pending_cmd_v1.json) else (echo No approve-run report found.)
pause
goto menu
:ai
cd /d D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT
py scripts\ai_layer_check_v1.py
pause
goto menu
:reports
cd /d D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT
if not exist storage\reports mkdir storage\reports
start "" storage\reports
goto menu
:gitstatus
cd /d D:\ECOM_GOVERNED_RUNTIME
echo === GIT STATUS READ-ONLY ===
git status --short
echo.
git log -1 --oneline
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
:end
echo ION HELPER V2 CLOSED
