# Azure infrastructure

**Status:** reviewed resource-group templates have not been added.

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
