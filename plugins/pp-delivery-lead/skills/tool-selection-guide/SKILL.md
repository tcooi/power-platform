---
name: tool-selection-guide
description: "Choose the right tool for a Power Platform task: pac CLI, Dataverse Web API, Dataverse MCP, maker designers, Microsoft plugins or CI actions. Use before running any command that changes or reads an environment."
---

# Tool selection guide

Pick the tool by task, not habit. Always confirm the environment first (`pac org who`).

| Task | Use | Avoid |
|---|---|---|
| Export, import, pack, unpack, version, check solutions | `pac solution ...` | Hand-zipping solutions |
| Source-controlled solution files | `pac solution unpack/pack` + git | Editing managed XML by hand |
| Tables, columns, relationships, choices (repeatable) | Dataverse **Web API** with `MSCRM.SolutionUniqueName` header, schema kept as JSON in the repo | Creating in the Default solution |
| Bulk load / migration | Web API `$batch`, `CreateMultiple`, `Upsert` with alternate keys | MCP or one-by-one calls |
| Ad hoc reads, quick lookups, small record edits | **Dataverse MCP** if connected (e.g. `read_query`, `create_record`) | Using it for schema or solution-aware changes; destructive calls without user approval |
| Security roles, privileges | Maker/admin UI to author, then ship in the solution; Web API to read and verify privileges | Editing roles in PROD |
| Forms, views, sitemap, app modules, business rules, BPFs, charts | App designer / maker portal, then `pac solution export` + unpack to commit | Hand-writing FormXml/SiteMap XML unless fixing a diff |
| Command bar | Modern command designer (Power Fx) | Ribbon XML |
| PCF controls, plug-in projects | `pac pcf`, `pac plugin`, `dotnet`, `npm` | Copying unmanaged DLLs between envs |
| Cloud flows | Microsoft `power-automate` plugin tools (validate, connections, run history). Fallback: Web API `workflow` table with `clientdata` JSON | Writing flow JSON blind without validating |
| Canvas apps | Microsoft `canvas-apps` plugin (live authoring and compile). Fallback: `pac canvas unpack/pack` | Editing `.msapp` binaries |
| Copilot Studio agents | Copilot Studio CLI/plugin or the Copilot Studio UI, ship in a solution | Editing published agents in PROD |
| Docs and syntax checks | Microsoft Learn MCP (bundled) | Answering from memory |
| CI/CD | `powerplatform-actions` (GitHub) or Power Platform Build Tools (Azure DevOps) | Manual imports to UAT/PROD |
| Tests | Test Engine (`pac test run`), EasyRepro/Playwright, unit tests | Only manual clicking |

## Rules
1. Everything that creates or changes a component goes into the working solution, whatever the tool.
2. Prefer the least powerful tool that does the job; read-only first.
3. Anything destructive (delete rows, tables, columns, solutions) needs explicit user approval, in any tool.
4. If the preferred tool is not available (not installed or not signed in), say so, name the fallback in the table, and ask before using it.
5. Repeatable beats clicked: when something was done in a designer, export and unpack so it lands in source control.
