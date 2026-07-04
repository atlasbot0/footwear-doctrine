---
id: mat-leather-sole
type: material
names: [leather soling, sole leather]
aliases: {trade: [bends, sole bends], premium: [oak-bark pit-tanned]}
domain: D9-bottom-stack
definition: Dense vegetable-tanned bovine bends cut for outsoles, midsoles, welts and heel lifts — the traditional bottom-stack material; breathable, burnishable, resolable.
key_parameters:
  - {name: substance, unit: mm, typical: "single sole 4–5.5; midsole layers 2–3; heel lifts stacked", confidence: medium, source: golding-1902}
  - {name: character, unit: n/a, typical: "wears by abrasion not delamination; slick when new/wet (add toe taps or rubber half-sole)", confidence: high, source: golding-1902}
tested_by: [std-satra-sole-wear-family]
failure_modes: [wet-slip, fast wear on abrasive urban surfaces, water wicking]
cost_drivers: [pit-tanned premium (JR/Baker class) vs drum-tanned commodity]
relationships: {lives_in: [con-goodyear-welt, con-blake], pairs_with: [mat-rubber-gum half-soles], feeds: [cmp-welt]}
sources: [golding-1902, shoegazing]
confidence: medium
status: seed
---
He asked for leather soles by name: this is the entity. The resole economy of welted footwear exists because this material wears gracefully and replaces cleanly.
