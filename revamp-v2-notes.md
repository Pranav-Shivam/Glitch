# Revamp v2 Notes — Generic Prompt (any chapter)

**How to call it** (only the Markdown path is required):

```
Use revamp-v2-notes.md. Markdown: <path to .md>
```

Optional overrides in the same message: `Old HTML: <path>`, `Chapter: 07 / 101`, `Next: <file>.html`, `Fix errors: yes`.

This file is self-contained. It works in a fresh session, for any chapter in any folder under `AIMaterials`.

---

## Task

Turn one Markdown chapter into `<slug>_v2.html`, saved next to the existing `<slug>.html`. The Markdown is the source of truth for **content**. The app's stylesheet and the shell below are the source of truth for **style**.

## Locate files

1. Read the Markdown file completely.
2. Derive `<slug>` from the Markdown filename (lowercase, hyphenated, no extension). If it does not match an HTML file, use the topic in the `#` title. If still ambiguous, ask.
3. Find the old file: same slug, `.html`, searched under `E:\Glitch\AIMaterials\` (skip `_v2` files). Its folder is the output folder. If not found, ask for the path or continue with overrides.
4. Assets path is relative to the old file. Detect it from the old `<link rel="stylesheet">` (normally `../assets/style.css`). Never hard-code it.

## What to read from the old HTML

Read only the first ~15 lines and the last ~15 lines. Pull out:

- `<title>`
- `data-category`, section `id`, `data-case-study` value
- kicker text (`Category · Chapter NN / TOTAL`)
- `.lede` text
- `.chapter-nav` links (Contents, Next), footer links
- any external source link (`.source-links`)

Do not read the body. If a value is missing, use an override from the user's message, otherwise leave a clearly marked placeholder and list it in the report.

Only read `assets/style.css` or `assets/glossary.js` if a component below seems to be missing, to confirm a class exists.

## Content rules

- Markdown content is exact. Keep every sentence, list, table, formula, diagram, example, story, quote, number, and order. No summarizing, dropping, rewording, or reordering.
- Do not fix, improve, or add technical content. Note errors and gaps in the report. Apply a fix only when the user says `Fix errors: yes`, and then flag each fix in the report.
- Layout-only edits are allowed: grouping, wrapping in components, adding ids, escaping characters.
- Markdown constructs convert to their HTML equivalents (see Mapping). Nothing is lost.

## Style rules

- Use only classes from `assets/style.css`. No inline styles, new CSS, new JS, or external libraries. Colors, fonts, and theme come from the app.
- Number `h2`s as `1. Title`, `2. Title`, ... The app's JS builds the section rail from these. Group Markdown sections into about 12 to 20 numbered `h2`s. Demote the rest to `h3`, or bold lead-in text for small sub-points.
- Split into two `.chapter-page` blocks:
  - `PAGE 1 · MECHANISM, MENTAL MODEL, THEORY`: definition, problem, intuition, mechanism, theory, research background.
  - `PAGE 2 · PRODUCTION, TRADE-OFFS, INTERVIEW REASONING`: scaling, production, failure modes, trade-offs, misconceptions, interview, remember.
  Adjust the split to where the Markdown naturally changes from theory to practice. If the Markdown is short or has no such divide, use one page.
- Put case study and audit/test sections after the chapter pages, only if the Markdown has that content.

## Shell (copy exactly; fill from old file)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/><meta content="width=device-width,initial-scale=1" name="viewport"/>
<title>{TITLE}</title>
<link rel="stylesheet" href="{ASSETS}/style.css"/>
</head>
<body id="top">
<div class="layout single">
<main>
<section class="chapter" data-category="{CATEGORY}" id="{ID}">
<div class="chapter-kicker">{KICKER}</div>
<h1>{H1}</h1>
<p class="lede">{LEDE}</p><div class="plain-bridge"><div class="plain-label">In plain English</div><p>{PLAIN_ENGLISH}</p></div>
<div class="chapter-page">
<div class="page-label">PAGE 1 · …</div>
… numbered h2 sections …
</div>
<div class="chapter-page">
<div class="page-label">PAGE 2 · …</div>
…
</div>
{optional production-case section}
{optional audit section}
<div class="status">{closing decision or one-line summary}</div>
<div class="chapter-nav"><a href="{INDEX}">Contents ↑</a><a href="{NEXT}">Next →</a></div>
</section>
</main>
</div>
<footer><a href="{INDEX}">Contents</a> &middot; <a href="{ASSETS}/glossary.html">Glossary</a></footer>
<script src="{ASSETS}/glossary.js"></script>
</body></html>
```

The `lede`, kicker, category, id, and nav links come from the old file. `H1` and the plain-English text come from the Markdown. If the Markdown has no plain-English callout, copy the old file's.

## Mapping (Markdown → app components)

| Markdown | HTML |
|---|---|
| Fenced ASCII diagram / flow | `<pre class="diagram">` |
| One-line formula or equation | `<div class="formula">` |
| Side-by-side or several short blocks | `<div class="two-col">` with `<pre>` or `<div><h3>…</h3><pre>…</pre></div>` |
| Plain-English callout, layman story, analogy | `<div class="plain-bridge"><div class="plain-label">…</div>…</div>` |
| Key takeaway blockquote | `<div class="status">` |
| Quoted question / short quote | `<div class="case-note">` |
| Table | `<table><thead>…</thead><tbody>…</tbody></table>` |
| Papers and references | `<div class="source-card">` with `<div class="meta">` |
| Claim → assumption → … chain | `<div class="topic-check"><code>…</code></div>` |
| Misconception / Reality / Why | `<p><strong>Misconception:</strong> …<br/><strong>Reality:</strong> …</p>` |
| Production case study | `<section class="production-case" data-case-study="{ID}">` with `.case-meta`, `.case-pill`, `.case-chain`, `.case-table`, `.case-note`, `.source-links`, `.case-fact` |
| Role tests / iteration checklist / decision checkpoint | `<section class="audit">` with `.badge`, `.agent-ai`, `.agent-research`, `.agent-staff`, `.agent-first`, `.decision` |
| Inline code | `<code>` |
| Bold, italic, lists | `<strong>`, `<em>`, `<ul>`, `<ol>` |

If an element has no mapping, use the closest existing component and list it in the report.

## HTML hygiene

- Escape `&`, `<`, `>` in text and inside `<pre>` (`Q &amp; K`).
- Keep box-drawing characters and alignment inside `<pre>` exactly.
- Close every tag. Double-quote attributes.
- Glossary: wrap a term in `<span class="glossary-term" data-glossary-term="…" data-tooltip="…" tabindex="0">` only when both the term and tooltip already exist in `{ASSETS}/glossary.html` or the old file. Never invent tooltip text. Skip the wrap when unsure.
- Keep external links with `rel="noopener" target="_blank"`.

## Checks (run before reporting)

- Tag counts balanced for `div`, `pre`, `section`, `p`, `table`, `ul`, `ol`.
- `h2` numbers sequential from 1.
- No leftover Markdown syntax (`**`, `##`, backticks, leading `>`, `|---|`).
- Old file unchanged (size and modified time).
- The first, middle, and last Markdown sections all appear in the output.

## Report (short)

1. Path of the new file.
2. How Markdown sections were grouped into numbered `h2`s.
3. Placeholders left because a value was missing.
4. Elements with no direct mapping and what was used.
5. Technical issues noticed but left unchanged, or fixes applied if `Fix errors: yes`.
6. The page has not been visually checked. Look first at the section rail and diagram blocks.

## Do not

- Do not overwrite the old file or any other chapter.
- Do not edit shared assets.
- Do not publish to claude.ai or any external service.
- Do not add commentary or improvements not in the Markdown.
- Do not ask questions the message or the old file already answers.
