@echo off
chcp 65001 >nul
cd /d D:\ECOM_GOVERNED_RUNTIME
if not exist ION_LOCAL_ASSISTANT\storage\reports mkdir ION_LOCAL_ASSISTANT\storage\reports
echo ION TELEGRAM HOLD READONLY V1>ION_LOCAL_ASSISTANT\storage\reports\telegram_hold_readonly_v1.txt
echo MODE: HOLD_NO_REMOTE_CONTROL_NO_COMPUTER_ACCESS>>ION_LOCAL_ASSISTANT\storage\reports\telegram_hold_readonly_v1.txt
echo.>>ION_LOCAL_ASSISTANT\storage\reports\telegram_hold_readonly_v1.txt
echo Telegram is parked for future project-control layer.>>ION_LOCAL_ASSISTANT\storage\reports\telegram_hold_readonly_v1.txt
echo Local helper does NOT give Telegram access to this computer.>>ION_LOCAL_ASSISTANT\storage\reports\telegram_hold_readonly_v1.txt
echo NEXT_SAFE_ACTION=keep_telegram_on_hold_until_helper_finish_pass>>ION_LOCAL_ASSISTANT\storage\reports\telegram_hold_readonly_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\telegram_hold_readonly_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\telegram_hold_readonly_v1.txt | clip
echo COPIED_TO_CLIPBOARD=1
pause
exit /b 0
