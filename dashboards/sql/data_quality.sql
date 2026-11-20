WITH raw AS (
  SELECT * FROM ct_salesanalytics.schema_salesanalytics.orders
),
c AS (
  SELECT * FROM read_files('/Volumes/ct_salesanalytics/schema_salesanalytics/vol_sales/customers.csv', format => 'csv', header => true)
),
p AS (
  SELECT * FROM read_files('/Volumes/ct_salesanalytics/schema_salesanalytics/vol_sales/products.csv', format => 'csv', header => true)
)
SELECT 1 AS check_order, 'Orders table' AS check_area, 'Rows in current orders table' AS check_name, COUNT(*) AS check_value FROM raw
UNION ALL SELECT 2, 'Orders table', 'Rows excluded: quantity null or <= 0', COUNT_IF(quantity IS NULL OR quantity <= 0) FROM raw
UNION ALL SELECT 3, 'Orders table', 'Rows included in metrics', COUNT_IF(quantity > 0) FROM raw
UNION ALL SELECT 4, 'Orders table', 'Rows with missing or unparseable sale_date', COUNT_IF(COALESCE(try_cast(sale_date AS DATE), CAST(try_to_timestamp(CAST(sale_date AS STRING), 'M/d/yyyy') AS DATE)) IS NULL) FROM raw
UNION ALL SELECT 5, 'Orders table', 'Duplicate sale_id rows', COUNT(*) - COUNT(DISTINCT sale_id) FROM raw
UNION ALL SELECT 6, 'Join coverage', 'Order rows with no matching customer_id', (SELECT COUNT(*) FROM raw r LEFT ANTI JOIN c ON r.customer_id = c.customer_id)
UNION ALL SELECT 7, 'Join coverage', 'Order rows with no matching product_id', (SELECT COUNT(*) FROM raw r LEFT ANTI JOIN p ON r.product_id = p.product_id)
UNION ALL SELECT 8, 'Customers file', 'Rows in customers.csv', COUNT(*) FROM c
UNION ALL SELECT 9, 'Customers file', 'Duplicate customer_id rows', COUNT(*) - COUNT(DISTINCT customer_id) FROM c
UNION ALL SELECT 10, 'Products file', 'Rows in products.csv', COUNT(*) FROM p
UNION ALL SELECT 11, 'Products file', 'Duplicate product_id rows', COUNT(*) - COUNT(DISTINCT product_id) FROM p
