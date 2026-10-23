# Capptus Mineral Bloom project instructions

Read README.md, design.md, docs/project-brief.md, and docs/decisions.md before making changes. Read any package and configuration files added later before editing implementation code.

## Brand boundaries

- Maintain the company-wide Capptus Mineral Bloom system selected on 23 October 2026. The repository retains its existing name; Edge-only Raw Bloom work is historical and lives in archive/raw-bloom/.
- Preserve the existing logo and existing tagline copy. Do not redraw, retype, distort, or generate a substitute logo.
- The inspiration image is a starting point, not an approved production identity. Its wordmark and proposed slogans must not replace existing brand assets or copy.
- Preserve the supplied credentials context and wording. Use the selected Bricolage Grotesque and Manrope families; do not import unrelated consulting-system typography.
- Separate source evidence, interpretation, proposal, and selected decisions. Mineral Bloom's five colours are the selected repository baseline; detailed component rules remain implementation choices unless explicitly approved. Keep tokens/mineral-bloom.json as the source of truth and generate its CSS with scripts/build_tokens.py.
- Keep Spanish accents and supplied bilingual wording. Preserve claim attribution, including Capptus versus partner results.
- Use a verified master logo when available. A preview in a PDF or moodboard is not proof of a production asset or permission to reconstruct it.

## Workspace and delivery

- Keep generated work inside this project. Keep source files unchanged at their existing paths and index them in sources/manifest.json.
- Use output/ for working reviews, renders, and exports. Keep the current portable reference in index.html, reusable assets in assets/, selected system tokens in tokens/, and superseded boards in archive/raw-bloom/.
- Explain substantial changes first. Prefer small, inspectable changes; do not delete files without explicit user approval.
- Do not commit or push unless explicitly asked. Creating or publishing a GitHub repository requires the requested destination and visibility to be resolved.
- Do not assume source decks, client marks, team information, or performance claims belong in a public repository.
- Do not add credentials, caches, local application configuration, or unrelated project copies.
- Run the applicable checks after edits and state exactly what was verified. Documentation checks do not prove visual quality, accessibility, or runtime behavior.
