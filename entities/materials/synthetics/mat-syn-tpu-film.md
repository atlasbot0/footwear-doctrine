---
id: mat-syn-tpu-film
type: material
names: [TPU film, weldable TPU]
aliases: {forms: [hot-melt film, HF-weld film, no-sew overlay]}
domain: D5-upper-materials
definition: Thermoplastic polyurethane in film/sheet form — welded or heat-pressed as no-sew overlays, toe puffs, skins and reinforcement zones.
key_parameters:
  - {name: gauge, unit: mm, typical: "0.15–0.5 overlays; 0.6–1.2 puff/counter sheet (0.6–0.8 observed 1906R toe puff)", confidence: high, source: nb-1906r-sheet}
  - {name: application, unit: n/a, typical: "HF weld or heat press replaces stitching — see prc-hf-welding", confidence: high, source: motawi-hsam}
tested_by: [std-satra-flex-family]
failure_modes: [edge lift, weld burn-through, yellowing (aromatic grades)]
compliance_flags: [uv-yellowing-risk]
cost_drivers: [aliphatic (non-yellowing) vs aromatic grades, film gauge]
relationships: {enables: [no-sew construction], feeds: [cmp-toe-puff, cmp-heel-counter, reinforcement 'highlights']}
sources: [nb-1906r-sheet, motawi-hsam]
confidence: high
status: seed
---
The reinforcement-of-highlights material: welded skins where stitches used to be.
