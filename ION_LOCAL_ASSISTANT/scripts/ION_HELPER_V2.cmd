@echo off

setlocal

chcp 65001 >nul

cd /d %~dp0\..

:menu

cls

echo ======================================

echo        ION HELPER V2

echo        ЛОКАЛЬНЫЙ БЕЗОПАСНЫЙ ОПЕРАТОР

echo ======================================

echo.

echo [1] ПРЕВЬЮ   - принять CMD из буфера и открыть Блокнот

echo [2] ЗАПУСК   - запустить pending CMD после safety-check

echo [3] ОТЧЁТ    - показать последний approve-run report

echo [4] AI       - проверить Ollama / Python / Git слой

echo [5] ОТЧЁТЫ   - открыть папку reports

echo [6] GIT      - read-only git status

echo [8] ECOM     - статус ECOM проекта read-only

echo [9] OPERATOR - подготовить статус для ChatGPT

echo [7] ВЫХОД

echo.

set /p choice=Выбери действие:

if "%choice%"=="1" goto preview

if "%choice%"=="2" goto approve

if "%choice%"=="3" goto report

if "%choice%"=="4" goto ai

if "%choice%"=="5" goto reports

if "%choice%"=="6" goto gitstatus

if "%choice%"=="8" goto ecom

if "%choice%"=="9" goto operator

if "%choice%"=="7" goto end

goto menu

:preview

py scripts\clipboard_cmd_preview_v1.py

pause

goto menu

:approve

py scripts\approve_run_pending_cmd_v1.py

pause

goto menu

:report

if exist storage\reports\approve_run_pending_cmd_v1.json (type storage\reports\approve_run_pending_cmd_v1.json) else (echo Нет approve-run report.)

pause

goto menu

:ai

py scripts\ai_layer_check_v1.py

pause

goto menu

:reports

if not exist storage\reports mkdir storage\reports

start "" storage\reports

goto menu

:gitstatus

cd /d %~dp0\..

echo === GIT STATUS READ-ONLY ===

git status --short

echo.

git log -1 --oneline

pause

goto menu

:ecom

call scripts\ecom_status_bridge_simple_v1.cmd

goto menu

:operator

call scripts\ecom_operator_prompt_v1.cmd

goto menu

:end

echo ION HELPER V2 CLOSED

exit /b 0
