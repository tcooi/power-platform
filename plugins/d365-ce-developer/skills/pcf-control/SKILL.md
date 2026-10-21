---
name: pcf-control
description: Create and package Power Apps component framework (PCF) controls. Use for custom UI controls in model-driven or canvas apps.
---

# PCF control

1. `pac pcf init --namespace Contoso --name MyControl --template field --run-npm-install` (or `dataset`).
2. Implement `init`, `updateView`, `getOutputs`, `destroy`; declare properties in `ControlManifest.Input.xml`.
3. Prefer React + Fluent UI virtual controls (platform libraries) for small bundles.
4. `npm start watch` to test in the harness; `pac pcf push --publisher-prefix <prefix>` for quick dev deploy.
5. Production: add to a solution project (`pac solution init`, `pac solution add-reference`), `dotnet build`, ship the managed solution.
6. Test keyboard/accessibility, dark theme, read-only and disabled states.
