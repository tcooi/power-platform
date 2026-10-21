---
name: security-roles-setup
description: "Create Dataverse security roles in the maker/admin UI and assign them to users, groups and application users with Microsoft's dv-security skill or pac admin commands. Use after tables exist."
---

# Security roles setup

## Author roles (UI)
- Copy the closest OOTB role (e.g. Basic User) and trim; set table privileges and depth (User/BU/Parent-child BU/Org) per the approved matrix.
- Include privileges for the model-driven app and any custom pages/flows the persona uses; assign the app to the roles.
- Add roles to the working solution, then export/unpack. Never edit roles directly in UAT/PROD.

## Assign roles (CLI, verified)
- Users: `dv-security` skill, or `pac admin assign-user --environment <id|url> --user <upn|objectId> --role "<role>" [--business-unit <id>]`.
- Application users: `pac admin assign-user … --application-user`; create the app registration + app user with `pac admin create-service-principal --environment <id> --role "<role>"` (default role is **System Administrator** — always pass a least-privilege role).
- Entra groups as Dataverse teams: `pac admin assign-group --group <objectId> --group-name <name> --team-type AadSecurityGroup --membership-type Members --role "<role>"`.
- List roles: `pac admin list-roles --environment <id>`.
- Role changes need a preview and confirmation naming user, role and environment.

## Verify
Sign in as a test user per persona and check visibility and CRUD; record results in the test plan.

Sources: learn.microsoft.com/power-platform/developer/cli/reference/admin, …/agents-plugin/reference#dv-security
