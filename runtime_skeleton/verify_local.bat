@echo off

cd /d D:\ECOM_OS_V7_3C_GITHUB_IMPORT_STAGE_10804

echo === VALIDATE CONTRACTS ===

python runtime_skeleton\validator.py

echo.
echo === GENERATE STATIC DASHBOARD ===

python runtime_skeleton\app.py

echo.
echo === GIT STATUS ===

git status --short

pause
