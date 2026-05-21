@echo off
chcp 65001 >nul
cd /d D:\ECOM_GOVERNED_RUNTIME
call ION_LOCAL_ASSISTANT\scripts\helper_server_operator_report_v1.cmd
echo.
echo OPERATOR REPORT COPIED TO CLIPBOARD.
echo Press any key to return to ION HELPER menu...
pause >nul
