---
id: prp-peel-strength
type: property
names: [peel strength, sole bond strength]
domain: D15-testing-compliance
definition: Force per width to peel sole from upper (or layer from layer) — the pass/fail of cemented footwear.
key_parameters:
  - {name: spec logic, unit: "N/mm", typical: "house minimums by category; measured per SATRA TM404-class sole adhesion methods incl. aged/wet conditions", confidence: medium, source: satra-catalogue}
  - {name: house benchmark, unit: "N/cm", typical: "≥3.0 N/cm bond strength (note unit: N/cm not N/mm)", confidence: medium, source: vince-spec-template}
tested_by: [std-satra-sole-bond-family]
relationships: {validates: [con-cold-cement, prc-halogenation-priming], failure_read: "adhesive vs cohesive vs substrate failure tells you WHERE the process broke"}
sources: [satra-catalogue, vince-spec-template]
confidence: medium
status: seed
---
Read the failure surface, not just the number — it names the guilty process step.
