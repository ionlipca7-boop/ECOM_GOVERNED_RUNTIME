@echo off
chcp 65001 >nul
cd /d D:\ECOM_GOVERNED_RUNTIME
if not exist ION_LOCAL_ASSISTANT\storage\reports mkdir ION_LOCAL_ASSISTANT\storage\reports
echo ION PHOTOS READONLY AUDIT V1>ION_LOCAL_ASSISTANT\storage\reports\photos_readonly_audit_v1.txt
echo MODE: READ_ONLY_NO_EDIT_NO_DELETE>>ION_LOCAL_ASSISTANT\storage\reports\photos_readonly_audit_v1.txt
echo.>>ION_LOCAL_ASSISTANT\storage\reports\photos_readonly_audit_v1.txt
echo === IMAGE FILES FOUND ===>>ION_LOCAL_ASSISTANT\storage\reports\photos_readonly_audit_v1.txt
dir /s /b *.jpg *.jpeg *.png *.webp *.gif >>ION_LOCAL_ASSISTANT\storage\reports\photos_readonly_audit_v1.txt 2>nul
echo.>>ION_LOCAL_ASSISTANT\storage\reports\photos_readonly_audit_v1.txt
echo NEXT_SAFE_ACTION=review_photo_folders_then_define_photo_workflow_no_edit>>ION_LOCAL_ASSISTANT\storage\reports\photos_readonly_audit_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\photos_readonly_audit_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\photos_readonly_audit_v1.txt | clip
echo COPIED_TO_CLIPBOARD=1
pause
exit /b 0
