---
id: cmp-lace
type: component
names: [shoelace, lace]
aliases: {factory: lace, UK: lace}
domain: D12-closures-trims
definition: Cord or tape closure threaded through eyelets/loops to tension the throat.
function: Fit adjustment and retention across the instep.
position: Throat/eyestay.
materials: [mat-textile-woven-nylon, mat-textile-cotton-canvas]
key_parameters:
  - {name: profile, unit: type, typical: "flat / oval / round; braided polyester dominant; waxed cotton for dress", confidence: high, source: motawi-hsam}
  - {name: width & length, unit: mm/cm, typical: "flat 6–10 mm wide; 90–120 cm by eyelet rows (7 mm × ~120 cm observed 1906R)", confidence: high, source: nb-1906r-sheet}
  - {name: house benchmark, unit: mm, typical: "flat 6–8 (populated example 8)", confidence: medium, source: vince-spec-template}
tested_by: [std-satra-lace-abrasion-family]
failure_modes: [abrasion at top eyelet, tip loss, elastic laces losing recovery]
cost_drivers: [braid construction, wax finish, custom tipping]
relationships: {tipped_by: [cmp-aglet], decorated_by: [cmp-deubre], alt_systems: [brd-boa]}
sources: [nb-1906r-sheet, satra-catalogue, vince-spec-template]
confidence: high
status: seed
---
Spec the braid, profile, width, length-per-eyelet-row, tip type and colour standard; lace-to-eyelet abrasion is a real test family, not an afterthought.
