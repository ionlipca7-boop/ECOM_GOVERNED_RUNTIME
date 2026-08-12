# REQUEST ROUTER RULES V1

Every request receives: request_id, source_agent, target_owner, type, priority, dependency, safety class, disposition and ACK state.

Disposition classes: SELF_PLAN_READONLY, ROUTE_TO_OWNER, ESCALATE_COORDINATOR, WAIT_OPERATOR, BLOCKED_SAFETY, DUPLICATE, DEBT.

Zero unanswered requests is the target.
