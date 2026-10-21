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

These plugins carry the consulting method (phases, approvals, standards). **Building is done with Microsoft's official tooling**, chosen per task by the `tool-selection-guide` skill.

| Plugin | Purpose |
|---|---|
| pp-delivery-lead | Orchestrator that breaks a Power Platform / Dynamics 365 CE request into parts and delegates them to specialist agents. |
| pp-solution-alm | Solution, publisher, environment variable and pipeline discipline for Power Platform delivery. |
| pro-code-developer | Pro-code development for Power Platform and D365 CE: C# plug-ins, JavaScript web resources, PCF controls, custom APIs and integrations. |
| canvas-app-builder | Canvas app design and build for Power Platform consultants. |
| power-automate-builder | Power Automate cloud flow design, build and troubleshooting. |
| copilot-studio-builder | Copilot Studio agent design and delivery. |
| pp-discovery-design | Discovery and solution design for Power Platform / D365 CE engagements: requirements, fit-gap, data and security model, design documents. |
| dataverse-builder | Builds Dataverse schema, security roles and sample data from an approved design. |
| model-driven-app-builder | Builds model-driven apps: app modules, sitemap, forms, views, command bar, business rules and process flows. |
| pp-quality-governance | Review, test, governance and handover for Power Platform / D365 CE solutions. |

## Prerequisites and connecting

### 1. Microsoft plugins (recommended; they do the actual building)
Claude Code:
```
/plugin marketplace add microsoft/power-platform-skills
/plugin install model-apps@power-platform-skills
/plugin install canvas-apps@power-platform-skills
/plugin install power-automate@power-platform-skills
/plugin install pcf@power-platform-skills
/plugin install dataverse@claude-plugins-official
```
Copilot CLI: same marketplace and plugins, but install Dataverse with `/plugin install dataverse@awesome-copilot`. Then ask: "Connect to my Dataverse environment" (the `dv-connect` skill sets up auth and the Dataverse MCP server).

### 2. Local tools
| Need | Used for | Setup |
|---|---|---|
| Power Platform CLI (`pac`) | solutions, environments, roles, plug-ins, PCF, model apps, Copilot Studio, pipelines | `dotnet tool install --global Microsoft.PowerApps.CLI.Tool`, then `pac auth create --environment <url>`; check `pac org who` |
| .NET SDK 10+ | canvas-apps plugin, `pac copilot mcp`, plug-in builds | `dotnet --list-sdks` |
| Node.js 18+ | Dataverse CLI / MCP proxy, power-automate plugin, PCF | |
| Azure CLI | power-automate plugin, Web API tokens | `az login --allow-no-subscriptions` |
| Dataverse CLI (preview) | headless data ops, local MCP proxy | `npm install -g @microsoft/dataverse` (installed by `dv-connect`) |
| Git + GitHub/Azure DevOps | source control, CI/CD | |

### 3. Admin setup (once per environment)
- **Dataverse MCP**: admin turns on "Allow MCP clients to interact with Dataverse MCP server" and enables the client (GitHub Copilot, Claude, or "Dataverse MCP CLI tool") in Power Platform admin center; tenant admin consent for the CLI proxy. Billed in Copilot Credits outside Copilot Studio.
- **Managed environments** for pipeline targets and Dataverse Git integration.
- **Canvas apps**: coauthoring on in Power Apps Studio for apps edited by the plugin.

Microsoft Learn MCP is bundled with `pp-delivery-lead`. Targeting: agents work on the environment `pac` is authenticated to; `pp-delivery-lead` runs a preflight and asks you to confirm it.

## Cross-tool authoring rules

- Layout per plugin: `.claude-plugin/plugin.json`, `agents/<name>.agent.md`, `skills/<name>/SKILL.md`.
- Agents: frontmatter only `name` + `description` (no `tools:`/`model:`, which differ between tools).
- Skills (`SKILL.md`) are portable. Avoid `commands/` (Claude Code only).
- Add a plugin: create the folder, then add an entry to `.claude-plugin/marketplace.json`. Bump `version` on every change or users won't get updates.
- Validate: `python3 scripts/validate.py`

## Sub-agents

Agents delegate to each other. Do not set `tools:` in agent frontmatter: omitted means all tools, which includes delegation in both Claude Code (`Agent`, up to 3 levels deep) and Copilot (`agent`). Specialists must be installed alongside `pp-delivery-lead`.
