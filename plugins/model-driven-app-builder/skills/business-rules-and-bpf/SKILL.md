---
name: business-rules-and-bpf
description: Create business rules and business process flows for model-driven apps. Use for form logic and guided stage-based processes.
---

# Business rules and BPFs

**Business rules**: scope = Entity (runs everywhere incl. server) vs Form. Use for show/hide, required, default values, simple validation. Avoid long chains; document the order.

**Business process flows**: stages and steps map to required columns; keep to 3-6 stages; use branching conditions sparingly; one active BPF per record view by default.
- BPFs are tables: ship them in the solution, assign security roles.
- Prefer a flow or plug-in for logic that must run regardless of UI.
