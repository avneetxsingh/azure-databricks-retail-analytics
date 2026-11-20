# Project handoff status

Last reviewed: November 20, 2026.

## Export and repository work completed

- Public GitHub repository connected to Databricks and ADF.
- Both copied notebooks reviewed; embedded SAS values removed from their published source.
- Revenue calculation, CSV/Delta output usage, and null-quantity rejection corrected.
- Five-page dashboard exported and placed directly under Git source control.
- Three dashboard dataset queries and two metric configurations extracted for review.
- Dashboard date handling and dark-mode KPI foreground corrected and synchronized to the workspace draft.
- Previews saved for all five pages plus the data-quality table.
- Original synthetic practice CSVs published with the owner's explicit confirmation and provenance notice.
- Azure resource-group snapshot and complete separate ADF ARM package exported and documented.
- Setup, architecture, definitions, contribution/security guidance, MIT code license, and third-party notices included.
- Optional development namespace SQL added.
- Local repository/sample-data checks, live dashboard checks, Catalog cleaning cells 1–9, and ADF definition validation passed. See [validation.md](validation.md).

## Operational follow-ups

These are outside the exported source package and are not claimed as completed:

1. Configure secrets before executing the SAS example.
2. Deliberately run output-write cells against the intended development destinations.
3. Run ADF Copy if needed and add orchestration if ADF should invoke Databricks.
4. Provision identities, external locations, and grants for another environment.
5. Test infrastructure deployment and the full workflow in a separate environment before claiming production reproducibility.
6. Add upstream practice-dataset attribution if its original source becomes available.

## Boundaries

Original workspace notebook copies/history may retain earlier SAS values. Only the reviewed Git-folder copies were published. Revoke/rotate old credentials as appropriate.

No new Azure infrastructure was created and no data-overwrite cells were run during packaging. Private credentials and cloud permission state are not portable repository assets.
