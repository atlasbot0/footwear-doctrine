---
id: cmp-crash-pad
type: component
names: [crash pad]
aliases: {alt: decoupled heel, factory: heel pod}
domain: D9-bottom-stack
definition: A softer and/or mechanically decoupled zone at the lateral heel that absorbs initial ground contact and smooths the loading path.
function: Heel-strike attenuation, transition smoothing, lateral-heel wear management.
position: Lateral rear outsole/midsole, often a separated segment or softer compound.
materials: [mat-rubber-blown, mat-eva]
key_parameters:
  - {name: implementation, unit: n/a, typical: "segmented outsole pod (observed 1906R: segmented crash pad in NDurance rubber) or softer durometer insert", confidence: high, source: nb-1906r-sheet}
  - {name: durometer offset, unit: Shore A/Asker C, typical: "5–10 points softer than surrounding stack when compound-based", confidence: low, source: model-knowledge}
tested_by: [std-satra-cushion-family]
failure_modes: [premature lateral-heel wear, pod delamination]
cost_drivers: [extra compound/pour, mould complexity]
relationships: {part_of: [cmp-outsole, cmp-midsole], relates_to: [foot plant / gait — D1]}
sources: [nb-1906r-sheet, model-knowledge]
confidence: medium
status: seed
---
Where gait science meets tooling: the decoupling groove is doing biomechanics with geometry.
