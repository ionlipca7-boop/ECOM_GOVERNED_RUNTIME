# MEMORY FRESHNESS CONTRACT V1

Every context packet must carry source identity, source hash/version, observed time and freshness classification: CURRENT, STALE, UNKNOWN or CONFLICT.

Agents may plan from STALE data only when explicitly marked. They may not claim PASS or execute integration from STALE/UNKNOWN context.

Coordinator refresh is mandatory before final acceptance, integration package creation, or conflict disposition.
