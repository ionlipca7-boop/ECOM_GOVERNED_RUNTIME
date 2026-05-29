# ION_SERVER_AUTO_SAFE_V1
echo "=== ION SERVER READONLY STATUS ADAPTER V2 COMPACT ==="
echo "MODE: READ_ONLY_NO_WRITE_NO_LIVE"
echo "MODE: READ_ONLY_COMPACT"
echo
echo "=== HOST ==="
hostname
whoami
pwd
date -Iseconds
echo
echo "=== CHECK RUNTIME PATHS ==="
for p in /home/ionlipca7/ecom_governed_runtime /home/ionlipca7/runtime_eco_v1; do
  if [ -d "$p" ]; then echo "PASS DIR $p"; else echo "MISSING DIR $p"; fi
done
echo
echo "=== GOVERNED RUNTIME POINTER HEAD ==="
if [ -f /home/ionlipca7/ecom_governed_runtime/storage/control_room/CURRENT_POINTER.json ]; then
  python3 - <<'PY'
import json
p="/home/ionlipca7/ecom_governed_runtime/storage/control_room/CURRENT_POINTER.json"
d=json.load(open(p,encoding="utf-8"))
for k in ["status","project","current_layer","next_allowed_action"]:
    print(f"{k}: {d.get(k)}")
PY
else
  echo "MISSING CURRENT_POINTER"
fi
echo
git_compact () {
  label="$1"
  root="$2"
  echo "=== ${label} GIT COMPACT ==="
  if [ -d "$root/.git" ]; then
    cd "$root" || return
    git log -1 --oneline
    c=$(git status --short | wc -l | tr -d ' ')
    echo "STATUS_COUNT=$c"
    git status --short | head -30
    if [ "$c" -gt 30 ]; then echo "STATUS_TRUNCATED=YES"; fi
  else
    echo "MISSING GIT REPO $root"
  fi
  echo
}
git_compact "GOVERNED RUNTIME" "/home/ionlipca7/ecom_governed_runtime"
git_compact "LEGACY RUNTIME" "/home/ionlipca7/runtime_eco_v1"
echo "=== TMUX SESSIONS ==="
tmux ls 2>/dev/null || echo "NO TMUX SESSION OR TMUX NOT AVAILABLE"
echo
echo "=== BOT PROCESS CHECK ==="
PROC=$(ps aux | grep -E "bot.py|telegram|ecom-bot" | grep -v grep | head -20)
if [ -n "$PROC" ]; then echo "$PROC"; else echo "NO BOT PROCESS FOUND"; fi
echo
echo "DECISION: SERVER_READONLY_STATUS_ADAPTER_V2_COMPACT_DONE"
echo "NEXT_ALLOWED_ACTION: analyze_server_readonly_status_v1"
echo "SAFETY: READ_ONLY_COMPACT_STATUS_ONLY"
echo "NO_WRITE_NO_DELETE_NO_CLEANUP_NO_EBAY_LIVE"
