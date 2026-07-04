---
id: cmp-zip
type: component
names: [zip, zipper, slide fastener]
aliases: {US: zipper, UK: zip}
domain: D12-closures-trims
definition: Toothed closure for boot shafts and entry systems; metal, moulded (Vislon-class) or coil.
function: Entry/exit closure where lacing is impractical; decorative entry on fashion boots.
position: Medial shaft (boots), heel entry, decorative panels.
key_parameters:
  - {name: chain gauge, unit: "#", typical: "footwear commonly #5–#10; heavier for boots", confidence: medium, source: ykk-opti}
  - {name: slider/locking, unit: n/a, typical: "auto-lock sliders for shafts; reversed/waterproof tapes available", confidence: high, source: ykk-opti}
tested_by: [std-satra-fastener-family]
failure_modes: [slider wear, tooth loss, tape seam failure, bottom-stop burst]
cost_drivers: [metal vs coil vs moulded, brand (YKK) vs generic, waterproofing]
compliance_flags: [nickel-release]
relationships: {brand_examples: [brd-ykk], pairs_with: [cmp-elastic-gusset for fit forgiveness]}
sources: [ykk-opti, satra-catalogue]
confidence: medium
status: seed
---
Spec chain type + gauge + slider + tape colour + top/bottom stop; burst and cycle testing sit in the SATRA fastener family.
