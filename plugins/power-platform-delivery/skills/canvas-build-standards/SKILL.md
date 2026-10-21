---
name: canvas-build-standards
description: "Our standards for canvas apps, applied together with Microsoft's canvas-apps plugin (/canvas-app with live coauthoring). Use whenever a canvas app is built or changed."
---

# Canvas build standards

**Microsoft tool**: `canvas-apps` plugin: `/configure-canvas-mcp`, then `/canvas-app`. Needs .NET SDK 10+, the app created and saved in the solution, Studio open with coauthoring on. Details: `canvas-performance-delegation`, `canvas-component-library`.

## Our rules
- Agree screens, data sources and key Power Fx before building.
- Dataverse over SharePoint/Excel where possible; delegable formulas; named formulas; light `OnStart`.
- Component library and theme tokens; no hard-coded colors.
- `IfError` with friendly notifications; accessible labels and focus order.
- Connection references, not personal connections. No `pac canvas pack/unpack` (deprecated).


## Always
- Run in the main session (the Microsoft skills ask you questions and wait for approval).
- Load `.pp/project.json`; confirm environment (`pac org who`), solution and prefix before the first change.
- After building, confirm every new component is in the solution (`pac solution add-solution-component` if not), export and unpack (or commit via Git integration), and log the result in `.pp/state/delivery.json`.
