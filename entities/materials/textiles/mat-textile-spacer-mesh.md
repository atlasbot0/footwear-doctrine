---
id: mat-textile-spacer-mesh
type: material
names: [spacer mesh, sandwich mesh]
aliases: {tech: 3D warp knit}
domain: D6-linings
definition: Two knitted faces held apart by monofilament pile — built-in cushioning and airflow in one textile; collar/tongue/lining staple.
key_parameters:
  - {name: thickness, unit: mm, typical: "2–6 footwear grades", confidence: medium, source: model-knowledge}
tested_by: [std-satra-lining-abrasion-family]
failure_modes: [pile collapse (set), face abrasion at heel]
cost_drivers: [thickness, face yarn quality]
relationships: {replaces: [foam+lining laminates in collars/tongues]}
sources: [motawi-smdg, model-knowledge]
confidence: medium
status: seed
---
Foam and lining in a single knit — fewer laminations, better wash-through of air.
