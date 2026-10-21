---
name: github-actions-pipeline
description: "Create GitHub Actions workflows for Power Platform export, check, build and deploy using microsoft/powerplatform-actions. Use for GitHub-based CI/CD."
---

# GitHub Actions for Power Platform

Use `microsoft/powerplatform-actions` (pin to a version/SHA): `actions-install`, `who-am-i`, `export-solution`, `unpack-solution`, `pack-solution`, `check-solution`, `import-solution`, `publish-solution`, `branch-solution`.

Pipeline: PR -> pack + `check-solution` (Solution Checker) -> merge -> pack managed -> import to TEST -> approval environment -> UAT/PROD.
- Auth with an Entra app registration (federated credentials preferred; secrets in GitHub environment secrets, never in repo).
- Use GitHub *environments* with required reviewers for UAT/PROD.
- Apply environment variables and connection references via deployment settings files (`pac solution create-settings`).
