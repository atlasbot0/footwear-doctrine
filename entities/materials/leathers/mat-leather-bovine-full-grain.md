---
id: mat-leather-bovine-full-grain
type: material
names: [full-grain bovine leather, full grain cowhide]
aliases: {trade: full grain, contrast: [top grain (buffed), corrected grain (embossed)]}
domain: D5-upper-materials
definition: Cattle hide with the intact grain layer — the strongest, most breathable and best-ageing upper leather class.
key_parameters:
  - {name: substance, unit: mm, typical: "1.4–1.8 sneaker/casual uppers; 1.8–2.2 boots", confidence: medium, source: model-knowledge}
  - {name: character, unit: n/a, typical: "tight break, natural grain, patinas; cut yield lower than corrected grain", confidence: high, source: motawi-smdg}
  - {name: cutting, unit: n/a, typical: "cut tight-to-toe with stretch direction; avoid loose belly in vamps", confidence: high, source: golding-1902}
tested_by: [std-satra-upper-family]
failure_modes: [looseness/pipiness in belly cuts, scratch visibility, water spotting (aniline)]
compliance_flags: [chrome-vi-risk, animal-welfare-policy]
cost_drivers: [selection grade, tannery, cutting yield, finish level]
relationships: {finishes: [mat-leather-pull-up, mat-leather-patent], tannages: [mat-leather-chrome-tan, mat-leather-veg-tan]}
sources: [motawi-smdg, golding-1902, nb-rsm-2024]
confidence: medium
status: seed
---
The reference upper material. Grade selection and clicking discipline (where on the hide each panel comes from) drive both cost and quality more than the spec sheet admits. Note sourcing policies: majors restrict hides from the Amazon biome and require traceability.
