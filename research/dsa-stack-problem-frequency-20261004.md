# Most-asked stack problems at large tech companies

- **Retrieved:** 2026-10-04
- **Question:** Which stack problems are asked most often at Meta, Amazon, Google and similar companies, and which curated lists include them?
- **Used for:** problem selection and provenance labels in `dsa/Stack-Mastery-Notes_v2.html` (Part 7 and Part 14).
- **Local cache checked first:** `dsa-array-problem-frequency-2026.md` (2026-10-04) only has stack problems in its "belongs to Stack" table (Valid Parentheses, Basic Calculator II, Min Remove to Make Valid Parentheses). No stack-specific file existed.

## Findings (what each source said)

### Curated lists
- **Grind 75** (via crackr.dev/grind75, fetched): section "Stack, 7 problems, 3h 20m": Valid Parentheses (Easy), Implement Queue using Stacks (Easy), Min Stack (Medium), Evaluate Reverse Polish Notation (Medium), Trapping Rain Water (Hard), Basic Calculator (Hard), Largest Rectangle in Histogram (Hard). Daily Temperatures is NOT in the list.
- **NeetCode 150** (via pypup.com/paths/neetcode-150, fetched; the neetcode.io page returned no list): Stack section: Valid Parentheses, Min Stack, Evaluate Reverse Polish Notation, Generate Parentheses, Daily Temperatures, Car Fleet, Largest Rectangle in Histogram. Generate Parentheses is a backtracking problem and is deferred in the notes.
- **Tech Interview Handbook "best practice questions"** (fetched): the only stack problem in its 5-week list is Valid Parentheses (Week 1).
- **Blind 75**: could not be fetched (HTTP 403). From memory (NOT verified in this session): Valid Parentheses is its only stack problem.
- **Hello Interview, stack overview** (fetched): practice problems Decode String and Longest Valid Parentheses; sidebar also lists Valid Parentheses, Monotonic Stack, Daily Temperatures, Largest Rectangle in Histogram. No frequency claims.

### Company or frequency data (low reliability)
- **dsaprep.dev company-wise article** (fetched): Valid Parentheses appears 191 times across 73 companies in its data; Trapping Rain Water 100 times across 42 companies. Method not explained.
- **Meta:** a web search summary (jobright.ai "Meta Technical Interview Questions: Complete 2026 Guide", not fetched in full) states Meta frequently asks Minimum Remove to Make Valid Parentheses (Medium) and Basic Calculator II (Medium). Single source.
- **Verve Copilot Meta top-30 list** (fetched): contains one parentheses question, "minimum number of operations to make a parentheses string valid" (a variant, LeetCode 921 style). No frequency numbers.
- **interviewpilot.dev** (fetched): claims "linked lists and stacks" are about 10% of FAANG coding questions, and names monotonic stack (next greater element) and largest rectangle as the main stack patterns. No per-company breakdown. Method not explained.
- **Design Gurus Amazon-14 list** (fetched): contains no stack problem except "balanced parentheses generation" (backtracking).

## What this means for the notes (inferred, not quoted)
- Problems in two or more independent sources here: Valid Parentheses, Min Stack, Evaluate RPN, Largest Rectangle in Histogram (Grind 75 + NeetCode 150, plus Hello Interview for the histogram), Trapping Rain Water (Grind 75 + dsaprep).
- Problems in only one source here: Daily Temperatures (NeetCode 150, Hello Interview sidebar), Car Fleet (NeetCode 150), Implement Queue using Stacks (Grind 75), Decode String (Hello Interview), Basic Calculator (Grind 75), Basic Calculator II and Minimum Remove to Make Valid Parentheses (Meta, one 2026 guide).
- Stacks are a small share of interview questions overall (about 10% by one third-party estimate, which combines them with linked lists). The pattern matters because it recurs inside harder problems (histogram, calculators, trees and graphs later).

## Reliability caveats
- All numbers are crowd-sourced or from prep-site blogs; their method is rarely explained. Treat as a signal, not a guarantee.
- Several results came from a search summary, not the page itself (Meta claim, Verve, jobright).
- Nothing here is specific to X (Twitter), Anthropic or OpenAI.

## Pages that could not be fetched
- leetcode.com/discuss/post/8343565 (Blind 75 overview): HTTP 403.
- leetcode.com/discuss/post/7417074 (most-asked 2025): HTTP 403.
- medium.com/@nikhil.cse16 (NeetCode 150 stack guide): HTTP 403.
- neetcode.io/roadmap: page shell only, no problem list.

## Sources
- [Grind 75 problems (crackr.dev)](https://crackr.dev/grind75)
- [NeetCode 150 path (pypup.com)](https://pypup.com/paths/neetcode-150)
- [Tech Interview Handbook, best practice questions](https://www.techinterviewhandbook.org/best-practice-questions/)
- [Hello Interview, stack overview](https://www.hellointerview.com/learn/code/stack/overview)
- [Company-wise LeetCode questions (dsaprep.dev)](https://www.dsaprep.dev/blog/company-wise-leetcode-questions/)
- [Meta technical interview questions 2026 (jobright.ai)](https://jobright.ai/blog/meta-technical-interview-questions-complete-2026-guide/)
- [Meta top 30 LeetCode questions (Verve Copilot)](https://www.vervecopilot.com/hot-blogs/meta-leetcode-interview-questions)
- [LeetCode interview questions, top patterns by company (interviewpilot.dev)](https://interviewpilot.dev/blog/leetcode-interview-questions)
- [14 most popular Amazon coding interview questions (Design Gurus)](https://www.designgurus.io/blog/amazon-14-question)
