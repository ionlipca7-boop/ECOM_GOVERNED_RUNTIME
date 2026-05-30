@echo off
chcp 65001 >nul
cd /d D:\ECOM_GOVERNED_RUNTIME
if not exist ION_LOCAL_ASSISTANT\storage\reports mkdir ION_LOCAL_ASSISTANT\storage\reports
echo ION ARCHIVE CHECKPOINT READONLY PLAN V1>ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt
echo MODE: READ_ONLY_PLAN_NO_COMMIT_NO_PUSH>>ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt
echo.>>ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt
echo === CURRENT POINTER ===>>ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt
if exist storage\control_room\CURRENT_POINTER.json type storage\control_room\CURRENT_POINTER.json >>ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt
echo.>>ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt
echo === LOCAL CHECKPOINTS ===>>ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt
dir /b ION_LOCAL_ASSISTANT\storage\checkpoints >>ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt 2>nul
echo.>>ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt
echo NEXT_SAFE_ACTION=build_final_helper_checkpoint_after_button_test>>ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\archive_checkpoint_readonly_plan_v1.txt | clip
echo COPIED_TO_CLIPBOARD=1
pause
exit /b 0
