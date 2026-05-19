@echo off
setlocal

cd /d %~dp0\..

echo ION LOCAL ASSISTANT V0
echo DRY_RUN_ONLY

if "%~1"=="" (
    echo Usage:
    echo run_scan_windows.cmd "C:\path\to\folder"
    exit /b 1
)

py scripts\scan_folder_report_v0.py --path "%~1"

echo.
echo REPORTS GENERATED IN:
echo storage\reports\
