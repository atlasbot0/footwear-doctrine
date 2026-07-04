---
id: mat-rubber-carbon
type: material
names: [carbon rubber]
aliases: {trade-examples: [NDurance (NB), XDR (Nike) — brand names for high-wear compounds]}
domain: D9-bottom-stack
definition: Carbon-black-reinforced vulcanised rubber — the high-abrasion outsole compound for heel plugs and full outsoles.
key_parameters:
  - {name: hardness, unit: Shore A, typical: "65–75 general; 85–90 observed on 1906R NDurance", confidence: high, source: nb-1906r-sheet}
  - {name: abrasion, unit: "mm³ ISO 4649", typical: "<100 achievable premium", confidence: medium, source: model-knowledge}
tested_by: [std-iso-4649, std-satra-tm144]
failure_modes: [marking floors (non-marking grades exist), harsher ride]
cost_drivers: [compound loading, cure time]
relationships: {pairs_with: [mat-rubber-blown in dual-compound outsoles], seen_on: [cmp-outsole, cmp-crash-pad]}
sources: [nb-1906r-sheet, satra-catalogue]
confidence: medium
status: seed
---
Where the shoe meets the road hardest. Dual-compound layouts put it at heel-strike and toe-off, blown rubber elsewhere.
