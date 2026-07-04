---
id: prp-martindale
type: property
names: [Martindale abrasion]
domain: D15-testing-compliance
definition: Oscillating-rub cycles to failure for textiles/linings — the upper-and-lining wear number (soling uses DIN drum instead).
key_parameters:
  - {name: class values, unit: cycles, typical: "linings specced in the tens of thousands; heel-pocket zones highest", confidence: low, source: model-knowledge}
tested_by: [std-satra-lining-abrasion-family]
relationships: {appears_on: [cmp-lining, mat-textile-* line items]}
sources: [satra-catalogue, model-knowledge]
confidence: low
status: seed
---
The lining's lifespan in one number; calibrate house minimums in P3 from SATRA guidance.
