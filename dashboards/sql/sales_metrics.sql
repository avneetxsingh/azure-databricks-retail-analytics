WITH orders_clean AS (
  SELECT sale_id,
         COALESCE(try_cast(sale_date AS DATE), CAST(try_to_timestamp(CAST(sale_date AS STRING), 'M/d/yyyy') AS DATE)) AS sale_date,
         customer_id,
         product_id,
         quantity,
         CAST(unit_price AS DECIMAL(18,2)) AS unit_price
  FROM ct_salesanalytics.schema_salesanalytics.orders
  WHERE quantity > 0
),
customers AS (
  SELECT customer_id, customer_name, city, state, country
  FROM read_files('/Volumes/ct_salesanalytics/schema_salesanalytics/vol_sales/customers.csv', format => 'csv', header => true)
  QUALIFY ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY customer_name) = 1
),
products AS (
  SELECT product_id, product_name, category, brand
  FROM read_files('/Volumes/ct_salesanalytics/schema_salesanalytics/vol_sales/products.csv', format => 'csv', header => true)
  QUALIFY ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY product_name) = 1
)
SELECT o.sale_id,
       o.sale_date,
       o.customer_id,
       o.product_id,
       o.quantity,
       o.unit_price,
       CAST(o.quantity * o.unit_price AS DECIMAL(18,2)) AS line_revenue,
       COALESCE(c.customer_name, 'Unmatched customer') AS customer_name,
       COALESCE(c.city, 'Unknown') AS city,
       COALESCE(c.state, 'Unknown') AS state,
       COALESCE(c.country, 'Unknown') AS country,
       COALESCE(p.product_name, 'Unmatched product') AS product_name,
       COALESCE(p.category, 'Unknown') AS category,
       COALESCE(p.brand, 'Unknown') AS brand
FROM orders_clean o
LEFT JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN products p ON o.product_id = p.product_id
