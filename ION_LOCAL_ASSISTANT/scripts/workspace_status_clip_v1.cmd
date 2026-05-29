@echo off
chcp 65001 >nul
set OUT=D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\storage\reports\workspace_last_start_status.txt
echo ION WORKSPACE STATUS CLIP V1>%OUT%
echo MODE=AUTO_SUMMARY_TO_CLIPBOARD>>%OUT%
echo.>>%OUT%
echo === NGROK / EYES STATUS FILE ===>>%OUT%
if exist D:\ECOM_GOVERNED_RUNTIME\NGROK_EYES_STATUS.txt (type D:\ECOM_GOVERNED_RUNTIME\NGROK_EYES_STATUS.txt>>%OUT%) else (echo NGROK_EYES_STATUS.txt MISSING>>%OUT%)
echo.>>%OUT%
echo === PROCESS CHECK ===>>%OUT%
tasklist | findstr /i ngrok.exe>>%OUT% 2>&1
tasklist | findstr /i powershell.exe>>%OUT% 2>&1
echo.>>%OUT%
echo MARKER_TO_TEST=ION_AUTO:SERVER_READONLY_STATUS_V1>>%OUT%
echo DECISION=WORKSPACE_STATUS_READY_AND_COPIED>>%OUT%
echo NEXT_ALLOWED_ACTION=test_marker_or_continue_project>>%OUT%
echo NO_DELETE_NO_CLEANUP_NO_EBAY_LIVE_NO_SERVER_WRITE>>%OUT%
type %OUT%
clip < %OUT%
echo === WORKSPACE STATUS COPIED TO CLIPBOARD ===
