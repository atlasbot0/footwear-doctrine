---
id: cmp-lining
type: component
names: [lining]
aliases: {IT: fodera, zones: [vamp lining, quarter lining]}
domain: D6-linings
definition: The interior skin of the shoe — leather, textile or membrane bootie — managing feel, moisture and wear against the foot.
function: Comfort against skin, moisture management, hides construction, carries counters/puffs.
position: Full interior, zoned vamp vs quarter.
materials: [mat-leather-pig, mat-leather-sheep, mat-textile-spacer-mesh]
key_parameters:
  - {name: leather substance, unit: mm, typical: "0.6–0.9 pig/sheep linings", confidence: medium, source: model-knowledge}
  - {name: textile spec, unit: n/a, typical: "non-woven (cambrelle-class) or spacer mesh; abrasion-rated at heel", confidence: medium, source: model-knowledge}
tested_by: [std-satra-lining-abrasion-family]
failure_modes: [heel lining wear-through, dye crocking onto socks, membrane puncture]
compliance_flags: [chrome-vi-risk]
failure_note: heel counter pocket is the abrasion hotspot
cost_drivers: [leather vs textile, membrane booties, seamless zones]
relationships: {contains: [cmp-heel-counter, cmp-toe-puff], membrane_option: [brd-gore-tex]}
sources: [golding-1902, satra-catalogue, nb-rsm-2024]
confidence: medium
status: seed
---
Zone it: leather where feel sells, engineered textile where abrasion and moisture rule. Crocking and Cr(VI) compliance live here because it touches skin all day.
