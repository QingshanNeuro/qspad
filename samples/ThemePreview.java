// Preview script for the QSpad theme
// Comments, keywords, strings, numbers, and functions should all
// read as the same flat color against the ivory background.

import java.util.List;

public class ThemePreview {
    private static final double THRESHOLD = 0.05;

    record GeneResult(String gene, double pValue) {
        boolean significant() {
            return pValue < THRESHOLD;
        }
    }

    static List<GeneResult> loadExpressionData() {
        return List.of(
            new GeneResult("ATP6V0A1", 0.001),
            new GeneResult("BRCA1", 0.08),
            new GeneResult("TP53", 0.042)
        );
    }

    static void summarize(List<GeneResult> results) {
        for (GeneResult r : results) {
            String status = r.significant() ? "significant" : "not significant";
            System.out.printf("%s: p = %.3f (%s)%n", r.gene(), r.pValue(), status);
        }
    }

    public static void main(String[] args) {
        summarize(loadExpressionData());
    }
}
