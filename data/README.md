# Data inputs and publication

The project uses `sales.csv`, `customers.csv`, and `products.csv`. Their headers are documented in the [data dictionary](../docs/data-dictionary.md). Original records are not committed.

The customer schema contains names and email addresses. Confirm provenance, whether the records are synthetic, and permission to publish before adding data. The MIT code license does not establish dataset rights.

For a sample-data contribution:

1. Confirm source and publication rights.
2. Prefer clearly synthetic records; exclude real contact details.
3. Preserve the documented columns and join keys.
4. Record the source, license, generation method if applicable, and modifications.
5. Add only reviewed files under `sample/`.

Keep unreviewed inputs outside Git or in ignored `data/private/`. Supply your own authorized files when executing the notebooks until shareable samples are added.
