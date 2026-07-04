---
id: cmp-shank
type: component
names: [shank]
aliases: {athletic: [stability frame, torsion bar, stability web], safety: puncture midsole plate}
domain: D8-reinforcement
definition: Stiffener bridging the waist between heel and ball, controlling torsion and preventing waist collapse.
function: Waist support, torsional rigidity, heel-lever integrity (critical under heels).
position: In the waist, between insole board and midsole/outsole.
materials: [mat-tpu, mat-leatherboard]
key_parameters:
  - {name: steel shank stiffness, unit: test, typical: "characterised per ISO 18896 for women's heeled footwear", confidence: medium, source: iso-tc216}
  - {name: length, unit: mm, typical: "spans ~heel breast to behind ball; last-bottom governed", confidence: medium, source: model-knowledge}
  - {name: carbon plate, unit: mm, typical: "1–3 embedded in racing midsoles; absent from lifestyle (574/990-class), present FuelCell-class", confidence: medium, source: vince-spec-guidance}
processes: [prc-lasting]
tested_by: [std-iso-shank-family]
failure_modes: [shank shift/click, fatigue fracture (steel), waist collapse if omitted]
cost_drivers: [steel vs nylon/fibreglass vs moulded TPU web vs carbon plate]
relationships: {works_with: [cmp-insole-board], athletic_form: "TPU midfoot web (observed 1906R)", extends_to: [carbon plates in racing stacks]}
sources: [nb-1906r-sheet, iso-tc216, golding-1902, vince-spec-guidance]
confidence: medium
status: seed
---
Dress and heeled footwear cannot skip it; athletic product re-invents it as moulded TPU webs, torsion systems and full-length plates. "Stability frame" language in briefs maps here.
