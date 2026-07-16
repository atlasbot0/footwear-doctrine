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
render: "VEGETABLE-TANNED LEATHER — Firm, dense bark-tanned hide with a warm natural tone that PATINAS and darkens with light and wear. Tight grain, stiff at first with a matte-to-low-satin natural finish (no heavy pigment). Distinct warm honey/tan undertone even when dyed; edges and flex points burnish to a glossy amber. Creases are firm and sculptural, holding structured folds. Natural tonal variation is pronounced — lighter on raised areas, richer amber in recesses. The heritage/artisanal choice — hand-welted boots, structured bags, saddle goods."
---
Everything structural-and-traditional in a welted shoe is veg tan; it's the tannage that behaves like a material you can carve.
