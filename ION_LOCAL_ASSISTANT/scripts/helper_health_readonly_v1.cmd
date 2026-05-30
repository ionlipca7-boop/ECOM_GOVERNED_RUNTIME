@echo off
chcp 65001 >nul
cd /d D:\ECOM_GOVERNED_RUNTIME
if not exist ION_LOCAL_ASSISTANT\storage\reports mkdir ION_LOCAL_ASSISTANT\storage\reports
echo ION HELPER HEALTH READONLY V1>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
echo MODE: READ_ONLY_NO_PATCH_NO_CLEANUP>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
echo.>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
echo === ACTIVE MENU KEY LINES ===>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
findstr /n /i /c:"ION HELPER FINAL LOCAL CONTROL" /c:"echo [7]" /c:"echo [8]" /c:"echo [9]" /c:"echo [S]" /c:"echo [P]" /c:"echo [F]" /c:"echo [C]" /c:"echo [A]" /c:"echo [T]" /c:"echo [H]" /c:"echo [X]" /c:"choice /c" /c:"if errorlevel 17" /c:"if errorlevel 14" /c:"if errorlevel 7" ION_LOCAL_ASSISTANT\scripts\ION_HELPER_V2.cmd >>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt 2>&1
echo.>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
echo === REQUIRED WRAPPERS ===>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
if exist ION_LOCAL_ASSISTANT\scripts\photos_readonly_audit_v1.cmd echo PASS photos>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
if exist ION_LOCAL_ASSISTANT\scripts\files_materials_readonly_audit_v1.cmd echo PASS files>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
if exist ION_LOCAL_ASSISTANT\scripts\computer_order_readonly_audit_v1.cmd echo PASS computer>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
if exist ION_LOCAL_ASSISTANT\scripts\archive_checkpoint_readonly_plan_v1.cmd echo PASS archive>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
if exist ION_LOCAL_ASSISTANT\scripts\telegram_hold_readonly_v1.cmd echo PASS telegram_hold>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
if exist ION_LOCAL_ASSISTANT\scripts\helper_health_readonly_v1.cmd echo PASS health>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
echo.>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
echo NEXT_SAFE_ACTION=manual_button_test_7_8_9_S_P_F_C_A_T_H_X>>ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\helper_health_readonly_v1.txt | clip
echo COPIED_TO_CLIPBOARD=1
pause
exit /b 0
