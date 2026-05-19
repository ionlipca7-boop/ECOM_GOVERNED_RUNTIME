@echo off
setlocal

cd /d %~dp0\..

:menu
cls
echo ======================================
echo ION LOCAL ASSISTANT CONTROL MENU
echo MODE: DRY_RUN_ONLY
echo ======================================
echo.
echo 1 - Basic folder scan
echo 2 - Extended folder scan
echo 3 - Project detector
echo 4 - Open reports folder
echo 5 - Exit
echo.
set /p choice=Select option: 

if "%choice%"=="1" goto basicscan
if "%choice%"=="2" goto extendedscan
if "%choice%"=="3" goto projectdetector
if "%choice%"=="4" goto reports
if "%choice%"=="5" exit

goto menu

:basicscan
set /p folder=Enter folder path: 
py scripts\scan_folder_report_v0.py --path "%folder%"
pause
goto menu

:extendedscan
set /p folder=Enter folder path: 
py scripts\scan_folder_report_v1.py --path "%folder%"
pause
goto menu

:projectdetector
set /p folder=Enter root path: 
py scripts\project_detector_v1.py --path "%folder%"
pause
goto menu

:reports
start "" storage\reports
goto menu
