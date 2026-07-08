// Preview script for the QSpad theme
// Comments, keywords, strings, numbers, and functions should all
// read as the same flat color against the ivory background.

const THRESHOLD: f64 = 0.05;

struct GeneResult {
    gene: String,
    p_value: f64,
}

impl GeneResult {
    fn significant(&self) -> bool {
        self.p_value < THRESHOLD
    }
}

fn load_expression_data() -> Vec<GeneResult> {
    vec![
        GeneResult { gene: "ATP6V0A1".to_string(), p_value: 0.001 },
        GeneResult { gene: "BRCA1".to_string(), p_value: 0.08 },
        GeneResult { gene: "TP53".to_string(), p_value: 0.042 },
    ]
}

fn summarize(results: &[GeneResult]) {
    for r in results {
        let status = if r.significant() { "significant" } else { "not significant" };
        println!("{}: p = {:.3} ({})", r.gene, r.p_value, status);
    }
}

fn main() {
    let results = load_expression_data();
    summarize(&results);
}
