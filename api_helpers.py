"""Live API requests used by the Quarto lessons and Jupyter notebooks."""

from datetime import date

import pandas as pd
import requests

GTEX_GENE_URL = "https://gtexportal.org/api/v2/reference/gene"
GTEX_EXPRESSION_URL = (
    "https://gtexportal.org/api/v2/expression/medianGeneExpression"
)
HUBMAP_CELLS_URL = "https://cells.api.hubmapconsortium.org/api/"
PHAROS_GRAPHQL_URL = "https://pharos-api.ncats.io/graphql"

HEART_TISSUES = {
    "Heart_Atrial_Appendage": "Heart - Atrial Appendage",
    "Heart_Left_Ventricle": "Heart - Left Ventricle",
}
VENTRICULAR_CELL_TYPE_ID = "CL:0002131"
VENTRICULAR_CELL_TYPE_LABEL = "regular ventricular cardiac myocyte"

PHAROS_TARGET_QUERY = """
query TargetContext($symbol: String!) {
  target(q: {sym: $symbol}) {
    sym
    name
    uniprot
    tdl
    publicationCount
    ligandCounts { name value }
    ppiCounts { name value }
  }
}
"""


def fetch_gtex_context(
    gene_symbols: list[str],
    timeout_seconds: int = 60,
) -> pd.DataFrame:
    """Return GTEx v10 median expression for two heart tissues."""
    gene_response = requests.get(
        GTEX_GENE_URL,
        params={
            "geneId": gene_symbols,
            "gencodeVersion": "v39",
            "genomeBuild": "GRCh38/hg38",
            "itemsPerPage": 100,
        },
        timeout=timeout_seconds,
    )
    gene_response.raise_for_status()
    gene_records = gene_response.json()["data"]
    gencode_ids = [record["gencodeId"] for record in gene_records]

    expression_response = requests.get(
        GTEX_EXPRESSION_URL,
        params={
            "gencodeId": gencode_ids,
            "datasetId": "gtex_v10",
            "tissueSiteDetailId": list(HEART_TISSUES),
            "itemsPerPage": 100,
        },
        timeout=timeout_seconds,
    )
    expression_response.raise_for_status()

    expression = (
        pd.DataFrame(expression_response.json()["data"])
        .rename(
            columns={
                "geneSymbol": "gene_symbol",
                "gencodeId": "gencode_id",
                "tissueSiteDetailId": "tissue_id",
                "ontologyId": "ontology_id",
                "median": "median_tpm",
                "datasetId": "dataset_id",
            }
        )
        .copy()
    )
    expression.loc[:, "tissue_name"] = expression["tissue_id"].map(
        HEART_TISSUES
    )
    expression.loc[:, "retrieved_date"] = date.today().isoformat()
    return (
        expression.loc[
            :,
            [
                "gene_symbol",
                "gencode_id",
                "tissue_id",
                "tissue_name",
                "ontology_id",
                "median_tpm",
                "dataset_id",
                "retrieved_date",
            ],
        ]
        .sort_values(["gene_symbol", "tissue_id"])
        .reset_index(drop=True)
    )


def _post_hubmap(
    path: str,
    form_data: dict[str, object] | list[tuple[str, object]],
    timeout_seconds: int,
) -> list[dict[str, object]]:
    """Post one Cells API form and return its result records."""
    response = requests.post(
        f"{HUBMAP_CELLS_URL}{path}",
        data=form_data,
        timeout=timeout_seconds,
    )
    response.raise_for_status()
    payload = response.json()
    if "results" not in payload:
        raise LookupError(payload.get("error", "Cells API returned no results"))
    return payload["results"]


def _create_cell_handle(
    input_type: str,
    input_values: list[str],
    timeout_seconds: int,
) -> str:
    form_data: list[tuple[str, object]] = [("input_type", input_type)]
    form_data.extend(("input_set", value) for value in input_values)
    results = _post_hubmap("cell/", form_data, timeout_seconds)
    return str(results[0]["query_handle"])


def _intersect_cell_handles(
    first_handle: str,
    second_handle: str,
    timeout_seconds: int,
) -> str:
    results = _post_hubmap(
        "intersection/",
        {
            "key_one": first_handle,
            "key_two": second_handle,
            "set_type": "cell",
        },
        timeout_seconds,
    )
    return str(results[0]["query_handle"])


def _count_cells(query_handle: str, timeout_seconds: int) -> int:
    results = _post_hubmap(
        "count/",
        {"key": query_handle, "set_type": "cell"},
        timeout_seconds,
    )
    return int(results[0]["count"])


def _fetch_hubmap_gene_values(
    query_handle: str,
    gene_symbol: str,
    sample_size: int,
    timeout_seconds: int,
) -> list[dict[str, object]]:
    form_data: list[tuple[str, object]] = [
        ("key", query_handle),
        ("set_type", "cell"),
        ("limit", sample_size),
        ("offset", 0),
        ("values_included", gene_symbol),
    ]
    return _post_hubmap("celldetailevaluation/", form_data, timeout_seconds)


def fetch_hubmap_ventricular_context(
    gene_symbols: list[str],
    sample_size: int = 500,
    timeout_seconds: int = 60,
) -> pd.DataFrame:
    """Summarize indexed expression in ventricular cardiac myocytes."""
    heart_handle = _create_cell_handle("organ", ["Heart"], timeout_seconds)
    cell_type_handle = _create_cell_handle(
        "celltype",
        [VENTRICULAR_CELL_TYPE_ID],
        timeout_seconds,
    )
    query_handle = _intersect_cell_handles(
        heart_handle,
        cell_type_handle,
        timeout_seconds,
    )
    total_matching_cells = _count_cells(query_handle, timeout_seconds)

    summary_records: list[dict[str, object]] = []
    for gene_symbol in gene_symbols:
        try:
            cell_records = _fetch_hubmap_gene_values(
                query_handle,
                gene_symbol,
                sample_size,
                timeout_seconds,
            )
        except LookupError:
            summary_records.append(
                {
                    "gene_symbol": gene_symbol,
                    "cell_type_id": VENTRICULAR_CELL_TYPE_ID,
                    "cell_type_label": VENTRICULAR_CELL_TYPE_LABEL,
                    "total_matching_cells": total_matching_cells,
                    "sampled_cells": 0,
                    "mean_normalized_expression": float("nan"),
                    "percent_detected": float("nan"),
                    "dataset_uuids": "",
                    "availability": "not_available_in_cells_api_index",
                    "retrieved_date": date.today().isoformat(),
                }
            )
            continue

        values = pd.Series(
            [record["values"][gene_symbol] for record in cell_records],
            dtype="float64",
        )
        dataset_uuids = sorted(
            {str(record["dataset"]) for record in cell_records}
        )
        summary_records.append(
            {
                "gene_symbol": gene_symbol,
                "cell_type_id": VENTRICULAR_CELL_TYPE_ID,
                "cell_type_label": VENTRICULAR_CELL_TYPE_LABEL,
                "total_matching_cells": total_matching_cells,
                "sampled_cells": len(values),
                "mean_normalized_expression": values.mean(),
                "percent_detected": values.gt(0).mean() * 100,
                "dataset_uuids": ";".join(dataset_uuids),
                "availability": "available",
                "retrieved_date": date.today().isoformat(),
            }
        )

    return pd.DataFrame(summary_records).sort_values("gene_symbol").reset_index(
        drop=True
    )


def _named_count(counts: list[dict[str, object]], name: str) -> int:
    """Return a named Pharos count or zero when that count is absent."""
    values = {str(item["name"]): int(item["value"]) for item in counts}
    return values.get(name, 0)


def fetch_pharos_context(
    gene_symbols: list[str],
    timeout_seconds: int = 60,
) -> pd.DataFrame:
    """Return selected Pharos target fields for explicit gene symbols."""
    target_records: list[dict[str, object]] = []
    for gene_symbol in gene_symbols:
        response = requests.post(
            PHAROS_GRAPHQL_URL,
            json={
                "query": PHAROS_TARGET_QUERY,
                "variables": {"symbol": gene_symbol},
            },
            timeout=timeout_seconds,
        )
        response.raise_for_status()
        payload = response.json()
        if payload.get("errors"):
            raise RuntimeError(payload["errors"])
        target = payload["data"]["target"]
        if target is None:
            raise LookupError(f"Pharos returned no target for {gene_symbol}")

        target_records.append(
            {
                "gene_symbol": target["sym"],
                "target_name": target["name"],
                "uniprot_id": target["uniprot"],
                "tdl": target["tdl"],
                "publication_count": target["publicationCount"],
                "ligand_count": _named_count(target["ligandCounts"], "ligand"),
                "drug_count": _named_count(target["ligandCounts"], "drug"),
                "ppi_count": _named_count(target["ppiCounts"], "Total"),
                "retrieved_date": date.today().isoformat(),
            }
        )

    return pd.DataFrame(target_records).sort_values("gene_symbol").reset_index(
        drop=True
    )
