---
name: plan-alm
description: "Plan environment strategy and promotion path (DEV, TEST, UAT, PROD) with solutions and pipelines before deploying anything. Use at project start."
---

# Plan ALM (planner only: never deploys)

1. Detect: existing solutions, publisher, environments, pipelines (`pac solution list`, `pac admin list`).
2. Ask: number of environments, managed/unmanaged, approvers, release cadence, source control (GitHub/Azure DevOps).
3. Write `docs/alm-plan.md`: environment table, solution layering (e.g. `core` -> `app` -> `integrations`), variables per environment, pipeline stages, rollback.
4. Get approval, then execute with `environment-strategy`, `source-control-unpack`, and a pipeline skill in that order.
