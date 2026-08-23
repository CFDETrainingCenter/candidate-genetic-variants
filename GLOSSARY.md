# Glossary


**Estimated time:** 5 minutes

Use this glossary as a reference while working through the module. The
definitions describe how each term is used in this tutorial.

## A to F

<a id="acmg-amp-classification"></a>
### ACMG/AMP classification
A framework for classifying sequence variants using categories such as
pathogenic, likely pathogenic, uncertain significance, likely benign, and
benign. This module starts with variants that have already been evaluated
and does not perform clinical classification. [Learn more about the ACMG/AMP
standards.](https://pubmed.ncbi.nlm.nih.gov/25741868/)

<a id="alphamissense"></a>
### AlphaMissense
A protein variant-effect prediction model that assigns a pathogenicity score
to possible human missense variants using evolutionary information and
protein structural context. ProtVar reports the score and its prediction
category. [Learn more about
AlphaMissense.](https://pubmed.ncbi.nlm.nih.gov/37733863/)

<a id="api"></a>
### Application programming interface (API)
A defined way for software to request data or services from another system.
The APIs in this module make the source, identifiers, and retrieval steps for
each evidence layer explicit and reproducible. [Learn more about
APIs.](https://developer.mozilla.org/en-US/docs/Glossary/API)

<a id="bulk-tissue"></a>
### Bulk tissue
A tissue sample measured as a mixture of its component cell types. GTEx
expression provides bulk-tissue context, so it does not identify which cell
type produced a transcript signal. [Learn more about the GTEx
project.](https://commonfund.nih.gov/gtex)

<a id="cell-type"></a>
### Cell type
A group of cells with shared biological characteristics. Cell-type-resolved
expression can help identify a relevant cellular setting for follow-up
experiments or modeling. [Explore terms in the Cell
Ontology.](https://www.ebi.ac.uk/ols4/ontologies/cl)

<a id="endpoint"></a>
### Endpoint
A specific API address that accepts a defined request and returns a defined
type of data. [Learn more about API paths and
endpoints.](https://swagger.io/docs/specification/v3_0/paths-and-operations/)

<a id="eve"></a>
### EVE
Evolutionary model of Variant Effect. EVE uses patterns in protein sequence
evolution to predict the effect of an amino acid substitution. ProtVar
reports an EVE score and prediction category when they are available. [Learn
more about EVE.](https://pubmed.ncbi.nlm.nih.gov/34707284/)

<a id="foldx"></a>
### FoldX
Software that uses an empirical energy function to estimate how a sequence
change may affect protein stability or interactions. ProtVar reports a FoldX
stability change for the selected *TNNT2* missense variant. [Learn more about
FoldX.](https://pubmed.ncbi.nlm.nih.gov/12079393/)

## G to M

<a id="gene-symbol"></a>
### Gene symbol
A standardized short name for a gene, such as *TTN*. Symbols are useful for
joining resources, but identifier changes and aliases can cause failed or
incorrect matches. [Learn more about human gene-naming
guidelines.](https://www.genenames.org/about/guidelines/)

<a id="graphql"></a>
### GraphQL
An API query language in which a request specifies the fields that should be
returned. The Pharos activities use GraphQL to retrieve selected target
information. [Learn more about GraphQL.](https://graphql.org/learn/)

<a id="gtex"></a>
### GTEx
The Genotype-Tissue Expression project. This module uses GTEx data to ask
whether a candidate gene is expressed in disease-relevant bulk tissues.
[Learn more about GTEx.](https://commonfund.nih.gov/gtex)

<a id="hgvs"></a>
### HGVS
Human Genome Variation Society sequence-variant nomenclature. HGVS
expressions describe a variant relative to a named reference sequence and
should be interpreted together with that sequence accession and version.
[Learn more about HGVS nomenclature.](https://hgvs-nomenclature.org/stable/)

<a id="hgvsc"></a>
### HGVSc (`hgvs_c`)
An HGVS description at the coding-DNA level. It usually reports the position
and nucleotide change relative to a specific transcript, so the transcript
accession is essential for interpreting the value. [Review HGVS syntax and
examples.](https://hgvs-nomenclature.org/stable/recommendations/summary/)

<a id="hgvsp"></a>
### HGVSp (`hgvs_p`)
An HGVS description of an observed or predicted protein-level consequence.
Parentheses commonly indicate that the protein consequence is predicted
rather than experimentally demonstrated. [Review HGVS syntax and
examples.](https://hgvs-nomenclature.org/stable/recommendations/summary/)

<a id="hubmap"></a>
### HuBMAP
The Human BioMolecular Atlas Program. This module uses HuBMAP cell data to
add cell-type-resolution context and identify potential cellular systems for
follow-up study. [Learn more about HuBMAP.](https://hubmapconsortium.org/)

<a id="idg"></a>
### IDG
Illuminating the Druggable Genome, a program that develops and organizes
knowledge about human proteins, especially proteins that remain
understudied. [Learn more about IDG.](https://commonfund.nih.gov/idg)

<a id="json"></a>
### JSON
A structured text format commonly returned by APIs. JSON stores information
as objects and arrays that analysis code can convert into tables. [Learn more
about JSON.](https://www.json.org/json-en.html)

<a id="many-to-one-join"></a>
### Many-to-one join
A table operation in which many variant rows can match one gene-level context
row. This preserves every original variant while attaching the same
gene-level evidence where appropriate. [Learn more about validating joins in
pandas.](https://pandas.pydata.org/docs/user_guide/merging.html#merge-key-uniqueness)

<a id="median-tpm"></a>
### Median TPM
The median transcripts-per-million expression value across samples in a
group. It summarizes relative transcript abundance within a tissue but is
not a direct measure of protein abundance. [Learn more in the GTEx Portal
documentation.](https://gtexportal.org/home/documentationPage)

<a id="missense-variant"></a>
### Missense variant
A sequence variant that changes a codon so that one amino acid is replaced by
another in the resulting protein. [Learn more about missense variants from
NHGRI.](https://www.genome.gov/genetics-glossary/Missense-Mutation)

## N to Z

<a id="normalized-expression"></a>
### Normalized expression
An expression value adjusted to make measurements more comparable within the
rules of a particular dataset. Values from different resources should not be
assumed to share the same scale or normalization method. [Learn more in the
GTEx Portal documentation.](https://gtexportal.org/home/documentationPage)

<a id="pathogenic-likely-pathogenic"></a>
### Pathogenic or likely pathogenic (P/LP)
Clinical classification categories indicating different strengths of
evidence that a variant contributes to disease. These labels describe the
prior evaluation and are not reassigned by this module. [Learn more about the
ACMG/AMP standards.](https://pubmed.ncbi.nlm.nih.gov/25741868/)

<a id="percent-detected"></a>
### Percent detected
The percentage of cells in a group in which a transcript was detected. It
provides a different view from average expression and depends on the
dataset's assay and processing choices. [Learn more about HuBMAP
APIs.](https://docs.hubmapconsortium.org/apis.html)

<a id="pharos"></a>
### Pharos
A knowledge portal and API for exploring protein targets, diseases, ligands,
and Target Development Levels. This module uses Pharos to determine what
kinds of follow-up tools or knowledge may already exist for a gene product.
[Explore Pharos.](https://pharos.nih.gov/)

<a id="plddt"></a>
### pLDDT
Predicted local distance difference test. AlphaFold assigns this confidence
score from 0 to 100 to each residue in a predicted protein structure. It
describes confidence in the local structural model, while variant-effect
predictions address the amino acid substitution. [Learn more about pLDDT in
the AlphaFold documentation.](https://alphafold.ebi.ac.uk/faq)

<a id="protvar"></a>
### ProtVar
An EMBL-EBI resource that maps human missense variants between genomic,
coding-DNA, and protein coordinates. It brings together functional,
population, structural, and variant-effect information for the mapped
protein position. [Learn more about
ProtVar.](https://pubmed.ncbi.nlm.nih.gov/38769064/)

<a id="reference-sequence"></a>
### Reference sequence
The accessioned DNA, RNA, or protein sequence against which a variant is
described. An HGVS expression can change when a different transcript or
sequence version is selected. [Learn more about NCBI
RefSeq.](https://www.ncbi.nlm.nih.gov/refseq/about/)

<a id="rest-api"></a>
### REST API
An API style that usually represents data as web resources addressed by URLs
and standard HTTP methods. The GTEx, HuBMAP, and ProtVar activities use REST
requests. [Learn more about
REST.](https://developer.mozilla.org/en-US/docs/Glossary/REST)

<a id="tdl"></a>
### Target Development Level (TDL)
An IDG classification of how well a protein target has been studied and what
types of tools or knowledge are available. TDL helps establish an appropriate
research next step. It does not measure disease relevance. [Learn more about
TDLs in Pharos.](https://pharos.nih.gov/)

<a id="tbio"></a>
### Tbio
A TDL for targets with substantial biological or disease-related knowledge
that do not meet the criteria for `Tclin` or `Tchem`. These targets may need
focused mechanistic or functional follow-up. [Learn more about TDLs in
Pharos.](https://pharos.nih.gov/)

<a id="tchem"></a>
### Tchem
A TDL for targets with sufficiently potent small-molecule activities that
meet IDG criteria. These targets may have chemical tools suitable for
experimental investigation. [Learn more about TDLs in
Pharos.](https://pharos.nih.gov/)

<a id="tclin"></a>
### Tclin
A TDL for targets associated with an approved drug and a known mechanism of
action. This can identify established pharmacological mechanisms to examine,
but it does not make a drug appropriate for a specific variant or patient.
[Learn more about TDLs in Pharos.](https://pharos.nih.gov/)

<a id="tdark"></a>
### Tdark
A TDL for understudied targets that meet IDG inclusion criteria but have
limited characterized biology or chemical tools. These targets may require
foundational characterization before targeted experiments are possible.
[Learn more about TDLs in Pharos.](https://pharos.nih.gov/)

<a id="transcript-accession"></a>
### Transcript accession
A stable identifier for a particular transcript sequence. Transcript choice
affects coding positions and protein consequences, so it must accompany an
HGVSc or HGVSp value. [Learn more about NCBI
RefSeq.](https://www.ncbi.nlm.nih.gov/refseq/about/)

<a id="uniprot-accession"></a>
### UniProt accession
A stable alphanumeric identifier assigned to a protein entry in UniProtKB.
For example, P45379 identifies human cardiac troponin T. Pharos and ProtVar
use UniProt accessions to refer to protein records. [Learn more about UniProt
accession numbers.](https://www.uniprot.org/help/accession_numbers)

<a id="vus"></a>
### Variant of uncertain significance (VUS)
A variant for which available evidence is insufficient or conflicting for a
pathogenic or benign classification. Biological context can guide research
prioritization, but it does not by itself resolve a VUS. [Learn more about
the ACMG/AMP standards.](https://pubmed.ncbi.nlm.nih.gov/25741868/)
