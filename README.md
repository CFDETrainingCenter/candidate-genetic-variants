# Prioritizing Candidate Genetic Variants Using GTEx, HuBMAP, and IDG

This CFDE training module uses tissue expression, cell-type expression, and
protein information to prioritize candidate genetic variants for follow-up.

The [interactive Quarto tutorial](https://cfdetrainingcenter.github.io/candidate-genetic-variants/)
extends the Jupyter notebooks by making the same analysis interactive and
available in a web browser. Learners can choose either format based on their
experience.

## Table of contents

- [Project background](#project-background)
- [What you will learn](#what-you-will-learn)
- [Module content](#module-content)
- [Data resources](#data-resources)
- [Using this module](#using-this-module)
- [Development setup](#development-setup)
- [Repository structure](#repository-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Author and maintainer](#author-and-maintainer)

## Project background

This module uses Supplementary Table S4 from a 2025 whole-genome sequencing
study of early-onset advanced heart failure by Linnér and colleagues ([PMID:
39910139](https://pubmed.ncbi.nlm.nih.gov/39910139/), [DOI:
10.1038/s41598-025-88465-8](https://doi.org/10.1038/s41598-025-88465-8)).
The table contains 54 variant rows from 46 participants and covers 25 genes. It
includes the reported variant classifications, participant phenotypes, and
study comments.

In this module, we will build on the published variant evidence with
tissue-level expression, cell-type expression, protein information, and
computational predictions. This dataset provides a practical example of how
multiple sources can help prioritize candidate genetic variants for follow-up.

## What you will learn

By the end of this module, you will be able to:

1. Explain what an application programming interface, or API, is and how APIs
   support repeatable research.
2. Use GTEx to check whether genes linked to candidate genetic variants are
   expressed in a disease-related tissue.
3. Use HuBMAP to study gene expression in specific cell types while accounting
   for missing data and small groups.
4. Use Pharos to interpret protein information and IDG Target Development
   Levels.
5. Combine several data sources to prioritize candidate genetic variants for
   follow-up.

## Module content

The module takes about two hours and follows eight short sections:

1. Module Introduction ([slides](https://cfdetrainingcenter.github.io/candidate-genetic-variants/slides/module-introduction.html))
2. Introduction to APIs
3. Published Variants and Candidate Genes
4. Tissue-Level Expression: GTEx
5. Cell-Type Resolution: HuBMAP
6. Protein Knowledge and Research Tools: IDG/Pharos
7. Variant Prioritization and Interpretation
8. Conclusion ([slides](https://cfdetrainingcenter.github.io/candidate-genetic-variants/slides/module-conclusion.html))

Each lesson includes explanations, browser-based activities, knowledge checks,
and a link to the matching notebook. The notebooks follow the same analysis.

## Data resources

- The [source paper](https://doi.org/10.1038/s41598-025-88465-8) provides the
  published variants, classifications, phenotypes, and study comments. The
  module starts with these reported results and focuses on research follow-up.
- [GTEx](https://gtexportal.org/home/) provides gene-expression data across
  human tissues. The module uses median expression from two heart tissues.
- [HuBMAP](https://portal.hubmapconsortium.org/) maps cells and molecules in
  human tissues. The module uses expression summaries for selected heart cell
  types.
- [IDG](https://commonfund.nih.gov/IDG/) studies understudied druggable
  proteins. [Pharos](https://pharos.nih.gov/) provides protein information and
  IDG Target Development Levels.
- [ProtVar](https://www.ebi.ac.uk/ProtVar/) provides protein annotations and
  predictions for one missense variant.

The website and notebooks query GTEx, HuBMAP, and Pharos by default. The
repository also includes dated teaching data for comparison and for times when
a live service is unavailable:

- `data/variants.csv`: all 54 published variant rows
- `data/gtex_expression.csv`: GTEx v10 values for the 25 genes and two heart
  tissues
- `data/hubmap_cell_expression.csv`: HuBMAP values or explicit availability
  records for 25 genes and six heart cell types
- `data/pharos_target_context.csv`: Pharos protein annotations for the 25 genes
- `data/protvar_predictions.csv`: ProtVar predictions for *TNNT2* p.Asp259Ala
- `data/integrated_prioritization.csv`: gene-level data joined to all 54
  variant rows

See [`data/README.md`](data/README.md) for sources, versions, retrieval dates,
and processing notes.

## Using this module

The interactive website runs in a browser. The same lessons are available as
Jupyter notebooks that you can run locally in JupyterLab.

Some Python knowledge is required for either format. You should be comfortable
reading variable assignments, calling functions, working with pandas
DataFrames, and interpreting code-cell output.

### Use the website

Open the [rendered training module](https://cfdetrainingcenter.github.io/candidate-genetic-variants/).
It requires a current web browser and no local setup.

### Use the notebooks in JupyterLab

Running the notebooks locally requires an internet connection and
[`uv`](https://docs.astral.sh/uv/). `uv` installs Python and creates an
environment for this module.

#### 1. Get the repository

If you use Git, open a terminal and run:

```bash
git clone https://github.com/CFDETrainingCenter/candidate-genetic-variants.git
cd candidate-genetic-variants
```

To download the repository without Git, open its
[GitHub page](https://github.com/CFDETrainingCenter/candidate-genetic-variants),
select **Code > Download ZIP**, extract the file, and open a terminal in the
`candidate-genetic-variants` folder.

Run the commands below from the folder containing `README.md`,
`requirements.txt`, and `notebooks/`.

#### 2. Install uv

Follow the [uv installation
instructions](https://docs.astral.sh/uv/getting-started/installation/) for your
operating system. Reopen the terminal, then confirm that `uv` is available:

```bash
uv --version
```

#### 3. Create the Python environment

Run these commands one at a time from the repository root:

```bash
uv venv --python 3.14
uv pip install -r requirements.txt
```

These commands create `.venv` and install JupyterLab and the packages used in
the lessons. The commands below use this environment directly.

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

Open `00_module_intro.ipynb` and continue through the numbered notebooks. If
Jupyter asks for a kernel, select Python 3. Run a cell with **Shift+Enter** or
the notebook toolbar.

Live API values and response times can change. Definitions are available in
[`GLOSSARY.md`](GLOSSARY.md).

To stop JupyterLab, return to the terminal, press **Control+C**, and confirm the
shutdown if prompted.

#### Common setup problems

- If `uv` is not found, reopen the terminal and run `uv --version`.
- If `requirements.txt` is not found, return to the folder containing
  `README.md`.
- If Jupyter asks for a kernel, select the Python 3 environment associated with
  this repository's `.venv` folder.

## Development setup

Building the website requires [Quarto](https://quarto.org/) 1.6 or later and
the Python environment created above. The Quarto Live extension is already in
`_extensions/`.

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

To create the complete website, replace `quarto preview` with `quarto render`.
`QUARTO_PYTHON` tells Quarto to use the Python packages installed for this
repository.

The landing page and project configuration are at the repository root. Lesson
source files are under `lessons/`. The ignored `docs/` directory contains the
rendered website.

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

Each push to `main` runs `.github/workflows/publish.yml`. The workflow renders
the Quarto project and publishes the website to the `gh-pages` branch.

Deployment requires two repository settings:

1. Give GitHub Actions read and write access under
   **Settings > Actions > General > Workflow permissions**.
2. Set GitHub Pages to publish from the `gh-pages` branch.

## Contributing

Use [GitHub Issues](https://github.com/CFDETrainingCenter/candidate-genetic-variants/issues)
to report problems or suggest improvements. Keep Quarto source files in the
repository root. Leave rendered files from `docs/` out of pull requests.

## License

Except where otherwise noted, original content and code in this repository are
made available under the [CC0 1.0 Universal](LICENSE) public-domain dedication.

Third-party software and materials retain their original licenses.

## Author and maintainer

- **Author and maintainer:** Shaurita D. Hutchins
- **Project:** A community-sourced module from the
  [CFDE Training Center](https://github.com/CFDETrainingCenter)
