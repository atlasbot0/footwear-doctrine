---
id: prc-hf-welding
type: process
names: [high-frequency welding, HF welding]
aliases: {alt: [RF welding, heat press bonding (cousin)]}
domain: D14-process-qa
definition: Radio-frequency energy fuses thermoplastic films/overlays (TPU, coated textiles) to substrates — the no-sew joining method; also embosses 3D logos.
key_parameters:
  - {name: observed, unit: n/a, typical: "1906R: HF reflective tongue patch; moulded logos — standard athletic trim kit", confidence: high, source: nb-1906r-sheet}
failure_modes: [burn-through, weak weld (contamination), edge lift in flex zones]
cost_drivers: [tooling dies per graphic, cycle time]
relationships: {joins: [mat-syn-tpu-film, brd-scotchlite films], substitutes_for: [stitch rows in overlays]}
sources: [nb-1906r-sheet, motawi-hsam]
confidence: medium
status: seed
---
Stitchless structure and branding in one die; the modern upper's quiet workhorse.
