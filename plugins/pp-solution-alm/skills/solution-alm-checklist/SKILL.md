---
name: solution-alm-checklist
description: Checklist for creating, exporting, versioning and deploying Power Platform solutions with pac CLI. Use when setting up or reviewing solutions and pipelines.
---

# Solution ALM checklist

1. `pac auth list` / `pac org who` - verify environment.
2. Publisher exists with client prefix; solution created under it.
3. Add components via solution-aware tooling, not Default solution.
4. `pac solution export --path out.zip --managed false` then `pac solution unpack` into `src/`.
5. Replace env-specific values with environment variables; connectors with connection references.
6. `pac solution check` before import; import managed to downstream envs.
7. Bump solution version on every release.
