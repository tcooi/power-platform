---
name: app-modules-forms-views
description: Create app modules, sitemap, forms and views for a model-driven app. Use when building or restructuring the UI of a model-driven app.
---

# App module, forms and views

1. App module in the solution; add only the tables the persona needs; assign security roles to the app.
2. Sitemap: group by task (Work, Customers, Setup), use dashboards for landing pages.
3. Main form per persona/context: header with key status fields, tabs by phase, related grids as sub-grids, timeline control where activities matter.
4. Views: public views for lists, with quick find fields; add a lookup view per table used in lookups.
5. Customize OOTB forms by creating a copy in your solution (or using form fallback ordering) to avoid upgrade conflicts.
6. Publish, test as each persona, check form load time (fewer controls, deferred tabs).
