#!/usr/bin/env python3
"""Generate INDEX.md — grouped id / name / definition listing."""
import re, pathlib, yaml
ROOT = pathlib.Path(__file__).resolve().parents[1]
groups = {}
for p in sorted((ROOT/"entities").rglob("*.md")):
    fm = yaml.safe_load(re.match(r"^---\n(.*?)\n---\n", p.read_text(), re.S).group(1))
    cat = str(p.relative_to(ROOT/"entities").parent)
    groups.setdefault(cat, []).append((fm["id"], fm["names"][0], fm["definition"].split(". ")[0].rstrip(".")+".", str(p.relative_to(ROOT))))
lines = ["# Footwear Doctrine — entity index (generated)", ""]
total = 0
for cat in sorted(groups):
    lines += [f"## {cat} ({len(groups[cat])})", ""]
    for eid, name, dfn, path in groups[cat]:
        lines.append(f"- **{eid}** — {name}: {dfn} ([file]({path}))")
        total += 1
    lines.append("")
lines.insert(2, f"_{total} entities._\n")
(ROOT/"INDEX.md").write_text("\n".join(lines))
print(f"INDEX.md written: {total} entities in {len(groups)} groups")
