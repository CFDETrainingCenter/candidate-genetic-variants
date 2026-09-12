# Data provenance

These CSV files provide dated teaching data when a live API is unavailable.
They also provide a reference for comparing results when a resource changes.

## Saved data

| File | Source | Version or identifiers | Retrieval date |
|---|---|---|---|
| `variants.csv` | Supplementary Table S4 from [Linnér et al.](https://doi.org/10.1038/s41598-025-88465-8) ([PMID 39910139](https://pubmed.ncbi.nlm.nih.gov/39910139/)) | Published HGVS names and transcript versions | Published in 2025 |
| `gtex_expression.csv` | GTEx Portal API v2 | GTEx v10, GENCODE v39, and GRCh38 | 2026-08-11 |
| `hubmap_cell_expression.csv` | HuBMAP Cells API | Cell Ontology IDs and dataset UUIDs stored in the CSV | 2026-08-11 |
| `pharos_target_context.csv` | Pharos GraphQL API | UniProt identifiers stored in the CSV | 2026-08-11 |
| `protvar_predictions.csv` | [ProtVar](https://www.ebi.ac.uk/ProtVar/release) API v2.0 and data release 2.1 | UniProt 2025_01, P45379, p.Asp259Ala, FoldX v5.0, and AlphaFold2 | 2026-08-11 |
| `integrated_prioritization.csv` | Derived from the variant, GTEx, HuBMAP, and Pharos files | 54 published variant rows joined to gene-level data | 2026-08-11 |

## Processing notes

- `variants.csv` contains all 54 rows from the source table. They represent 46
  participants and 25 genes. Blank protein HGVS fields remain blank. One
  URL-encoded equals sign was changed from `%3D` to `=`.
- `gtex_expression.csv` contains median TPM for the atrial appendage and left
  ventricle. Gene identifiers were resolved through the GTEx reference endpoint.
- `hubmap_cell_expression.csv` summarizes up to the first 500 cells for each
  gene and selected heart cell type. Means and detection percentages were
  calculated from cell-level values after the aggregate endpoint returned a
  server error. `not_available_in_cells_api_index` marks an index gap and remains
  separate from a measured zero.
- `pharos_target_context.csv` contains the selected target fields returned for
  the 25 genes.
- `protvar_predictions.csv` records the AlphaMissense, EVE, FoldX, and AlphaFold
  results returned for p.Asp259Ala.
- `integrated_prioritization.csv` keeps the study classifications and each
  gene-level measure in separate columns.

## Live results and data drift

The GTEx request specifies the fixed v10 release. HuBMAP and Pharos may update
their data over time. Their retrieval dates, Cell Ontology IDs, dataset UUIDs,
and UniProt identifiers define the saved results used in this module.

ProtVar API v2.0 and data release 2.1 were used on 2026-08-11 for UniProt
P45379, residue 259, and alternate amino acid A. ProtVar identifies the
AlphaMissense and EVE sources by name. Its documentation specifies FoldX v5.0
on AlphaFold2 structures. The same results were verified on 2026-09-12.
