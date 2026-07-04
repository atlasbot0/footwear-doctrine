---
id: mat-tpu
type: material
names: [TPU, thermoplastic polyurethane]
domain: D9-bottom-stack
definition: "Injection-mouldable urethane elastomer — the structural plastic of modern footwear: heel cages, shanks/webs, plates, outsole inserts, welded films."
key_parameters:
  - {name: hardness, unit: Shore A/D, typical: "cages/frames 85–98 A (85 A observed 1906R heel cage); plates into Shore D", confidence: high, source: nb-1906r-sheet}
  - {name: virtues, unit: n/a, typical: "high abrasion + tear + rebound; transparent grades; bonds well with priming", confidence: high, source: model-knowledge}
tested_by: [std-iso-4649, std-satra-flex-family]
failure_modes: [yellowing (aromatic), creep under sustained load, cold stiffening]
compliance_flags: [uv-yellowing-risk]
cost_drivers: [aliphatic clear grades, tooling]
relationships: {film_form: [mat-syn-tpu-film], bead_foam_form: [mat-etpu], seen_as: [cmp-shank athletic web, cmp-heel-counter external cage]}
sources: [nb-1906r-sheet, model-knowledge]
confidence: medium
status: seed
---
Where the shoe needs an engineered part rather than a foam or fabric, it's usually TPU.
