---
id: cmp-aglet
type: component
names: [aglet, lace tip]
aliases: {factory: tipping}
domain: D12-closures-trims
definition: The hard termination on a lace end that prevents fray and aids threading.
function: Anti-fray, threading, brand detail (metal/custom tips).
position: Both ends of each lace.
materials: [mat-syn-tpu-film]
key_parameters:
  - {name: type, unit: n/a, typical: "acetate film wrap (standard), moulded plastic, crimped metal", confidence: high, source: model-knowledge}
  - {name: length, unit: mm, typical: "12–18", confidence: medium, source: model-knowledge}
failure_modes: [tip pull-off, cracking, metal tip scratching eyelets]
cost_drivers: [metal/custom logo tips vs acetate]
relationships: {part_of: [cmp-lace]}
sources: [motawi-hsam, model-knowledge]
confidence: medium
status: seed
---
Tiny part, disproportionate perceived-quality signal. Custom metal aglets are a classic premiumisation lever.
