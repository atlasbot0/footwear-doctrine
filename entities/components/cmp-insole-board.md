---
id: cmp-insole-board
type: component
names: [insole board, lasting board]
aliases: {UK: insole, factory: lasting insole}
domain: D9-bottom-stack
definition: The structural board the upper is lasted over and the sole is built against — the foundation of a board-lasted shoe. Not the removable footbed.
function: Lasting substrate, torsional platform, stitch/tack anchor.
position: Directly under the foot, above midsole/outsole, hidden by the sockliner.
materials: [mat-leatherboard, mat-cork]
key_parameters:
  - {name: thickness, unit: mm, typical: "1.5–2.5 cellulose board; up to ~3 for welted", confidence: medium, source: model-knowledge}
  - {name: stitch/tack holding, unit: test, typical: "assessed per insole stitch-tear methods (ISO 20876 family)", confidence: medium, source: iso-tc216}
processes: [prc-lasting]
tested_by: [std-iso-insole-family]
failure_modes: [cracking at flex line, moisture swelling, delamination of ribs]
cost_drivers: [board grade, shank fitting, rib attachment for welted work]
relationships: {part_of: [bottom stack], works_with: [cmp-shank, cmp-gemming-rib], distinct_from: [cmp-sockliner, cmp-strobel-board]}
sources: [texon-lib, golding-1902, motawi-hsam]
confidence: medium
status: seed
---
Cellulose fibreboards (Texon/Bontex class) dominate. In Goodyear work the insole carries the rib (gemming or channelled leather) that the welt seam anchors to — the single most debated durability detail in welted construction.
