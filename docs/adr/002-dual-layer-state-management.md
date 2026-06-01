# ADR 002: Dual-Layer State Management (PostgreSQL + Redis)

## Status
Accepted

## Context
Enterprise agentic workflows require two distinct types of persistence:
1. **Short-term ephemeral state:** High-frequency checkpointing of LangGraph runs to support "resume-from-failure" and low-latency token streaming.
2. **Long-term historical state:** Permanent audit logs, cost-tracking, and evaluation results for compliance and analytics.

## Decision
We will implement a dual-layer state management strategy:
- **Redis (Memorystore):** Acts as the primary LangGraph Checkpointer (`RedisSaver`) for fast state serialization and workflow recovery.
- **PostgreSQL (Cloud SQL):** Acts as the system of record for domain entities (Tenants, Users) and a cold-storage destination for completed workflow traces.

## Rationale
- **Performance:** Redis minimizes the latency impact of frequent state saves during multi-step agent loops.
- **Scalability:** PostgreSQL allows for complex analytical queries (e.g., "What was the average cost-per-session for Tenant X last month?") that are inefficient in Redis.
- **Resiliency:** This "Hot/Cold" architecture ensures that even if a transient Redis failure occurs, the permanent audit log remains intact.

## Consequences
- Requires synchronization logic (background workers) to move completed traces from Redis to Postgres.
- Increased infrastructure complexity (managing two stateful services).
