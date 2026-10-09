# Most-asked hashing (hash map / hash set) problems at large tech companies

- **Retrieved:** 2026-10-09
- **Question:** Which hash map / hash set problems are most commonly asked at Meta, Amazon, Google and similar companies, and which curated lists include them?
- **Used for:** `dsa/Hashing_Notes_v1.html` (Part 7 provenance labels, Sources note).
- **Local cache checked first:** `dsa-array-problem-frequency-2026.md` already assigns Two Sum, Contains Duplicate, Group Anagrams, Valid Anagram, First Duplicate to Hashing; lists Subarray Sum Equals K at 81% Meta / 72.9% Amazon (low reliability). `dsa-company-interview-calibration-2026.md` says Amazon's loop includes hash tables and Anthropic themes include hash maps, LRU cache, time-based/in-memory stores.

## Findings

- **NeetCode 150 "Arrays & Hashing" (9 problems), per a Scribd copy and a GitHub summary:** Contains Duplicate (E), Valid Anagram (E), Two Sum (E), Group Anagrams (M), Top K Frequent Elements (M), Encode and Decode Strings (M), Product of Array Except Self (M), Valid Sudoku (M), Longest Consecutive Sequence (M). A DEV Community write-up says Two Sum, Group Anagrams and Longest Consecutive Sequence share one hash-lookup idea.
- **Conflict:** a LeetCode Discuss post titled as NeetCode's list shows a different "Array & Hashing" section (includes Maximum Subarray etc.); looks like a community reconstruction. Used the 9-problem list.
- **Blind 75 "Arrays & Hashing":** sources disagree on count (8 vs 10). Names above were confirmed only from the NeetCode lists, not from a fetched Blind 75 page.
- **Subarray Sum Equals K (560):** appears on a Meta most-asked article (Arrays & Strings), interviewing.io, Educative, Design Gurus; standard solution prefix sum + hash map of earlier prefix sums.
- **Insert Delete GetRandom O(1) (380):** in a Medium compilation of map questions; a third-party Apple table shows about 59.5% (method unknown). Not tagged Meta on the Meta index seen.
- **LRU Cache (146):** no frequency data found; a Tesla prep guide says it matters for systems-adjacent / senior roles. Local calibration file: Anthropic reportedly asks LRU cache with escalating requirements.
- **2025 LeetCode Discuss recap:** Hash Table is among topics that stay consistent across firms (Arrays, Strings, Search/Sorting, Hash Tables, Trees, Graphs, DP).

## Caveats

- Crowd-sourced prep-site claims, no stated method, no counts for hashing specifically. Treat as a signal.
- Problems 205, 219, 202, 36 (partly), 525, 974, 454 are NOT individually backed by a source above beyond curated-list membership noted; labelled "added for pattern coverage" in the notes unless listed above. 36 is on NeetCode 150.
- The search tool returned summaries only; no list page was opened in full.

## Could not be fetched / unusable

- `1point3acres.com` Meta frequency list (login-gated).
- LeetCode Discuss pages (HTTP 403 earlier in this repo's research); official Blind 75 list page not retrieved.

## Sources

- [NeetCode 150 copy (Scribd)](https://www.scribd.com/document/940061900/NeetCode-150)
- [NeetCode practice tracker (Scribd)](https://www.scribd.com/document/875684854/Practice)
- [NeetCode 150 list (LeetCode Discuss)](https://leetcode.com/discuss/post/5808617/heres-the-list-of-neetcodes-top-150-ques-rydm/)
- [DEV Community: the only interview prep sheet I finished](https://dev.to/soham0047/the-only-interview-prep-sheet-i-actually-finished-4alb)
- [Subarray Sum Equals K (interviewing.io)](https://interviewing.io/questions/subarray-sum-equals-k)
- [2025 LeetCode Discuss recap](https://leetcode.com/discuss/post/7417074/)
- Local: `research/dsa-array-problem-frequency-2026.md`, `research/dsa-company-interview-calibration-2026.md`
