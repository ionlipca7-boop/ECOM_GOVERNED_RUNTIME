@echo off 
chcp 65001 >nul 
cd /d D:\ECOM_GOVERNED_RUNTIME 
echo ION SERVER STATUS READONLY V2 > ION_LOCAL_ASSISTANT\storage\reports\server_status_readonly_v2.txt 
echo MODE: LOCAL_HELPER_TO_SERVER_READONLY >> ION_LOCAL_ASSISTANT\storage\reports\server_status_readonly_v2.txt 
echo. >> ION_LOCAL_ASSISTANT\storage\reports\server_status_readonly_v2.txt 
ssh -i "C:\Users\Ion Lipca\.ssh\ecom_os_v3_server_ed25519" -o IdentitiesOnly=yes -o BatchMode=yes -o ConnectTimeout=10 -o StrictHostKeyChecking=yes ionlipca7@34.29.150.106 "echo SERVER_SSH_OK; hostname; whoami; pwd; echo PATHS; if [ -d /home/ionlipca7/ecom_governed_runtime ]; then echo PASS GOVERNED_RUNTIME; else echo MISS GOVERNED_RUNTIME; fi; if [ -d /home/ionlipca7/runtime_eco_v1 ]; then echo PASS LEGACY_RUNTIME; else echo MISS LEGACY_RUNTIME; fi; echo TMUX; tmux ls 2>/dev/null || echo NO_TMUX" >> ION_LOCAL_ASSISTANT\storage\reports\server_status_readonly_v2.txt 2>&1 
echo. >> ION_LOCAL_ASSISTANT\storage\reports\server_status_readonly_v2.txt 
echo END SERVER STATUS READONLY >> ION_LOCAL_ASSISTANT\storage\reports\server_status_readonly_v2.txt 
type ION_LOCAL_ASSISTANT\storage\reports\server_status_readonly_v2.txt 
type ION_LOCAL_ASSISTANT\storage\reports\server_status_readonly_v2.txt | clip 
rem NOTEPAD_DISABLED_REPORT_IS_PRINTED_AND_COPIED 
echo COPIED_TO_CLIPBOARD=1 
