# Decisions log

## 2026-07-04 — v0.1 seed scope
- Seed targets breadth-with-teeth: every category populated, materials weighted per brief
  (ripstop, engineered knits, leathers by animal, branded IP names, leather soles,
  leatherboard, PVC welt, wovens).
- Branded/IP entities get `type: brand` with `generic_equivalent` cross-links so retrieval
  answers both "what is Cordura" and "what generic material class is it".
- NB RSM 2024v1 synthesised at framework level (field schema, testing matrix logic,
  policy positions) — facts with attribution, no text reproduction.
- Upload gap: Specs.docx, Spec_Guidence.docx, NB_Spec_Sheet.docx and
  New_Shoe_Spec_Detailed_Template.csv arrived empty / absent from disk. Template built
  from NB 1906R sheet + tech-pack norms; merge Vince's templates when re-sent.
- Numeric ranges from model knowledge marked confidence: medium and flagged for P3
  dual-source triangulation. First-party 1906R values cited as nb-1906r-sheet.

## 2026-07-04 — v0.2 merge
- Upload gap resolved via PDF export route; docx/csv originals still stall as cloud placeholders.
- Vince's templates registered as first-party but flagged AI-drafted/Vince-curated — benchmarks
  carry confidence medium until factory corroboration; where they agree with the 1906R sheet
  (collar ~30 kg/m³, vamp EVA 1.5–2 mm) confidence effectively strengthens.
- "9-Jul" in the SPI column decoded as Excel date-mangling of 7–9 — logged as a data-hygiene
  lesson for CSV ingestion (P3 rule: quarantine date-typed cells in numeric columns).
- Outsole hardness spread noted: guidance band 70–80 Shore A vs 1906R NDurance 85–90 —
  both true (general band vs hard-wearing carbon compound); doctrine stores both with context.
