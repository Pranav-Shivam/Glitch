# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A static, offline HTML study book. No build, no package manager, no tests, no server: open `index.html` (or any chapter file) directly in a browser. There are no lint or test commands. Verify a change by opening the file in a browser.

It holds three separate things that do not share code:

1. **The AI book** (11 section folders, `assets/`, `index.html`). Described in `README.md`.
2. **`dsa/`**: a separate DSA interview-prep series with its own `dsa/assets/dsa.css` and `dsa/assets/dsa.js`. It does not use the book's `assets/`.
3. **`glitch.html`**: an older, large single-file version of the notes (about 2.4 MB, "45 chapters"). The 101-chapter book supersedes it. Leave it alone unless asked.

## The AI book: things that need several files to understand

- Each chapter is a standalone `.html` in its section folder. Only `assets/style.css` and `assets/glossary.js` are shared, and every page links to them with a relative path (`../assets/...`).
- **Navigation is not in the chapter files.** `assets/glossary.js` injects the top bar, left panel, search and section rail at runtime. Chapter titles, order, folder and filename come from a `RAW` array in that file (`CHAPTERS` is derived from it, around line 244). Adding, removing, renaming or moving a chapter means updating `RAW` (and its `EXCERPTS`) **and** the counts and section list in `index.html`, or navigation and search go out of sync. `README.md` hardcodes "101 chapters" and per-folder counts too.
- The "On this page" rail is built from each chapter's `h2` headings, so `h2`s must be numbered `1. Title`, `2. Title`, ...
- Styling is all in `assets/style.css` through CSS custom properties. Use existing classes. Do not add inline styles or new CSS to a chapter.
- Chapters come in pairs during the v2 revamp: `<slug>.html` (old) and `<slug>_v2.html` (new), with the Markdown source `<slug>-v2.md` beside them. The Markdown is the source of truth for content.
- To convert a Markdown chapter to `_v2.html`, follow `revamp-v2-notes.md` (invoke it as: `Use revamp-v2-notes.md. Markdown: <path>`). Its key rules: keep the Markdown content exact, never overwrite the old HTML, read only the first and last ~15 lines of the old file for shell values, and use only classes that exist in `assets/style.css`.

## `dsa/`

- `dsa/das_prompt.md` is the master prompt for generating a topic's notes (14 teaching parts, a practice part, a practical build track, research-first problem selection, calibration for a 3–4 year engineer targeting large tech companies). Read it before generating or editing a topic.
- Each topic is one self-contained notes page (`Arrays_Notes_v3.html`, `two-pointers-notes_v2.html`, `Sliding_Window_Notes_v2.html`, `Stack-Mastery-Notes_v2.html`). They link `dsa/assets/dsa.css` and `dsa/assets/dsa.js`. These are the rebuilds from the current `das_prompt.md`; the earlier versions were removed (recoverable from git commit `83e2785`).
- `dsa.js` expects `<body data-key="slug">` (used as the localStorage key for checklist ticks), one `.section` per tab with a matching `.nav-tab[data-tab]`, code blocks as paired `pre.pane[data-l="py"|"java"]`, and `#practice-mode` / `.reveal-btn` for Practice mode. Checklist inputs need unique `id`s.
- Code in the notes must be verified. The convention is to run each optimal solution against a brute force on thousands of random inputs, in Python and in Java (a JDK is at `C:\Program Files\Java\jdk-27`). Do not claim a solution is correct without running it.

## Research cache (`research/`)

- Before any web search or fetch, read `research/README.md` and grep `research/` for the topic. If a file covers it and is not stale, use it and say it came from local research with its retrieval date.
- After any web research, save the findings to `research/<area>-<topic>-<timestamp>.md` and add a row to the index in `research/README.md`. Each file records the retrieval date, the question, findings, reliability caveats, pages that could not be fetched, and source links. Never overwrite an old file: append a dated update or add a new file.

## Conventions

- Windows machine. Use the Bash tool with forward slashes or PowerShell. When Python prints non-ASCII text to the console, set `PYTHONIOENCODING=utf8`.
- Prefer new files over overwriting existing chapters or notes. Existing `.html` files here are often large, so read only the parts you need.
