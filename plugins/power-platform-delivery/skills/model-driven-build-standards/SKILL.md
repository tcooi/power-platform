---
name: model-driven-build-standards
description: "Our standards for model-driven apps and changes to out-of-the-box apps, applied together with Microsoft's model-apps plugin (/app-builder, /genpage) and pac model. Use whenever app modules, forms, views, sitemap, command bar, business rules or BPFs are built."
---

# Model-driven build standards

**Microsoft tool**: `model-apps` plugin (`/app-builder`, `/genpage`); `pac model create --name … --solution <solution> --publish` (always pass `--solution`). Details: `app-modules-forms-views`, `command-bar-power-fx`, `business-rules-and-bpf`.

## Our rules
- Role-based apps with a small, task-grouped sitemap; assign the app to security roles.
- OOTB apps (Sales Hub, Customer Service Hub…): your own app module, forms and views in your solution; never edit managed originals.
- Business rules and Power Fx command bar before JavaScript; code goes to the `pro-code-developer` sub-agent.
- Forms: key status in header, tabs by phase, few controls on load. Views: the columns users need, quick-find columns, lookup views.
- Generative pages only where a form/view/dashboard can't do the job; record why.


## Always
- Run in the main session (the Microsoft skills ask you questions and wait for approval).
- Load `.pp/project.json`; confirm environment (`pac org who`), solution and prefix before the first change.
- After building, confirm every new component is in the solution (`pac solution add-solution-component` if not), export and unpack (or commit via Git integration), and log the result in `.pp/state/delivery.json`.
