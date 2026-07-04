---
id: prp-abrasion-din
type: property
names: [DIN abrasion, rotary drum abrasion]
domain: D15-testing-compliance
definition: Volume loss (mm³) of soling on the ISO 4649 / DIN 53516 rotary drum — the standard outsole wear number.
key_parameters:
  - {name: benchmarks, unit: "mm³", typical: "<100 premium; <150 good; safety norms cap by class (e.g. ≤250 in EN ISO 20345 contexts)", confidence: medium, source: model-knowledge}
  - {name: house benchmark, unit: "mm³", typical: "≤150 QC threshold — first-party corroboration of the <150 band", confidence: medium, source: vince-spec-template}
tested_by: [std-iso-4649]
relationships: {appears_on: [cmp-outsole line items], trades_with: [grip, weight]}
sources: [satra-catalogue, model-knowledge, vince-spec-template]
confidence: medium
status: seed
---
Lower is longer-lasting; pair it with hardness or the number lies.
