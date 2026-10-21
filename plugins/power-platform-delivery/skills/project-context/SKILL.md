---
name: project-context
description: "Per-project settings and delivery state on disk (.pp/project.json and .pp/state/delivery.json) so every agent uses the same environment, solution and publisher, and work resumes after a session reset. Use at the start of every Power Platform session and after every phase, decision or build step."
---

# Project context and state

## `.pp/project.json` (settings, created once per client project)
```json
{
  "client": "Contoso",
  "tenantId": "<guid>",
  "environments": {
    "dev":  { "url": "https://contoso-dev.crm4.dynamics.com", "type": "Developer" },
    "test": { "url": "https://contoso-test.crm4.dynamics.com", "type": "Sandbox", "managed": true },
    "prod": { "url": "https://contoso.crm4.dynamics.com", "type": "Production", "managed": true }
  },
  "solution": { "uniqueName": "ContosoCore", "publisher": "Contoso", "prefix": "con" },
  "sourceControl": "git-integration | pac-unpack",
  "deployment": "pipelines | github-actions | azure-devops",
  "docs": "docs/"
}
```
- If missing, the delivery lead creates it with the user (values confirmed, never guessed) before any build.
- No secrets in this file. Commit it.

## `.pp/state/delivery.json` (progress, updated as you go)
```json
{
  "phase": "design",
  "mode": "full",
  "approvals": [{ "item": "design v1", "by": "user", "date": "2026-10-21" }],
  "decisions": [{ "id": "D1", "decision": "Model-driven app over canvas", "reason": "…" }],
  "tasks": [{ "id": "T1", "title": "Create tables", "owner": "main/dv-metadata", "status": "done" }],
  "artifacts": ["docs/design/solution-design.md"],
  "openQuestions": [],
  "risks": [],
  "lessons": []
}
```

## Rules
1. Read both files first; if state exists, resume from it instead of starting over.
2. Update state after every phase change, approval, decision and build step, in the same step.
3. Never overwrite history: append to arrays.
4. Sub-agents receive the relevant parts in their brief (`spawn-templates`); they return results and the lead writes state.
