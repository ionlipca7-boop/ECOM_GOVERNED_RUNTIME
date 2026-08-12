# LEASE AND COLLISION CONTRACT V1

One active writer per owned target. A task lease binds agent_id, owner_scope, target paths, start time and expiry. Competing write requests are blocked or routed, never merged silently. READONLY agents do not need write leases. Stale leases require Coordinator disposition before reuse.
