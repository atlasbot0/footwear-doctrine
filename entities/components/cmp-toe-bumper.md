---
id: cmp-toe-bumper
type: component
names: [toe bumper, toe guard]
aliases: {alt: mudguard (when extended around forepart), vulc: toe cap (rubber)}
domain: D8-reinforcement
definition: External abrasion guard over the toe — rubber (vulc), stitched leather/synthetic mudguard, or moulded TPU.
function: Scuff/abrasion protection at the highest-wear external zone; design signature (vulc caps).
position: External forepart over the featherline.
materials: [mat-rubber-gum, mat-tpu, mat-leather-suede-split]
key_parameters:
  - {name: reinforcement stitching, unit: rows, typical: "double row on mudguards; per prp-edge-distance-gauge", confidence: medium, source: model-knowledge}
tested_by: [std-satra-abrasion-family]
failure_modes: [edge lift, abrasion through, stitch abrasion]
cost_drivers: [moulded TPU tooling vs cut-and-stitch]
relationships: {external_counterpart_of: [cmp-toe-puff], classic_on: [con-vulcanised, con-stitchdown]}
sources: [misiu-con, model-knowledge]
confidence: medium
status: seed
---
The "reinforcement of the highlights" zone: bumpers, mudguards and welded films take the hits so the vamp doesn't.
