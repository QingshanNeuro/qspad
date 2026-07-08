# Preview script for the QSpad theme
# Comments, keywords, strings, numbers, and functions should all
# read as the same flat color against the ivory background.

import csv
from dataclasses import dataclass

THRESHOLD = 0.05
SAMPLE_SIZE = 42


@dataclass
class GeneResult:
    gene: str
    p_value: float

    @property
    def significant(self) -> bool:
        return self.p_value < THRESHOLD


def load_expression_data(path: str, min_reads: int = 10) -> list[dict]:
    with open(path) as handle:
        rows = csv.DictReader(handle)
        return [row for row in rows if int(row["reads"]) >= min_reads]


def summarize(results: list[GeneResult]) -> None:
    for r in results:
        status = "significant" if r.significant else "not significant"
        print(f"{r.gene}: p = {r.p_value:.3f} ({status})")


if __name__ == "__main__":
    results = [
        GeneResult("ATP6V0A1", 0.001),
        GeneResult("BRCA1", 0.08),
        GeneResult("TP53", 0.042),
    ]
    summarize(results)
