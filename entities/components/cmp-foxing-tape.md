---
id: cmp-foxing-tape
type: component
names: [foxing tape, foxing]
domain: D9-bottom-stack
definition: The uncured rubber strip wrapped around the sole edge/upper junction of a vulcanised shoe, fused to the assembly in the autoclave.
function: Bonds and seals upper to sole in vulcanised construction; defines the classic sneaker sidewall look.
position: Perimeter band over the sole/upper joint.
materials: [mat-rubber-gum, mat-rubber-carbon]
key_parameters:
  - {name: application, unit: process, typical: "laid up green (uncured), then cured 130–160 °C in autoclave", confidence: medium, source: misiu-con}
tested_by: [std-satra-sole-bond-family]
failure_modes: [foxing peel at toe, under-cure tack, over-cure embrittlement]
cost_drivers: [hand lay-up labour, autoclave cycle time]
relationships: {defines: [con-vulcanised], us_customs_note: "'foxing or foxing-like band' affects duty classification"}
sources: [misiu-con, tsc-8con]
confidence: medium
status: seed
---
Hand-applied, which is why vulcanised lines are labour-shaped despite cheap materials. The toe bumper is foxing's cousin.
