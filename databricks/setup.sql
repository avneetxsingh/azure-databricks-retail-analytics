-- Optional development namespace setup. Review names before running.
-- Requires catalog/schema/volume creation privileges and configured managed storage.
-- This does not recreate the original external location, credential, or grants.
CREATE CATALOG IF NOT EXISTS ct_salesanalytics;
CREATE SCHEMA IF NOT EXISTS ct_salesanalytics.schema_salesanalytics;
CREATE VOLUME IF NOT EXISTS ct_salesanalytics.schema_salesanalytics.vol_sales;

-- Upload data/sample/*.csv to the volume root through Catalog Explorer.
-- Run the Catalog notebook to build orders; it overwrites its configured targets.
