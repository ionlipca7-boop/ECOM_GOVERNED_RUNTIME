@echo off

setlocal

chcp 65001 >nul

cd /d %~dp0\..

echo ======================================

echo ION APPROVE RUN PENDING CMD

echo ======================================

py scripts\approve_run_pending_cmd_v1.py

pause
