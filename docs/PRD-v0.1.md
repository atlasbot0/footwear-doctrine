---
date: 2026-07-04
source_runtime: other
project: footwear-doctrine
agent_role: pm-agent
decision_status: surfaced
linked_files: []
tags: [footwear-doctrine, prd, research-brief, knowledge-base, llm-kb, rollie, componentry]
summary: "PRD v0.1 for the Footwear Doctrine — an exhaustive shoe componentry, materials and construction knowledge base built for LLM retrieval and platform tooling"
next_action: "Vince confirms §4 terminology, approves scope and Phase 1 kickoff"
---

# Footwear Doctrine — PRD v0.1

**Working title:** Footwear Doctrine (codename open — see Open Questions)
**Owner:** Vince Lebon
**Status:** Draft for review. No research executed beyond a first-round resource scan.
**Date:** 4 July 2026

---

## 1. Intent

Build the most complete machine-readable body of knowledge on footwear componentry, materials, construction and manufacturing that exists outside a factory's head. Not a glossary. A doctrine — every component, every material, every construction method, every spec parameter, every test standard, every failure mode, cross-linked and cited.

The doctrine is not the product. It is the substrate. It exists to be loaded into an LLM knowledge base (LightRAG / retrieval layer on the existing three-tier stack) so that platforms and tools can be built on top of it: spec generators, tech-pack copilots, material selectors, costing estimators, factory QA assistants, design education products, and the internal spec system for Rollie and Rob Miles product development.

Two hard requirements distinguish this from "scrape the internet about shoes":

1. **Spec-grade depth.** Not "EVA is a foam used in midsoles" but density ranges in kg/m³, Asker C / Shore hardness bands, compression-set behaviour, CM vs injection phylon process implications, hydrolysis and yellowing risk, cost drivers, and which test standard verifies each property.
2. **Retrieval-grade structure.** Every entity carries a schema, controlled vocabulary with aliases, units, relationships, provenance and a confidence rating. A file without metadata is invisible to the OS — same rule as canonical outputs.

## 2. Non-goals (v1)

- Retail, marketing, brand or trend content. This is manufacturing and design engineering only.
- Machine operation manuals (how to service a Ströbel machine). We capture what the machine does to the shoe, not how to maintain it.
- A consumer-facing product. v1 output is the corpus + schema + retrieval evals, nothing shipped externally.
- Regional labour/compliance law beyond what touches product spec (chemical compliance is in scope; factory audit protocol is not).
- Reproducing paywalled standards text verbatim (see §9, Licensing). We capture the facts, parameters and requirements in our own words with citation.

## 3. End-state definition

Done for v1 means:

1. A frozen ontology and entity schema (see §6).
2. A corpus of **500+ canonical entities** across the 16 domains in §5, every entity cited to at least one source, every numeric spec parameter triangulated to two sources or flagged.
3. A **source register** of 150–300 graded resources (tiered, licensed-status flagged, acquisition status tracked).
4. **Complete specification capability for footwear** — a master spec template covering every component from lace tip to outsole compound, validated by fully populating reference specs for archetype products spanning the construction space (see §7).
5. Corpus ingested into LightRAG + mirrored to Notion, with a **golden Q&A eval set (150–200 questions)** and ≥90% retrieval-answer pass rate on expert review.

## 4. Terminology normalisation (dictation → canonical)

The brief was dictated; several terms need locking before they enter the controlled vocabulary. This mapping doubles as the first alias table. Confirm or correct:

| As dictated | Canonical term (proposed) | Notes |
|---|---|---|
| "double road" | double row (stitching) | Row configurations: single, double, triple, twin-needle gauges |
| "interlock" | interlock stitch / interlock knit | Both captured — stitch class and knit fabric are separate entities |
| "lace debris" | lace deubré (dubrae) | The lace tag/jewel, e.g. AF1-style |
| "back counter toolbox" | heel (back) counter + toe box | Two entities |
| "Last spec chat" | last spec chart | The last specification sheet |
| "foot plant" | foot plant (gait) + last bottom plan | Both captured: biomechanics of foot strike, and the last bottom pattern |
| "for lasted" | board-lasted / force-lasted | Both captured as distinct lasting methods |
| "rapid welt stitch" | Blake Rapid (Blake/Rapid construction) | Midsole Blake-stitched, outsole rapid-stitched |
| "staccato" | sacchetto **or** San Crispino | Both captured — sacchetto (bag-lasted Italian construction) and San Crispino (lasting edge folded over insole, stitched). Confirm which was meant; doctrine includes both |
| "stitch out" | stitchout / stitchdown (veldtschoen) | Flanged-out upper stitched to sole |
| "hand fill" | hand / hand-feel (temper) | Leather and textile handle |
| "replacement pattern" | placement print (vs repeat print) | Textile print engineering; also captures placement vs repeating pattern in cutting/nesting |
| "it's got oil so it's got a foil" | oil / pull-up finish; foil (metallic) finish | Two leather finish families |
| "stable frame" | stability frame / shank / stabiliser | Includes external heel clips, torsion units, plates |
| "complete specs for four specifically" | complete specs **for shoes/footwear** specifically | Brief-level fix, confirmed by Vince 4 Jul — resolved in §7 |

## 5. Scope — the domain map

Sixteen domains. Each lists representative sub-entities and the spec parameters the research must capture. This map is the checklist Phase 3 executes against; it is deliberately wider than the dictated list because the brief said "this is not extensive — there's even more."

### D1. Foot, fit and biomechanics
Foot anatomy (bones, arches, soft tissue), foot types, gait cycle and foot plant (heel strike, midstance, toe-off, pronation/supination), pressure mapping, foot dimensions (foot length, ball girth, waist girth, instep girth, long/short heel girth, heel width, toe depth, heel-to-ball), population anthropometrics, 3D foot scanning, Brannock method.
**Parameters:** all girths/lengths in mm, size-grading increments, foot-to-last allowances by category (dress vs athletic vs sandal), kids' growth allowances.

### D2. Sizing and grading systems
UK, US men's/women's, EU/Paris point, CM/JP, Mondopoint; width fittings (A–EEE, UK F/G/H); conversion logic and its failure points; grade rules (length and girth increments per size); half-size and width grading; last grading vs pattern grading vs sole/tooling grading.
**Parameters:** increment tables per system, tooling size-run economics.

### D3. The last
Types (dress, athletic, boot, sandal, pump, unisex); materials — wood (beech/maple), plastic (HDPE/HMWPE), aluminium (vulcanising and injection), 3D-printed; hinge and split types (scoop block, V-hinge, telescopic); the last spec chart: stick length, ball girth and width, instep, waist, heel curve, cone, back height, toe spring, heel pitch/height, featherline, toe shape and recede, bottom plan and bottom radius; last-to-foot allowance logic; lastmaking process (turning, CAD/CAM — Shoemaster, ICad3D+, Delcam heritage); fitting-trial protocol and pullover tests.
**Parameters:** every chart value with units and typical ranges by category; toe spring vs heel height vs rocker relationships.

### D4. Patterns and upper engineering
Mean form / forme development, standard creation, pattern springing (when and why a pattern must be sprung), design lines and panel logic (vamp, quarter, mudguard, eyestay, counter pocket, collar), allowances — lasting margin, folding, underlay/overlay seam allowances, stitching edge distances; grading; nesting and cutting yield; leather cutting direction and stretch (tight-to-toe); repeat vs placement patterns in cutting and print; CAD toolchain.
**Parameters:** allowance values in mm by operation, yield percentage norms by material.

### D5. Upper materials
Leathers — full grain, top grain, corrected grain, splits, suede, nubuck; tannage (chrome, vegetable, chrome-free/wet-white); finishes — aniline, semi-aniline, pigmented, pull-up (oil/wax), patent, foil/metallic, brush-off, burnished, embossed; leather specs — thickness (mm and oz), substance tolerance, break/pipiness, temper/hand, cut yield, lastability. Textiles — canvas, denim, ripstop, flat/circular/jacquard/engineered knits, sandwich and air mesh. Synthetics — PU leather, microfibre (Clarino-class), coated fabrics, TPU films and welded overlays, KPU mouldings. Surface character — shine/gloss, nap and shading direction, drag, patina and ageing behaviour.
**Parameters:** thickness, GSM/denier, Martindale abrasion, colourfastness (crocking, light), flex resistance, water resistance, tensile/tear.

### D6. Linings and inner environment
Leather linings (pig, sheep, calf), textile linings (cambrelle-class non-wovens, spacer mesh), seamless/Strobel sock constructions, waterproof-breathable membranes and bootie systems (GORE-TEX, Sympatex, OutDry-class), moisture management, antimicrobial treatments, vamp vs quarter lining strategies, unlined constructions.
**Parameters:** MVTR/breathability, abrasion (lining-grade), wicking, thickness.

### D7. Padding and foams (comfort package)
Collar and tongue foams — open-cell PU, latex, EVA sheet, memory/slow-recovery, reticulated; Achilles pillow; padding lamination and quilting; density and firmness selection by touchpoint.
**Parameters:** density kg/m³, Asker C hardness, compression set %, thickness.

### D8. Reinforcement and structure
Toe puffs/toe boxes — thermoplastic sheet, solvent-activated, leatherboard; safety toes (steel/composite, EN ISO 20345 context); heel (back) counters — thermoplastic, leatherboard, moulded external TPU clips; side stabilisers and eyestay reinforcement; fusible tapes and backers; shanks — steel, nylon, fibreglass, carbon; torsion systems; plates.
**Parameters:** activation temperatures, thickness, stiffness values, back-part moulding specs, ISO 18896 shank stiffness context.

### D9. The bottom stack
Insole board (cellulose/Texon-Bontex class, non-woven Strobel board, poly board; Goodyear rib/gemming); sockliner/inner sock (die-cut EVA, moulded PU, OrthoLite-class, cork-latex, leather; top cloth); midsole — EVA (compression-moulded vs injection phylon), dual density, PU, supercritical/bead foams (E-TPU, PEBA, nitrogen-infused), drop-in vs Strobel-attached; posts, crash pads and decoupled heels; wedges; outsole — rubber compounds (carbon, blown, gum, natural/SBR blends), TR, TPU, PU, EVA outsole, KPU, ABS (heels), leather, crepe; cupsole vs sheet vs unit sole; lug geometry, siping, flex grooves, traction pattern design by surface; stack height, drop/offset, toe spring interaction with sole geometry.
**Parameters:** density, Shore A/Asker C hardness bands per compound, abrasion (DIN/ISO 4649 mm³), wet/dry slip (SATRA TM144 / EN ISO 13287 / ASTM F2913 lineage), flex (Ross/Bennewart), shock absorption, hydrolysis and yellowing risk.

### D10. Constructions and lasting methods
Cold cement (the default athletic/casual method), vulcanised (autoclave + foxing tape), Goodyear welt (gemming, cork fill, storm/split reverse welts), hand welt, Blake/McKay, Blake Rapid, stitchdown/veldtschoen, Norwegian, San Crispino, sacchetto, California/slip-lasted, true moccasin, Bologna, opanka, string-lasted, board-lasted vs force-lasted (Strobel) vs slip-lasted, direct injection (PU/TPU/PVC DIP), stitch-and-turn (turnshoe), full-moulded. For each: layer diagram, process sequence, machinery, weight/flexibility/water-resistance/resoleability profile, tooling cost and MOQ implications, brand archetypes.
**Parameters:** a construction selection matrix scoring each method across ~10 attributes.

### D11. Closing room — stitching, seams, threads
Stitch classes (ISO 4915 — 301 lockstitch, 401 chainstitch, 304 zigzag, 500-class overedge, moc stitch); seam classes (ISO 4916 — superimposed, lapped, bound, flat); row configurations — single, double, triple row, twin-needle gauges; edge distance and row gauge conventions; SPI/stitch density norms for uppers; seam strength engineering (SPI × thread strength × stitch-type factor); functional vs decorative stitching; bar tacks; needle systems, sizes and points for leather vs textile; threads — bonded nylon, polyester (Gral-class), corespun; Tex/ticket sizing; vulcanisation yellowing of nylon threads; edge treatments — folded, raw, skived, French binding; skiving specs.
**Parameters:** SPI bands by application, edge distances in mm, thread size selection tables, seam strength formulas and test methods.

### D12. Closures and trims
Laces (round/flat/oval, braided polyester, waxed cotton, elastic; tipping/aglets — acetate, metal); lace deubré; eyelets (blind, washered, sizes), speed hooks, D-rings, webbing loops, ghillies; zips (metal, coil, moulded; gauge sizes; waterproof; locking vs auto-lock sliders; footwear-grade bottom stops); buckles, snaps, hook-and-loop (sew vs weld), elastic gussets (gauge, stretch %, braided vs knitted), dial/lace-reel systems (BOA-class), cordlocks and toggles; ornaments — metal badges, TPU logos, HF-welded appliqués, heat transfers, embroidery, screen/pad print, foil print, deboss/emboss.
**Parameters:** zip gauge sizes and cycle-test values, eyelet pull-out strength, gusset stretch specs, trim fatigue tests.

### D13. Adhesives and chemistry
Adhesive families — solvent and water-based PU, neoprene/CR contact, hot melts (EVA/PA/PES for toe puffs, folding, lasting); primers and surface prep — halogenation of rubber, UV primers, roughing/scouring; crosslinkers/hardeners; open time, green strength, activation temperature and pressing parameters; bond testing (peel strength, SATRA TM411-class, rapid sole adhesion); failure modes — contamination, under-activation, hydrolysis, plasticiser migration; the impact of glue selection on flexibility, creep, yellowing and recyclability; VOC/REACH pressure and the shift to water-based systems; mould making and release agents.
**Parameters:** peel strength requirements N/mm, activation temps, coverage rates, pot life.

### D14. Manufacturing process flow and QA
Cutting (clicker dies, CNC knife, laser and edge sealing), splitting and skiving, preparation (marking, punching, embossing), closing, lasting (heat conditioning, toe/side/seat lasting, wrinkle standards), bottoming lines, heat setting and chilling, finishing (edge ink, waxes), lacing and treeing, packing; QC systems — inline vs final, AQL sampling, metal detection and broken-needle policy; fitting and wear-test protocols; sample stages (pullover, CFM, salesman sample, confirmation).
**Parameters:** AQL levels, standard tolerances (component placement ±mm), takt-relevant operation lists.

### D15. Testing, standards and compliance
The standards landscape: SATRA test methods (250+ catalogue), ISO/TC 216 footwear test methods and ISO 19952 vocabulary, ISO/TC 137 sizing (19407/19408, Mondopoint), EN ISO 20344/20345 safety footwear, ASTM footwear methods, AATCC colourfastness; whole-shoe vs component tests; chemical compliance — REACH, CA Prop 65, CPSIA (children's), phthalates, PFAS restrictions; care labelling.
**Parameters:** a crosswalk table mapping every property in D5–D13 to its governing test method(s) and typical pass thresholds by product category.

### D16. Commercial, costing and sustainability
BOM structure and consumption/yield maths (leather sq-ft logic); FOB cost anatomy; tooling amortisation (outsole moulds per size); MOQs and colourway minimums; HTS/duty classification basics; sample and development cost norms. Sustainability: LWG tanneries, chrome-free tanning, recycled content (rPET, recycled rubber), bio-based EVA, water-based cements, design for disassembly, Higg/LCA framing, EU digital product passport direction — directly relevant to the platform ambition.
**Parameters:** BOM field standard, cost-driver flags per entity.

Domains D1–D16 are the coverage contract. Anything discovered in Phase 1 that doesn't fit gets a new sub-domain proposal, not silent inclusion.

## 6. Data architecture

Follows the existing three-tier pattern: **Git/Markdown canonical → Notion mirror → LightRAG retrieval.**

Proposed repo: `~/Code/vince-agents/knowledge/footwear-doctrine/` (or standalone `footwear-doctrine` repo — decide at kickoff).

```
footwear-doctrine/
  ontology/schema.yaml          # entity types, fields, controlled vocab rules
  entities/
    components/                 # one .md per entity, YAML frontmatter + body
    materials/
    constructions/
    processes/
    properties/
    standards/
    tools-machinery/
  sources/register.yaml         # graded source register w/ licence status
  specs/                        # the four reference specifications
  evals/golden-qa.yaml          # retrieval eval set
  docs/                         # this PRD, taxonomy notes, decisions
```

**Entity types:** component, material, construction, process, property, standard, supplier-class, tool. Relationships are first-class: `part_of`, `made_from`, `attached_by`, `shaped_by`, `tested_by`, `fails_by`, `substitutes_for`.

**Entity template (worked example):**

```yaml
---
id: cmp-heel-counter
type: component
names: [heel counter, back counter]
aliases: {UK: stiffener, IT: contrafforte, factory: counter}
domain: D8-reinforcement
function: "Holds heel shape, locks calcaneus, prevents backpart collapse"
position: "Rear quarter, between upper and lining (or external clip)"
materials: [thermoplastic-sheet, leatherboard, moulded-tpu]
key_parameters:
  - {name: thickness, unit: mm, typical: "1.2–2.0", confidence: medium}
  - {name: activation_temp, unit: "°C", typical: "60–85", confidence: medium}
  - {name: height, unit: mm, note: "driven by last back height"}
processes: [skiving, back-part-moulding, heat-activation]
tested_by: [backpart-stiffness, dimensional-stability]
failure_modes: [collapse, edge print-through, delamination, cracking]
cost_drivers: [material grade, moulded external vs internal sheet]
relationships:
  part_of: [quarter-assembly]
  shaped_by: [last-heel-curve]
  attached_by: [hot-melt-adhesive, stitching]
sources: [{ref: motawi-hsam-2020, loc: "ch. reinforcements"}, {ref: satra-bulletin}]
confidence: draft
---
Body: prose explanation, diagrams, regional practice notes, spec guidance.
```

Rules: no entity without a source; numeric values carry confidence; aliases are mandatory (this domain is terminology-chaotic across US/UK/IT/factory-floor usage — ISO 19952 vocabulary is the tie-breaker where it exists); units SI-first with imperial in parentheses; chunking for RAG at entity level with frontmatter embedded.

## 7. Complete specifications for footwear

The dictated "complete specs for four specifically" resolves to **complete specs for shoes/footwear**: the doctrine must be able to fully specify a shoe — any shoe — end to end. Two deliverables carry that requirement:

1. **Master spec template.** A tech-pack-grade line-item schema, 50–80+ fields per shoe: every component from D1–D16 instantiated with material call-out, dimensions and tolerances, stitch spec (type, SPI, gauge, thread), adhesive system, lasting method, test plan and cost-driver annotations. Modelled against real factory spec formats acquired in P1 (Motawi's bundle ships a genuine line-item factory spec in .xls — a direct structural reference).
2. **Archetype reference specs as the acceptance test.** To prove the template + corpus can spec anything, P4 populates full reference specs for a small set of archetypes spanning the construction space — proposed: cold-cemented leather derby (Rollie core DNA), vulcanised sneaker, Goodyear-welted boot, Strobel/force-lasted trainer, and a sandal to exercise open constructions. Count is flexible; coverage is the point. Any line item the doctrine can't populate is a P3 gap and loops back.

Once validated, the same template becomes the working spec backbone for Rollie and Rob Miles product development.

## 8. Research methodology and phases

| Phase | Work | Output | Est. effort |
|---|---|---|---|
| P0 | This PRD | Approved brief | Done |
| P1 — Resource harvest | Systematic source discovery and acquisition across the tiers in §10; grade each source; buy the short-list of books/standards; digitise first-party assets (Rollie tech packs, factory spec sheets, Fitzroy swatch library, Pensole materials) | `sources/register.yaml`, 150–300 graded entries; acquisition list with costs | 2–3 days agent time + purchase approvals |
| P2 — Ontology freeze | Lock schema, controlled vocabulary seed (ISO 19952-aligned), domain map amendments | `ontology/schema.yaml` v1 | 1 day |
| P3 — Deep extraction | Domain-by-domain entity build via Claude Code agents; every entity cited, numerics triangulated ×2 or flagged; weekly batch review | 500+ entities | 2–4 weeks part-time, parallelisable per domain |
| P4 — Spec template + reference specs | Build the master spec template; populate archetype reference specs from the corpus; gaps loop back to P3 | Master template + 4–5 archetype specs | 1 week |
| P5 — SME validation | Vince review + factory partner spot-checks (and Betts/Michael where useful); confidence upgrades; corrections logged | Validated corpus | 3–5 days elapsed |
| P6 — Ingestion + evals | LightRAG ingestion, Notion mirror, golden Q&A set built and scored | Live KB + eval report | 2–3 days |

Execution surface: Claude Code on Atlas with parallel domain agents; deep-research runs for P1; defuddle for scraping; archive.org bulk ingestion for public-domain texts. Checkpoint gates after P1 (approve purchases) and P2 (approve schema) before the heavy P3 spend.

## 9. Licensing and copyright posture

This matters because the corpus feeds commercial tooling.

- **Public domain (ingest verbatim):** the classical technical literature — Golding's 1902 treatise and multi-volume series, Swaysland, Plucknett — is public domain and freely ingestible in full. These are unusually deep on bottoming, welting, lastmaking, pattern drafting and adhesives, and they anchor the traditional-construction domains at zero licence risk.
- **Paywalled standards (facts only, never text):** SATRA test methods and ISO standards are purchased documents. We buy the priority set, extract requirements/parameters in our own words with citation, and never store or reproduce their text. ISO 19952 (footwear vocabulary) is the one near-mandatory purchase — it seeds the controlled vocabulary.
- **Commercial books (owned copies, synthesis only):** Motawi's series, Luximon's handbook, Choklat, etc. Purchased, read, synthesised into entities with page-level citation. No verbatim reproduction.
- **Supplier technical literature (freely published, cite and synthesise):** Coats, YKK, Vibram, Texon, OrthoLite-class datasheets and info hubs are published for exactly this use; capture with attribution.
- **First-party (unrestricted):** Rollie tech packs, factory spec sheets, swatch library, Pensole notes — the proprietary tier that makes this doctrine non-replicable. Flag anything factory-confidential so it can be excluded from any externally-shipped product later.

## 10. First-round resource map

Scan completed 4 July 2026. Tiered, with acquisition status. Phase 1 expands this to the full register.

**Tier 1 — Practitioner texts (buy):**
- Wade Motawi / Shoemakers Academy: *How Shoes are Made* (26 chapters: design, materials, stitching, outsoles, tooling, EVA forming, lasts, pricing, QC), *Shoe Material Design Guide*, *Footwear Pattern Making and Last Design* (covers toe spring, heel height, ball girth, cuboid roll, cone, last geometry, grading — and pattern springing explicitly), *How to Start Your Own Shoe Company*. The Start-Up Pro bundle includes real factory patterns, an 8-page spec drawing, a line-item spec in .xls, and outsole blueprints — direct schema references for our spec template. (sneakerfactory.net / shoemakersacademy.com)
- Tim Skyrme *Bespoke Shoemaking*; Aki Choklat *Footwear Design*; making-focused titles (sandal, handmade boot guides) as secondary. *(verify editions in P1)*

**Tier 2 — Academic and reference (buy/licence):**
- Luximon (ed.), *Handbook of Footwear Design and Manufacture*, 2nd ed., Elsevier/Textile Institute — foot anatomy, biomechanics and gait, foot measurement, last design/manufacture, sizing and grading, plus AI personalisation and green footwear chapters.
- *Footwear Science* journal (Taylor & Francis) for biomechanics/comfort science. *(verify access route in P1)*
- Goonetilleke, *The Science of Footwear*. *(verify in P1)*

**Tier 3 — Standards bodies (selective purchase + free surface content):**
- SATRA: 250+ test method catalogue; the Bulletin archive is freely readable and unusually rich (e.g. sole testing series covering shock absorption TM142, rapid sole adhesion TM404, slip TM144, whole-footwear abrasion TM362, heel security TM96). Membership question flagged for P1.
- ISO/TC 216 (footwear tests + ISO 19952:2025 vocabulary, 51pp, CHF 199) and ISO/TC 137 (sizing: ISO 19407/19408, Mondopoint conversion logic). iTeh previews give free scoping before purchase; TC 216 WG1 abstracts already surface component standards (sole adhesion, insole stitch tear ISO 20876, shank stiffness ISO 18896, stiffener bondability ISO 20863, sole flex ISO 17707).
- EN ISO 20344/20345 for the safety-footwear reference frame.

**Tier 4 — Supplier technical libraries (free, authoritative on their component):**
- Coats info hub: footwear FAQ (SPI norms of 8–10 for adult uppers, thread recommendations, nylon-yellowing-under-vulcanisation warning), seam-strength formula (SPI × thread strength × stitch factor), seam type and thread selection bulletins, thread consumption guide. American & Efird SPI technical bulletins as a second thread source.
- YKK/Opti zip specifications; Vibram sole catalogue; Texon/Bontex insole boards; OrthoLite; membrane suppliers; BASF/Covestro/Huntsman PU-TPU literature; tannery guides (LWG). *(enumerate fully in P1)*

**Tier 5 — Public domain classics (free, ingest verbatim):**
- Golding, *The Manufacture of Boots and Shoes* (1902) — archive.org, public domain; the Google Books index alone shows depth on girths, grading, formes, springing, skiving, seams.
- Golding (ed.), *Boots and Shoes: Their Making, Manufacture and Selling*, multi-volume — archive.org + the Honourable Cordwainers' Company hosts clean PDFs; Vol. VI covers upper material selection, closing, bottom-stuff preparation, adhesives, insole prep, welting, costing.
- Swaysland, *Boot and Shoe Design and Manufacture* — public domain scan on archive.org.
- Plucknett, *Boot and Shoe Manufacture* (1916) — public domain; foot anatomy + patterns.

**Tier 6 — Institutional and course material:**
- UNIDO Leather Panel (leatherpanel.org) — free technical publications including a full pattern-making engineering course PDF (last copying, feather edge, forme development). High-value, free, institutional.
- Arsutoria (school + magazine archive), SLEM, FDRA courses and podcast, ShoeSchool/DigiLast last-collection documents (measurement charts + last glossary). *(verify current offerings in P1)*

**Tier 7 — Enthusiast/deep-craft (triangulation and photography):**
- Shoegazing construction guides (gemming, Blake/Rapid mechanics, storm welt distinctions), Total Shoe Concept (8-construction overview incl. San Crispino and DIP), Heddels construction guide (veldtschoen history, Norwegian vs storm welt), Misiu Academy (vulcanising process detail — aluminium lasts, autoclave, foxing). Rose Anvil-style teardown video channels for cross-section evidence. The Crispin Colloquy forum for bespoke edge cases. *(register in P1)*

**Tier 8 — First-party (proprietary moat):**
- Rollie tech packs and factory spec sheets; Iconic/DJ compliance specs; Fitzroy material swatch library (digitisation workstream); Vince's Pensole and Adidas Brooklyn training materials; Betts Group knowledge via the Rob Miles workstream; factory partner Q&A during P5.

**Tier 9 — Patents:** Google Patents for midsole chemistry, construction methods and test-method citations (e.g. traction patents that document SATRA/ASTM slip protocols in the open).

## 11. Success metrics

- Coverage: 16/16 domains populated; ≥500 entities; master spec template complete and every archetype reference spec fully populated with zero "unknown" line items.
- Citation: 100% entities sourced; ≥80% of numeric parameters dual-sourced; remainder flagged low-confidence.
- Retrieval: ≥90% pass on the 150–200 question golden set (graded by Vince/SME); answers cite entities, not vibes.
- Utility proof: one downstream tool prototype (e.g. tech-pack field auto-suggester) can be built against the KB without new research.

## 12. Risks

- **Terminology chaos** (same part, five names, three countries) → mitigated by alias-mandatory schema + ISO 19952 as tie-breaker.
- **Standards paywall cost creep** → P1 produces a priced purchase list for approval before buying; SATRA membership decision made once, deliberately.
- **Hallucination contamination** → hard rule: no entity without a citation; numeric triangulation; SME spot-checks in P5.
- **Supplier marketing bias** → supplier claims marked as such until independently verified.
- **Scope creep into retail/trend** → non-goals enforced at weekly batch review.
- **Dictation ambiguities entering the vocabulary** → §4 table must be confirmed before P2 freeze.

## 13. Open questions (Vince to call)

1. **Sacchetto vs San Crispino** and any other §4 corrections.
2. **Archetype set for §7:** derby / vulcanised / Goodyear / Strobel / sandal as proposed, or redline?
3. **Repo home:** inside `vince-agents/knowledge/` or standalone repo?
4. **Budget envelope for P1 purchases** (books ~AUD 300–500; ISO/SATRA documents potentially AUD 1–3k depending on the shortlist; SATRA membership is a separate, larger call).
5. **First-party digitisation:** green-light scanning Rollie tech packs and the swatch library into the proprietary tier in P1, or defer to P3?
6. **Codename:** Footwear Doctrine as-is, or name it (e.g. LASTWORK, DOCTRINE, CORDWAIN)?

---

*Approve scope + answer §13, and P1 kicks off with the graded source register as the first deliverable.*
