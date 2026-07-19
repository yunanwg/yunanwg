// Imports
#import "@preview/brilliant-cv:4.1.0": cv-section, cv-skill, h-bar

#cv-section("Skills")

#cv-skill(
  type: [Languages],
  info: [Teochew #h-bar() Mandarin #h-bar() French #h-bar() English #h-bar() and saying no, fluently, in all four],
)

#cv-skill(
  type: [Toolchain],
  info: [Typst (dangerously) #h-bar() tmux #h-bar() Neovim #h-bar() chezmoi],
)

#cv-skill(
  type: [Superpowers],
  info: [Deleting things (expert) #h-bar() French bureaucracy (survivor)],
)

// Star count is injected by CI (--input stars=<n>) so the footer stays fresh.
#let stars = sys.inputs.at("stars", default: "809")

#v(8pt)
#align(center)[
  #text(size: 8pt, style: "italic", fill: rgb("#8b8b8b"))[
    Typeset with #link("https://github.com/yunanwg/brilliant-CV")[brilliant-CV] #sym.star.filled #stars --- the only résumé line on this page.
  ]
]
