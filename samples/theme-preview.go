// Preview script for the QSpad theme
// Comments, keywords, strings, numbers, and functions should all
// read as the same flat color against the ivory background.

package main

import (
	"fmt"
)

const threshold = 0.05

type geneResult struct {
	gene    string
	pValue  float64
}

func (r geneResult) significant() bool {
	return r.pValue < threshold
}

func loadExpressionData(path string, minReads int) ([]geneResult, error) {
	results := []geneResult{
		{"ATP6V0A1", 0.001},
		{"BRCA1", 0.08},
		{"TP53", 0.042},
	}
	return results, nil
}

func summarize(results []geneResult) {
	for _, r := range results {
		status := "not significant"
		if r.significant() {
			status = "significant"
		}
		fmt.Printf("%s: p = %.3f (%s)\n", r.gene, r.pValue, status)
	}
}

func main() {
	results, err := loadExpressionData("./data", 10)
	if err != nil {
		panic(err)
	}
	summarize(results)
}
