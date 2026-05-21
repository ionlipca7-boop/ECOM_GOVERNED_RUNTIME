@echo off 
chcp 65001 >nul 
cd /d D:\ECOM_GOVERNED_RUNTIME 
call ION_LOCAL_ASSISTANT\scripts\server_status_readonly_v2.cmd 
echo ION HELPER SERVER OPERATOR REPORT V1 > ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo MODE: LOCAL_PLUS_SERVER_READONLY >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo. >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo === LOCAL CURRENT POINTER === >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
if exist storage\control_room\CURRENT_POINTER.json type storage\control_room\CURRENT_POINTER.json >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo. >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo === HELPER SERVER BRIDGE CHECKPOINT === >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
if exist ION_LOCAL_ASSISTANT\storage\checkpoints\LOCAL_HELPER_SERVER_STATUS_BRIDGE_PASS_V1.json type ION_LOCAL_ASSISTANT\storage\checkpoints\LOCAL_HELPER_SERVER_STATUS_BRIDGE_PASS_V1.json >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo. >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo === SERVER STATUS READONLY === >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
type ION_LOCAL_ASSISTANT\storage\reports\server_status_readonly_v2.txt >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo. >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo === LOCAL GIT READONLY === >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
git log -1 --oneline >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
git status --short >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo. >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo === NEXT SAFE ACTION === >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
echo prepare_git_review_gate_no_commit_or_resume_ecom_project_readonly >> ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
type ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt 
type ION_LOCAL_ASSISTANT\storage\reports\helper_server_operator_report_v1.txt | clip 
echo COPIED_TO_CLIPBOARD=1 
