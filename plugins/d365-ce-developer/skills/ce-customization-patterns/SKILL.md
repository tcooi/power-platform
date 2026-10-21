---
name: ce-customization-patterns
description: Patterns for customizing Dynamics 365 CE forms, command bar, web resources and plug-ins. Use when deciding between config and code, or writing form scripts.
---

# CE customization patterns

| Need | Prefer |
|---|---|
| Show/hide, require, set value | Business rule |
| Computed value | Calculated / rollup column |
| Command bar button | Power Fx command bar (modern), else Ribbon Workbench |
| Cross-record validation | Synchronous plug-in (PreValidation/PreOperation) |
| Heavy/async work | Async plug-in or cloud flow |
| Custom UI control | PCF |

Form script skeleton:
```js
var Contoso = Contoso || {};
Contoso.Account = {
  onLoad: function (executionContext) {
    var formContext = executionContext.getFormContext();
  }
};
```
