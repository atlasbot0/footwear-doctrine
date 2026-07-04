---
id: cmp-sockliner
type: component
names: [sockliner, inner sock, footbed]
aliases: {consumer: insole, UK: sock, factory: sockliner}
domain: D9-bottom-stack
definition: The removable (or glued-in) comfort layer directly under the foot, usually foam with a top cloth.
function: Step-in comfort, moisture handling, fit tuning, print real estate (size/brand).
position: On top of the insole/strobel board.
materials: [mat-eva, mat-pu-foam, mat-latex-foam, mat-cork]
key_parameters:
  - {name: forefoot thickness, unit: mm, typical: "3–5 die-cut EVA; 4–8 moulded PU", confidence: medium, source: model-knowledge}
  - {name: foam density, unit: "kg/m³", typical: "OrthoLite-class open-cell PU ~160–250", confidence: low, source: model-knowledge}
processes: [prc-lasting]
tested_by: [std-satra-cushion-family]
failure_modes: [compression set (packs out), top-cloth delamination, odour retention]
cost_drivers: [die-cut vs moulded, branded foams, top-cloth spec]
relationships: {sits_on: [cmp-insole-board, cmp-strobel-board], brand_examples: [brd-ortholite]}
sources: [ortholite-lib, motawi-hsam]
confidence: medium
status: seed
---
Die-cut EVA is the value option; moulded PU (often branded) resists compression set and carries comfort marketing. Contoured footbeds shade into orthotic territory — different discipline, same slot.
