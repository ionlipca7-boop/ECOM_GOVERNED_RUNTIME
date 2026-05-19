@echo off
setlocal
chcp 65001 >nul

cd /d %~dp0\..

:menu
cls
echo ======================================
echo        ION ЛОКАЛЬНЫЙ ПОМОЩНИК
echo        РЕЖИМ: ТОЛЬКО ПРОВЕРКА
echo ======================================
echo.
echo [1] ФАЙЛЫ  - быстрая проверка папки
echo [2] ФАЙЛЫ  - глубокая проверка папки
echo [3] ФОТО   - проверить и сгруппировать фотографии
echo [4] ПРОЕКТЫ - найти и распознать папки проектов
echo [5] ОТЧЁТЫ - открыть папку с отчётами
echo [6] AI     - проверить будущий AI-слой
echo [7] ВЫХОД
echo.
set /p choice=Выбери действие: 

if "%choice%"=="1" goto fastscan
if "%choice%"=="2" goto deepscan
if "%choice%"=="3" goto photos
if "%choice%"=="4" goto projects
if "%choice%"=="5" goto reports
if "%choice%"=="6" goto ai
if "%choice%"=="7" exit

goto menu

:fastscan
set /p folder=Вставь путь к папке: 
py scripts\scan_folder_report_v0.py --path "%folder%"
pause
goto menu

:deepscan
set /p folder=Вставь путь к папке: 
py scripts\scan_folder_report_v1.py --path "%folder%"
pause
goto menu

:photos
set /p folder=Вставь путь к папке с фото: 
py scripts\photo_organizer_dry_run_v1.py --path "%folder%"
pause
goto menu

:projects
set /p folder=Вставь путь к общей папке: 
py scripts\project_detector_v1.py --path "%folder%"
pause
goto menu

:reports
if not exist storage\reports mkdir storage\reports
start "" storage\reports
goto menu

:ai
py scripts\ai_layer_check_v1.py
pause
goto menu
