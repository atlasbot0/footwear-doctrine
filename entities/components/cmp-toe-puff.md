---
id: cmp-toe-puff
type: component
names: [toe puff, box toe]
aliases: {US-colloquial: toe box, IT: puntale, safety: toe cap}
domain: D8-reinforcement
definition: Stiffener over the toe that preserves toe-box shape and protects the forepart; distinct from the toe box (the space it creates).
function: Toe shape retention, scuff protection, crease control at the vamp break.
position: Between upper and lining at the forepart, set back from the featherline.
materials: [mat-syn-tpu-film, mat-leatherboard]
key_parameters:
  - {name: thickness, unit: mm, typical: "0.6–1.2 sheet; 0.6–0.8 observed (1906R)", confidence: high, source: nb-1906r-sheet}
  - {name: setback from toe tip, unit: mm, typical: "~30 observed (1906R); style dependent", confidence: high, source: nb-1906r-sheet}
processes: [prc-skiving, prc-lasting]
tested_by: [std-en-iso-20345]
failure_modes: [ridge print-through, delamination, collapse after wetting (solvent types)]
cost_drivers: [thermoplastic vs solvent-activated vs safety cap (steel/composite)]
relationships: {part_of: [vamp assembly], shaped_by: [last toe shape, toe spring], substitutes_for: [steel/composite safety toe under EN ISO 20345]}
sources: [nb-1906r-sheet, motawi-hsam]
confidence: high
status: seed
---
Grades run from soft (unstructured dress) to safety caps. Thermoplastic sheet dominates volume production: die-cut, skived, heat-activated during toe lasting so it takes the last's toe shape exactly.
