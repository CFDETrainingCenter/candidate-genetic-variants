# Frozen teaching data

These small files keep the module reproducible while showing how each source can
be queried. They provide biological context for follow-up prioritization. They
must not be interpreted as direct evidence that a variant is pathogenic.

## `variants.csv`

All 54 rows from Supplementary Table S4 of Linnér and colleagues, *Whole genome
sequencing in early onset advanced heart failure* ([PMID:
39910139](https://pubmed.ncbi.nlm.nih.gov/39910139/), [DOI:
10.1038/s41598-025-88465-8](https://doi.org/10.1038/s41598-025-88465-8)). The
rows represent 46 subjects and 25 genes. Published HGVS names, study scores,
classes, phenotypes, and comments are retained. Four blank protein HGVS fields
remain blank. One URL-encoded equals sign was normalized from `%3D` to `=`.

The paper used whole-genome sequencing, a 369-gene filter, computational
ranking, manual review, and clinical classification. This file records the
paper's reported results. It is not a new clinical interpretation.

## `gtex_expression.csv`

Median gene expression in GTEx v10 heart atrial appendage and left ventricle,
retrieved from `GET /api/v2/expression/medianGeneExpression` on 2026-08-11. The
unit returned by the API was TPM. Gene identifiers were resolved through
`GET /api/v2/reference/gene` using GENCODE v39 and GRCh38.

The file has two tissue rows for each of the 25 genes. GTEx provides bulk
tissue context and does not measure the effect of a listed variant.

## `hubmap_cell_expression.csv`

A teaching extract from the HuBMAP Cells API, retrieved on 2026-08-11. It
contains one row for each combination of 25 genes and six selected heart cell
types. For an available combination, the extract summarizes up to the first
500 cells returned by `POST /api/celldetailevaluation/` after intersecting the
Heart organ handle with a cell-type handle. `total_matching_cells` reports the
full matching set, while `sampled_cells` reports the number summarized.

The Cells API aggregate endpoint returned a server error during retrieval, so
means and detection percentages were calculated from the returned cell-level
values. Genes were checked separately because a missing gene could break a
mixed-gene request. The file has 84 available combinations and 66 combinations
recorded as `not_available_in_cells_api_index`, not as measured zeros. Small
groups are not appropriate for strong quantitative comparisons.

## `pharos_target_context.csv`

Target name, UniProt identifier, target development level, publication count,
ligand and drug counts, and protein interaction count retrieved from the Pharos
GraphQL API on 2026-08-11 for all 25 genes. These fields describe knowledge and
tractability. They do not measure disease causality or variant pathogenicity.

## `integrated_prioritization.csv`

A 54-row join of the published variants and gene-level context used in the
final activity. No combined pathogenicity score is provided. Learners keep
biological context, data availability, and target development level as
separate dimensions.
