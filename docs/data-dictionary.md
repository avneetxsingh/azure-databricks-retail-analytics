# Data dictionary and metric definitions

Column names were checked against the project's local CSV headers. The owner confirmed that the original records are synthetic practice data and authorized their publication under `data/sample/`; see the provenance notice there.

## Sales

| Column | Meaning / handling |
| --- | --- |
| `sale_id` | Sale identifier; deduplication key and assumed order ID |
| `sale_date` | Transaction date, parsed as `M/d/yyyy` |
| `customer_id` | Customer join key |
| `product_id` | Product join key |
| `quantity` | Integer; positive/non-null values accepted |
| `unit_price` | Transaction unit price, cast to double |
| `total_amount` | Derived quantity × transaction unit price |

Verify business grain before equating `sale_id` with an order. The example assumes one record per identifier after deduplication.

## Customers

| Column | Meaning |
| --- | --- |
| `customer_id` | Customer key |
| `customer_name` | Customer display name |
| `email` | Customer contact email; potentially personal data |
| `city` | Customer city |
| `state` | Customer state |
| `country` | Customer country |
| `signup_date` | Customer signup date |

Confirm provenance and sharing rights before publishing customer records. An instructional filename does not establish that data is synthetic.

## Products

| Column | Meaning |
| --- | --- |
| `product_id` | Product key |
| `product_name` | Product display name |
| `category` | Product category |
| `unit_price` | Catalog-listed unit price |
| `brand` | Product brand |

Use the **sale's** price for revenue, not the product's listed price. Qualify both columns when joining.

## Metrics

| Metric | Definition |
| --- | --- |
| Revenue | Sum of validated `total_amount` |
| Orders | Distinct `sale_id`, subject to the grain assumption |
| Units sold | Sum of validated quantity |
| Average order value | Revenue / distinct orders, with zero handling |
| Customers with purchases | Distinct customer IDs in validated sales for the selected period |
| Products sold | Distinct product IDs in validated sales for the selected period |
| Revenue share | Group revenue / clearly identified filtered total |

Master-data customer/product counts are different from purchasing-customer/product counts. The dashboard uses USD formatting; currency is not present in the source schema.

## Limitations

- Counts are taken after deduplication; removed duplicates are not quarantined.
- Conflicting duplicate IDs have no deterministic winner.
- Quantity validation does not check all dates, prices, customer/product references, or other business rules.
- Invalid date/cast behavior depends on runtime configuration; complete parsing quarantine is not implemented.
- Monetary decimals, refunds, historical pricing, and currency conversion need further design.
- Check dimension key uniqueness and unmatched rows to prevent inflated or missing revenue.
