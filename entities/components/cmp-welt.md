---
id: cmp-welt
type: component
names: [welt]
aliases: {IT: guardolo, variants: [storm welt, split reverse welt, Norwegian welt]}
domain: D9-bottom-stack
definition: The strip running the featherline that the upper/insole seam and the outsole seam both anchor to — the mechanical heart of welted construction; also a cosmetic strip on cemented shoes.
function: Joins upper+insole to outsole via two independent seams; enables resoling; storm profiles seal the featherline.
position: Perimeter of the sole edge at the featherline.
materials: [mat-leather-sole, mat-tr, mat-pvc, mat-tpu]
key_parameters:
  - {name: leather welt section, unit: mm, typical: "width ~16–22, substance ~3–4", confidence: low, source: model-knowledge}
  - {name: material note, unit: n/a, typical: "PVC/TPR extruded welts common on value boots and mock-welted cemented shoes", confidence: high, source: tsc-8con}
compliance_flags: [pvc-restricted-major-brands, phthalate-risk]
processes: [prc-skiving]
tested_by: [std-satra-seam-family]
failure_modes: [welt seam rot, gemming failure beneath (Goodyear), PVC plasticiser migration/embrittlement]
cost_drivers: [leather vs extruded synthetic, storm profile, hand vs machine welting]
relationships: {central_to: [con-goodyear-welt, con-stitchdown], cosmetic_on: [con-cold-cement], compliance_note: "PVC prohibited outright in NB product; spec TPR/TPU welts for majors"}
sources: [shoegazing, tsc-8con, nb-rsm-2024, golding-1902]
confidence: medium
status: seed
---
Two very different lives: structural (Goodyear/stitchdown, where it makes the shoe rebuildable) and decorative (a stitched or mock-stitched strip on cemented product). The PVC welt sits in the second life — cheap, mouldable, and now a compliance liability with majors that prohibit PVC.
