# Mineral Bloom tokens

[mineral-bloom.json](mineral-bloom.json) is the source of truth for the selected five-colour palette, semantic aliases and reference typography. [mineral-bloom.css](mineral-bloom.css) is generated from that file.

```sh
python3 scripts/build_tokens.py
python3 scripts/build_tokens.py --check
```

```css
@import url("./tokens/mineral-bloom.css");

.example {
  background: var(--capptus-surface);
  color: var(--capptus-text);
  font-family: var(--capptus-font-body);
}
```

The selected palette is the repository baseline. Semantic aliases and font weights describe the supplied implementation; they do not constitute a full product component library. Use mineral ink for text and functional controls on limestone. Signature blue on limestone is for nonessential decorative details only.

Do not edit generated CSS independently or derive the logo's colours from these tokens. See the [specification](../design.md) for usage and measured contrast.
