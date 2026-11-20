# Azure Data Factory

**Status:** connected to GitHub and imported from `adf-retailsales-analytics-df` on November 20, 2026. Root: `/adf`; collaboration branch: `main`; publish branch: `adf_publish`.

## Included resources

| Asset | Purpose |
| --- | --- |
| `pipeline/PL_CopyData.json` | Copy sales CSV from `raw` to `processed` |
| `dataset/DS_Blob.json` | Delimited-text dataset with container/directory/filename parameters |
| `linkedService/LS_Blob.json` | Azure Blob Storage connection definition |
| `factory/` | Factory settings imported by ADF |
| `publish_config.json` | Publish branch configuration |
| `arm/` | Separate ARM export, including factory creation and linked-template variants |

The pipeline reads `csalesdata/raw/sales.csv` and writes `csalesdata/processed/sales_processed.csv`. It does not invoke either Databricks notebook. Notebook inputs use different locations, so the current stages require explicit coordination; end-to-end orchestration is not implemented or tested here.

ADF generated a factory-bound `encryptedCredential` in the source linked service. It is not a plaintext key and cannot be treated as a portable credential. Reconfigure authentication when deploying elsewhere. The ARM version instead uses a secure-string connection parameter with an empty example value. Supply credentials securely at deployment time, never in a committed parameter file.

Export preserves the original Copy settings, including sink `fileExtension: .txt` and `allowDataTruncation: true`; the configured filename is `sales_processed.csv`. Review these settings for your intended output contract. They were not changed or run during export.

## Connection settings for another environment

1. Open ADF Studio → **Manage → Git configuration → Configure**.
2. Choose GitHub and `avneetxsingh/azure-databricks-retail-analytics`.
3. Set collaboration branch `main`, publish branch `adf_publish`, root folder `/adf`.
4. Select **Import existing resources to repository** and import into `main`.
5. Review exported pipelines, datasets, linked services, triggers, and other resources.

If already connected elsewhere, inspect the existing configuration before replacing it. Preserve this guide during import.

Committing Git changes and publishing to the live factory are separate actions. Do not publish unrelated pending edits just to populate Git. ADF Git integration does not upload repository data files into Azure Storage.

Prefer appropriate identity-based authentication or Key Vault references. Inspect custom parameters, notebook activities, and URLs for hardcoded credentials before committing.

[Microsoft: ADF source control](https://learn.microsoft.com/en-us/azure/data-factory/source-control)
