@echo off
chcp 65001 >nul
cd /d D:\ECOM_GOVERNED_RUNTIME
if not exist ION_LOCAL_ASSISTANT\storage\reports mkdir ION_LOCAL_ASSISTANT\storage\reports
echo ION COMPUTER ORDER READONLY AUDIT V1>ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt
echo MODE: READ_ONLY_NO_CLEANUP_NO_DELETE>>ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt
echo.>>ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt
echo === GIT STATUS ===>>ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt
git log -1 --oneline >>ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt 2>&1
git status --short >>ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt 2>&1
echo.>>ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt
echo === POSSIBLE NOISE BACKUPS ===>>ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt
dir /s /b *before_* *.bak *.tmp >>ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt 2>nul
echo.>>ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt
echo NEXT_SAFE_ACTION=prepare_cleanup_gate_plan_only_no_delete>>ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt
type ION_LOCAL_ASSISTANT\storage\reports\computer_order_readonly_audit_v1.txt | clip
echo COPIED_TO_CLIPBOARD=1
pause
exit /b 0
