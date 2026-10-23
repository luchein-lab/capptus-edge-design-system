"""Validate the current Mineral Bloom package without third-party dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys
from build_tokens import render

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['README.md', 'AGENTS.md', 'design.md', 'index.html',
            'docs/project-brief.md', 'docs/decisions.md', 'docs/distribution.md',
            'docs/mineral-bloom-research.md', 'docs/validation.md',
            'sources/manifest.json', 'assets/manifest.json',
            'archive/raw-bloom/manifest.json', 'tokens/mineral-bloom.json',
            'tokens/mineral-bloom.css', 'styles/mineral-bloom.css',
            'scripts/reference.js', 'assets/mineral-bloom-preview.jpg',
            'assets/fonts/bricolage-grotesque-OFL.txt', 'assets/fonts/manrope-OFL.txt']
errors = []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_link(origin, target):
    parts = urlsplit(target)
    if parts.scheme or not parts.path:
        return
    destination = (origin.parent / unquote(parts.path)).resolve()
    if not destination.is_relative_to(ROOT) or not destination.exists():
        errors.append(f'Broken or nonportable link in {origin.relative_to(ROOT)}: {target}')


for name in REQUIRED:
    if not (ROOT / name).is_file():
        errors.append(f'Missing required file: {name}')

for source in json.loads((ROOT / 'sources/manifest.json').read_text())['sources']:
    path = ROOT / source['path']
    if not path.exists():
        print(f'SKIP optional original reference: {source["id"]}')
    elif digest(path) != source['sha256']:
        errors.append(f'Source changed: {source["id"]}')
    else:
        print(f'PASS source integrity: {source["id"]}')

files = [ROOT / 'README.md', ROOT / 'AGENTS.md', ROOT / 'design.md']
for directory in ['docs', 'assets', 'archive', 'tokens']:
    files.extend((ROOT / directory).rglob('*.md'))
    for path in (ROOT / directory).rglob('*.json'):
        try:
            json.loads(path.read_text())
        except (ValueError, UnicodeError):
            errors.append(f'Invalid JSON: {path.relative_to(ROOT)}')
for path in files:
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text()):
        check_link(path, target)

count = 0
for name in ['assets/manifest.json', 'archive/raw-bloom/manifest.json']:
    manifest = ROOT / name
    if not manifest.exists():
        continue
    for entry in json.loads(manifest.read_text())['files']:
        path = ROOT / entry['path']
        if not path.is_file() or digest(path) != entry['sha256']:
            errors.append(f'Package integrity failed: {entry["path"]}')
        count += 1
print(f'Checked {count} packaged file checksums')

logo = ROOT / 'assets/logo/capptus-original.png'
if digest(logo) != '55f5309be7b3d0e8c36c35c99188a98a6451e15c461bf03ea815af8fb2c73886':
    errors.append('Original logo changed')
if (ROOT / 'tokens/mineral-bloom.css').read_text() != render():
    errors.append('Generated CSS is stale; run python3 scripts/build_tokens.py')


class ReferenceParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for key in ['href', 'src']:
            if key in values:
                check_link(ROOT / 'index.html', values[key])
        if tag == 'img' and not values.get('alt'):
            errors.append('Reference image is missing an alt description')


html = (ROOT / 'index.html').read_text()
ReferenceParser().feed(html)
for path in (ROOT / 'styles').glob('*.css'):
    for target in re.findall(r'url\(["\']?([^\)"\']+)', path.read_text()):
        check_link(path, target)
for forbidden in ['window.openai', 'localhost', '/Users/', 'http://127.0.0.1']:
    if forbidden in html or forbidden in (ROOT / 'scripts/reference.js').read_text():
        errors.append(f'Nonportable runtime reference: {forbidden}')
for filename in re.findall(r'<option value="([^"]+)"', html):
    if not (ROOT / 'assets/imagery/baja/images' / (filename + '.png')).is_file():
        errors.append(f'Missing selectable collage: {filename}')


def luminance(value):
    rgb = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in rgb]
    return sum(v * w for v, w in zip(linear, [.2126, .7152, .0722]))


def contrast(a, b):
    lo, hi = sorted([luminance(a), luminance(b)])
    return (hi + .05) / (lo + .05)


tokens = json.loads((ROOT / 'tokens/mineral-bloom.json').read_text())['color']
for name, entry in tokens.items():
    if entry['value'] not in html or entry['value'] not in (ROOT / 'design.md').read_text():
        errors.append(f'Token missing from visual reference or specification: {name}')
for background in ['limestone', 'warm-coral', 'sun-citron']:
    ratio = contrast(tokens['mineral-ink']['value'], tokens[background]['value'])
    if ratio < 4.5:
        errors.append(f'Text contrast below 4.5:1 for mineral ink on {background}')
    print(f'Contrast mineral ink / {background}: {ratio:.2f}:1')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print('PASS package integrity, original logo, local links, token agreement and selected text contrast')
print('Browser review, audience acceptance and full accessibility conformance are separate checks.')
