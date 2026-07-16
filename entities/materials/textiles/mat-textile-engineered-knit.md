---
id: mat-textile-engineered-knit
type: material
names: [engineered knit upper]
aliases: {brand-class: [Flyknit (Nike), Primeknit (adidas), Hyposkin — brand names for the class], tech: [flat knit, jacquard knit]}
domain: D5-upper-materials
definition: A flat- or circular-knitted upper where structure, stretch zones, ventilation and pattern are programmed into the knit itself — panel count collapses toward one.
key_parameters:
  - {name: machine, unit: gauge, typical: "flat-knit 12–18 gg typical for uppers", confidence: low, source: model-knowledge}
  - {name: zoning, unit: n/a, typical: "tuck/miss/inlay structures create hold vs stretch vs vent zones in one piece; fused yarns (TPU-wrapped) add lock", confidence: medium, source: model-knowledge}
tested_by: [std-satra-upper-family]
failure_modes: [bagging without inlay/skin support, snagging, toe abrasion]
cost_drivers: [knit programming time, yarn mix (fusible/melt yarns), waste ~near-zero vs cut-and-sew]
relationships: {kills: [cut-and-sew panel count], needs: [internal skins/cages for containment], sustainability_note: "near-zero cutting waste is the pitch"}
sources: [motawi-hsam, model-knowledge]
confidence: medium
status: seed
render: "ENGINEERED KNIT — Machine-knit textile with visible interlocking V-shaped yarn loops (yarn gauge 0.3-0.8mm, individual stitch loops 1-2mm wide x 2-3mm tall) in programmed zone-varied density. Tight dense knit for support areas (heel, midfoot); looser open knit for breathability zones (toe, collar). 60% less waste than cut-and-sew construction. Surface has a soft textile matte finish with topographical texture depth from stitch pattern. Natural tonal variation from the knit structure — raised yarn loop peaks catch light, recessed valleys between stitches sit in micro-shadow, creating a fine regular light/dark micro-pattern following stitch rows. Multi-color yarns create a heathered mottled appearance — individual loops of each color visible at close range as a pixelated color field. Zone density transitions create visible bands of tighter/looser texture across the upper. Under tension, stitches stretch open revealing underlying color. Upper weight as low as 34g. More structured than woven fabric, softer than mesh — Flyknit, Primeknit aesthetic."
---
Pattern engineering migrates from the cutting table into the knit program — repeat vs placement logic becomes stitch-map logic.
