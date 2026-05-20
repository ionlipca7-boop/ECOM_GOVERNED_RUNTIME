@echo off

setlocal

chcp 65001 >nul

cd /d %~dp0\..\..

set OUT=ION_LOCAL_ASSISTANT\storage\reports\ecom_status_bridge_simple_v1.txt

echo ION ECOM STATUS BRIDGE SIMPLE V1>%OUT%

echo MODE: READ_ONLY>>%OUT%

echo.>>%OUT%

echo === CURRENT POINTER ===>>%OUT%

type storage\control_room\CURRENT_POINTER.json>>%OUT%

echo.>>%OUT%

echo === HELPER CHECKPOINT ===>>%OUT%

type ION_LOCAL_ASSISTANT\storage\checkpoints\LOCAL_HELPER_CORE_V1_PASS.json>>%OUT%

echo.>>%OUT%

echo === GIT LAST COMMIT ===>>%OUT%

git log -1 --oneline>>%OUT%

echo.>>%OUT%

echo === GIT STATUS SHORT ===>>%OUT%

git status --short>>%OUT%

type %OUT%

clip < %OUT%

echo.

echo SUMMARY COPIED TO CLIPBOARD

pause
