---
id: mat-leatherboard
type: material
names: [leatherboard, bonded leather fibreboard]
aliases: {cousin: cellulose board (Texon/Bontex class — distinct chemistry, same slots)}
domain: D9-bottom-stack
definition: Board of milled leather fibres bonded with latex — counters, insoles, heel-lift stacks, midsole layers in traditional work; the recycled-leather structural sheet.
key_parameters:
  - {name: thickness, unit: mm, typical: "1.0–3.0 by role", confidence: medium, source: model-knowledge}
  - {name: contrast, unit: n/a, typical: "cheaper + more uniform than solid leather; weaker wet-strength than cellulose boards' modern grades", confidence: medium, source: texon-lib}
tested_by: [std-iso-insole-family]
failure_modes: [delamination when saturated, edge crumble]
cost_drivers: [fibre content %, latex binder grade]
relationships: {slots: [cmp-heel-counter, cmp-insole-board, heel lifts], neighbours: [brd-texon]}
sources: [texon-lib, golding-1902]
confidence: medium
status: seed
---
"Leather board" in briefs = this. Distinguish from cellulose boards in the spec — different wet behaviour, same positions.
