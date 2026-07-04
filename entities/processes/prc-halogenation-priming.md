---
id: prc-halogenation-priming
type: process
names: [halogenation / priming]
aliases: {factory: [chlorination wipe, UV primer line]}
domain: D13-adhesives
definition: Chemical surface activation of rubber/EVA/TPU before cementing — the invisible step that decides whether cold-cement bonds live or die.
key_parameters:
  - {name: logic, unit: n/a, typical: "solvent wipe/scour → halogenate rubber (or UV prime) → primer → PU cement two-coat → heat activate → press", confidence: medium, source: model-knowledge}
tested_by: [std-satra-sole-bond-family]
failure_modes: [skipped/expired primer, contamination (mould release, pull-up oils), open-time misses]
cost_drivers: [chemical logistics, line discipline, water-based system conversion]
relationships: {enables: [con-cold-cement], conflicts_with: [oily leathers → mat-leather-pull-up note], compliance_note: "MRSL governs solvent choices (toluene etc. restricted) — see std-mrsl-zdhc"}
sources: [satra-catalogue, nb-rsm-2024, model-knowledge]
confidence: medium
status: seed
---
Delamination is almost never the cement's fault; it's this step, skipped or stale.
