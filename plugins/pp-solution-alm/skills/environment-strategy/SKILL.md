---
name: environment-strategy
description: "Define Power Platform environment types, naming and ownership for a project. Use when deciding DEV/TEST/PROD layout."
---

# Environment strategy

- Minimum: DEV (unmanaged, one per developer if parallel), BUILD/TEST (managed), UAT (managed), PROD (managed).
- Use Sandbox for DEV/TEST, Production for PROD; developer environments for individual makers.
- Name `<client>-<app>-<stage>`; record owner, region, Dataverse language/currency.
- Enable managed environments for UAT/PROD; configure DLP policies and solution checker enforcement.
- Never develop in PROD; no unmanaged customizations in downstream stages.

## Tooling
Create and inspect environments in the Power Platform admin center or with `pac admin create` / `pac admin list`; set managed environments, DLP and solution checker enforcement there. Switch the active target with `pac auth select` / `pac org select`. See `tool-selection-guide`.
