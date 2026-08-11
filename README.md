# Prioritizing Candidate Genetic Variants Using GTEx, HuBMAP, and IDG

A reproducible CFDE training module that uses tissue, cell-type, and protein
context to prioritize candidate genetic variants for further study.

The lesson is available as a [Quarto website](https://cfdetrainingcenter.github.io/candidate-genetic-var/).
Learners can run the analysis code in the website or use the accompanying
Jupyter notebooks.

## Table of contents

- [Project background](#project-background)
- [Module content](#module-content)
- [Data resources](#data-resources)
- [Install and setup](#install-and-setup)
- [Usage](#usage)
- [Repository structure](#repository-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Project background

This repository contains a CFDE training module about prioritizing candidate
genetic variants. Early-onset advanced heart failure provides the teaching
example. Five candidate variants move through a single workflow:

1. Review variant and gene annotations.
2. Examine tissue-level gene expression with GTEx.
3. Examine cell-type expression with HuBMAP.
4. Review protein context and target development levels with IDG and Pharos.
5. Combine the evidence to compare candidates.

The module also introduces application programming interfaces, or APIs. Saved
teaching data keep the exercises stable, while the website and notebooks show
the code used to request data from GTEx, HuBMAP, and Pharos.

GTEx expression, HuBMAP cell-type patterns, and Pharos target information add
biological context. They do not prove that a variant causes disease. This
module is for education and research training, not clinical variant
classification.

## Module content

The lesson takes about two hours and follows eight short sections:

1. Module Introduction
2. Introduction to APIs
3. Variant and Gene Context
4. Tissue-Level Expression: GTEx
5. Cell-Type Resolution: HuBMAP
6. Protein Context and Druggability: IDG/Pharos
7. Variant Prioritization and Interpretation
8. Conclusion

Each substantive section includes a short explanation, a Python activity, two
answer-selection knowledge checks, and a link to the matching notebook. The
website activity and section notebook use the same analysis code. The
integrated notebook contains the complete workflow.

## Data resources

- [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/intro/) provides the submitted
  variant annotations represented in the candidate teaching table. The module
  does not query a ClinVar API.
- [GTEx](https://gtexportal.org/home/) is a reference resource for gene
  expression and genetic regulation across human tissues. The module uses
  median expression from two heart tissues.
- [HuBMAP](https://portal.hubmapconsortium.org/) maps cells and molecules within
  human tissues. The module uses expression summaries for selected heart cell
  types.
- [IDG](https://commonfund.nih.gov/IDG/) studies understudied druggable proteins.
  [Pharos](https://pharos.nih.gov/) provides integrated protein and target
  development information from IDG and other resources.

Small saved files allow learners to get the same results without depending on
live API availability:

- `data/variants.csv`: shared five-variant teaching set
- `data/gtex_expression.csv`: GTEx v10 heart-tissue expression
- `data/hubmap_cell_expression.csv`: HuBMAP heart cell-type expression
- `data/pharos_target_context.csv`: Pharos target development context
- `data/integrated_prioritization.csv`: joined table used in the final activity

See [`data/README.md`](data/README.md) for endpoints, retrieval dates,
transformations, missing-data handling, and limitations.

## Install and setup

### Requirements

- [Quarto](https://quarto.org/) 1.6 or later to render the website
- [Python](https://www.python.org/) to run the notebooks locally
- [uv](https://docs.astral.sh/uv/) to create the recommended Python environment

The Quarto Live extension is stored in `_extensions/`, so it does not need to
be installed separately.

### Python environment

From the repository root, create a local environment and install the pinned
packages:

```bash
uv venv --python 3.14
uv pip install -r requirements.txt
```

## Usage

### Use the website

Open the [rendered training module](https://cfdetrainingcenter.github.io/candidate-genetic-var/).
Its Quarto Live exercises run in a current web browser without a local Python
installation.

### Use the notebooks

Start JupyterLab from the repository root:

```bash
.venv/bin/python -m jupyter lab notebooks/
```

Use `notebooks/00_course_orientation.ipynb` for an introduction. Use the
numbered section notebooks for focused activities, or open
`notebooks/05_variant_prioritization.ipynb` for the complete prioritization
workflow.

### Preview the website locally

```bash
quarto preview
```

To create the complete website in `docs/`, run:

```bash
quarto render
```

All Quarto source files remain in the repository root. The ignored `docs/`
directory contains only rendered website files.

## Repository structure

```text
candidate-genetic-var/
├── _quarto.yml
├── index.qmd
├── objectives.qmd
├── variant-context.qmd
├── gtex.qmd
├── hubmap.qmd
├── pharos.qmd
├── prioritization.qmd
├── conclusion.qmd
├── styles.scss
├── knowledge-checks.js
├── data/
├── notebooks/
├── images/
├── includes/
├── _extensions/
└── .github/workflows/publish.yml
```

## Deployment

A push to `main` starts `.github/workflows/publish.yml`. The workflow renders
the Quarto project and publishes the result to the `gh-pages` branch.

The repository must allow GitHub Actions read and write access under
**Settings > Actions > General > Workflow permissions**. GitHub Pages must use
the `gh-pages` branch as its publishing source.

## Contributing

Use [GitHub Issues](https://github.com/CFDETrainingCenter/candidate-genetic-var/issues)
to report problems or suggest improvements. Pull requests should keep the
Quarto source files in the repository root and should not commit rendered files
from `docs/`.

## License

Except where otherwise noted, original content and code in this repository are
made available under the [CC0 1.0 Universal](LICENSE) public-domain dedication.

Third-party software and materials retain their original licenses.

## Authors

- [CFDE Training Center](https://github.com/CFDETrainingCenter), training module
  development and maintenance
