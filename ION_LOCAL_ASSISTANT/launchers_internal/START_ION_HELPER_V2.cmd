@echo off
chcp 65001 >nul
title ION HELPER STARTER
cd /d D:\ECOM_GOVERNED_RUNTIME || (echo FAIL: root folder missing & pause & exit /b 1)
if not exist D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\scripts\ION_HELPER_V2.cmd (echo FAIL: helper menu missing & pause & exit /b 1)
call D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\scripts\ION_HELPER_V2.cmd
echo.
echo ION HELPER RETURNED TO STARTER. WINDOW STAYS OPEN.
pause
