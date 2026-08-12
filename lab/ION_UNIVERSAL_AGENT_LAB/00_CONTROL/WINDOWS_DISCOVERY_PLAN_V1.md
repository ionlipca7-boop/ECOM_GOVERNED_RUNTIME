# WINDOWS DISCOVERY PLAN V1

Goal: discover the physical Windows lab root without touching production.

Preferred root: D:\ION_UNIVERSAL_AGENT_LAB
Fallback: reuse an already-existing adjacent lab root only after exact readback.

Rules:
- READONLY discovery first.
- Never rename/move/delete production files.
- ECOM OS remains canonical.
- Knowledge Lab and IWE are READONLY dependencies.
- No marketplace/eBay/save/publish.

Discovery outputs: root existence, tree, writable test target inside lab only, dependency paths, version pointers, hashes where available.
