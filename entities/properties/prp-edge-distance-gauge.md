---
id: prp-edge-distance-gauge
type: property
names: [edge distance, stitch margin]
aliases: {twin-needle: gauge (needle spacing)}
domain: D11-closing
definition: Distance from material edge to first stitch row, and between rows (gauge) — the visual rhythm and tear-resistance geometry of the upper.
key_parameters:
  - {name: anchors, unit: mm, typical: "first row 1.5–2.0 from edge typical; overlays ~3 observed (1906R); twin gauges 1/8″–1/4″ (3.2–6.4)", confidence: high, source: nb-1906r-sheet}
tested_by: [std-satra-seam-family]
relationships: {pairs_with: [prp-spi-stitch-density], failure_link: "too tight to edge = tear-out; uneven margin = the cheapness tell"}
sources: [nb-1906r-sheet, model-knowledge]
confidence: high
status: seed
---
Quality perception is mostly parallel lines at consistent margins. Now it's a number.
