$ErrorActionPreference = 'Continue'
$Root = 'D:\ECOM_GOVERNED_RUNTIME'
$Marker = 'ION_AUTO:SERVER_READONLY_STATUS_V1'
$LastHash = ''
$LastOutputPath = Join-Path $Root 'ION_LOCAL_ASSISTANT\storage\reports\server_auto_clip_watch_v2_last_output.txt'

Write-Host '=== ION SERVER AUTO CLIP WATCH V2 ==='
Write-Host 'MODE=MARKER_ONLY_TO_STABLE_R_ENGINE'
Write-Host 'COPY MARKER: ION_AUTO:SERVER_READONLY_STATUS_V1'
Write-Host 'OUTPUT=CONSOLE_AND_CLIPBOARD_AND_LAST_REPORT_FILE'
Write-Host 'READY=1'

while ($true) {
  try {
    $Clip = Get-Clipboard -Raw -ErrorAction Stop
  } catch {
    Start-Sleep -Seconds 1
    continue
  }

  if ($null -eq $Clip) {
    Start-Sleep -Seconds 1
    continue
  }

  $Trim = $Clip.Trim()

  if ($Trim -ne $Marker) {
    if ($LastHash -ne '') { $LastHash = '' }
    Start-Sleep -Seconds 1
    continue
  }

  $Bytes = [Text.Encoding]::UTF8.GetBytes($Trim)
  $Hash = [BitConverter]::ToString([Security.Cryptography.SHA1]::Create().ComputeHash($Bytes))

  if ($Hash -eq $LastHash) {
    Start-Sleep -Seconds 1
    continue
  }

  $LastHash = $Hash

  Write-Host ''
  Write-Host 'AUTO_MARKER_DETECTED'
  Write-Host 'AUTO_EXEC_START'

  $Out = & py -X utf8 (Join-Path $Root 'ION_LOCAL_ASSISTANT\scripts\ION_R_SERVER_WORK_MODE_V1.py') 2>&1 | Out-String

  Set-Content -Path $LastOutputPath -Value $Out -Encoding UTF8
  Set-Clipboard -Value $Out

  Write-Host ''
  Write-Host '===== ION AUTO OUTPUT BEGIN ====='
  Write-Host $Out
  Write-Host '===== ION AUTO OUTPUT END ====='
  Write-Host ''
  Write-Host 'AUTO_DONE_OUTPUT_PRINTED_AND_COPIED_TO_CLIPBOARD'
  Write-Host ('LAST_REPORT=' + $LastOutputPath)

  Start-Sleep -Seconds 2
}