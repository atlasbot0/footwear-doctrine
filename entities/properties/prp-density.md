---
id: prp-density
type: property
names: [density]
aliases: {foam-trade: [kg/m³ (padding), g/cm³ (soling)]}
domain: D15-testing-compliance
definition: Mass per volume — the weight/cushion/durability lever on every foam and soling line item.
key_parameters:
  - {name: anchors, unit: mixed, typical: "collar PU ~30 kg/m³ (1906R); CM EVA 0.18–0.25 g/cm³; PU soling 0.35–0.55; PEBA ~0.1", confidence: medium, source: nb-1906r-sheet}
relationships: {trades_with: [prp-shore-hardness, durability], appears_on: [cmp-midsole, cmp-collar-padding]}
sources: [nb-1906r-sheet, model-knowledge]
confidence: medium
status: seed
---
Weight is a spec line, and this is where it hides.
