---
id: cmp-midsole
type: component
names: [midsole]
aliases: {dress-trade: mid-sole (leather layer between insole and outsole)}
domain: D9-bottom-stack
definition: The cushioning/structural layer between upper platform and outsole; in athletic footwear the primary performance component.
function: Cushioning, energy management, stability geometry, stack height and drop.
position: Between strobel/insole board and outsole.
materials: [mat-eva, mat-pu-foam, mat-etpu, mat-peba, mat-tpu]
key_parameters:
  - {name: hardness, unit: Asker C, typical: "45–60 mainstream EVA; softer 35–45 for max-cushion", confidence: medium, source: model-knowledge}
  - {name: density, unit: "g/cm³", typical: "CM EVA 0.18–0.25; injection phylon 0.12–0.20; PU 0.35–0.55", confidence: medium, source: model-knowledge}
  - {name: geometry, unit: mm, typical: "stack height, drop/offset, sidewall spring — style governed", confidence: high, source: motawi-hsam}
processes: [prc-heat-setting]
tested_by: [std-satra-cushion-family, std-iso-17707]
failure_modes: [compression set, hydrolysis (PU), yellowing (UV), sidewall cracking]
cost_drivers: [compound (EVA vs supercritical), moulds per size, dual-density inserts]
compliance_flags: [hydrolysis-risk, uv-yellowing-risk]
relationships: {part_of: [bottom stack], carries: [cmp-shank, cmp-crash-pad], observed_example: "1906R: ACTEVA LITE EVA + ABZORB SBS pods + TPU stability web"}
sources: [nb-1906r-sheet, motawi-hsam, satra-bulletin]
confidence: medium
status: seed
---
Compression-moulded EVA is the workhorse; injection phylon trades density for tooling economics; PU gives durability with weight and hydrolysis risk; bead/supercritical foams (E-TPU, PEBA) buy resilience at cost. Multi-part midsoles combine foams, gel/pod inserts and TPU frames.
