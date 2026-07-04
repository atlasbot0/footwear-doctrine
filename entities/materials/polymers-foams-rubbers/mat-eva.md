---
id: mat-eva
type: material
names: [EVA, ethylene-vinyl acetate foam]
aliases: {process-forms: [CM EVA (compression-moulded), IP/injection phylon, sheet EVA]}
domain: D9-bottom-stack
definition: The default midsole foam — closed-cell EVA copolymer, crosslinked and expanded; light, mouldable, cheap, compression-set prone.
key_parameters:
  - {name: hardness, unit: Asker C, typical: "45–60 midsoles; 25–40 sockliner/plush", confidence: medium, source: model-knowledge}
  - {name: density, unit: "g/cm³", typical: "CM 0.18–0.25; injection phylon 0.12–0.20; sheet 0.1–0.3", confidence: medium, source: model-knowledge}
  - {name: VA content, unit: "%", typical: "~18–28 footwear grades — softness/resilience lever", confidence: low, source: model-knowledge}
tested_by: [std-satra-cushion-family, std-iso-17707]
failure_modes: [compression set (dead midsole), shrinkage post-mould, UV yellow]
compliance_flags: [uv-yellowing-risk]
cost_drivers: [CM (two-step, denser, sharper detail) vs IP (one-shot, lighter, cheaper/pair at volume), bio-based EVA premium]
relationships: {upgrades: [mat-etpu, mat-peba], branded_ultralight_cousin: [brd-xl-extralight], acronym_note: "RSLs flag acetophenone/2-phenyl-2-propanol residues in EVA (peroxide crosslinking by-products)"}
sources: [motawi-hsam, nb-rsm-2024, nb-1906r-sheet]
confidence: medium
status: seed
---
CM vs injection phylon is the first tooling/cost fork in any athletic brief. The RSM even carries an EVA-specific chemical test (crosslinking residues) — chemistry follows the foam all the way to the lab.
