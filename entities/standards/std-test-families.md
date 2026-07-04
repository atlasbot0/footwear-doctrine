---
id: std-test-families
type: standard
names: [test-method families (placeholder map)]
domain: D15-testing-compliance
definition: Resolution map for the family-level test references used across entities before P1 acquires exact method numbers — each family names its SATRA/ISO territory.
key_parameters:
  - {name: families, unit: n/a, typical: "backpart (counter stiffness/set), seam (strength/burst), cushion (set/shock — TM142 class), sole-bond (TM404 class), upper (tensile/flex), lining-abrasion (Martindale class), crocking (colour rub), flex (fatigue), hydrolysis (aged PU), heel (pin retention — TM96 class), fastener (zip/eyelet), lace-abrasion, elastic (recovery), abrasion (general), sole-wear (whole-sole — TM362 class), insole (stitch-tear — ISO 20876 class), shank (ISO 18896 class)", confidence: medium, source: satra-catalogue}
relationships: {resolves: [all tested_by family references], replaced_by: "exact TM/ISO numbers during P1 acquisition"}
sources: [satra-catalogue, iso-tc216]
confidence: medium
status: seed
---
Honest placeholder: entities cite families now, exact method numbers land in P1 — the map keeps every reference resolvable meanwhile.
