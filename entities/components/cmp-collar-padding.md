---
id: cmp-collar-padding
type: component
names: [collar padding, collar foam]
aliases: {factory: collar sponge, region: Achilles pillow (rear lobe)}
domain: D7-padding
definition: Foam ring around the topline gripping the ankle and cushioning the Achilles.
function: Heel hold, topline comfort, perceived plushness at try-on.
position: Inside the collar between upper and lining, heaviest at the Achilles.
materials: [mat-pu-foam, mat-eva, mat-latex-foam]
key_parameters:
  - {name: thickness, unit: mm, typical: "15 at Achilles / 8 at sides observed (1906R); 6–15 typical range", confidence: high, source: nb-1906r-sheet}
  - {name: density, unit: "kg/m³", typical: "~30 observed (1906R); 25–40 typical open-cell PU", confidence: high, source: nb-1906r-sheet}
  - {name: house benchmark, unit: mixed, typical: "Achilles 10–15 mm ~30 kg/m³ Shore C ~35; sides 8–10 mm ~28 kg/m³ — Vince template, corroborates 1906R", confidence: medium, source: vince-spec-guidance}
tested_by: [std-satra-cushion-family]
failure_modes: [compression set, foam crumble with age, lining wear-through at Achilles]
cost_drivers: [foam grade, memory foams, quilting operations]
relationships: {part_of: [collar assembly], pairs_with: [cmp-lining]}
sources: [nb-1906r-sheet, vince-spec-guidance]
confidence: high
status: seed
---
The try-on moment lives here. Density × thickness is the spec; the 1906R's 15/8 mm split at 30 kg/m³ is a textbook lifestyle-runner recipe.
