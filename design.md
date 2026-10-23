# Capptus Mineral Bloom design system

Version 1.0, 23 October 2026. Selected company-wide repository baseline. This supersedes the earlier Edge-only Raw Bloom direction; historical boards remain in the archive.

## Identity and existing language

Use the verified [original logo](assets/logo/capptus-original.png) without recolouring, retyping, distortion or reconstruction. Its blue and gray artwork remains unchanged. The surrounding signature-blue token does not authorize changes to the logo itself. No new wordmark or Edge lockup is introduced.

Preserve these supplied strings:

- “Menos ruido, más crecimiento”
- “Your Digital Oasis for Growth”
- “HUMAN CRAFTED. AI AMPLIFIED. SCALED WITH SALESFORCE.”

The visual reference uses them as specimens. Selection of a visual direction does not rewrite company positioning or validate commercial claims.

## Colour

The source of truth is [mineral-bloom.json](tokens/mineral-bloom.json); the CSS is generated from it.

| Token | Value | Use |
| --- | --- | --- |
| limestone | `#F3E8D7` | Main backgrounds, breathing space and business documents |
| mineral-ink | `#23332F` | Headlines, body copy, controls and dark panels |
| warm-coral | `#E89B86` | Leading expressive panels and editorial emphasis |
| sun-citron | `#D5D83E` | Small accents and selected emphasis |
| signature-blue | `#0094E2` | Small recurring graphic details |

Begin with limestone and mineral ink. Choose one leading expressive colour per composition. Use citron sparingly; the collages already contain energetic accents. Blue should remain visible in deliberate details without becoming the main background. No universal coverage percentages are required.

The five hex values are sRGB screen values. Print conversions and material proofs have not been established.

## Contrast and functional roles

| Foreground / background | Ratio | Reference use |
| --- | --- | --- |
| Mineral ink / limestone | 10.93:1 | Body text and headlines |
| Mineral ink / warm coral | 5.97:1 | Text on expressive panels |
| Mineral ink / sun citron | 8.65:1 | Labels on accents |
| Limestone / mineral ink | 10.93:1 | Inverse text and primary action |
| Signature blue / limestone | 2.74:1 | Nonessential decoration only |

The selected text pairs exceed the 4.5:1 normal-text minimum. Blue on limestone does not reach the 3:1 threshold either; do not use that pairing for small text, essential icons, borders that identify controls, or focus indicators. Blue also cannot be assumed safe for white text or buttons. Use the documented mineral-ink action with limestone text.

Use underlined text links, visible keyboard focus and labels independent of colour. The reference uses a mineral-ink focus outline. Its logo is unchanged artwork; logotype exemptions do not extend to ordinary interface text. Pair calculations are not a complete accessibility audit.

## Typography

| Role | Family | Reference weight |
| --- | --- | --- |
| Display and headlines | Bricolage Grotesque | 700 |
| Body and controls | Manrope | 400 |
| Labels and emphasis | Manrope | 600 |

The font families were selected previously and are retained in Mineral Bloom. Weights, fluid sizes and spacing in the visual reference are implementation choices. Use large expressive headlines, readable body text, and short labels. Preserve Spanish accents and avoid using lettering as a substitute for the original logo.

Bundled WOFF2 files support the demonstrated Latin and Spanish text. Other scripts require appropriate licensed font subsets. See [font provenance](assets/fonts/README.md).

## Imagery and composition

The [six selected Baja collages](assets/imagery/baja/README.md) establish material warmth: cream torn paper, coral flowers and folds, sunlit rock, cactus texture, muted sea blue, and small citron details. Preserve the source images. Do not recolour every photograph to force exact token matches.

Use an orderly editorial grid and generous cream space around expressive imagery. Keep text on a solid field rather than across detailed photography. Let a single collage carry the image-led composition; avoid decorating every business page with cactus imagery.

These are generated concepts, not actual client work, team photography or verified locations. The image palette is broader than the five flat system colours.

## Company-wide application

- Proposals and business documents: limestone and mineral ink lead; coral and imagery mark introductions or important sections.
- Campaign and creative work: increase image scale, coral and selected citron accents while keeping the same type and logo.
- Interfaces: use the functional text/action pairs above; derive additional semantic status colours only when real product requirements justify them.

Mineral Bloom is one shared visual system. It does not assign separate palettes or new logos to each Capptus practice.

## Implementation and validation

Use the [portable visual reference](index.html) and [tokens](tokens/README.md) together. Regenerate CSS after token changes. Run `python3 scripts/check_project.py` for file integrity, local links, token agreement, source checks and contrast checks.

See the [validation record](docs/validation.md) for completed checks and limits. A full production component library, print specifications, audience testing and application-specific accessibility audits remain future work.
