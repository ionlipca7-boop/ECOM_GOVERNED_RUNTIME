@echo off
setlocal
chcp 65001 >nul

cd /d %~dp0\..

echo ОТКРЫВАЕМ ION DASHBOARD...

start "" dashboard\index.html
