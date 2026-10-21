---
name: security-governance-review
description: "Review governance: DLP policies, connection and flow ownership, environment settings, roles and licensing. Use before go-live."
---

# Security and governance review

- DLP: connectors used vs the environment's policy groups (Business/Non-Business/Blocked); no HTTP to unknown hosts.
- Flows/agents/connections owned by service accounts or app users, with a co-owner; no personal connections in PROD.
- Secrets in environment variables (secret type) or Key Vault, not in flow definitions.
- Roles: no System Administrator for end users; audit enabled on sensitive tables.
- Sharing: apps shared to security groups, not individuals.
- Licensing: premium connectors, Dataverse capacity, Copilot Studio capacity for the actual user count.
