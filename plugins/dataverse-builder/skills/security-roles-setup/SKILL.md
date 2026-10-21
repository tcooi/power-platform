---
name: security-roles-setup
description: "Create and assign Dataverse security roles, teams and field security profiles from the approved security model. Use after tables exist."
---

# Security roles setup

1. Copy the closest OOTB role (`Basic User` pattern) rather than creating from scratch; roles must be in the solution.
2. Set table privileges per the approved matrix (depth: User/BU/Parent-child/Org).
3. Add the privileges for the model-driven app, custom pages and any service tables (e.g. `Process`, `Connection`).
4. Create owner/access teams; for production use group teams linked to Entra security groups.
5. Create the application user for integrations/flows and assign a minimal role.
6. Test with each persona: sign in as the test user and verify visibility and CRUD.
Export roles in the solution; do not hand-edit in PROD.

## Tooling
Author roles in the admin/maker UI (Power Platform admin center or the solution's Security roles), add them to the solution, then `pac solution export` + unpack to commit. Use the Web API only to read and verify (`roleprivilegescollection`, `systemuserroles`) and to assign roles/teams in bulk. Dataverse MCP can read role assignments but should not change them. See `tool-selection-guide`.
