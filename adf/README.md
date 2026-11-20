# Azure Data Factory

**Status:** factory definitions have not been imported. This folder is the intended Git root for the existing retail factory.

## Connect

1. Open ADF Studio → **Manage → Git configuration → Configure**.
2. Choose GitHub and `avneetxsingh/azure-databricks-retail-analytics`.
3. Set collaboration branch `main`, publish branch `adf_publish`, root folder `/adf`.
4. Select **Import existing resources to repository** and import into `main`.
5. Review exported pipelines, datasets, linked services, triggers, and other resources.

If already connected elsewhere, inspect the existing configuration before replacing it. Preserve this guide during import.

Committing Git changes and publishing to the live factory are separate actions. Do not publish unrelated pending edits just to populate Git. ADF Git integration does not upload repository data files into Azure Storage.

Prefer appropriate identity-based authentication or Key Vault references. Inspect custom parameters, notebook activities, and URLs for hardcoded credentials before committing.

[Microsoft: ADF source control](https://learn.microsoft.com/en-us/azure/data-factory/source-control)
