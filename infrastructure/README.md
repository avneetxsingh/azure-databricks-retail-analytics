# Azure infrastructure

**Status:** resource-group ARM export captured and reviewed on November 20, 2026. No deployment has been run.

## Included files

- [resource-group.json](resource-group.json): sanitized Azure export, with location parameterized.
- [parameters.example.json](parameters.example.json): nonsecret example values. Change globally unique resource names before deploying elsewhere.
- [ADF ARM export](../adf/arm/ARMTemplateForFactory.json): separate export for factory artifacts; factory creation is under `adf/arm/factory/`.

The resource-group snapshot contains eight definitions: a Databricks access connector, a serverless premium workspace, a StorageV2 account, its Blob/File/Queue/Table services, and the `csalesdata` container. Storage hierarchical namespace is enabled. Other storage properties are preserved from the export, including the Cold access tier; review costs and feature compatibility before reuse.

Azure reported `ExportTemplateCompletedWithErrors`. The resource-group export omitted ADF; its separate export is included under `adf/arm/`. This does not establish that all role assignments, Unity Catalog objects, or other non-resource state were captured.

The public template removes the workspace's environment-specific `authorizations` block and empty `createdBy`/`updatedBy` fields. It does not recreate the original authorization grants. Originals were retained locally outside the repository. No live Azure access settings were changed during sanitization.

Deployment readiness is unverified: exported API versions and properties are retained, and more changes may be required for your subscription and region. The files are configuration snapshots, not a tested production deployment.

## Export

1. Open the retail project's resource group in Azure Portal.
2. Select **Export template** and download the supported ARM export.
3. Inspect warnings for omitted resources or properties.
4. Remove credentials and replace environment-specific values with parameters.
5. Add the reviewed template and a safe `parameters.example.json` here.

An export is a starting point rather than proof of a deployable environment. ADF requires a separate export/Git integration. Storage data, notebook files, dashboards, Unity Catalog objects/grants, and secrets are separate.

Do not export Databricks-managed internal resources as a substitute for a workspace definition. Document storage containers, identities, role assignments, volume setup, and external locations that need separate provisioning.

Test in an isolated environment before describing a template as deployable. No infrastructure deployment has been tested for this repository version.

[Microsoft: resource-group export](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal)
