---
id: mat-textile-open-mesh
type: material
names: [open mesh]
aliases: {variants: [hex mesh, engineered mesh, double-layer mesh]}
domain: D5-upper-materials
definition: Warp-knitted polyester mesh with visible open cells — the breathability workhorse of athletic uppers.
key_parameters:
  - {name: cell size, unit: mm, typical: "~3 mm hex openings observed (1906R); 1–5 typical", confidence: high, source: nb-1906r-sheet}
  - {name: build, unit: n/a, typical: "usually laminated: mesh face + foam + tricot backer, or double-jacquard self-spaced", confidence: medium, source: model-knowledge}
tested_by: [std-satra-upper-family]
failure_modes: [snag/tear at flex creases, foam laminate delamination, dirt entrapment]
cost_drivers: [jacquard patterning, lamination passes]
relationships: {sibling: [mat-textile-spacer-mesh], observed_on: [nb-1906r-sheet]}
sources: [nb-1906r-sheet, motawi-smdg]
confidence: high
status: seed
---
Spec face yarn, cell geometry, laminate stack and backer — "mesh" alone is not a spec.
