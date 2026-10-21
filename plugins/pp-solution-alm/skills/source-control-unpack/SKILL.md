---
name: source-control-unpack
description: Export, unpack and commit solutions to git with a clean folder structure. Use for source-controlled solution development.
---

# Source control for solutions

```
pac solution export --name <sol> --path out/<sol>.zip --managed false
pac solution unpack --zipfile out/<sol>.zip --folder src/<sol> --packagetype Both --processCanvasApps
```
- Commit `src/<sol>`; ignore `out/`.
- Run `pac solution sync` or re-export + unpack to update; review diffs of XML before merging.
- Branch per feature; avoid two developers editing the same component (XML merge conflicts).
- Rebuild: `pac solution pack --zipfile out/<sol>_managed.zip --folder src/<sol> --packagetype Managed`.
