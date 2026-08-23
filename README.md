# Prioritizing Candidate Genetic Variants Using GTEx, HuBMAP, and IDG

A reproducible CFDE training module that uses tissue, cell-type, and protein
context to prioritize candidate genetic variants for further study.

The module is available as a [deployed training website](https://cfdetrainingcenter.github.io/candidate-genetic-variants/).
Learners can run the analysis code in the website or use the accompanying
Jupyter notebooks.

## Table of contents

- [Project background](#project-background)
- [Module content](#module-content)
- [Data resources](#data-resources)
- [Using the module](#using-the-module)
- [Repository structure](#repository-structure)
- [Maintainer setup](#maintainer-setup)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Author and maintenance](#author-and-maintenance)

## Project background

This repository contains a CFDE training module about prioritizing candidate
genetic variants. Early-onset advanced heart failure provides the teaching
example. The starting dataset is the complete 54-row Supplementary Table S4
from Linnér and colleagues' 2025 whole-genome sequencing study ([PMID:
39910139](https://pubmed.ncbi.nlm.nih.gov/39910139/), [DOI:
10.1038/s41598-025-88465-8](https://doi.org/10.1038/s41598-025-88465-8)). The
table represents 46 study participants and 25 genes. Those records move
through a single workflow:

1. Review variant and gene annotations.
2. Examine tissue-level gene expression with GTEx.
3. Examine cell-type expression with HuBMAP.
4. Review protein context and target development levels with IDG and Pharos.
5. Combine the evidence to compare candidates.

The module also introduces application programming interfaces, or APIs. The
website and notebooks query GTEx, HuBMAP, and Pharos by default, then use
ProtVar for one selected missense variant. Dated teaching files provide a
commented backup for the GTEx, HuBMAP, and Pharos activities when a live service
is unavailable.

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

The website includes explanations, executable activities, and knowledge checks
where they support the lesson. Each instructional page links to a matching
notebook. The notebooks preserve the lesson content and provide completed,
executable examples. Interactive website questions appear as regular Markdown
in Jupyter. `notebooks/06_variant_prioritization.ipynb` contains the complete
prioritization workflow.

## Data resources

- [Source paper](https://doi.org/10.1038/s41598-025-88465-8) provides the
  published variant table, study scores, classifications, phenotypes, and
  comments used as the starting dataset. ClinVar contributed to the paper's
  ranking process, but this module does not query ClinVar or repeat the
  clinical classification.
- [GTEx](https://gtexportal.org/home/) is a reference resource for gene
  expression and genetic regulation across human tissues. The module uses
  median expression from two heart tissues.
- [HuBMAP](https://portal.hubmapconsortium.org/) maps cells and molecules within
  human tissues. The module uses expression summaries for selected heart cell
  types.
- [IDG](https://commonfund.nih.gov/IDG/) studies understudied druggable proteins.
  [Pharos](https://pharos.nih.gov/) provides integrated protein and target
  development information from IDG and other resources.
- [ProtVar](https://www.ebi.ac.uk/ProtVar/) provides protein-level annotations
  and predictions for the selected missense variant example.

Small saved files let learners continue if a live API is unavailable:

- `data/variants.csv`: all 54 published variant rows
- `data/gtex_expression.csv`: GTEx v10 values for the 25 genes and two heart
  tissues
- `data/hubmap_cell_expression.csv`: HuBMAP values or explicit availability
  records for 25 genes and six heart cell types
- `data/pharos_target_context.csv`: Pharos target context for the 25 genes
- `data/integrated_prioritization.csv`: gene-level context joined to all 54
  variant rows

See [`data/README.md`](data/README.md) for endpoints, retrieval dates,
transformations, missing-data handling, and limitations.

## Using the module

### Use the website

Open the [rendered training module](https://cfdetrainingcenter.github.io/candidate-genetic-variants/).
The website is already deployed. You only need a current web browser and an
internet connection. You do not need to install Python, Jupyter, `uv`, or
Quarto.

### Use the notebooks in JupyterLab

JupyterLab opens notebooks in a web-browser interface. A notebook contains text
and code in separate cells. You can run one code cell at a time and inspect its
output directly below it.

For local notebook use, you need an internet connection and
[`uv`](https://docs.astral.sh/uv/). You do not need an existing Python
installation. `uv` downloads the requested Python version and creates an
isolated environment for this module.

#### 1. Get the repository

If you use Git, open a terminal and run:

```bash
git clone https://github.com/CFDETrainingCenter/candidate-genetic-variants.git
cd candidate-genetic-variants
```

If you do not use Git, open the repository's
[GitHub page](https://github.com/CFDETrainingCenter/candidate-genetic-variants),
select **Code > Download ZIP**, and extract the downloaded file. Then open a
terminal in the extracted `candidate-genetic-variants` folder.

The commands below must be run from the repository root. This is the folder
that contains `README.md`, `requirements.txt`, and the `notebooks/` directory.

#### 2. Install uv

Follow the [official uv installation
instructions](https://docs.astral.sh/uv/getting-started/installation/) for your
operating system. Close and reopen the terminal after installation, then
confirm that `uv` is available:

```bash
uv --version
```

#### 3. Create the Python environment

Run these commands one at a time from the repository root:

```bash
uv venv --python 3.14
uv pip install -r requirements.txt
```

The first command creates a local `.venv` folder containing Python. The second
installs JupyterLab and the packages used in the lessons. You do not need to
activate the environment.

#### 4. Open JupyterLab

On macOS or Linux, run:

```bash
.venv/bin/python -m jupyter lab notebooks/
```

On Windows PowerShell, run:

```powershell
.venv\Scripts\python.exe -m jupyter lab notebooks
```

JupyterLab should open in your web browser. If it does not, copy the URL shown
in the terminal and paste it into the browser.

#### 5. Run the notebooks

Open `00_module_intro.ipynb` first, then continue through the numbered
notebooks. Select the Python 3 kernel if Jupyter asks you to choose one. To run
a selected code cell, press **Shift+Enter** or use the run button in the
notebook toolbar.

The notebooks query live APIs, so returned values and response times can
change. GTEx, HuBMAP, and Pharos lessons include instructions for using dated
teaching files if a service is unavailable. Definitions for terms used in the
module are available in [`GLOSSARY.md`](GLOSSARY.md).

To stop JupyterLab, return to the terminal, press **Control+C**, and confirm the
shutdown if prompted.

#### Common setup problems

- If `uv` is not found, close and reopen the terminal, then run `uv --version`.
- If `requirements.txt` is not found, return to the folder containing
  `README.md` before running the setup commands.
- If Jupyter asks for a kernel, select the Python 3 environment associated with
  this repository's `.venv` folder.

## Maintainer setup

Learners do not need Quarto. Contributors who preview or build the website
locally need [Quarto](https://quarto.org/) 1.6 or later and the Python
environment created above. The Quarto Live extension is stored in
`_extensions/` and does not require a separate installation.

### Preview the website locally

On macOS or Linux, run:

```bash
QUARTO_PYTHON=".venv/bin/python" quarto preview
```

On Windows PowerShell, run:

```powershell
$env:QUARTO_PYTHON=".venv\Scripts\python.exe"
quarto preview
```

To create the complete website locally, replace `quarto preview` with
`quarto render`. Setting `QUARTO_PYTHON` ensures that Quarto uses the Python
packages installed for this repository.

The landing page and project configuration remain at the repository root.
Lesson source files are organized under `lessons/`. The ignored `docs/`
directory contains rendered website files.

## Repository structure

```text
candidate-genetic-variants/
├── _quarto.yml
├── GLOSSARY.md
├── README.md
├── api_helpers.py
├── index.qmd
├── requirements.txt
├── assets/
│   ├── styles.scss
│   └── images/
│       ├── cfde.svg
│       └── evidence-flow.svg
├── lessons/
│   ├── objectives.qmd
│   ├── variant-context.qmd
│   ├── gtex.qmd
│   ├── hubmap.qmd
│   ├── pharos.qmd
│   ├── prioritization.qmd
│   ├── conclusion.qmd
│   └── glossary.qmd
├── data/
├── notebooks/
│   ├── 00_module_intro.ipynb
│   ├── 01_api_introduction.ipynb
│   ├── 02_variant_background.ipynb
│   ├── 03_gtex_tissue_expression.ipynb
│   ├── 04_hubmap_cell_type_expression.ipynb
│   ├── 05_pharos_target_context.ipynb
│   ├── 06_variant_prioritization.ipynb
│   └── 07_conclusion.ipynb
├── _extensions/
└── .github/workflows/publish.yml
```

## Deployment

A learner does not need to deploy the website. The deployed training module is
available through the link at the top of this README.

A push to `main` starts `.github/workflows/publish.yml`. The workflow renders
the Quarto project and publishes the result to the `gh-pages` branch.

The repository must allow GitHub Actions read and write access under
**Settings > Actions > General > Workflow permissions**. GitHub Pages must use
the `gh-pages` branch as its publishing source.

## Contributing

Use [GitHub Issues](https://github.com/CFDETrainingCenter/candidate-genetic-variants/issues)
to report problems or suggest improvements. Pull requests should keep the
Quarto source files in the repository root and should not commit rendered files
from `docs/`.

## License

Except where otherwise noted, original content and code in this repository are
made available under the [CC0 1.0 Universal](LICENSE) public-domain dedication.

Third-party software and materials retain their original licenses.

## Author and maintenance

- **Author:** Shaurita D. Hutchins
- **Development and maintenance:** This is a community-sourced module from the
  [CFDE Training Center](https://github.com/CFDETrainingCenter), which
  coordinates training module development and maintenance.
