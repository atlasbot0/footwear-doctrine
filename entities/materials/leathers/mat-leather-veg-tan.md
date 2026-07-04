---
id: mat-leather-veg-tan
type: material
names: [vegetable-tanned leather]
aliases: {trade: veg tan, sole-grade: oak bark / pit-tanned bends}
domain: D5-upper-materials
definition: Tannin (bark/wood extract) tannage — firm, mouldable, burnishable, patinas; the tannage of soles, welts, insoles and tooling leather.
key_parameters:
  - {name: character, unit: n/a, typical: "firm temper, wet-mouldable, edges burnish, darkens with wear", confidence: high, source: golding-1902}
  - {name: process time, unit: n/a, typical: "weeks (drum) to 12+ months (pit) for sole bends", confidence: medium, source: model-knowledge}
failure_modes: [water spotting, stiffness if over-tanned, higher cost]
cost_drivers: [tannage duration, tannin source]
relationships: {feeds: [mat-leather-sole, cmp-welt, cmp-insole-board (leather option)], contrast: [mat-leather-chrome-tan]}
sources: [golding-1902, model-knowledge]
confidence: medium
status: seed
---
Everything structural-and-traditional in a welted shoe is veg tan; it's the tannage that behaves like a material you can carve.
