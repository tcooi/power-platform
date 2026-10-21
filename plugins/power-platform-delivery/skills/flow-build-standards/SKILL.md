---
name: flow-build-standards
description: "Our standards for Power Automate cloud flows, applied together with Microsoft's power-automate plugin (/build-flow, /debug-flow). Use whenever a cloud flow is built, changed or debugged."
---

# Flow build standards

**Microsoft tool**: `power-automate` plugin (`/setup`, `/build-flow`, `/create-flow`, `/debug-flow`, `/diagnose-flow`, `/manage-flows`); needs `az login --allow-no-subscriptions`. New flows are created stopped for review. Details: `flow-error-handling-pattern`, `flow-dataverse-triggers`.

## Our rules
- Flows live in the solution with connection references and environment variables; verify membership after the plugin creates a flow.
- Dataverse triggers filter rows and select columns; guard against update loops.
- Try/Catch/Finally scopes; failures logged and alerted.
- Child flows for reuse; deliberate concurrency and pagination.
- Production flows owned by a service account or application user with a co-owner.
- Turn flows on only after review.


## Always
- Run in the main session (the Microsoft skills ask you questions and wait for approval).
- Load `.pp/project.json`; confirm environment (`pac org who`), solution and prefix before the first change.
- After building, confirm every new component is in the solution (`pac solution add-solution-component` if not), export and unpack (or commit via Git integration), and log the result in `.pp/state/delivery.json`.
