@echo off
setlocal

cd /d D:\ECOM_OS_V7_3C_GITHUB_IMPORT_STAGE_10804

echo === VALIDATE CONTRACTS ===
python runtime_skeleton\validator.py
if errorlevel 1 goto failed

echo.
echo === GENERATE STATIC DASHBOARD ===
python runtime_skeleton\app.py
if errorlevel 1 goto failed

echo.
echo === PYTHON COMPILE CHECK ===
py -m py_compile runtime_skeleton\app.py runtime_skeleton\contract_loader.py runtime_skeleton\validator.py
if errorlevel 1 goto failed

echo.
echo === GIT DIFF CHECK ===
git diff --check
if errorlevel 1 goto failed

echo.
echo === GIT STATUS ===
git status --short

echo.
echo LOCAL VERIFY PASS. No commit, no push, no delete.
pause
exit /b 0

:failed
echo.
echo LOCAL VERIFY FAILED. No commit, no push, no delete.
pause
exit /b 1
