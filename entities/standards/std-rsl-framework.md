---
id: std-rsl-framework
type: standard
names: [RSL framework (brand restricted substances)]
aliases: {exemplar: NB RSM 2024v1, industry: AFIRM RSL}
domain: D15-testing-compliance
definition: The brand-side chemical governance structure — a Finished-Product RSL table (CAS number, substance, adult limit, children's limit, key regulations, test method, lab detection limit), plus packaging/EEE lists, testing matrices by material type, risk-tiered sampling and CAR corrective loops.
key_parameters:
  - {name: schema fields, unit: n/a, typical: "CAS | substance | limit(adult) | limit(child 0–14) | regulation basis | test method | MDL — the table grammar every supplier reads", confidence: high, source: nb-rsm-2024}
  - {name: hard positions (NB exemplar), unit: n/a, typical: "PVC prohibited outright; PFAS: banning detectable levels incl. raw-material purchase; DMFu prohibited; azo amines 20 mg/kg each; Cr(VI) 3 mg/kg with aging test; phthalates sum 500 mg/kg; formaldehyde 75 adult / 16 child mg/kg", confidence: high, source: nb-rsm-2024}
  - {name: testing logic, unit: n/a, typical: "risk-tiered sampling by supplier score + material type + colour risk (black/red/fluoro high) + treatments; approved labs (BV/SGS class); annual re-tests", confidence: high, source: nb-rsm-2024}
relationships: {constrains: [every material entity via compliance_flags], aligned_with: [afirm-rsl], animal_policy: "exotics prohibited; Amazon-biome bovine prohibited; calfskin prohibited (NB); kangaroo exit end-2024; mulesed wool banned"}
sources: [nb-rsm-2024, afirm-rsl]
confidence: high
status: seed
---
Synthesised at framework level from the NB RSM 2024v1 Vince supplied: the point isn't NB's numbers, it's that every major runs this grammar — the doctrine stores the grammar plus exemplar positions so specs can be written compliance-first.
