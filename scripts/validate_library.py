#!/usr/bin/env python3
"""Footwear Doctrine library validator (v0.1).
Checks every entities/**/*.md for: parseable YAML frontmatter, required fields,
enum validity, id/prefix/type agreement, id uniqueness, and source-key existence
in sources/register.yaml. Exit 1 on any error."""
import sys, re, pathlib
try:
    import yaml
except ImportError:
    sys.exit("pyyaml required")

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = yaml.safe_load((ROOT/"ontology"/"schema.yaml").read_text())
REG = yaml.safe_load((ROOT/"sources"/"register.yaml").read_text())["sources"]
REQ = SCHEMA["required_fields"]; PREF = SCHEMA["id_prefixes"]
CONF = set(SCHEMA["confidence_values"]); STAT = set(SCHEMA["status_values"])
DOM = set(SCHEMA["domains"])

errors, warns, counts = [], [], {}
ids = {}
for p in sorted((ROOT/"entities").rglob("*.md")):
    rel = p.relative_to(ROOT)
    m = re.match(r"^---\n(.*?)\n---\n", p.read_text(), re.S)
    if not m:
        errors.append(f"{rel}: no frontmatter"); continue
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        errors.append(f"{rel}: YAML error: {e}"); continue
    for f in REQ:
        if f not in fm: errors.append(f"{rel}: missing required '{f}'")
    eid, etype = fm.get("id",""), fm.get("type","")
    if eid in ids: errors.append(f"{rel}: duplicate id {eid} (also {ids[eid]})")
    ids[eid] = rel
    if etype in PREF and not eid.startswith(PREF[etype]):
        errors.append(f"{rel}: id '{eid}' lacks prefix '{PREF[etype]}' for type {etype}")
    if fm.get("confidence") not in CONF: errors.append(f"{rel}: bad confidence {fm.get('confidence')}")
    if fm.get("status") not in STAT: errors.append(f"{rel}: bad status {fm.get('status')}")
    if fm.get("domain") not in DOM: errors.append(f"{rel}: bad domain {fm.get('domain')}")
    srcs = fm.get("sources") or []
    if not srcs: errors.append(f"{rel}: empty sources")
    for s in srcs:
        if s not in REG: errors.append(f"{rel}: unknown source key '{s}'")
    if not fm.get("names"): errors.append(f"{rel}: empty names")
    counts[etype] = counts.get(etype,0)+1

print(f"Entities: {sum(counts.values())}  by type: {dict(sorted(counts.items()))}")
for w in warns: print("WARN:", w)
if errors:
    print(f"\n{len(errors)} ERROR(S):"); [print(" -", e) for e in errors]; sys.exit(1)
print("VALID ✓")
