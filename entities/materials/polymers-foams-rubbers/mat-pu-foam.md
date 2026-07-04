---
id: mat-pu-foam
type: material
names: [polyurethane foam (soling), PU]
aliases: {forms: [PU midsole, PU unit sole (DIP), open-cell PU (padding/sockliner)]}
domain: D9-bottom-stack
definition: Reaction-poured/injected urethane — denser, more durable and more abrasion-resistant than EVA, with hydrolysis as the defining lifetime risk.
key_parameters:
  - {name: density, unit: "g/cm³", typical: "midsole 0.35–0.55; comfort unit soles 0.45–0.65", confidence: medium, source: model-knowledge}
  - {name: padding grade, unit: "kg/m³", typical: "collar/tongue open-cell 25–40 (30 observed 1906R)", confidence: high, source: nb-1906r-sheet}
tested_by: [std-satra-hydrolysis-family, std-iso-4649]
failure_modes: [hydrolysis crumble (polyester PU in humid storage), heavier ride]
compliance_flags: [hydrolysis-risk]
cost_drivers: [polyether (hydrolysis-resistant) vs polyester systems, DIP machinery]
relationships: {construction_home: [con-direct-injection], comfort_home: [cmp-collar-padding, cmp-sockliner], boot_class: "cellular PU boots (Dunlop Purofort class)"}
sources: [nb-1906r-sheet, satra-bulletin, misiu-con]
confidence: medium
status: seed
---
Two PU lives: dense soling (durability, DIP economics) and open-cell comfort foam. Both share the hydrolysis caveat; chemistry choice is the mitigation.
