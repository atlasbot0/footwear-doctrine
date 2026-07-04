---
id: prp-shore-hardness
type: property
names: [Shore hardness, durometer]
aliases: {scales: [Shore A (rubbers/TPU), Shore D (rigid), Asker C (foams — JIS sibling)]}
domain: D15-testing-compliance
definition: Indentation hardness on lettered scales — the one-number feel/performance proxy quoted on every sole and foam spec.
key_parameters:
  - {name: anchor values, unit: n/a, typical: "outsole rubber 55–75 A (1906R carbon rubber 85–90 A); TPU cage 85 A (1906R); EVA midsole 45–60 Asker C", confidence: high, source: nb-1906r-sheet}
  - {name: caution, unit: n/a, typical: "Asker C ≠ Shore A; never compare across scales; state scale + material + temp", confidence: high, source: model-knowledge}
  - {name: house benchmarks, unit: mixed, typical: "outsole common band 70–80 A (vs 1906R hard-wear 85–90); cushion foams 45–55 Shore C", confidence: medium, source: vince-spec-guidance}
tested_by: [durometer per ASTM D2240 class]
relationships: {appears_on: [cmp-outsole, cmp-midsole, mat-tpu], spec_rule: "hardness + density + abrasion travel together"}
sources: [nb-1906r-sheet, model-knowledge, vince-spec-guidance]
confidence: high
status: seed
---
The most quoted, most mis-compared number in footwear. Scale discipline is the doctrine.
