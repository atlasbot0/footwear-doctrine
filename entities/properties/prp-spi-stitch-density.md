---
id: prp-spi-stitch-density
type: property
names: [stitches per inch, SPI]
aliases: {metric: stitch length mm, machine: [lockstitch 301, chainstitch 401, zigzag 304 — ISO 4915 types]}
domain: D11-closing
definition: Stitch density of a seam — with thread size and stitch type, the seam-strength recipe of the upper.
key_parameters:
  - {name: anchors, unit: SPI/mm, typical: "uppers 6–10 SPI (1906R: ~4 mm pitch = 6–8 SPI); Coats guidance 8–10 for uppers", confidence: high, source: nb-1906r-sheet}
  - {name: strength model, unit: n/a, typical: "seam strength ≈ SPI × single-thread strength × 1.5 (lockstitch) or ×1.7 (chainstitch) — Coats rule", confidence: medium, source: coats-hub}
  - {name: trade-off, unit: n/a, typical: "too-high SPI perforates leather (tear-off line); too-low reads cheap and leaks strength", confidence: high, source: coats-hub}
  - {name: house benchmark, unit: SPI, typical: "7–9 SPI, Tex 60 lockstitch, tolerance ±1 (de-mangled from Excel '9-Jul')", confidence: medium, source: vince-spec-template}
tested_by: [std-iso-4915-4916, std-satra-seam-family]
relationships: {pairs_with: [prp-edge-distance-gauge, thread Tex size], vulcanising_note: "nylon thread yellows in autoclave — polyester for vulc (Coats)"}
sources: [coats-hub, nb-1906r-sheet, vince-spec-template]
confidence: high
status: seed
---
The seam recipe: type + SPI + thread + rows. Spec all four or you specced nothing.
