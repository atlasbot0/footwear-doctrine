# Footwear Doctrine — structured library v0.2 (seed)

Machine-readable knowledge base of footwear componentry, materials, constructions,
processes, properties and standards. Built as the substrate for LLM retrieval
(LightRAG) and downstream tooling: spec generators, tech-pack copilots, material
selectors, QA assistants.

## Structure

```
ontology/     schema.yaml (entity contract) + controlled-vocabulary.yaml (aliases, decodes)
entities/     one .md per entity, YAML frontmatter + short body
  components/                    physical parts of a shoe
  materials/leathers/            by animal + tannage + finish
  materials/textiles/            wovens, knits, meshes
  materials/synthetics/          PU leather, microfibre, films
  materials/polymers-foams-rubbers/  EVA, PU, TPU, TR, rubbers, boards, leather soling
  materials/branded/             IP / trade-name register (Cordura, Vibram, etc.)
  constructions/                 lasting + sole-attachment methods
  processes/                     manufacturing operations
  properties/                    measurable spec parameters
  standards/                     test methods + compliance frameworks
sources/      register.yaml — graded source register with licence posture
specs/        master spec template + first-party reference observations
evals/        golden Q&A seed for retrieval evaluation
scripts/      validate_library.py, build_index.py
docs/         PRD, decisions log
INDEX.md      generated entity index
```

## Rules (non-negotiable)

1. No entity without a `sources` list. 2. Numeric values carry `confidence`
(high/medium/low). 3. Aliases are mandatory where terminology varies (US/UK/IT/
factory floor); ISO 19952 is the tie-breaker. 4. SI units first. 5. Facts from
paywalled standards are paraphrased, never reproduced. 6. Run
`python3 scripts/validate_library.py` before committing; `build_index.py` to
regenerate INDEX.md.

## Status

v0.1 seed — schema frozen for review, ~115 seed entities weighted to materials
(incl. branded IP), components and constructions. Phase 3 (deep extraction to
500+ entities, dual-source triangulation) runs against this scaffold.
Canonical home: `~/Code/vince-agents/knowledge/footwear-doctrine/` (or standalone
repo — open decision in docs/PRD-v0.1.md §13).
