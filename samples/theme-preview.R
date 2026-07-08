# Preview script for the dyslexia-friendly VSCode theme
# Comments, keywords, strings, numbers, and functions should all
# read as muted, low-contrast greens against the ivory background.

library(dplyr)

sample_size <- 42L
threshold   <- 0.05

load_expression_data <- function(path, min_reads = 10) {
  raw <- read.csv(path, stringsAsFactors = FALSE)
  filtered <- raw[raw$reads >= min_reads, ]
  return(filtered)
}

is_significant <- function(p_value) {
  if (p_value < threshold) {
    TRUE
  } else {
    FALSE
  }
}

genes <- c("ATP6V0A1", "BRCA1", "TP53")

results <- data.frame(
  gene    = genes,
  p_value = c(0.001, 0.08, 0.042),
  stringsAsFactors = FALSE
)

results$significant <- sapply(results$p_value, is_significant)

for (i in seq_len(nrow(results))) {
  cat(sprintf("%s: p = %.3f (%s)\n",
              results$gene[i],
              results$p_value[i],
              ifelse(results$significant[i], "significant", "not significant")))
}
