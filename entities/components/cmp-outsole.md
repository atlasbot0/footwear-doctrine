---
id: cmp-outsole
type: component
names: [outsole]
aliases: {UK: sole, IT: suola, factory: bottom}
domain: D9-bottom-stack
definition: The ground-contact layer delivering traction, abrasion resistance and flex behaviour.
function: Traction, wear, flex control, protection; carries lug geometry, siping, flex grooves.
position: Ground side of the stack; cupsole, sheet, or unit sole formats.
materials: [mat-rubber-carbon, mat-rubber-blown, mat-rubber-gum, mat-tr, mat-tpu, mat-pu-foam, mat-eva, mat-leather-sole, mat-rubber-crepe]
key_parameters:
  - {name: hardness, unit: Shore A, typical: "55–75 general; 85–90 observed on 1906R NDurance carbon rubber", confidence: high, source: nb-1906r-sheet}
  - {name: abrasion, unit: "mm³ (ISO 4649)", typical: "premium <100; good <150", confidence: medium, source: model-knowledge}
  - {name: thickness, unit: mm, typical: "sheet 3.5–6; lugged units 8–15+ incl. lugs", confidence: medium, source: model-knowledge}
processes: [prc-halogenation-priming]
tested_by: [std-satra-tm144, std-iso-4649, std-iso-17707]
failure_modes: [wear-through at heel strike, delamination, lug tear, wet-slip failure]
cost_drivers: [compound, mould set per size, multi-colour pours, brand units (Vibram)]
relationships: {part_of: [bottom stack], includes: [cmp-crash-pad], brand_examples: [brd-vibram, brd-dunlop]}
sources: [nb-1906r-sheet, vibram-lib, satra-catalogue]
confidence: medium
status: seed
---
Compound choice is a traction/wear/weight triangle: carbon rubber wears longest, blown rubber cushions and lightens, gum grips. Geometry (lug shape, siping, flex grooves, decoupled crash pad) does as much work as chemistry.
