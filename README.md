# AI Engineering & Research — Deep Dive

An offline HTML study book covering modern AI systems end to end: mechanisms,
training, retrieval and agents, evaluation and safety, production serving,
MLOps, data engineering, DevOps, computer vision, and deep reinforcement
learning.

- **101 chapters**, each a standalone HTML file, two reading pages per
  chapter (mechanism and mental model first, then production trade-offs and
  interview reasoning).
- **11 sections** (folders), one per topic area.
- **No build step, no server.** Open `index.html` directly in a browser.

## Opening it

Double-click `index.html`, or open it from a browser's File menu. Every
chapter file works the same way — open it directly, nothing needs to run
first.

## Structure

```
index.html                  Landing page — what the book covers (no links;
                             navigate via the top bar / left panel / search)
assets/
  style.css                 All styling — design tokens, layout, components
  glossary.js               All interactive behavior (see below)
  glossary.html             Glossary of terms used throughout the book
foundations/                 5 chapters
training-adaptation/        11 chapters
context-retrieval-agents/    8 chapters
evaluation-safety/           6 chapters
serving-efficiency/          9 chapters
emerging-research/           6 chapters
ml-ops/                       8 chapters
data-ops/                    15 chapters
dev-ops/                     10 chapters
computer-vision/             12 chapters
deep-reinforcement-learning/ 11 chapters
```

Each chapter's HTML lives entirely in its own folder — no shared partials,
no templating. The only shared files are `assets/style.css` and
`assets/glossary.js`, which every page links to.

## Navigation

All wayfinding is chrome injected by `assets/glossary.js` at runtime — no
chapter file needs editing to change how navigation behaves:

- **Top bar** (every page): all 11 sections, plus search and the theme
  toggle. Sticky, full width.
- **Left panel**: on a chapter page it's pinned, showing the current
  section's full chapter list with your position highlighted ("you are
  here"). On any other page (the homepage, the glossary) it's a drawer —
  click a section in the top bar to open it there instead.
- **Search**: press `/` or `Ctrl`/`Cmd`+`K` from anywhere to fuzzy-search
  all 101 chapter titles and jump straight to one.
- **Per-chapter "on this page" nav**: a right-hand rail (or a dropdown on
  narrow screens) built from that chapter's own numbered headings.

## Editing

- **Content**: edit a chapter's `.html` file directly. Its title, chapter
  number, and folder are read at runtime from the `CHAPTERS` array in
  `assets/glossary.js` — if you add, remove, rename, or move a chapter file,
  update that array (and the counts/labels in `index.html`'s section list)
  to match, or navigation, the left panel, and search will be out of sync.
- **Styling**: everything is in `assets/style.css`, driven by CSS custom
  properties (`--accent`, `--ink`, `--surface`, etc.) so light mode, dark
  mode, and the manual theme toggle all resolve from the same rules.
- **Chrome/behavior**: everything interactive (top bar, left panel, search,
  reading progress, section rail, theme toggle) lives in
  `assets/glossary.js` and is injected into every page automatically —
  there is nothing to duplicate per chapter.

## Print

Each chapter is print-friendly (`@media print` rules hide the chrome and
break pages sensibly). Open a chapter and use the browser's print dialog.
