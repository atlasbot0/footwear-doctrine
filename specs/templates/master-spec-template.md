# Master spec template — field guidance (v0.1)

One CSV row per specifiable line item; sections UPPER / REINFORCEMENT / CLOSURE /
BOTTOM / ASSEMBLY / COMPLIANCE. Target 50–80 populated rows for a full production
spec — this seed carries 25 skeleton rows for a strobel-lasted sneaker.

Column rules:
- material_id — must reference a doctrine entity id (or TBD until specced).
- stitch spec travels as four fields: stitch_type_iso4915 + spi + rows + edge_distance_mm,
  with thread_spec (Tex + chemistry). "Double stitched" is not a spec.
- density_or_hardness — state the scale (Asker C ≠ Shore A).
- confidence — template | example-1906r (first-party observed) | specified (real value
  entered for a live product).
- compliance_flags — from ontology/schema.yaml vocab; COMPLIANCE section rows carry the
  RSL/MRSL package so chemistry is a line item, not an afterthought.

Row provenance in this seed: rows marked example-1906r carry values observed on the
NB 1906R factory sheet (uploaded 2026-07-04) as calibration anchors.
When Vince's own template files re-upload cleanly (Specs.docx, Spec_Guidence.docx,
NB_Spec_Sheet.docx, New_Shoe_Spec_Detailed_Template.csv), merge their fields/sections here.
