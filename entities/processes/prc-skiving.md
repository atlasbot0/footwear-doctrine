---
id: prc-skiving
type: process
names: [skiving]
domain: D14-process-qa
definition: Thinning component edges (bell-knife machines) so folds, seams and overlaps stay flat and even — the difference between refined and clunky closing.
key_parameters:
  - {name: edge treatments, unit: n/a, typical: "fold skive, raw-edge skive, lap skive; depth/width specced per edge", confidence: high, source: motawi-hsam}
failure_modes: [cut-through, uneven feed chatter, over-thin tear lines]
cost_drivers: [operations per panel edge]
relationships: {precedes: [folding, closing seams], applies_to: [cmp-heel-counter, cmp-toe-puff, all upper edges]}
sources: [motawi-hsam, golding-1902]
confidence: high
status: seed
---
Everything that looks "clean" on an upper was skived first.
