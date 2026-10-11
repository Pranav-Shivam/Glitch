# DSA roadmap gap check: which topics and phases are missing

- **Retrieved:** 2026-10-11
- **Question:** Beyond the 13-topic roadmap (Arrays ... DP), which topics and prep phases do the big curated lists and recent candidate reports suggest are missing for a 3-4 year engineer targeting Meta, Google, Amazon, Netflix, Anthropic, OpenAI, X and similar?
- **Used for:** the roadmap and "Roadmap rules" in `dsa/dsa_prompt.md`, and the roadmap table in `dsa.html`.
- Related: [dsa-company-interview-calibration-2026.md](dsa-company-interview-calibration-2026.md) (2026-10-04).

## Findings

### Topic coverage in curated lists
- **NeetCode 150 categories** (third-party GitHub repo, counts approximate, not from neetcode.io): Arrays & Hashing 9, Two Pointers 5, Sliding Window 6, Stack 7, Binary Search 7, Linked List 11, Trees 15, Tries 3, Heap 7, Backtracking 9, Graphs 13, **Advanced Graphs 6**, 1-D DP 12, 2-D DP 11, **Greedy 8, Intervals 6, Math & Geometry 8, Bit Manipulation 7**. So the current roadmap has no home for Greedy, Intervals, Math, Bit Manipulation, Advanced Graphs, and does not split DP.
- **Blind 75** categories (Scribd list): Arrays & Hashing, Two Pointers, Sliding Window, Stack, Binary Search, Linked List, Trees, Tries, Heap, Backtracking, Graphs, Advanced Graphs, 1D/2D DP, Greedy, Intervals. Per-topic counts conflict between sources; not confirmed.
- **Tech Interview Handbook study cheatsheet** priorities: **High:** Array, String, Sorting and searching, Matrix, Tree, Graph. **Mid:** Hash Table, Recursion, Linked List, Queue, Stack, Heap, Trie, Interval. **Low:** Dynamic programming, Binary, Math, Geometry. So **String, Sorting, Matrix and Recursion are explicit topics there** and are absent from the roadmap. Note TIH rates DP "Low" while Google reports below rate it high: weight depends on company.
- TIH Interval page: treated as a subset of array questions; essential: Merge Intervals, Insert Interval; practice: Non-overlapping Intervals, Meeting Rooms (I, II). Key moves: sort by start, overlap check, merge two.
- TIH prep page: study one topic then practise it immediately; warns against unstructured grinding; recommends mock interviews (interviewing.io); says nothing about spaced review. Bare minimum ~30 h, well prepared ~100 h, holistic ~3 months at 2-3 h/day.

### Frequency signals (all weak, crowd-sourced)
- Amazon (candidate-report table, ~500 questions): Array 50.8%, String 27.4%, DP 18.8%. Another analysis: DP ~55%, Graphs ~48% (estimate, method unclear); Arrays, Trees, Strings >60% combined.
- Meta (2026 guide): prefix sum + hashmap ~25% of loops, BFS/DFS on trees and grids ~20%, DP ~10%.
- Google (same guide): BFS/DFS ~25%, DP ~20%. A Google India prep page claims DP ~58% and graphs ~49% of technical rounds, bit manipulation ~16% (no sample size given, 2022-2025 data). Another says Google question choice varies significantly by team.
- A 2026 LeetCode Discuss post (analysis of 74 interviews, 2024-2026; page returned 403 so only the search snippet was read) says Google, LinkedIn, Microsoft show the clearest DSA signal; Meta is increasingly hybrid (system design and behavioural alongside DSA); Amazon design depth and Leadership Principles appear as consistently as DSA; Google lists graphs and DP as recurring.
- Meta glassdoor reports (June 2026): two coding sessions of two mediums, plus system design and a behavioural round with a manager. Recurring topic text: arrays, strings, trees, graphs, BFS/DFS, heaps, hash maps, DP (may be a shared snippet, not independent).
- No reliable 2026 source gave a frequency for intervals, greedy or math.

### Practical / design / concurrency signals
- Anthropic: aggregator pages (PracHub) list concurrent web crawlers, crawler deduplication, parallel/batch image processors; one Jan 2026 phone-screen report was a web crawler question; an Aug 2026 report says coding tests multithreading. Another guide argues the round that filters most candidates is discussing the downsides of the system you built. All anecdotal; aggregator sites sell access.
- OpenAI: one 1point3acres thread describes a 75-minute onsite on concurrency primitives, threads, locks, task queues (details behind login, not verified).
- Uber SDE-2: a 90-minute machine-coding round reported (object-oriented, extensible, async, thread sync). A guide says dedicated machine-coding / LLD rounds are reported by 2026 SDE-2 candidates, 45-60 min: rate limiter, file system, trip state machine, parking lot. Amazon SDE-2 reported to test OOP and low-level design across the loop.
- Nothing specific found for Atlassian.

### Review and mocks
- Spaced-repetition tools for LeetCode exist (intervals like 1, 3, 7, 14 days; or doubling after each success). Practitioner advice: hide the solution and re-solve from scratch before checking. No source found on practising without code execution; the Meta no-run editor claim comes from the earlier calibration file.

## Conclusions (inferred from the above, not stated by a source)
1. Add topics: **Strings, Recursion, Intervals and Sorting, Greedy, Bit Manipulation and Math**.
2. Split **Graphs** (BFS/DFS plus grid/matrix, topological sort, Union-Find, shortest path) and **DP** (1-D, 2-D, other); both are repeatedly reported as high-frequency at Google and Amazon.
3. Add a **practical build / design / concurrency** phase (LRU, rate limiter, crawler, OOD) because Anthropic, OpenAI, Uber and Amazon reports point at it.
4. Add a **mixed review and mock** phase at the end, and a light spaced-review rule.
5. Treat Segment tree / Fenwick, KMP, advanced geometry as optional extras (NeetCode and TIH both mark them low priority; no E4-level evidence found).

## Caveats
- Every frequency number is from a prep site or candidate post; methods are not disclosed and several are SEO pages. Treat as direction only.
- Counts for NeetCode/Blind categories come from third-party repos, not the official sites.

## Could not be fetched / returned nothing useful
- `leetcode.com/discuss/post/8446005/` (HTTP 403; only search snippet seen).
- `techinterviewhandbook.org/grind75/` (title and nav only, no topic list).
- Search "Grind 75 topic breakdown" returned unrelated results.
- No per-problem 2026 "times asked" counts for Number of Islands or Merge Intervals found.

## Sources
- [NeetCode topic counts (GitHub, third-party)](https://github.com/bhanuprasadChesetti/neetcode-dsa-roadmap)
- [Blind 75 list (Scribd)](https://www.scribd.com/document/894381025/75)
- [Blind 75 topic counts (Codingshuttle)](https://www.codingshuttle.com/sheets/blind-75-sheet/)
- [Tech Interview Handbook: study cheatsheet](https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/)
- [Tech Interview Handbook: coding interview prep](https://www.techinterviewhandbook.org/coding-interview-prep/)
- [Tech Interview Handbook: intervals](https://www.techinterviewhandbook.org/algorithms/interval/)
- [Meta coding interview questions 2026 (copilotinterview)](https://copilotinterview.com/blog/meta-coding-interview-questions)
- [Amazon coding interview questions 2026 (dsaprep.dev)](https://www.dsaprep.dev/blog/amazon-coding-interview-questions)
- [Google L4 coding questions 2026 (dglearning)](https://dglearning.substack.com/p/the-12-google-coding-questions-l4)
- [Google LeetCode questions 2026 (papersadda)](https://papersadda.com/article/leetcode-questions-google-2026/)
- [Where leetcode still matters in 2026 (LeetCode Discuss, 403)](https://leetcode.com/discuss/post/8446005/)
- [Anthropic interview questions (PracHub)](https://prachub.com/companies/anthropic?page=2)
- [Anthropic coding summary (1point3acres)](https://www.1point3acres.com/interview/thread/1171355)
- [OpenAI 75-min concurrency onsite (1point3acres)](https://www.1point3acres.com/interview/thread/1154031)
- [Uber SDE-2 experience (roundz)](https://roundz.substack.com/p/interview-experience-169-uber-sde2)
- [SDE-2 prep guide (workat.tech)](https://workat.tech/general/article/sde-2-interview-prep-ultimate-guide-dn1am88dbutl/index.html)
- [Spaced repetition schedule (redgreencode)](https://www.redgreencode.com/leetcode-tip-10-planning-a-spaced-repetition-schedule/)
