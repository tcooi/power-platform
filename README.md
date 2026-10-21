# ppp - Power Platform marketplace

One marketplace for **Claude Code** and **GitHub Copilot CLI** (also VS Code agent plugins). Both read `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json`.

## Install

Claude Code:
```
/plugin marketplace add tcooi/power-platform
/plugin install pp-solution-alm@ppp
```
Copilot CLI:
```
copilot plugin marketplace add tcooi/power-platform
copilot plugin install pp-solution-alm@ppp
```

## Plugins

Lifecycle: discover -> design -> ALM plan -> build -> review/test -> go-live -> handover. Start with `pp-delivery-lead`; it delegates to the others.

| Plugin | Purpose |
|---|---|
| pp-delivery-lead | Orchestrator that breaks a Power Platform / Dynamics 365 CE request into parts and delegates them to specialist agents. |
| pp-solution-alm | Solution, publisher, environment variable and pipeline discipline for Power Platform delivery. |
| pro-code-developer | Dynamics 365 Customer Engagement customization and development. |
| canvas-app-builder | Canvas app design and build for Power Platform consultants. |
| power-automate-builder | Power Automate cloud flow design, build and troubleshooting. |
| copilot-studio-builder | Copilot Studio agent design and delivery. |
| pp-discovery-design | Discovery and solution design for Power Platform / D365 CE engagements: requirements, fit-gap, data and security model, design documents. |
| dataverse-builder | Builds Dataverse schema, security roles and sample data from an approved design. |
| model-driven-app-builder | Builds model-driven apps: app modules, sitemap, forms, views, command bar, business rules and process flows. |
| pp-quality-governance | Review, test, governance and handover for Power Platform / D365 CE solutions. |

## Prerequisites and connecting

The skills are instructions only. They contain no connectors, scripts or credentials; agents act through tools in your session, so set these up first.

| Need | Used for | Setup |
|---|---|---|
| Power Platform CLI (`pac`) | solutions, PCF, plug-ins, checker, auth | install (`dotnet tool install --global Microsoft.PowerApps.CLI.Tool` or the VS Code extension), then `pac auth create --environment <url>`; check with `pac org who` |
| Azure CLI (`az`) | tokens for the Dataverse Web API | install, `az login --tenant <tenant>`; token via `az account get-access-token --resource <orgUrl>` |
| Node.js, .NET SDK | PCF builds, plug-in builds | install LTS versions |
| Git (+ GitHub or Azure DevOps access) | source control, pipelines | pipelines also need an Entra app registration and secrets stored in the CI system |
| Microsoft Learn MCP | doc lookups | bundled with `pp-delivery-lead` (`.mcp.json`), no setup |
| Flow and canvas tooling (optional) | create/debug flows, edit canvas apps | install Microsoft's `power-automate` and `canvas-apps` plugins from `microsoft/power-platform-skills` |

Targeting: every agent works on the environment `pac` is currently authenticated to. `pp-delivery-lead` runs a preflight (`pac org who`, `az account show`), shows you the environment and asks you to confirm before building. Use `pac auth select` / `pac org select` to switch.

## Cross-tool authoring rules

- Layout per plugin: `.claude-plugin/plugin.json`, `agents/<name>.agent.md`, `skills/<name>/SKILL.md`.
- Agents: frontmatter only `name` + `description` (no `tools:`/`model:`, which differ between tools).
- Skills (`SKILL.md`) are portable. Avoid `commands/` (Claude Code only).
- Add a plugin: create the folder, then add an entry to `.claude-plugin/marketplace.json`. Bump `version` on every change or users won't get updates.
- Validate: `python3 scripts/validate.py`

## Sub-agents

Agents delegate to each other. Do not set `tools:` in agent frontmatter: omitted means all tools, which includes delegation in both Claude Code (`Agent`, up to 3 levels deep) and Copilot (`agent`). Specialists must be installed alongside `pp-delivery-lead`.
