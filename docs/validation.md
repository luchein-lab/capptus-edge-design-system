# Mineral Bloom validation

23 October 2026. Validation applies to the selected system and portable reference in this repository, not to a hosted production website.

## Automated checks

Run `python3 scripts/check_project.py` from the repository root. The check validates:

- Required files, JSON and local Markdown/HTML/CSS references.
- Current asset and historical archive checksums.
- The unchanged original-logo hash and available source-reference hashes.
- Agreement between JSON tokens, generated CSS, specification and palette labels.
- Presence of all six selectable collage images and absence of private runtime dependencies in the reference.
- Mineral-ink text contrast on limestone, coral and citron, all exceeding 4.5:1.

The generated CSS can also be checked with `python3 scripts/build_tokens.py --check`. JavaScript syntax is checked with `node --check scripts/reference.js`. No third-party packages are needed for these checks.

## Browser review

- Reference served over localhost without external asset requests. Direct file-URL opening was not tested because the browser tool allows only HTTP/HTTPS.
- Desktop reference reviewed at 1280 pixels; document width matched the viewport without horizontal overflow.
- Narrow reference reviewed at 320 pixels; document width matched the viewport without horizontal overflow.
- All six image choices loaded successfully and updated the image description and visible status.
- Native keyboard interaction changed the selected collage. The focused select exposed a visible 3-pixel outline.
- The README preview was rendered from the current reference markup and reviewed before saving.
- Original logo proportions, supplied Spanish accents and the displayed palette values were visually checked.

## Preserved provenance

All 45 files in the previous release were hash-checked immediately after relocation, before updating text records. Original image, PDF and SVG binaries remain unchanged. The previous working documents were preserved locally before replacement. The public archive clearly marks the earlier boards as superseded.

## Limits

This is a selected visual-system baseline and reference implementation. The work does not establish audience recognition, print colour matching, a full product component library or complete WCAG conformance. Historical board validation describes the original exports. GitHub publication does not update any separately hosted Sites deployment.
