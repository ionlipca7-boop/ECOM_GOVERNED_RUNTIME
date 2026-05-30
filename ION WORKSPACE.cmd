@echo off
setlocal EnableExtensions
title ION WORKSPACE HUB V1
cd /d D:\ECOM_GOVERNED_RUNTIME
echo ION WORKSPACE HUB V1
echo STARTING=Server Eyes + AutoWatch + Helper + GitHub YSTATUS
echo NO_EBAY_LIVE=true
echo NO_GIT_PUSH=true
echo NO_DELETE=true
if exist "ION_LOCAL_ASSISTANT\launchers_internal\START_ECOM_EYES_ALL.cmd" start "ECOM EYES ALL" /min "ION_LOCAL_ASSISTANT\launchers_internal\START_ECOM_EYES_ALL.cmd"
timeout /t 4 /nobreak >nul
if exist "ION_LOCAL_ASSISTANT\launchers_internal\START_ION_SERVER_AUTOWATCH_V2.cmd" start "ION SERVER AUTOWATCH V2" /min "ION_LOCAL_ASSISTANT\launchers_internal\START_ION_SERVER_AUTOWATCH_V2.cmd"
timeout /t 3 /nobreak >nul
if exist "ION_LOCAL_ASSISTANT\launchers_internal\START_ION_HELPER_V2.cmd" start "ION HELPER V2" "ION_LOCAL_ASSISTANT\launchers_internal\START_ION_HELPER_V2.cmd"
timeout /t 6 /nobreak >nul
echo FINAL_STATUS=RUNNING_YSTATUS_V2
if exist "ION_LOCAL_ASSISTANT\autoclip\YSTATUS.cmd" call "ION_LOCAL_ASSISTANT\autoclip\YSTATUS.cmd"
echo WORKSPACE_HUB_STARTED=true
echo FINAL_CLIPBOARD_SHOULD_BE=ION_AUTO:ECOM_WORKSPACE_STATUS_V2
pause
