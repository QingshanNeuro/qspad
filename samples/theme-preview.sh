#!/usr/bin/env bash
# Preview script for the QSpad theme
# Comments, keywords, strings, numbers, and variables should all
# read as the same flat color against the ivory background.

set -euo pipefail

THRESHOLD=0.05
INPUT_DIR="${1:-./data}"

load_expression_data() {
  local path="$1"
  local min_reads="${2:-10}"
  awk -F',' -v min="$min_reads" 'NR > 1 && $3 >= min { print }' "$path"
}

is_significant() {
  local p_value="$1"
  awk -v p="$p_value" -v t="$THRESHOLD" 'BEGIN { exit !(p < t) }'
}

for file in "$INPUT_DIR"/*.csv; do
  gene=$(basename "$file" .csv)
  rows=$(load_expression_data "$file" 10)
  echo "processed $gene: $(echo "$rows" | wc -l) rows"
done

echo "done"
