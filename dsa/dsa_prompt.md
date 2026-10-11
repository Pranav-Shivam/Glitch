
# DSA Topic Mastery Prompt

I am preparing for technical interviews, and I want to master DSA **one topic at a time**, from first principles to interview-ready problem-solving.

The DSA progression is:

**Arrays → Hashing/Hash Maps → Two Pointers → Sliding Window → Stack → Binary Search → Linked List → Trees → Tries → Heaps → Backtracking → Graphs → Dynamic Programming**

## My Current Topic

> **[INSERT CURRENT TOPIC]**

## My Previous Topics (already completed)

> **[INSERT PREVIOUS TOPICS]**

## My Profile

- **Experience:** 3–4 years as a software engineer (mid-level: roughly Meta E4, Google L4, Amazon SDE-2, or the equivalent at other companies).
- **Target companies:** Meta, Amazon, Netflix, Google, Anthropic, OpenAI, X (Twitter), and other large multinationals (for example Microsoft, Apple, Uber, Stripe, Atlassian).
- **Main language:** Python (Java as a second option).

Calibrate everything to this profile (see "Calibration" below). If I tell you my level or targets changed, recalibrate.

Assume I am learning the current topic for the **first time**, even if I already know some Python.

If I attach source material (my own notes, a video transcript, a lecture, a PDF), **merge it** with this prompt instead of ignoring either one. Tag points that come only from the source. Where the source is loose, wrong, or imprecise, give the precise version and say what changed.

---

## Your Teaching Objective

Teach me this topic the same way we mastered the previous topics.

Do **not** dump a huge list of LeetCode problems on me.

Do **not** optimize for the number of problems solved.

Optimize for:

> **Understanding → Pattern Recognition → Implementation → Problem Solving → Interview Readiness**

The goal is that when I see an unfamiliar interview problem, I can recognize whether this topic/pattern applies, know how to approach it, and know when it does **not** apply.

---

## Calibration for my level and target companies

Research (and re-research each time) what my target companies actually ask a candidate with 3–4 years of experience, then adjust. Findings so far (researched, dated 2026; treat as a signal, not a guarantee):

- **Two styles of interview exist, and I need to prepare for both:**
  1. **Algorithmic, pattern-based** (Meta, Google, Amazon, Microsoft, Uber, and to a lesser extent X): LeetCode medium as the core, medium-hard at Google, mostly timed. Meta runs two coding rounds of about 45 minutes with typically two problems each, in a no-execution editor, so I must write correct code without running it. Amazon's online assessment is about 90 minutes for two medium problems, and its loop adds behavioural and design questions.
  2. **Practical, build-from-scratch** (Anthropic, OpenAI, Stripe, and partly Netflix): realistic engineering tasks such as an LRU cache, a time-based key-value store, a rate limiter, an in-memory database, or a banking system with levels that escalate, plus debugging in a real codebase. Anthropic reportedly requires Python and stresses concurrency, edge cases and justifying decisions over speed.
- **At my level, the easy problems are warm-ups.** The core is medium problems solved quickly, with clean code, correct edge cases, complexity analysis, and answers to follow-up questions. Hard problems are a stretch goal (more relevant at Google).
- **Topic weight is not equal.** Arrays are foundational but are often the building block inside harder problems. Reported high-frequency Meta mid-level problems lean towards strings, stacks, trees, and graphs. So for every topic, tell me honestly **how much interview weight this topic has at my targets** and what it unlocks next.
- **Timing matters.** Aim to solve a medium problem in about 15–20 minutes including discussion and testing. Include a timed attempt in practice.
- **Reliability warning:** most of this data comes from prep-site blogs, candidate posts and Glassdoor-style pages. Data on X (Twitter) is thin and may predate its 2022 changes. Level mapping for some companies is unclear. Say when you are unsure.

---

# PART 1 — First Principles

Start from absolute fundamentals.

Open with a **one-paragraph summary** of the topic in plain words (what it is, what it turns into what, e.g. "turns O(n²) into O(n)"). Then explain:

- What this data structure / pattern is
- Why it exists
- What problem it solves
- What problem it solves better than simpler approaches
- How it works internally at a conceptual level
- The **core invariant**: the one fact that stays true throughout and makes the technique correct
- When I should use it
- When I should NOT use it
- Where I already meet it in real life or in tools I use
- How it relates to the previous DSA topic(s), and how it prepares the next one

Use simple examples and ASCII diagrams where useful. If a step-by-step animation or trace table would show the mechanism better than prose, use it.

Do not assume I already understand the terminology. Define each term the first time it appears.

---

# PART 2 — Language Toolkit (Python, plus Java)

Teach me exactly how this topic is represented and implemented in **Python** (primary). Also show **Java** equivalents for every code block, because interviews may require either. Keep the two side by side, or behind a Python/Java toggle if the notes are HTML.

Cover:

- Important syntax
- Built-in data structures/classes that are relevant
- Important methods
- Common patterns
- Common interview tricks
- What each operation does
- Time complexity
- Space complexity
- **Traps**: operations that look cheap but are not (e.g. `list.pop(0)`, string concatenation in a loop, slicing copies, mutable default arguments), and Java-specific traps (e.g. `==` on boxed Integers, `String` immutability, integer overflow)

For every important operation, show a small example.

Do not teach language features that rarely matter in DSA interviews.

---

# PART 3 — Complexity

Teach me the complexity model for this topic.

I should understand:

- Time complexity
- Space complexity
- Best/average/worst case where relevant
- **Amortized** cost where relevant, and the argument for why it holds (for example, "each element is added once and removed once, so total work is O(n) even with a loop inside a loop")
- Why the complexity is what it is

Create a concise complexity table that I can memorize.

More importantly, explain **why** the complexity occurs rather than asking me to blindly memorize it. If the code *looks* worse than it is (nested loops that are really O(n)), address that directly.

---

# PART 4 — Core Patterns

Identify the important interview patterns associated with this topic. Label them as lettered types (Type A, Type B, ...) so I can refer to them later.

For each pattern explain:

1. What the pattern is
2. What problem it solves
3. How to recognize it from a problem statement
4. The intuition behind it
5. The generic algorithm
6. The **state** it keeps, the **validity/invariant condition**, and what happens on each step (the pieces I must write down before coding)
7. Python (and Java) implementation/template
8. Time complexity
9. Space complexity
10. A tiny example traced by hand

For example, for Arrays this included ideas such as:

- Traversal
- Maintaining state
- Prefix/running information
- Pair comparisons
- In-place modification
- Swapping
- Boundary handling

Do the equivalent for the current topic.

---

# PART 5 — Pattern Recognition

This is extremely important.

Teach me how to recognize the topic/pattern from the wording of an interview problem.

Give me examples like:

> "If a problem says X, you should start thinking about Y."

Show:

**Problem clue → Pattern → Reasoning**

Provide:

- A **keyword → pattern map** (phrases in the problem statement that point to a specific pattern)
- A **decision flowchart** (a few yes/no questions that narrow down to the right pattern)
- A **"looks like this topic, but actually needs something else"** table with columns: *Looks like / Actually needs / Why*

I want to develop pattern recognition rather than memorize solutions.

---

# PART 6 — Brute Force → Optimization

For the important problem types, teach the progression:

```text
Brute Force
    ↓
Why it is slow
    ↓
Observation
    ↓
Better approach
    ↓
Optimal/common interview approach
```

For each important pattern:

- Show the naive approach
- Give its complexity
- Explain why it is inefficient (name the repeated or wasted work)
- Show how the new data structure/pattern improves it
- Explain the key insight
- Show the optimized solution
- Compare the complexities

This is especially important because I want to understand **why** we use a technique rather than simply knowing that we use it.

---

# PART 7 — Representative Problems

Only after teaching the concepts, give me a **small curated set** of representative problems, grouped by the pattern types from Part 4.

Do NOT give me 30–50 problems. Aim for roughly 12–20 solved problems, and fewer if fewer cover the patterns.

## How to choose the problems (research first, not memory)

Do **not** pick problems from memory alone. Before choosing, **research on the web** which problems for this topic are asked most often at large tech companies (Google, Meta, Amazon, Microsoft, Apple and similar). Use several independent sources, for example:

- Curated lists: Blind 75, NeetCode 150, Grind 75, Tech Interview Handbook "best practice questions"
- Company-tagged frequency lists (LeetCode company tags, interview-experience posts, prep-site breakdowns)
- Recent candidate reports for the current year

**Check the local cache first.** Read `research/README.md` and look in `research/` for this topic (for example `research/dsa-array-problem-frequency-2026.md` and `research/dsa-company-interview-calibration-2026.md`). Reuse what is there and say it is from local research with its date. Search the web only for what is missing or stale (older than about 6 months). **After every web search, save the findings to `research/`** (retrieval date, question, findings, caveats, pages that failed to load, source links) and update the index, so the same research never has to be repeated.

Then:

1. **Build a "most asked" list for this topic.** Keep a problem if it shows up in two or more independent sources, or in a curated list plus a company-tagged list.
2. **Check pattern coverage.** Every pattern from Part 4 needs at least one problem. If a pattern is only covered by a rarely asked problem, keep it but label it "added for pattern coverage".
3. **Label provenance for every problem:** *"Frequently asked (sources: ...)"* or *"Added for pattern coverage"*. Never present a memory-based pick as if it were research.
4. **Handle problems that belong to a later topic.** If a frequently asked problem needs a technique from a later topic in the progression (for example Two Sum needs hashing, 3Sum needs two pointers, Search in Rotated Array needs binary search), do NOT solve it here. Put it in a short **"Deferred to [topic]"** table with the reason, so I know it is on the roadmap.
5. **Handle problems that belong to no topic in the progression** (for example intervals, greedy, bit manipulation, math). If the problem is commonly asked and array-based, include it here or flag it in an **"Outside the roadmap"** list with a suggested place to study it. Do not silently drop it.
6. **Be honest about the data.** Company frequency numbers are crowd-sourced and from third-party sites, and their method is rarely explained. Treat them as a signal, not a guarantee, and say so. Interviewers rarely reuse a problem word for word, so patterns matter more than exact titles.
7. **Include a short "Sources" note** in the notes file: the links used and the date of the research, because this data goes stale.

Choose problems that collectively cover every important pattern. Include at least one problem that **looks** like this topic but needs a twist (a variant, a different pattern, or a combination).

For each problem provide:

- Problem name and LeetCode number
- Where it is reported (which target companies, from which sources), or "added for pattern coverage"
- Difficulty
- Pattern being tested
- Why it is important
- What I should recognize before coding
- What skill it teaches
- Brute force → optimal solution, with complexity for both
- Code in Python (and Java)

**Every solution must be verified.** Run the optimal solution against the brute force on many random inputs (thousands) in each language, and report the result. Do not present unrun code as correct.

How to verify properly (lessons learned):

- **One source of truth.** Keep each problem's Python and Java code (brute force and optimal) in one data file, and generate both the test harness and the notes page from it, so the code I read is the code that was tested.
- **Find the tools first.** Check that a JDK is installed (look in `C:\Program Files\Java` and similar) before saying Java cannot be verified. Compile and run it. Only say "not compiled" if you truly cannot.
- **Inputs must respect the problem's constraints.** For example no leading zeros for Plus One, a guaranteed majority element for Majority Element, values in `1..n` for Find Duplicates, `m` sorted values then zero padding for Merge Sorted Array. A harness that feeds invalid input gives false failures.
- **Test in-place problems by comparing the mutated array and the return value**, not just the return value.
- **Verify every claim about a bug with a failing example.** If the notes say "this common mistake gives the wrong answer", run the buggy version on a concrete input that actually fails. A coincidental pass on a lucky input proves nothing (the Python `a[i], a[a[i]-1] = ...` swap bug looks fine on some inputs).
- **Skeleton templates.** A template that uses placeholder helpers (`combine()`, `keep()`) is a skeleton, not verified code. Either make it runnable and test it, or label it "skeleton, not runnable". Prefer runnable templates taken from a verified solution.
- **Report what was and was not verified**: which languages, how many cases, and anything not run (for example a page not viewed in the browser).

Organize problems from:

**Easy → Medium → Hard**

But prioritize **pattern coverage over quantity**.

---

# PART 8 — Problem-Solving Method

Teach me a repeatable interview process for solving problems involving this topic.

For example:

```text
1. Understand the input
2. Identify constraints
3. Clarify edge cases
4. Think of brute force
5. Identify the bottleneck
6. Recognize the pattern
7. Design optimized approach
8. State complexity
9. Code
10. Test
```

Adapt this process to the current topic. For each step, give the **specific question to ask** and an example of what to say aloud. Include the topic's own "write this down before coding" checklist (for example the state, the invariant, the update rule, and what counts as an answer).

---

# PART 9 — Edge Cases

Give me the important edge cases I should automatically think about.

Examples where relevant:

- Empty input
- One element
- Duplicate values
- Negative values
- Zero
- Very large input
- Already sorted input
- Reverse sorted input
- Repeated values
- Boundary indexes
- Missing values
- No valid answer (what do I return: 0, -1, empty, null?)
- Integer overflow (Java)
- etc.

Explain **why each edge case matters**, and which pattern it breaks.

---

# PART 10 — Common Mistakes

Give me the mistakes beginners commonly make with this topic.

Include:

- Conceptual mistakes
- Python mistakes
- Java mistakes
- Complexity mistakes
- Boundary mistakes (off-by-one, wrong loop condition)
- Interview reasoning mistakes

For each mistake explain how to avoid it.

---

# PART 11 — Interview Templates

Create the minimum set of reusable code templates I should remember, as a one-page **recall sheet**.

For example:

```python
# Generic template
...
```

Do not give me templates for every possible problem.

Give me only the templates that cover the major patterns.

For each template, state which problems it applies to, its complexity, and the one line that people most often get wrong.

---

# PART 12 — Mental Model

At the end, give me a compact mental model.

Something like:

```text
When I see ______
        ↓
Think about ______
        ↓
Because ______
        ↓
Use ______
        ↓
Expected complexity: ______
```

Add one diagram of the core idea (for example, what is eliminated, what is kept, what is reused). I should be able to review this section before an interview.

---

# PART 13 — Mastery Checklist

Create a checklist divided into:

### Level 1 — Fundamentals

Can I explain the concept?

### Level 2 — Python (and Java)

Can I implement the basic operations and templates without looking?

### Level 3 — Complexity

Can I explain the time/space complexity, including the amortized argument?

### Level 4 — Patterns

Can I recognize the major patterns and the look-alikes?

### Level 5 — Problem Solving

Can I solve representative Easy/Medium problems?

### Level 6 — Interview Ready

Can I explain my approach aloud and solve an unfamiliar problem?

Include timed items, for example: "I can solve a representative medium problem in about 15–20 minutes, including stating brute force, complexity and one test", "I can write correct code without running it", and "I can answer a follow-up that changes a constraint".

Each item must be a concrete "I can ..." statement, not a vague topic.

Do not mark anything as mastered for me.

Instead, give me a self-assessment checklist. If the notes are HTML, make the ticks persist in the browser and show a progress count.

---

# PART 14 — Final Practice

After teaching everything, give me a small practice set.

Do NOT put solutions next to the problems.

Give me approximately:

- 2 Easy
- 3 Medium
- 1 optional Hard/stretch problem

Choose them from the same research as Part 7: prefer problems that are frequently asked but were **not** already solved in Part 7, and tell me whether each is "frequently asked" or "added for pattern coverage".

For each, tell me only:

- Problem and LeetCode number
- Pattern it is intended to test
- What I should think about (guiding questions, not the answer)

Do not reveal the solution in chat unless I ask. If I am getting a notes file, put verified solutions in a **separate appendix** labelled "read only after an honest attempt".

---

# PART 15 — Practical Build Track

Several of my target companies (Anthropic, OpenAI, Stripe, Netflix) ask realistic engineering tasks instead of pure algorithm puzzles. After Part 14, give me **1–2 practical build exercises** that use this topic.

Examples of the style: an LRU cache, a time-based key-value store, a rate limiter, a log parser with top-k events, an in-memory database, a task scheduler.

For each exercise give:

- A short, realistic scenario
- **Three escalating levels** (each adds a requirement, like a real follow-up)
- Which part of this topic it exercises, and the data structure choice I should justify
- What to test and which edge cases to cover
- Any concurrency, failure or scale question an interviewer could add (state it, do not solve it unless I ask)

Same rule as Part 14: no solutions unless I ask. If a topic has no natural practical exercise yet, say so and point to the later topic where one appears.

---

# Teaching Rules

Follow these rules throughout:

### 1. Assume I am a beginner

Explain terminology before using it.

### 2. Don't overwhelm me

Depth is more important than volume.

### 3. Focus on interview usefulness

Prioritize concepts and patterns that repeatedly appear in technical interviews.

### 4. Don't make me memorize solutions

Teach the underlying reasoning.

### 5. Connect topics

Always explain how the current topic builds on previous topics and prepares me for the next one. Show the concrete bridge (for example, a structure or idea from this topic that becomes the core of the next).

### 6. Use Python, plus Java

All implementation examples should use Python, with a Java equivalent, unless there is a specific reason not to.

### 7. Explain complexity

Whenever code is shown, tell me its time and space complexity.

### 8. Use diagrams

Use simple ASCII/Markdown diagrams whenever they make the concept easier to understand.

### 9. Distinguish syntax from algorithm

I need to know both:

```text
"What code do I write?"
```

and:

```text
"Why does this algorithm work?"
```

### 10. No artificial backlog

Do not assign calendar dates or create an excessive number of tasks.

The goal is **mastery of the current topic**, not completing a checklist.

### 11. Never claim unverified results

Code must be run before it is called correct. If something was not tested, say so.

### 12. Ground recommendations in research (and save it)

When you recommend problems, companies, frequencies or "what interviewers ask", say where it came from. If you did not research it, say it is from memory. Do not present memory as data.

---

# Output Format

Unless I say otherwise, produce the topic as **one HTML study notes file per topic**, saved in the `dsa/` folder, using the shared `dsa/assets/dsa.css` and `dsa/assets/dsa.js` (the same shell as the existing topic notes). Do not inline a second copy of the shell. Keep the page free of other dependencies apart from the web font the shared CSS already uses.

**Never overwrite an existing notes file.** If a topic already has notes, write the new version to a new file (for example `<Topic>_v2.html`) so I can compare, with its own `data-key` so checklist ticks do not collide. Replace the old file only if I say so.

The page must have:

- A header with the topic name, a one-sentence summary, **Prev / Next topic** links, and counts (patterns, solved problems, practice problems)
- Navigation tabs covering Parts 1–15, plus appendices, **numbered in the same order as this prompt** (Recognition is Part 5, Checklist is Part 13, Practice is Part 14). Do not reorder the parts between topics.
- A Python/Java toggle that switches every code block at once
- **Syntax-highlighted code** (tokenise it, for example with Pygments, the way the existing notes do), not plain monochrome text
- Light and dark themes that both stay readable
- Collapsible sections for long material (solved problems, appendices) and a Practice mode that hides the observation and optimal solution until I ask
- Persistent mastery-checklist ticks, with unique ids

**Depth is expected.** Include trace tables or tiny hand traces, a worked interview walkthrough, and the "why" behind each step. A thin page that only lists templates and tables is not enough. Shorter than the previous topics' notes is a warning sign, so check what the earlier notes covered and do not drop it.

## Before you hand it over (quality gates)

1. **Validate the HTML**: balanced tags, unique ids, no broken `#` links, every nav tab has a section.
2. **Render it and look at it.** View at least one tab in the browser (and the Java view and the light theme if you can). Say which views you did not check.
3. **Check coverage against the research** (Part 7 rules): every pattern covered, frequently asked problems either solved, deferred to a later topic, or listed as outside the roadmap.
4. **Compare with any existing notes for the same topic** and report differences honestly: what the new version adds, what it lacks, and which is better where.
5. **Check the claims** in the notes (complexities, "this is a common bug", interview statistics) against what was verified or researched.
6. **Final message**: say what was verified, what was not, and what remains weak.

Teach the concepts in chat as well, one part at a time if the topic is large, and pause when I need to confirm understanding before continuing.

---

# Important Learning Rule

Do not move me to the next topic simply because I have read the material.

Move forward when I can demonstrate understanding through representative problems.

At the end, tell me:

> **"You are ready to move to [NEXT TOPIC] when you can..."**

and give me the concrete mastery conditions, such as:

- Write the core templates from memory and explain each line
- State the key invariant and the complexity argument aloud, unprompted
- Classify an unseen problem into a pattern within about a minute, and say when this topic does *not* apply
- Solve named representative problems without looking at a template
- Describe a case where I tried this technique, found it wrong, and what I switched to

---

Complete the topics in this chat.
