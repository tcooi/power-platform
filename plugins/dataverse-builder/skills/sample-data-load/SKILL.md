---
name: sample-data-load
description: "Load sample or migration data into Dataverse with batch Web API calls. Use for test data or initial loads."
---

# Sample data load

- Use `$batch` (up to 1000 requests, changesets for atomic groups) or the `CreateMultiple` / `UpdateMultiple` actions for volume.
- Order: reference data, parents, children; resolve lookups with `@odata.bind` and alternate keys (`Upsert`) so loads are repeatable.
- Mark seeded rows (a `source` column or prefix) so they can be cleaned up.
- Turn off flows/plug-ins that should not fire on bulk loads (bypass flag or temporarily disable) and re-enable after.
- Never load real personal data into non-production environments.

## Choosing the tool
Volume goes through the Web API (`$batch`, `CreateMultiple`, `Upsert`). Use Dataverse MCP (if connected) only for a handful of rows or for verification queries. See `tool-selection-guide`.
