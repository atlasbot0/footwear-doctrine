---
id: mat-syn-pu-leather
type: material
names: [PU synthetic leather, PU leather]
aliases: {trade: [action leather (PU-coated split), vegan leather (marketing)], avoid: pleather}
domain: D5-upper-materials
definition: Polyurethane skin on a textile (or split-leather) substrate embossed to a grain — the volume leather substitute.
key_parameters:
  - {name: build, unit: n/a, typical: "PU film 0.2–0.6 mm on knit/non-woven backer; total 1.0–1.6 mm", confidence: medium, source: model-knowledge}
  - {name: lifetime risk, unit: n/a, typical: "hydrolysis: PU skins age-crack in storage humidity; spec hydrolysis-resistant grades + test", confidence: high, source: satra-bulletin}
tested_by: [std-satra-hydrolysis-family, std-satra-flex-family]
failure_modes: [hydrolysis flaking, cold-crack, emboss flattening]
compliance_flags: [hydrolysis-risk]
cost_drivers: [PU grade (polyether resists hydrolysis better than polyester PU), solvent vs water-based coagulation]
relationships: {upgrade_path: [mat-syn-microfibre], substitutes_for: [mat-leather-bovine-full-grain]}
sources: [satra-bulletin, motawi-smdg]
confidence: medium
status: seed
---
The failure that shows up two summers later in the warehouse: hydrolysis. Spec the PU chemistry, not just the look.
