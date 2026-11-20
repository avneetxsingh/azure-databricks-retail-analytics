"""Validate the bundled practice CSVs and reconcile their documented snapshot."""

import csv
from datetime import datetime
from decimal import Decimal
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    with (ROOT / "data" / "sample" / name).open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def verify():
    sales, customers, products = map(load, ("sales.csv", "customers.csv", "products.csv"))
    for rows, key in ((sales, "sale_id"), (customers, "customer_id"), (products, "product_id")):
        assert rows, f"Empty input: {key}"
        assert all(row[key] for row in rows), f"Missing {key}"
        assert len({row[key] for row in rows}) == len(rows), f"Duplicate {key}"
    customer_ids = {row["customer_id"] for row in customers}
    product_ids = {row["product_id"] for row in products}
    assert all(row["customer_id"] in customer_ids for row in sales), "Unmatched customer"
    assert all(row["product_id"] in product_ids for row in sales), "Unmatched product"
    dates = [datetime.strptime(row["sale_date"], "%m/%d/%Y").date() for row in sales]
    quantities = [int(row["quantity"]) for row in sales]
    assert all(quantity > 0 for quantity in quantities), "Unexpected invalid quantity in baseline data"
    revenue = sum(Decimal(row["quantity"]) * Decimal(row["unit_price"]) for row in sales)
    assert (len(sales), len(customers), len(products), sum(quantities), revenue) == (
        20, 10, 10, 29, Decimal("7519.71")
    ), "Bundled baseline differs from the documented snapshot"
    return {
        "sales_rows": len(sales), "customer_rows": len(customers),
        "product_rows": len(products), "units": sum(quantities),
        "revenue_usd_display": str(revenue),
        "first_sale": min(dates).isoformat(), "last_sale": max(dates).isoformat(),
        "duplicate_keys": 0, "unmatched_customer_or_product": 0,
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
