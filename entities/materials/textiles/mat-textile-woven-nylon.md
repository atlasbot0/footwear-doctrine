---
id: mat-textile-woven-nylon
type: material
names: [woven nylon, nylon oxford/taffeta]
aliases: {weights: [70D taffeta, 210D oxford, 420D pack cloth]}
domain: D5-upper-materials
definition: Plain-woven nylon in graded deniers — the runner-heritage upper fabric (waffle-era) and quarter-panel staple.
key_parameters:
  - {name: denier ladder, unit: D, typical: "70/210/420 conventions; higher = heavier + tougher", confidence: high, source: model-knowledge}
tested_by: [std-satra-upper-family]
failure_modes: [fray at raw edges, UV fade, abrasion at eyestay]
cost_drivers: [denier, dope-dyed vs piece-dyed, recycled nylon]
relationships: {reinforced_by: [suede/synthetic overlays], premium_class: [brd-cordura]}
sources: [motawi-smdg, cordura-lib]
confidence: medium
status: seed
---
The retro-runner recipe is nylon body + suede structure; the denier number is the shorthand spec.
