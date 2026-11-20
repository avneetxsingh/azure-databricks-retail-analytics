# Sales cleaning notebooks

Choose one method. Both start from the original sales CSV and apply the same quantity rule.

| Notebook | Purpose |
| --- | --- |
| [Sales-Cleaning- Method1- SAS-Token](Sales-Cleaning-%20Method1-%20SAS-Token.ipynb) | Blob REST download/upload with SAS tokens supplied through a secret scope |
| [Sales-Cleaning-Method2-Catalog](Sales-Cleaning-Method2-Catalog.ipynb) | Governed volume access with CSV outputs and a validated managed Delta table |

Read [setup instructions](../docs/setup.md). Run from the first cell after changing transformations. Notebook variables preserve earlier transformations, so rerunning a date-conversion cell alone can give misleading results.

## Outputs

The SAS method writes one CSV blob to `<container>/valid/valid_sales.csv`. The included account/container are `strsalesdata` and `csalesdata`; use your own authorized resources.

The Catalog method writes under its configured volume:

```text
processed/valid/valid_sales/       # CSV part files and Spark metadata
processed/invalid/invalid_sales/   # CSV part files and Spark metadata
```

It also writes `ct_salesanalytics.schema_salesanalytics.orders` as a managed Delta table after validation. These writes use overwrite mode. A CSV directory is not a Delta table; `.format("delta").csv(...)` does not create Delta data.

## Constraints

- The SAS example uses pandas and `toPandas()`, collecting data on the driver; use only small inputs.
- Source schema inference and double-valued prices are instructional choices. Production ingestion needs explicit schemas and appropriate decimal precision.
- Deduplication does not specify a winner for conflicting duplicate IDs.
- Null quantities are rejected, but broader data-quality rules are not implemented.
- Historical displayed results in a workspace copy do not validate edited code. Outputs are excluded from Git.
- Catalog cells 1–9 passed in Databricks (20 valid, 0 invalid). Output-write cells and SAS-method execution were not run during packaging.
