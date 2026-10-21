---
name: canvas-component-library
description: "Create and reuse canvas component libraries and a consistent theme. Use for multi-app consistency."
---

# Component library

- Create a component library app in the solution; export components with custom properties (input/output/events).
- Use design tokens as a theme record in named formulas; no hardcoded colors in screens.
- Version library components; consuming apps must update on change, so batch breaking changes.
- Keep components responsive (`Parent.Width`) and accessible (labels, focus order, contrast).

## Tooling
Create libraries in Power Apps Studio inside the solution; edit with Microsoft's `canvas-apps` plugin when installed, or `pac canvas unpack/pack`. Ship the library and consuming apps in the same solution. See `tool-selection-guide`.
