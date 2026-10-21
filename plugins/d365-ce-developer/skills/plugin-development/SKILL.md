---
name: plugin-development
description: Write, register and deploy C# plug-ins for Dataverse / D365 CE with pac plugin and plug-in packages. Use when server-side logic is required.
---

# Plug-in development

1. `pac plugin init` (or a class library targeting .NET Framework 4.6.2 for assemblies; use plug-in packages for dependencies).
2. Implement `IPlugin`: get `IPluginExecutionContext`, `IOrganizationServiceFactory`, `ITracingService`; never store state in fields.
3. Guard: check `context.Depth` (loop protection), message/entity name, `InputParameters["Target"]` type, and use `PreImage`/`PostImage` for changes.
4. Pick stage deliberately: PreValidation (reject early), PreOperation (modify target, in transaction), PostOperation (side effects). Async only for non-critical work.
5. Bulk-safe: avoid calls per record; support `CreateMultiple/UpdateMultiple`.
6. Register steps via the Plug-in Registration Tool or `pac plugin push`; add the assembly/package and steps to the solution.
7. Unit test with FakeXrmEasy or XrmMockup; test in a dev env with trace logs on.
Limits: 2 minute timeout, 1 second sandbox expectation, no UI.
