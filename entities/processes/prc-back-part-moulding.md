---
id: prc-back-part-moulding
type: process
names: [back part moulding]
domain: D14-process-qa
definition: Pre-forming the quarter/counter assembly on heated then chilled forms before lasting — locks heel cup shape and centres the backseam.
key_parameters:
  - {name: cycle, unit: n/a, typical: "hot form (activate counter) → cold form (set); counter material governs temps", confidence: medium, source: motawi-hsam}
failure_modes: [off-centre seams, counter wrinkles, under-set springback]
relationships: {shapes: [cmp-heel-counter], precedes: [prc-lasting]}
sources: [motawi-hsam]
confidence: medium
status: seed
---
Heel fit is decided here, before the last ever sees the upper.
