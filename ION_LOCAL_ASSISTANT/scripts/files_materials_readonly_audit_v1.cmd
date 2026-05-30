@echo off
chcp 65001 >nul
cd /d D:\ECOM_GOVERNED_RUNTIME
if not exist ION_LOCAL_ASSISTANT\storage\reports mkdir ION_LOCAL_ASSISTANT\storage\reports
echo ION FILES MATERIALS READONLY AUDIT V1>ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt
echo MODE: READ_ONLY_NO_MOVE_NO_DELETE>>ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt
echo.>>ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt
echo === ROOT FILES ===>>ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt
dir /b >>ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt 2>&1
echo.>>ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt
echo === RECENT REPORTS ===>>ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt
dir /b /o-d ION_LOCAL_ASSISTANT\storage\reports >>ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt 2>nul
echo.>>ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt
echo NEXT_SAFE_ACTION=classify_files_before_any_cleanup_gate>>ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\files_materials_readonly_audit_v1.txt | clip
echo COPIED_TO_CLIPBOARD=1
pause
exit /b 0
