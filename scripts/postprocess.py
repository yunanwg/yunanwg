#!/usr/bin/env python3
"""Post-process the Typst SVG output for the profile README.

- Crops the A4 page to the content area (fixed height, tuned to the layout).
- Derives assets/cv-dark.svg by remapping fills to the GitHub dark palette.
"""

from pathlib import Path

LIGHT = Path("assets/cv-light.svg")
DARK = Path("assets/cv-dark.svg")

A4_VIEWBOX = 'viewBox="0 0 595.275590551 841.88976378"'
A4_HEIGHT = 'height="841.88976378pt"'
CROP_PT = 392  # content ends ~370pt; keep a little breathing room

# light -> GitHub dark palette (terracotta lightened for contrast)
DARK_MAP = [
    ("#ffffff", "#0d1117"),  # page background
    ("#343a40", "#c9d1d9"),  # body text
    ("#212529", "#e6edf3"),  # name
    ("#000000", "#e6edf3"),  # rules / black text
    ("#8b8b8b", "#8b949e"),  # footer gray
    ("#aaaaaa", "#7d8590"),  # date/location gray
    ("#a0674b", "#c98d6f"),  # terracotta accent
]


def main() -> None:
    svg = LIGHT.read_text()
    svg = svg.replace(A4_VIEWBOX, f'viewBox="0 0 595.275590551 {CROP_PT}"')
    svg = svg.replace(A4_HEIGHT, f'height="{CROP_PT}pt"')
    LIGHT.write_text(svg)

    dark = svg
    for light_hex, dark_hex in DARK_MAP:
        dark = dark.replace(f'fill="{light_hex}"', f'fill="{dark_hex}"')
    DARK.write_text(dark)


if __name__ == "__main__":
    main()
