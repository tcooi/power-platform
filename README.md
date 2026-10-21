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

## Cross-tool authoring rules

- Layout per plugin: `.claude-plugin/plugin.json`, `agents/<name>.agent.md`, `skills/<name>/SKILL.md`.
- Agents: frontmatter only `name` + `description` (no `tools:`/`model:`, which differ between tools).
- Skills (`SKILL.md`) are portable. Avoid `commands/` (Claude Code only).
- Add a plugin: create the folder, then add an entry to `.claude-plugin/marketplace.json`. Bump `version` on every change or users won't get updates.
- Validate: `python3 scripts/validate.py`

## Sub-agents

Agents delegate to each other. Do not set `tools:` in agent frontmatter: omitted means all tools, which includes delegation in both Claude Code (`Agent`, up to 3 levels deep) and Copilot (`agent`). Specialists must be installed alongside `pp-delivery-lead`.

## Starting the delivery lead

- **Claude Code:** installing `pp-delivery-lead` makes it the default agent for every session (via the plugin's `settings.json`), so plain instructions go to the lead, which delegates to the specialists. Override with your own `agent` in `~/.claude/settings.json`, or disable the plugin when not doing Power Platform work.
- **Copilot CLI:** no default-agent setting exists. Start it with `copilot --agent=pp-delivery-lead`, or `/agent` in a session, or add `alias ppp='copilot --agent=pp-delivery-lead'` to your shell profile.
