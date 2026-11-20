# Retail sales dashboard

Workspace asset: `DBC_RetailSales`. Dashboard JSON and screenshots have not been exported into this repository yet.

## Export

1. Open the finished draft dashboard.
2. Select **⋮ → File actions → Export**.
3. Add the `.lvdash.json` file here.
4. Review query definitions for credentials and environment-specific references.
5. Add clean screenshots under `screenshots/` and embed them in the root README.

An imported definition still needs source tables, volumes, appropriate permissions, and an attached SQL warehouse. It does not contain table data or recreate access grants.

Reconcile metrics against the [data dictionary](../docs/data-dictionary.md). Check uniqueness and unmatched rows when joining dimensions. Review raw-date conversions against the cleaned Date column written by the revised Catalog notebook.

Only show targets, profit, prior-period growth, or forecasts when their required data actually exists.

[Microsoft: dashboard import/export](https://learn.microsoft.com/en-us/azure/databricks/dashboards/automate/import-export)
