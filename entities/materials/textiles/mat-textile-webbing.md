---
id: mat-textile-webbing
type: material
names: [webbing, tape]
aliases: {uses: [heel pull loop, strap, binding tape, lace loops]}
domain: D12-closures-trims
definition: Narrow woven or knitted tape — straps, pull tabs, bindings, sandal uppers; also the elastic-core version for gussets.
key_parameters:
  - {name: width, unit: mm, typical: "10–38 common footwear widths", confidence: medium, source: model-knowledge}
  - {name: tensile, unit: n/a, typical: "spec break strength for load points (heel pulls, sandal straps)", confidence: medium, source: satra-catalogue}
tested_by: [std-satra-fastener-family]
failure_modes: [edge fray, bar-tack pull-out at anchor]
cost_drivers: [fibre (nylon vs PP vs polyester), jacquard logos]
relationships: {anchored_by: [bar tacks per prp-spi], elastic_form: [cmp-elastic-gusset]}
sources: [satra-catalogue, model-knowledge]
confidence: medium
status: seed
---
Every strap is a load path: the bar tack spec matters more than the tape.
