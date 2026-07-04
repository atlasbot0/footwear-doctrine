---
id: con-cold-cement
type: construction
names: [cold cement construction]
aliases: {alt: [cemented, stuck-on, Board/Strobel-lasted cemented]}
domain: D10-constructions
definition: Upper lasted (board or force) and bonded to the sole unit with adhesives under press — no through-stitching; the dominant modern construction for sneakers and light casuals.
key_parameters:
  - {name: adhesive system, unit: n/a, typical: "PU cement two-coat with primers; heat activation ~45–70 °C, press, cure — see prc-halogenation-priming", confidence: medium, source: model-knowledge}
  - {name: bond spec, unit: "N/mm", typical: "sole-bond peel per SATRA TM404-class methods; spec minimums by category", confidence: medium, source: satra-catalogue}
tested_by: [std-satra-sole-bond-family]
failure_modes: [delamination (prep failure), edge void, cement bloom]
cost_drivers: [surface-prep labour, press cycle, VOC management (water-based systems)]
relationships: {pairs_with: [con-strobel-force-lasted, con-board-lasted], contrast: [con-vulcanised, con-goodyear-welt], rollie_note: "Rollie core DNA: lightweight cemented derby"}
sources: [motawi-hsam, satra-catalogue]
confidence: medium
status: seed
---
Everything hinges on surface prep and chemistry discipline; the bond IS the construction.
