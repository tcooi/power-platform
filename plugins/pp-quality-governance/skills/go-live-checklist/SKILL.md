---
name: go-live-checklist
description: Production deployment and go-live checklist for Power Platform solutions. Use before releasing to PROD.
---

# Go-live checklist

- [ ] Managed solution version bumped, checker passed, UAT signed off
- [ ] Environment variables and connection references set for PROD (deployment settings)
- [ ] Security roles, teams, app sharing assigned; licenses assigned
- [ ] Flows turned on under the service account; agents published; scheduled jobs active
- [ ] Data migration done and reconciled; backups taken (`pac admin backup` / manual backup)
- [ ] Monitoring: flow failure alerts, Application Insights / Managed Environments insights
- [ ] Rollback plan tested; support contacts and hypercare agreed
