@echo off
chcp 65001 >nul
cd /d D:\ECOM_GOVERNED_RUNTIME
if not exist "ION_LOCAL_ASSISTANT\storage\reports\server_auto_clip_watch_v2_last_output.txt" echo STATUS=BLOCK_LAST_REPORT_NOT_FOUND& exit /b 1
type "ION_LOCAL_ASSISTANT\storage\reports\server_auto_clip_watch_v2_last_output.txt"
clip < "ION_LOCAL_ASSISTANT\storage\reports\server_auto_clip_watch_v2_last_output.txt"
echo STATUS=PASS_LAST_AUTOWATCH_REPORT_RECOPIED_TO_CLIPBOARD
echo FILE=ION_LOCAL_ASSISTANT\storage\reports\server_auto_clip_watch_v2_last_output.txt
exit /b 0