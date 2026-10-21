---
name: custom-api-and-actions
description: "Design Dataverse custom APIs and custom actions with plug-ins as the implementation. Use for reusable server-side operations called from flows, apps or integrations."
---

# Custom API

- Create a Custom API record (unique name with prefix, binding type, allowed step type, request parameters, response properties) inside the solution.
- Implement logic in a plug-in registered on the Custom API message, PostOperation/synchronous.
- Prefer Custom API over legacy custom process actions for new work.
- Call from Power Fx (`Environment`/ connector), flows (Perform an unbound action), Web API (`POST /<name>`).
- Secure with a privilege so only specific roles can execute.
