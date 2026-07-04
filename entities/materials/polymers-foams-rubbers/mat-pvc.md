---
id: mat-pvc
type: material
names: [PVC, polyvinyl chloride]
domain: D9-bottom-stack
definition: Plasticised vinyl — historically ubiquitous in cheap soles, welts, air-blown sandals, coated fabrics and prints; now a headline restricted material at major brands.
key_parameters:
  - {name: status, unit: compliance, typical: "prohibited outright in NB footwear/apparel/equipment (Beilstein screen + FTIR confirm); phthalate plasticisers separately capped (sum 500 mg/kg class limits)", confidence: high, source: nb-rsm-2024}
compliance_flags: [pvc-restricted-major-brands, phthalate-risk]
failure_modes: [plasticiser migration → embrittlement, cold crack, compliance rejection]
cost_drivers: [cheapest mouldable 'rubbery' plastic — which is exactly the trap]
relationships: {legacy_uses: [cmp-welt (PVC welt), rain boots, prints], substitutions: [mat-tr, mat-tpu, TPU/water-based inks per approved-ink lists]}
sources: [nb-rsm-2024, tsc-8con]
confidence: high
status: seed
---
Kept in the doctrine precisely because it's banned: you can't spec substitutions for what you can't name. PVC welts and PVC screen inks are the two places it still sneaks into footwear supply chains.
