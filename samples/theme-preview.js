// Preview script for the QSpad theme
// Comments, keywords, strings, numbers, and functions should all
// read as the same flat color against the ivory background.

const THRESHOLD = 0.05;
const SAMPLE_SIZE = 42;

class GeneResult {
  constructor(gene, pValue) {
    this.gene = gene;
    this.pValue = pValue;
  }

  get significant() {
    return this.pValue < THRESHOLD;
  }
}

async function loadExpressionData(path, minReads = 10) {
  const raw = await fetch(path).then((res) => res.json());
  return raw.filter((row) => row.reads >= minReads);
}

function summarize(results) {
  for (const r of results) {
    const status = r.significant ? "significant" : "not significant";
    console.log(`${r.gene}: p = ${r.pValue.toFixed(3)} (${status})`);
  }
}

const results = [
  new GeneResult("ATP6V0A1", 0.001),
  new GeneResult("BRCA1", 0.08),
  new GeneResult("TP53", 0.042),
];

summarize(results);
