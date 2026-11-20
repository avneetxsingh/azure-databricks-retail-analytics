# Retail practice data

The original owner-approved synthetic practice files are included in [sample/](sample/):

| File | Rows | Purpose |
| --- | ---: | --- |
| [sales.csv](sample/sales.csv) | 20 | Transaction facts |
| [customers.csv](sample/customers.csv) | 10 | Customer and geography dimensions |
| [products.csv](sample/products.csv) | 10 | Product, category, and brand dimensions |

The owner confirmed they are entirely practice data and may be published. See the [provenance notice](sample/NOTICE.md) for the limits of the supplied attribution/license information. Records are unchanged from the supplied originals.

Upload all three files to the Databricks volume root for the dashboard. The SAS example additionally expects sales.csv in the configured Blob raw directory; ADF Git integration does not upload CSV contents to Azure automatically.

Run `python tools/validate_sample_data.py` to reconcile 20 sales, 29 units, and $7,519.71, verify unique keys, and check customer/product joins. Column contracts are in the [data dictionary](../docs/data-dictionary.md).

Keep unreviewed future inputs outside Git or under ignored `data/private/`. Do not replace the practice customer records with real contact information.
