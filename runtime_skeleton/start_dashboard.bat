@echo off
cd /d D:\ECOM_OS_V7_3C_GITHUB_IMPORT_STAGE_10804
echo === VALIDATE CONTRACTS ===
python runtime_skeleton\validator.py
if errorlevel 1 (
  echo VALIDATION FAILED
  pause
  exit /b 1
)
echo.
echo === GENERATE LOCAL DASHBOARD ===
python runtime_skeleton\app.py
if errorlevel 1 (
  echo DASHBOARD GENERATION FAILED
  pause
  exit /b 1
)
echo.
echo === START LOCAL DASHBOARD SERVER ===
echo Open: http://127.0.0.1:8730/runtime_skeleton/_output/index.html
start "" "http://127.0.0.1:8730/runtime_skeleton/_output/index.html"
echo.
echo Keep this CMD window open. Press CTRL+C to stop local server.
python -m http.server 8730 --bind 127.0.0.1
pause
