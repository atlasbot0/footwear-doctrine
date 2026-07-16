---
id: mat-textile-ripstop
type: material
names: [ripstop nylon]
aliases: {variant: ripstop polyester}
domain: D5-upper-materials
definition: Lightweight woven with a reinforcing grid of heavier yarns that arrests tear propagation — the visible-grid technical upper fabric.
key_parameters:
  - {name: base yarn, unit: denier, typical: "70–210D nylon common in footwear panels", confidence: medium, source: model-knowledge}
  - {name: signature, unit: n/a, typical: "box/diamond grid every ~5–8 mm; tear strength >> plain weave of equal weight", confidence: high, source: model-knowledge}
tested_by: [std-satra-upper-family]
failure_modes: [abrasion (thin base), edge fray without seal, coating delamination]
cost_drivers: [denier, coatings (PU/silicone — mind PFAS-free DWR), recycled yarns]
compliance_flags: [pfas-phase-out]
relationships: {big_brother: [brd-cordura], backer_note: "usually laminated to foam/tricot backer for footwear hand"}
sources: [cordura-lib, nb-rsm-2024]
confidence: medium
status: seed
render: "RIPSTOP — Lightweight woven fabric with a reinforcement grid of heavier denier yarns (typically 70D base with 210D reinforcement threads) woven at regular intervals, creating a subtle SQUARE or DIAMOND grid pattern (3-6mm spacing) visible across the surface. The grid pattern appears and disappears with viewing angle — most visible when light catches the heavier reinforcement threads at a raking angle. Between grid lines, the base fabric is thin and lightweight. Folds do NOT drape softly — ripstop holds angular, sharp creases and shows structured fold memory. The grid DISTORTS at crease points where fold stress pulls the pattern out of alignment. Matte to semi-matte finish. Cut edges fray unless sealed or bound. Pairs with synthetic overlays, rubberized toe guards, taped seams, and webbing straps. Associated with military, outdoor, and technical trail footwear."
---
Buy the tear stop, engineer the abrasion: footwear ripstop is almost always a laminate, not a bare fabric.
