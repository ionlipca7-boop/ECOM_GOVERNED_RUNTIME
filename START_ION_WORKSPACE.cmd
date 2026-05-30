@echo off
chcp 65001 >nul
title ION WORKSPACE START
cd /d D:\ECOM_GOVERNED_RUNTIME || (echo FAIL: root folder missing & pause & exit /b 1)
echo ==== ION WORKSPACE START ====
echo MODE=LOCAL_START_ONLY_NO_DELETE_NO_EBAY_NO_SERVER_WRITE
echo.
if not exist D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\launchers_internal\START_ECOM_EYES_ALL.cmd (echo FAIL: START_ECOM_EYES_ALL.cmd missing & pause & exit /b 1)
if not exist D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\launchers_internal\START_ION_HELPER_V2.cmd (echo FAIL: START_ION_HELPER_V2.cmd missing & pause & exit /b 1)
if not exist D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\launchers_internal\START_ION_SERVER_AUTOWATCH_V2.cmd (echo FAIL: START_ION_SERVER_AUTOWATCH_V2.cmd missing & pause & exit /b 1)
echo STEP 1 - start Server Eyes / ngrok workspace minimized
start "ION ECOM EYES ALL" /min cmd /k call "D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\launchers_internal\START_ECOM_EYES_ALL.cmd"
echo WAIT 55 SEC FOR EYES/NGROK STATUS
timeout /t 55 /nobreak >nul
echo STEP 2 - start AutoWatch Hub
start "ION AUTOWATCH HUB" cmd /k call "D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\launchers_internal\START_ION_SERVER_AUTOWATCH_V2.cmd"
timeout /t 2 /nobreak >nul
echo STEP 3 - start ION Helper menu
start "ION HELPER MENU" cmd /k call "D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\launchers_internal\START_ION_HELPER_V2.cmd"
echo STEP 4 - collect clean workspace status to clipboard
call D:\ECOM_GOVERNED_RUNTIME\ION_LOCAL_ASSISTANT\autoclip\YSTATUS.cmd"
timeout /t 5 /nobreak >nul
exit /b 0

