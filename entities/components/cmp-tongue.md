---
id: cmp-tongue
type: component
names: [tongue]
aliases: {IT: linguetta}
domain: D12-closures-trims
definition: The padded flap under the lacing that distributes lace pressure and seals the throat.
function: Instep pressure distribution, debris sealing (gusseted), branding surface.
position: Under the eyestay, stitched at the vamp throat.
materials: [mat-eva, mat-pu-foam, mat-textile-open-mesh]
key_parameters:
  - {name: padding, unit: mm, typical: "4–10 foam, quilted or laminated; lighter on racing product", confidence: medium, source: model-knowledge}
  - {name: house benchmark, unit: mm, typical: "mesh + 6 mm PU foam", confidence: medium, source: vince-spec-template}
  - {name: attachment, unit: n/a, typical: "throat stitch + optional lace loop / gusset wings", confidence: high, source: motawi-hsam}
failure_modes: [tongue slide, top-edge abrasion, label delamination]
cost_drivers: [gusseted vs free, woven label vs HF welded badge]
relationships: {carries: [woven labels, HF patches — observed 1906R reflective tongue patch], works_with: [cmp-lace]}
sources: [nb-1906r-sheet, motawi-hsam, vince-spec-template]
confidence: medium
status: seed
---
Gusset it and it seals; free it and it slides — lace loops are the compromise. Prime badge real estate.
