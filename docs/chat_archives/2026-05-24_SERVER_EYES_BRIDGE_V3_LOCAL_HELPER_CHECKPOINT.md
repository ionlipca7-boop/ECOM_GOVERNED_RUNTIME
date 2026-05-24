# 2026-05-24 — SERVER EYES BRIDGE V3 LOCAL HELPER CHECKPOINT

## Summary
SERVER EYES BRIDGE V3 is the local Windows helper for restoring ChatGPT Direct Eyes read-only visibility.

## V3 button
- Governed runtime button: `SERVER EYES BRIDGE.cmd`
- Desktop button: `SERVER EYES BRIDGE.cmd`

## V3 wait-time patch
- Internal SSH forward wait time was increased from 4 seconds to 20 seconds.
- Purpose: allow SSH forward V7 enough time to become visible before Cloudflare quick tunnel capture.

## Autostart
- Installed in Windows Startup folder as `SERVER EYES BRIDGE STARTUP.cmd`.
- Expected previous PASS: `DECISION=PASS_SERVER_EYES_STARTUP_FOLDER_INSTALLED`.

## Direct Eyes V3 app
- ECOM Server Direct Eyes V3 uses a Cloudflare quick tunnel MCP URL.
- Quick tunnel URL is temporary/random/test-mode.
- If stale, run `SERVER EYES BRIDGE.cmd`, wait for `DECISION=PASS_BRIDGE_VISIBLE_URL_COPIED`, then update/create ChatGPT app MCP URL.

## Safety separation from R
- Server Eyes Bridge = read-only server eyes tunnel helper.
- R = separate server block execution bridge and must not be mixed with Server Eyes Bridge.
- No marketplace write, no restart, no cleanup/delete/move, no sensitive values.
