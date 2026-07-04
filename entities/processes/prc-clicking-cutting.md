---
id: prc-clicking-cutting
type: process
names: [clicking, cutting]
aliases: {heritage: clicking (the knife's click), modern: [die cutting, CNC knife, waterjet]}
domain: D14-process-qa
definition: Cutting upper components from hides/materials — the yield-and-quality gate of the whole factory; panel placement on the hide decides stretch behaviour and defect exposure.
key_parameters:
  - {name: hide discipline, unit: n/a, typical: "vamps from butt/bend (tight), avoid belly looseness in stress panels; stretch direction across the foot", confidence: high, source: golding-1902}
tested_by: [std-satra-upper-family]
failure_modes: [loose-cut vamps (pipiness), defect inclusion, poor nesting yield]
cost_drivers: [yield %, die inventory vs CNC programming]
relationships: {feeds: [everything], upstream_of: [prc-skiving]}
sources: [golding-1902, motawi-hsam]
confidence: high
status: seed
---
The most leveraged 30 seconds in shoemaking: where the panel comes from on the hide is invisible in the tech pack and decisive on the foot.
