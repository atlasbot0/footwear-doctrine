---
id: cmp-eyelet
type: component
names: [eyelet]
aliases: {variants: [blind eyelet, washered eyelet, speed hook, D-ring, ghillie loop]}
domain: D12-closures-trims
definition: Reinforced lace aperture — punched-and-set metal, moulded, or a bare punched hole in reinforced facing.
function: Lace guidance and eyestay reinforcement against tension tear.
position: Eyestay/facing rows.
materials: [mat-abs]
key_parameters:
  - {name: set type, unit: n/a, typical: "blind (barrel hidden) vs washered (two-part, stronger)", confidence: high, source: model-knowledge}
  - {name: pull-out strength, unit: N, typical: "verified per eyelet attachment strength methods (SATRA family)", confidence: medium, source: satra-catalogue}
compliance_flags: [nickel-release]
failure_modes: [pull-through, plating corrosion, facing tear between eyelets]
cost_drivers: [metal finish, washered vs blind, hooks/D-rings hardware]
relationships: {reinforced_by: [eyestay backer tapes], guides: [cmp-lace]}
sources: [satra-catalogue, nb-rsm-2024]
confidence: medium
status: seed
---
Boots graduate to speed hooks and D-rings up top; the facing reinforcement under the hardware matters more than the hardware.
