@echo off
cd /d D:/ECOM_OS_V7_3C_GITHUB_IMPORT_STAGE_10804
echo === VALIDATE ===
python runtime_skeleton/validator.py
echo === START DASHBOARD ===
echo Open http://localhost:8000
python runtime_skeleton/app.py
