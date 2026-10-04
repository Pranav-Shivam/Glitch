# Company interview calibration for a 3–4 year engineer

- **Retrieved:** 2026-10-04
- **Question:** What do Meta, Amazon, Netflix, Google, Anthropic, OpenAI, X (Twitter) and other multinationals ask a candidate with 3–4 years of experience?
- **Used for:** the "Calibration" section of `dsa/das_prompt.md`.

## Summary

Two interview styles exist.

1. **Algorithmic, pattern-based:** Meta, Google, Amazon, Microsoft, Uber, partly X. LeetCode medium core, timed.
2. **Practical, build-from-scratch:** Anthropic, OpenAI, Stripe, partly Netflix. Realistic engineering tasks, escalating levels, debugging in a codebase.

At mid-level, easy problems are warm-ups. Core skill is medium problems quickly, with clean code, edge cases, complexity and follow-ups.

## Per company

### Meta (E4 mid-level, E5 senior)
- Onsite has 2 coding rounds of 45 minutes. Typically 2 problems per round, in CoderPad with no code execution. Usually one medium plus one easy, sometimes two mediums, occasionally a hard.
- E5 round layout reported: 5 min intro, 35 min coding for 2 problems, 5 min questions. About 18–20 minutes per problem.
- Most-reported E4 problems: 1249 Minimum Remove to Make Valid Parentheses, 227 Basic Calculator II, 236 Lowest Common Ancestor of a Binary Tree, 680 Valid Palindrome II, 314 Binary Tree Vertical Order Traversal.
- Most-reported E5 problems: 1249, 314, 227, 215 Kth Largest Element in an Array, 408 Valid Word Abbreviation.
- Topic mix for E4: string manipulation, tree traversal, stack/queue (parentheses, calculators), binary trees, graph (islands), palindrome/substring. So arrays are a foundation, not the headline topic.
- Hello Interview claims "Meta almost only asks questions from their recently asked questions list". Single-source claim.
- Tip from sources: practise mediums and hards in under 15 minutes each. If stuck on problem 1 for more than 15 minutes, outline a partial solution and move on.

### Google (L4 mid-level)
- Phone screen: 1–2 medium problems. Onsite: 2–3 coding rounds of 45 minutes, usually one challenging problem each.
- Medium to hard. Expect graph traversal, dynamic programming, string manipulation, BFS/DFS, two pointers, backtracking.
- Watches code structure, variable names, edge-case handling, and explaining approach and complexity before coding.

### Amazon (SDE-2)
- Online assessment: about 90 minutes coding with 2 LeetCode-style problems, plus a 15-minute work simulation and a 10-minute work-style survey.
- Reported array-like questions: find all anagram start indices, sliding window sum and maximum for window size 3, pairs of strings differing by one right rotation.
- Loop covers medium to hard: graphs/trees, arrays/strings, linked lists, search/sort, stacks/queues, hash tables, DP. Also behavioural and design.
- A design-gurus article says Amazon does not copy problems verbatim, but its questions map closely to LeetCode mediums and hards.

### Microsoft
- 4 interviews of about 45 minutes, typically one DSA question each. Mostly LeetCode easy to medium, straightforward rather than tricky. Level mapping for 3–4 years NOT confirmed.

### Uber
- Coding rounds at medium to slightly harder, runnable code expected. Plus a specialisation round, system design with scale math, and behavioural.

### X (Twitter)
- Reported: phone screen, 2 coding rounds, 1 system design, 1 hiring manager/behavioural. LeetCode medium typical, sometimes harder. Categories: array/string, graph traversal (DFS/BFS), trees and prefix trees.
- **Weak data:** from Glassdoor-style pages, unclear whether it reflects the company after the 2022 changes.

### Netflix
- Onsite loop of 4–5 back-to-back interviews of 45–60 minutes: DSA, object-oriented design, system architecture, culture.
- Coding is practical and production-flavoured: caches (LRU), log parsing, top-k events, pagination, TTL behaviour, debugging service functions. Also reported: interval merging, k most frequent elements, word transformation sequences, sliding window.
- Senior candidates get more tradeoff and design-adjacent probes.

### Anthropic
- Process: recruiter call, coding challenge, onsite of about 4–5 hours.
- Coding challenge: one problem split into 4 levels in about 90 minutes (CodeSignal), each level unlocked after passing the previous tests. Some roles get a 60-minute live assessment.
- Not LeetCode puzzles: build an in-memory database, a banking system, a task scheduler, a URL crawler. Reported: LRU cache with escalating constraints, longest-running function from stack-trace samples, deduplicate files in a directory, extend a feature in an unfamiliar codebase.
- Themes: data mutation, concurrency and multithreading (recurs across rounds), hash maps, parsing, arrays, strings, sorting, edge cases, justifying decisions.
- Python reportedly mandatory. Less time pressure than Meta or OpenAI, less code written, more weight on reasoning.
- Details given are for mid to senior-level engineers.

### OpenAI
- Process: recruiter screen, technical screen (45–60 min live coding), panel/onsite of 4–6 hours with 4–6 interviewers over 1–2 days, bar-raiser/hiring committee review.
- Recurring theme: practical stateful components under time pressure. Time-based key-value store, rate limiter, usage-credit system with expiry, LRU cache. Also system discussions: distributed rate limiting, API gateway behaviour, chat products, inference-serving tradeoffs.
- Formats vary by team: pair coding, take-home, technical tests.

### Stripe
- No LeetCode. Real codebase with a failing test to debug, or build a feature against an unfamiliar API with docs and internet open. Long story-driven prompts like rate limiters or data parsing.

### Atlassian
- One-hour interview with about four algorithm questions that extend each other, plus OOP/OS/GC theory in the last 10 minutes. (Single older candidate post.)

## Reliability caveats
- Sources are prep sites, candidate posts and Glassdoor-style pages. Not company-published.
- Processes change. Re-check before relying on any single detail.
- Microsoft level mapping and X post-2022 data unconfirmed.

## Not retrievable
- `leetcode.com/discuss/post/6017658/` (HTTP 403).
- `interviewsolver.com/interview-questions/meta` (page returned navigation only, no data).

## Sources
- [Anthropic interview process (interviewing.io)](https://interviewing.io/anthropic-interview-questions)
- [Anthropic SWE interview (IGotAnOffer)](https://igotanoffer.com/en/advice/anthropic-software-engineer-interview)
- [OpenAI SWE interview guide (Interview Query)](https://www.interviewquery.com/interview-guides/openai-software-engineer)
- [Netflix coding screen guide](https://www.coditioning.com/blog/503/netflix-swe-coding-screen)
- [Netflix senior SWE questions (Interview Kickstart)](https://interviewkickstart.com/interview-questions/companies/netflix/senior-software-engineer)
- [Meta E4 guide (Hello Interview)](https://www.hellointerview.com/guides/meta/e4)
- [Meta E5 guide (Hello Interview)](https://www.hellointerview.com/guides/meta/e5)
- [Google L4 guide (Hello Interview)](https://www.hellointerview.com/guides/google/l4)
- [Amazon SDE-2 experience, 3–4 years (LeetCode Discuss)](https://leetcode.com/discuss/post/8420230/amazon-sde-2-interview-experience-2026-e-t1g8/)
- [X software engineer interview questions (Glassdoor)](https://www.glassdoor.com/Interview/Twitter-Software-Engineer-Interview-Questions-EI_IE100569.0,7_KO8,25.htm)
- [Uber interview process (interviewing.io)](https://interviewing.io/uber-interview-questions)
- [Stripe SWE interview (Interview Coder)](https://www.interviewcoder.co/blog/stripe-software-engineer-interview)
- [Amazon interview questions (Design Gurus)](https://www.designgurus.io/blog/amazon-14-question)
