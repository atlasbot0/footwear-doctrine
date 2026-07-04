---
id: mat-leather-suede-split
type: material
names: [suede, split suede]
aliases: {precise: [split suede (from drop split), reverse suede (flesh-side of full hide)]}
domain: D5-upper-materials
definition: Napped leather — either the buffed drop split or a full hide worn flesh-out; defined by nap, shading and drag.
key_parameters:
  - {name: substance, unit: mm, typical: "1.4–1.8 sneakers/desert boots", confidence: medium, source: model-knowledge}
  - {name: nap behaviour, unit: n/a, typical: "directional shading; spec nap direction per panel and brush/drag consistency across pairs", confidence: high, source: model-knowledge}
tested_by: [std-satra-crocking-family]
failure_modes: [crocking (dye rub-off), water staining, nap crush/shine at flex]
compliance_flags: [chrome-vi-risk]
cost_drivers: [split vs reverse, dye depth, water-repellent treatment (mind PFAS-free)]
relationships: {classic_on: [con-stitchdown, con-vulcanised], property_links: [prp-nap-drag]}
sources: [motawi-smdg, heddels-con, nb-rsm-2024]
confidence: medium
status: seed
---
Suede is where "nap, drag, shading" stop being poetry and become QC criteria — pairs must shade the same way under store light. DWR treatments now need PFAS-free chemistry.
