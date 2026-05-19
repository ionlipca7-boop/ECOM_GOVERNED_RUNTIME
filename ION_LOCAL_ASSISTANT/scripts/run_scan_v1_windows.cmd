@echo off
setlocal

cd /d %~dp0\..

echo ======================================
echo ION LOCAL ASSISTANT V1
echo MODE: DRY_RUN_ONLY
echo ======================================

if "%~1"=="" (
    echo Usage:
    echo run_scan_v1_windows.cmd "C:\path\to\folder"
    exit /b 1
)

py scripts\scan_folder_report_v1.py --path "%~1"

echo.
echo REPORTS GENERATED IN:
echo storage\reports\
echo.
pause
