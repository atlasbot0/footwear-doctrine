---
id: cmp-deubre
type: component
names: [deubré, lace tag]
aliases: {alt-spellings: [dubrae, deubray], colloquial: lace jewel/lace lock ornament}
domain: D12-closures-trims
definition: Ornamental plate threaded onto the lower laces (AF1-style); pure branding real estate.
function: Brand/identity ornament; occasionally functional lace lock.
position: Threaded across the lower two lace rows.
materials: [mat-tpu, mat-abs]
key_parameters:
  - {name: attachment, unit: n/a, typical: "two lace slots; metal (zinc alloy plated) or moulded TPU/ABS", confidence: high, source: model-knowledge}
compliance_flags: [nickel-release]
failure_modes: [plating wear, nickel-release non-compliance on skin-contact metal]
cost_drivers: [metal + plating vs moulded, MOQ on custom tooling]
relationships: {mounts_on: [cmp-lace]}
sources: [model-knowledge, nb-rsm-2024]
confidence: medium
status: seed
---
The "lace debris" of dictation legend. Metal versions need nickel-release compliance like any skin-contact trim.
