---
name: dataverse-schema-build
description: "Create Dataverse tables, columns and relationships in a solution via the Web API / pac. Use when implementing an approved data model."
---

# Dataverse schema build

1. `pac auth list`, `pac org who`; get an access token (`az account get-access-token --resource <orgUrl>`).
2. Confirm solution + publisher prefix exist.
3. Create each table with `POST /api/data/v9.2/EntityDefinitions` and header `MSCRM.SolutionUniqueName: <solution>`.
4. Add columns via `POST EntityDefinitions(LogicalName='<t>')/Attributes`.
5. Relationships via `POST RelationshipDefinitions` (OneToMany / ManyToMany).
6. `POST PublishAllXml` (or publish the solution) and verify with a GET.
7. Wait for propagation (30-60s) before creating dependents; retry on 'not found' metadata errors.

Prefer defining the schema as JSON files under `src/schema/` so it is repeatable across environments, but ship via the solution, not by re-running scripts, for TEST/PROD.
