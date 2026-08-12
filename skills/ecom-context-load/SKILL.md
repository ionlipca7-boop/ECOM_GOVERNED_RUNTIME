---
name: ecom-context-load
version: 0.1.0
mode: READONLY
risk: LOW
---

# ECOM Context Load

## Purpose

Build one bounded, hash-anchored context packet before planning or acting. This skill does not modify project files, Product Vault, browser state, marketplace state, Git branches, or canonical registries.

## Required order

1. Resolve the exact approved ECOM root and root_id.
2. Read root governance (`AGENTS.md`).
3. Read `storage/v3_core/reports/COORDINATOR_INBOX_CURRENT_RU.md` and capture its SHA256.
4. Read current project/master/stage pointers that the inbox names or requires.
5. Resolve the active product/case/listing/screen context only from canonical pointers or explicit operator input.
6. Resolve current owner(s), owner locks and source SHA guards.
7. Read relevant debt/idea/request queues.
8. Produce `ECOM_FACTORY_CONTEXT_PACKET_V1`.
9. Validate fail-closed safety flags.
10. Return exactly one `next_safe_action` consistent with current governance.

## Required safety defaults

```text
marketplace_write=false
ebay_write=0
save_publish=false
active_ui_write=false
delete_move_rename=false
```

If any required authoritative pointer is missing, stale, contradictory or unreadable, output BLOCK with the conflicting sources and stop. Do not infer a replacement authority.

## Product-bound rule

If a task is product-bound, `product_key` must come from canonical Product Vault/Product Intake binding or explicit operator instruction that is subsequently verified. Never guess a product key from a title, photo or marketplace URL.

## Owner rule

This skill may identify owners and read their evidence. It never becomes a new domain owner and never writes into an owner's source path.

## Output

A JSON object conforming to:

`schemas/ecom_factory_context_packet_schema_v1.json`

The packet must include source paths and hashes sufficient for a later skill to detect drift before acting.
