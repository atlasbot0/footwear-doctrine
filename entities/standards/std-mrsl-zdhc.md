---
id: std-mrsl-zdhc
type: standard
names: [MRSL / ZDHC]
domain: D15-testing-compliance
definition: Manufacturing-side restricted substances — chemicals banned from the PROCESS (solvents, cleaners, primers, adhesives, inks) regardless of finished-product residues; ZDHC's MRSL is the industry list, with wastewater guidelines attached.
key_parameters:
  - {name: footwear-relevant bans, unit: n/a, typical: "toluene, benzene, DMF/DMAC/NMP-class solvents, MOCA, ozone-depleting agents — the cement/primer line is the exposure zone", confidence: high, source: nb-rsm-2024}
relationships: {governs: [prc-halogenation-priming chemistry, ink systems], pairs_with: [std-rsl-framework — product side], doc_hook: "factory Chemical Information List (CIL) inventories every chemical on site"}
sources: [nb-rsm-2024]
confidence: high
status: seed
---
RSL asks "what's in the shoe"; MRSL asks "what's in the factory". Cement lines answer to the second one.
