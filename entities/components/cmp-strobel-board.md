---
id: cmp-strobel-board
type: component
names: [strobel board, strobel sock]
aliases: {factory: strobel, alt: sock bottom}
domain: D9-bottom-stack
definition: Flexible textile/non-woven bottom stitched to the upper's lasting margin (Strobel stitch) to close it into a sock before force lasting.
function: Closes the upper for force lasting; gives a soft, flexible underfoot platform.
position: Sewn to the upper perimeter; sits on the midsole.
materials: [mat-textile-woven-nylon]
key_parameters:
  - {name: seam, unit: stitch, typical: "Strobel-class overseam around full perimeter (observed 1906R: stitched perimeter, strobel lasting)", confidence: high, source: nb-1906r-sheet}
processes: [prc-lasting]
tested_by: [std-satra-seam-family]
failure_modes: [seam burst at flex, board tear at toe]
cost_drivers: [board grade, seam operation time]
relationships: {part_of: [upper assembly], enables: [con-strobel-force-lasted], distinct_from: [cmp-insole-board]}
sources: [nb-1906r-sheet, motawi-hsam]
confidence: high
status: seed
---
The default athletic platform: lighter and more flexible than board lasting, and it lets the midsole do the structural work.
