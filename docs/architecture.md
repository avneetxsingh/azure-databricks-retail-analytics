# Architecture and design decisions

## Two processing paths

**SAS / HTTP:** download a small CSV from Azure Blob Storage, read it with pandas on the driver, create a Spark DataFrame, clean it, and upload validated records as a single CSV blob. Credentials come from Databricks secrets.

**Unity Catalog:** read through a governed volume, transform records with Spark, write valid/rejected CSV directories, and replace the managed `orders` Delta table with validated records.

The methods are alternatives with different outputs. Both cast types, convert dates, deduplicate sale IDs, calculate revenue, and split positive/non-null quantities from rejected quantities.

## Analytics

The inspected workspace dashboard used `orders` plus customer and product CSV dimensions. It showed KPIs, daily revenue, category/product contribution, customer/state revenue, and transaction details.

Earlier notebook code wrote raw records to `orders` before transformations, so the dashboard repeated cleaning in SQL. The revised Catalog notebook writes validated records at the end. Review dashboard date conversions and other repeated logic against that new schema before using them together. The unchanged table name does not guarantee query compatibility.

The dashboard remains a workspace asset until its `.lvdash.json` is exported to Git. Publishing, exporting, and committing are separate actions.

## Orchestration and infrastructure

ADF is connected to this repository on `main`, using `/adf` as its root. The imported `PL_CopyData` pipeline uses the parameterized `DS_Blob` dataset and `LS_Blob` linked service to copy `csalesdata/raw/sales.csv` to `csalesdata/processed/sales_processed.csv`. It does not call a Databricks notebook. An ADF-to-Databricks end-to-end run has not been verified. The notebooks currently use their own input locations rather than consuming that copied output automatically.

Resource-group templates cover supported Azure infrastructure properties. They do not replace exports of notebook/dashboard assets, storage contents, Unity Catalog setup, grants, and secrets. ADF definitions need a separate export or Git integration.

## Tradeoffs

| Choice | Benefit | Constraint |
| --- | --- | --- |
| Retain both access methods | Explain authentication and governed reads | Readers must choose a workflow |
| Volume-based Catalog access | Keep file access under governance | Requires configured storage and permissions |
| Inferred schema and double prices | Preserve a readable learning workflow | Explicit schemas/decimal handling remain improvements |
| Batch overwrite | Simple repeatable demonstration | Replaces destinations; not incremental ingestion |
| Secret references | Keep credentials out of source | Provisioning and rotation remain manual |

GitHub Actions runs offline repository checks without cloud credentials. Cloud runtime/integration tests and deployment automation are not included. Future improvements could include deterministic deduplication, richer rejection reasons, explicit schemas, decimal prices, incremental processing, orchestration, and deployment bundles.
