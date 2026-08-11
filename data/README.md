# Frozen teaching data

These small files keep the module reproducible while showing how each source can
be queried. They provide biological context for follow-up prioritization. They
must not be interpreted as direct evidence that a variant is pathogenic.

## `variants.csv`

Five ClinVar-linked cardiomyopathy examples supplied with the original module
scaffold. ClinVar assertions can change. Recheck the linked variation record for
clinical use.

## `gtex_expression.csv`

Median gene expression in GTEx v10 heart atrial appendage and left ventricle,
retrieved from `GET /api/v2/expression/medianGeneExpression` on 2026-08-11. The
unit returned by the API was TPM. Gene identifiers were resolved through
`GET /api/v2/reference/gene` using GENCODE v39 and GRCh38.

## `hubmap_cell_expression.csv`

A teaching extract from the HuBMAP Cells API, retrieved on 2026-08-11. For each
selected heart cell type, the extract summarizes up to the first 500 cells
returned by `POST /api/celldetailevaluation/`. `total_matching_cells` reports
the full matching set, while `sampled_cells` reports the number summarized.

The Cells API aggregate endpoint returned a server error during retrieval, so
means and detection percentages were calculated from the returned cell-level
values. `LMNA` and `PKP2` were not present in the API's indexed expression store.
Those entries are recorded as unavailable rather than zero. Small groups,
especially atrial cardiac myocytes and general endothelial cells, are not
appropriate for strong quantitative comparisons.

## `pharos_target_context.csv`

Target name, UniProt identifier, target development level, publication count,
ligand and drug counts, and protein interaction count retrieved from the Pharos
GraphQL API on 2026-08-11. These fields describe knowledge and tractability.
They do not measure disease causality or variant pathogenicity.

## `integrated_prioritization.csv`

A compact join of the four evidence layers for the final activity. No combined
pathogenicity score is provided. Learners keep biological context, data
availability, and target development level as separate dimensions.
