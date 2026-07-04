---
id: mat-syn-kpu
type: material
names: [KPU]
aliases: {expansion: "K(o)PU — moulded PU skin overlays; trade usage varies"}
domain: D5-upper-materials
definition: Low-pressure moulded polyurethane overlays formed directly with 3D texture — cage/mudguard/logo pieces with sculpted relief, stitched or bonded on.
key_parameters:
  - {name: thickness, unit: mm, typical: "0.8–2.0 with moulded relief", confidence: low, source: model-knowledge}
tested_by: [std-satra-flex-family]
failure_modes: [edge peel, flex cracking if over-thick, yellowing]
compliance_flags: [uv-yellowing-risk]
cost_drivers: [mould tooling, per-part cycle time]
relationships: {siblings: [mat-syn-tpu-film], role: [sculpted reinforcement/branding overlays]}
sources: [model-knowledge]
confidence: low
status: seed
---
Trade term with fuzzy edges — treat as "moulded PU overlay class" and triangulate supplier definitions in P3.
