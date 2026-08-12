# ecom-context-restore

Purpose: resume from a saved checkpoint without guessing.

1. Read checkpoint and referenced source truth.
2. Revalidate exact refs/SHAs and owner leases.
3. Mark stale references explicitly.
4. Re-read current coordinator/control pointers when available.
5. Restore only decisions supported by evidence.
6. If a required ref changed, return REBASE_REQUIRED instead of silently continuing.
7. No production write during restore.
