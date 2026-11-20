# Validation record

Reviewed November 20, 2026. Results below distinguish local checks, live read-only execution, and deployment scope.

| Check | Result |
| --- | --- |
| Notebook JSON/Python syntax and selected credential patterns | Passed locally |
| Original synthetic CSV keys and dimension coverage | Passed: 20 sales, 10 customers, 10 products; no duplicates or unmatched references |
| Source-data revenue and units | $7,519.71 and 29 units |
| Catalog notebook cells 1–9 | Passed in Databricks: Total Records 20, Valid Records 20, Invalid Records 0 |
| Catalog output cells 10–13 | Not executed during this review; overwrite destinations require deliberate execution |
| Five dashboard pages | Loaded and visually inspected after Git synchronization |
| Dashboard baseline | Revenue $7,519.71; orders 20; units 29; AOV $375.99; purchasing customers 10; products 10 |
| Shared Category = Electronics | Executive and transaction pages both show $3,799.95, 4 orders, and 5 units |
| Filter reset | Restored $7,519.71, 20 orders, and 29 units |
| Dashboard data-quality query | 0 missing/invalid dates, duplicate IDs, unmatched customers, or unmatched products; 20 included rows |
| ADF Validate all | Passed in ADF Studio: factory validated, no errors found |
| Azure/ADF JSON exports | Parsed locally; credential parameters have no populated secret values |
| GitHub Actions | Offline repository and sample-data checks run on main/PRs |

## Limits

No ADF Copy run or revised notebook storage write was triggered in this validation. No new Azure environment was deployed, no original infrastructure grants were recreated, and SAS-method execution still requires the documented secret scope. The ADF pipeline copies a CSV and does not invoke Databricks automatically. These are operational/deployment follow-ups, not missing exports.

The dashboard source supports raw text or cleaned Date columns; live dashboard checks used the current workspace orders table. Spark cleaning separately produced a Date column in memory. The reviewed output table was not overwritten.

Screenshots are normal-viewport captures of the actual workspace draft. They are not fabricated full-page mockups. Static Executive Overview commentary intentionally describes the full dataset and does not follow filters.
