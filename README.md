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

| Plugin | Purpose |
|---|---|
| personal-power-platform | Builds into solution `model` / publisher `TC` |
| pp-solution-alm | Solutions, publishers, env vars, pac, pipelines |
| d365-ce-developer | D365 CE customization, plug-ins, web resources, OOTB app changes |
| canvas-app-builder | Canvas apps and Power Fx |
| power-automate-builder | Cloud flows |
| copilot-studio-builder | Copilot Studio agents |

## Cross-tool authoring rules

- Layout per plugin: `.claude-plugin/plugin.json`, `agents/<name>.agent.md`, `skills/<name>/SKILL.md`.
- Agents: frontmatter only `name` + `description` (no `tools:`/`model:`, which differ between tools).
- Skills (`SKILL.md`) are portable. Avoid `commands/` (Claude Code only).
- Add a plugin: create the folder, then add an entry to `.claude-plugin/marketplace.json`. Bump `version` on every change or users won't get updates.
- Validate: `python3 scripts/validate.py`
