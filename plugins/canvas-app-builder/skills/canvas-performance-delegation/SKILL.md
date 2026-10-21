---
name: canvas-performance-delegation
description: "Review canvas app formulas for delegation warnings and performance. Use when a canvas app is slow or returns incomplete data."
---

# Canvas performance and delegation

- Fix every blue delegation warning: use delegable functions/operators for the data source; move filtering server-side (`Filter` on indexed columns).
- Reduce `OnStart`; use named formulas (`App.Formulas`) and lazy-load per screen.
- Use `Concurrent()`, cache lookups into collections only when small and rarely changing.
- Minimise controls per screen (< ~300), avoid nested galleries, set images to proper sizes.
- Use the Monitor tool and Solution Checker/App Checker for hotspots.
- Raise the data row limit only with a clear reason.

## Tooling
Use Microsoft's `canvas-apps` plugin for live authoring, compile and app-checker errors when installed; otherwise `pac canvas unpack` / `pac canvas pack` to edit source files, and the Monitor tool in Studio for profiling. See `tool-selection-guide`.
