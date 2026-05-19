@echo off
setlocal
chcp 65001 >nul

cd /d %~dp0\..

echo ======================================
echo ЗАПУСК ION ЛОКАЛЬНОГО AI ПОМОЩНИКА
echo ======================================
echo.

py scripts\ai_chat_cli_v1.py

pause
