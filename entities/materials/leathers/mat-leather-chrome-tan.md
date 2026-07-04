---
id: mat-leather-chrome-tan
type: material
names: [chrome-tanned leather]
aliases: {trade: wet blue (intermediate), alt: chrome-free/wet-white (substitution class)}
domain: D5-upper-materials
definition: Chromium(III)-salt tannage — fast, soft, thermally stable, dye-versatile; ~85–90% of world footwear leather.
key_parameters:
  - {name: process time, unit: n/a, typical: "day-scale drum tannage vs weeks/months veg", confidence: high, source: motawi-smdg}
  - {name: shrink temperature, unit: "°C", typical: "≥100 (boilfast) — enables lasting/heat processes", confidence: medium, source: model-knowledge}
compliance_flags: [chrome-vi-risk]
failure_modes: [Cr(VI) formation from poor process control/aging — RSLs cap at 3 mg/kg with aging test 0.5–3", confidence-note: see std-rsl-framework]
cost_drivers: [effluent treatment, LWG tannery rating]
relationships: {substitutes: [chrome-free wet-white, mat-leather-veg-tan], compliance_source: nb-rsm-2024}
sources: [nb-rsm-2024, motawi-smdg]
confidence: medium
status: seed
---
The default tannage. The compliance story is Cr(VI) — a process-control failure mode, not an ingredient — which is why RSLs pair the limit with an aging test.
