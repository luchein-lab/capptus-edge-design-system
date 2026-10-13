"""Check foundation files, source checksums and local Markdown links."""
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["README.md", "AGENTS.md", "design.md", "docs/project-brief.md",
            "docs/reference-notes.md", "docs/decisions.md", "docs/roadmap.md",
            "docs/creative-direction.md",
            "sources/manifest.json", "assets/README.md", "tokens/README.md",
            ".gitignore", ".editorconfig"]
errors = []
for name in REQUIRED:
    if not (ROOT / name).is_file():
        errors.append(f"Missing required file: {name}")
manifest = ROOT / "sources/manifest.json"
if manifest.is_file():
    for source in json.loads(manifest.read_text())["sources"]:
        path = ROOT / source["path"]
        if not path.is_file():
            # Reference binaries are deliberately not distributed by default.
            print(f"SKIP absent local reference: {source['path']}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != source["sha256"]:
            errors.append(f"Source changed: {source['path']}")
        else:
            print(f"PASS source integrity: {source['id']}")
markdown_files = [ROOT / name for name in REQUIRED if name.endswith(".md")]
markdown_files += list((ROOT / "explorations").rglob("*.md"))
markdown_files += [ROOT / "docs/distribution.md"]
for path in markdown_files:
    name = str(path.relative_to(ROOT))
    if not path.is_file():
        continue
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
        if "://" in target or target.startswith(("#", "mailto:")):
            continue
        target = unquote(target.split("#")[0])
        if not (path.parent / target).exists():
            errors.append(f"Broken link in {name}: {target}")
release = ROOT / "explorations/manifest.json"
if not release.is_file():
    errors.append("Missing exploration release manifest")
else:
    entries = json.loads(release.read_text())["files"]
    for entry in entries:
        path = ROOT / entry["path"]
        if not path.is_file():
            errors.append(f"Missing packaged file: {entry['path']}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            errors.append(f"Packaged file changed: {entry['path']}")
    print(f"Checked {len(entries)} packaged file checksums")
for path in (ROOT / "explorations").rglob("*.json"):
    try:
        json.loads(path.read_text())
    except (ValueError, UnicodeError):
        errors.append(f"Invalid JSON: {path.relative_to(ROOT)}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("PASS foundation files and local Markdown links")
