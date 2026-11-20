# Setup and execution

## Prerequisites

- An Azure subscription and Databricks workspace you can use.
- Compute capable of running the Spark/Python notebooks.
- Authorized source data matching the [data dictionary](data-dictionary.md).
- Storage permissions for your selected method.
- `requests` and `pandas` available for the SAS example.

Provisioning, credentials, and grants are manual in this repository version.

## 1. Connect Git

Link GitHub in Databricks user settings, then create a Git folder using:

```text
https://github.com/avneetxsingh/azure-databricks-retail-analytics.git
```

Start with `main`. Pull before editing if GitHub or another clone has newer changes. Preserve and resolve local changes before pulling.

## 2. Prepare input

Supply `sales.csv` with:

```text
sale_id,sale_date,customer_id,product_id,quantity,unit_price
```

Dates should follow the included parsing format, for example `9/1/2026`. Customer and product CSVs support the dashboard but are not loaded by the two cleaning notebooks. Git integration does not upload CSVs to a storage container or volume automatically.

## 3A. Unity Catalog method

1. Use a Unity Catalog-enabled workspace.
2. Create or choose a development catalog and schema.
3. Create the appropriate managed or external volume. External volumes require configured external locations and storage credentials; cloning Git does not create these.
4. Ensure your identity has the required catalog/schema usage, volume read/write, and table creation/replacement privileges.
5. Upload `sales.csv` to the volume root.
6. Review the notebook's input, output directories, and table target before execution.

The included input path is:

```text
/Volumes/ct_salesanalytics/schema_salesanalytics/vol_sales/sales.csv
```

Run `Sales-Cleaning-Method2-Catalog` from the top. Cells 1–9 load and clean records. Cells 10–11 overwrite CSV directories. Cell 12 replaces `ct_salesanalytics.schema_salesanalytics.orders`, including its schema. Cell 13 prints the saved schema.

Use an isolated development target for first execution. Review dashboard dependencies before replacing an existing table.

## 3B. SAS / HTTP method

1. Upload the source CSV to the configured Blob path. The example uses `csalesdata/raw/sales.csv` in `strsalesdata`.
2. Generate fresh SAS credentials for the exact account and resources. The source needs Read; the destination needs the permissions required for creating/writing the blob.
3. Create or use a Databricks secret scope called `retail-sales`.
4. Store the source token as `source-sas` and the output token as `output-sas` through approved secret-management tooling. Do not put values in source code or commit them.
5. Adjust the source URL, `storage_account`, and `container` for your environment.
6. Run `Sales-Cleaning- Method1- SAS-Token` from the top.

The output is `<container>/valid/valid_sales.csv`. Secret references do not automatically create tokens or grant storage permissions. This method collects files/records on the driver; use governed Spark reads and distributed writes for larger data.

## 4. Verify

- Reconcile post-deduplication total records with valid plus invalid counts.
- Inspect cast types, dates, and the revenue formula.
- Test zero, negative, and null quantities in an isolated fixture.
- Check that CSV outputs are CSV and the managed table uses Delta.
- For dashboard joins, verify dimension key uniqueness and unmatched sales before aggregating.

Historical README metrics are context, not execution evidence for the edited notebooks.

## 5. Package remaining assets

- [ADF Git configuration](../adf/README.md)
- [Dashboard export](../dashboards/README.md)
- [Azure infrastructure export](../infrastructure/README.md)

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Blob 404 | Exact account, container, directory, filename, and case |
| SAS signature mismatch | Fresh unedited token, correct scope, and matching destination |
| SAS authorization failure | Required permissions, token validity, and storage restrictions |
| Volume access denied | Usage grants, volume privileges, and storage configuration |
| Missing `price` column | Revenue uses `quantity` and `unit_price` |
| CSV appears as a folder | Expected Spark output: inspect `part-*.csv` files |
| Table still has raw records | Editing notebook code does not run its final write |

Never print a signed URL for troubleshooting. Stop unused compute through normal project operating practices to avoid unnecessary charges.
