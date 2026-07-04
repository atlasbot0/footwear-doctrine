---
id: cmp-eyestay
type: component
names: [eyestay, facing]
aliases: {UK: facing, factory: eyerow}
domain: D12-closures-trims
definition: The reinforced panel housing the lacing system — carries eyelets, distributes lace tension into the quarter, and frames the throat opening.
function: Lace-load distribution, throat-opening geometry, eyelet anchorage.
position: Either side of the throat from vamp point to collar.
materials: [mat-leather-suede-split, mat-syn-tpu-film, mat-leather-bovine-full-grain]
key_parameters:
  - {name: opening width, unit: mm, typical: "base 15–20 tapering to 10–15 at top (populated example 20→12)", confidence: medium, source: vince-spec-guidance}
  - {name: reinforcement, unit: n/a, typical: "backer tape full length; bartack + reinforced top two eyelets (highest load)", confidence: medium, source: vince-spec-template}
tested_by: [std-satra-seam-family, std-satra-fastener-family]
failure_modes: [tear between eyelets, facing stretch (throat gape), top-eyelet pull-through]
cost_drivers: [material grade, backer spec, bartack operations]
relationships: {carries: [cmp-eyelet], loads_into: [quarter], geometry_note: "taper sets lace-pressure gradient across the instep"}
sources: [vince-spec-guidance, vince-spec-template, motawi-hsam]
confidence: medium
status: seed
---
The throat's load-bearing frame: the taper is a fit decision (pressure gradient), the top-two-eyelet reinforcement is a warranty decision.
