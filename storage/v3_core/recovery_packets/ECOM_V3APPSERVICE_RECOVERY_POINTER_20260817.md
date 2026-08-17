# ECOM V3AppService Recovery Pointer — 2026-08-17

Canonical emergency recovery SHA256: `3ff407fec4d15b852cb0c1c7139c1ebd208b110e1d4e46c02cbc04878199c2c1`

Corrupted production SHA256: `41ca955586b3a1bf99452b04289af437edfbb38f29eca7c305e8f05717d8819f`

Recovery marker: `V3APPSERVICE_RECOVERY_BRIDGE_V2`

Rules: never write an `ECOM_OS_SHA_PATCH_V1` JSON envelope as a `.py` payload; whole-file/real in-memory patch only; verify preimage SHA, compile, symbol/import smoke, postwrite SHA readback, rollback on failure; one writer per target; workers may not restart Project Server; canonical One-Click only; marketplace write/save/publish fail-closed by default.

Current status at capture: V7 isolated validation PASS; local activation true; public toolset 13/13 PASS; public/local parity PASS. Remaining non-terminal debts: `STOP_SAFE_HOME_P1_ISOLATED_ACCEPTANCE_FAILED_SERVER_HEALTHY` and audit chain `previous_event_hash mismatch` count 1274.
