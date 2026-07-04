---
id: cmp-heel-counter
type: component
names: [heel counter, back counter]
aliases: {UK: stiffener, IT: contrafforte, factory: counter}
domain: D8-reinforcement
definition: Semi-rigid reinforcement moulded around the backpart, between upper and lining (or as an external clip), that holds heel shape and locks the calcaneus.
function: Backpart shape retention, rearfoot stability, prevents topline collapse.
position: Rear quarter, wraps heel seat to backline.
materials: [mat-tpu, mat-leatherboard, mat-syn-tpu-film]
key_parameters:
  - {name: sheet thickness, unit: mm, typical: "1.2–2.0 (internal); 0.6–1.0 moulded TPU cage walls", confidence: medium, source: model-knowledge}
  - {name: height, unit: mm, typical: "~50–65; 60 observed on NB 1906R internal counter", confidence: high, source: nb-1906r-sheet}
  - {name: activation temp (thermoplastic), unit: "°C", typical: "60–85", confidence: medium, source: model-knowledge}
processes: [prc-skiving, prc-back-part-moulding]
tested_by: [std-satra-backpart-family]
failure_modes: [collapse, edge print-through, delamination, cracking at flex line]
cost_drivers: [external moulded clip vs internal sheet, material grade]
relationships: {part_of: [quarter assembly], shaped_by: [last heel curve], attached_by: [hot-melt adhesive, stitching]}
sources: [nb-1906r-sheet, motawi-hsam, golding-1902]
confidence: medium
status: seed
---
Internal counters are die-cut from thermoplastic sheet or leatherboard, skived at the edges, heat-activated and moulded in back-part moulding before or during lasting. Athletic designs increasingly split the job: a slim internal counter for fit plus an external TPU heel cage for structure and design language (both present on the 1906R).
