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
render: "WEBBING — High-tenacity woven tape (typically 15-25mm wide, 1-2mm thick) used for lace loops, straps, pull tabs, harnesses, and structural anchors. Distinct RIBBED WEAVE pattern visible at close range — parallel warp threads create a fine linear texture running along the tape length. Matte to semi-sheen finish. Edges are HEAT-SEALED (slightly glazed/melted bead) or FOLDED (doubled at ends). At anchor points, webbing is secured with BARTACK or BOX-X stitch patterns — dense, concentrated rectangular or X-shaped stitch clusters (6-10mm long) that create a visible raised stitch block. Webbing stands PROUD off the upper surface (0.5-1.5mm) when slack, lies FLATTER when tensioned. Under tension, webbing is taut and straight with slight edge curl; when slack, it shows subtle lift and slight S-curve. Nylon webbing has semi-gloss sheen; polyester webbing is more matte. Associated with trail runners, technical sandals, and performance footwear harness systems."
---
Every strap is a load path: the bar tack spec matters more than the tape.
