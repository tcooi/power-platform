---
name: azure-devops-pipeline
description: "Create Azure DevOps YAML pipelines using Power Platform Build Tools. Use for Azure DevOps-based CI/CD."
---

# Azure DevOps pipelines

Use Power Platform Build Tools tasks: `PowerPlatformToolInstaller`, `PowerPlatformExportSolution`, `PowerPlatformUnpackSolution`, `PowerPlatformPackSolution`, `PowerPlatformChecker`, `PowerPlatformImportSolution`, `PowerPlatformPublishCustomizations`.
- Service connection with an Entra app registration (workload identity federation where available).
- Stages: Build (pack + checker) -> Deploy TEST -> Deploy UAT (environment approval) -> Deploy PROD.
- Pass environment variables / connection references via a deployment settings JSON per stage; keep secrets in variable groups / Key Vault.
