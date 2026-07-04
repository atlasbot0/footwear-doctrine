---
id: mat-leather-patent
type: material
names: [patent leather]
domain: D5-upper-materials
definition: Leather finished with a high-gloss PU film — the maximum-shine finish class; historically linseed lacquer, now PU coating.
key_parameters:
  - {name: gloss, unit: n/a, typical: "mirror finish; shine is the spec — measure gloss units on lab dips", confidence: medium, source: model-knowledge}
  - {name: coating, unit: n/a, typical: "PU film over corrected grain; minimal breathability", confidence: high, source: motawi-smdg}
failure_modes: [film cracking at flex, plasticiser migration between contacting patent surfaces (colour transfer), scuff whitening]
compliance_flags: [phthalate-risk]
cost_drivers: [film quality, colour-transfer-safe formulations]
relationships: {property_links: [prp-hand-temper — stiff], classic_on: [formal, Mary-Janes]}
sources: [motawi-smdg, nb-rsm-2024]
confidence: medium
status: seed
---
"Shine" as a controlled property. Store patent pairs with tissue interleave — patent-on-patent contact transfer is a real claim category.
