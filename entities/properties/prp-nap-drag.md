---
id: prp-nap-drag
type: property
names: [nap, drag, shading]
domain: D5-upper-materials
definition: Directional surface behaviour of suede/nubuck — nap direction changes colour read (shading) and touch (drag); a cut-plan and QC property, not a defect.
key_parameters:
  - {name: spec rule, unit: n/a, typical: "state nap direction per panel; pairs matched under standard light; brush direction at finish", confidence: high, source: model-knowledge}
relationships: {applies_to: [mat-leather-suede-split, mat-leather-nubuck], qc_hook: [pair-matching stations]}
sources: [motawi-smdg, model-knowledge]
confidence: medium
status: seed
---
Why one suede shoe photographs two-tone: nobody specced the nap.
