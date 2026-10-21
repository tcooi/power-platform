---
name: solution-checker-review
description: "Run and triage pac solution check / Solution Checker results. Use before each release."
---

# Solution Checker review

```
pac solution check --path out/<sol>_managed.zip --outputDirectory out/check
```
- Triage by severity: Critical/High must be fixed or have a written waiver; Medium reviewed; Low tracked.
- Group findings by rule, fix at the root (e.g. sync XHR, deprecated APIs, missing `RetrievePrimaryAttribute`).
- Record waivers in `docs/checker-waivers.md` with reason and owner.
- Add as a blocking step in the pipeline.
