@echo off

setlocal

chcp 65001 >nul

cd /d %~dp0\..\..

set OUT=ION_LOCAL_ASSISTANT\storage\reports\ecom_operator_status_prompt_v1.txt

echo ION ECOM OPERATOR STATUS WORKFLOW V1>%OUT%

echo MODE: READ_ONLY>>%OUT%

echo TASK FOR CHATGPT: Analyze current ECOM state and give the next safe ION step. Do not start over. No live action. No cleanup. No git commit.>>%OUT%

echo.>>%OUT%

echo CURRENT_POINTER:>>%OUT%

type storage\control_room\CURRENT_POINTER.json>>%OUT%

echo.>>%OUT%

echo HELPER_CHECKPOINT:>>%OUT%

type ION_LOCAL_ASSISTANT\storage\checkpoints\ION_HELPER_V2_ECOM_BUTTON_PASS.json>>%OUT%

echo.>>%OUT%

echo NEXT REQUEST:>>%OUT%

echo Give one safe next CMD/action in ION format.>>%OUT%

type %OUT%

clip < %OUT%

echo.

echo OPERATOR PROMPT COPIED TO CLIPBOARD

pause
