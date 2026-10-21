---
name: solution-alm-checklist
description: "Checklist for creating, exporting, versioning and deploying Power Platform solutions with pac CLI. Use when setting up or reviewing solutions and pipelines."
---

# Solution ALM checklist

1. `pac auth list`, `pac org who` — verify environment.
2. Publisher with client prefix exists; solution created under it (`dv-solution` can discover/create both).
3. Build components via solution-aware tools; if one lands outside, `pac solution add-solution-component`.
4. Source control: Git integration, or `pac solution export --name <sol> --path out/<sol>.zip` then `pac solution unpack --zipfile out/<sol>.zip --folder src/<sol> --packagetype Both`.
5. Environment variables and connection references for anything environment-specific; generate a settings file with `pac solution create-settings --solution-zip out/<sol>.zip --settings-file deploy/<stage>.json`.
6. `pac solution check --path out/<sol>.zip --outputDirectory out/check --geo <geo>` before import.
7. Version: `pac solution version` (build/revision) or `pac solution online-version --solution-name <sol> --solution-version x.y.z.w`.
8. Import managed downstream (pipelines or CI); never unmanaged into TEST/PROD.
