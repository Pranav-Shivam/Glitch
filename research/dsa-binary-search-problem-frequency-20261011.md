# Binary Search: which problems are asked

- **Retrieved:** 2026-10-11
- **Question:** Which binary search problems are asked most often at large tech companies (Google, Meta, Amazon, Microsoft, Apple and similar), for a 3-4 year engineer, and which patterns do they cover?
- **Used for:** `dsa/Binary_Search_Notes_v1.html` (Part 7 provenance, Appendix sources).
- **Local cache checked first:** `dsa-array-problem-frequency-2026.md` (Search in Rotated Sorted Array and Find Minimum in Rotated Sorted Array are deferred to Binary Search), `dsa-java-collections-problem-frequency-20261009.md` (Grind 75: Time Based Key-Value Store sits in the Binary Search section), `dsa-company-interview-calibration-2026.md`. No file covered binary search directly, so the web was searched.

## Findings

### Grind 75 (crackr.dev/grind75, fetched 2026-10-11; LeetCode numbers not shown on the page)
- Binary Search section has four problems: Binary Search (E), First Bad Version (E), Search in Rotated Sorted Array (M), Time Based Key-Value Store (M). No other problem on the page was tagged as binary search by the fetch tool.

### NeetCode 150 (community copy via search summary, NOT verified on neetcode.io; neetcode.io/roadmap returned only a title)
- Binary Search section reported as 7 problems: Binary Search, Search a 2D Matrix, Koko Eating Bananas, Find Minimum in Rotated Sorted Array, Search in Rotated Sorted Array, Time Based Key-Value Store, Median of Two Sorted Arrays. The same post's section headers were inconsistent (rotated-array problems also under Arrays and Hashing), so treat as a signal only.

### Company-tagged CSVs: github.com/liquidslr/leetcode-company-wise-problems (raw CSV `<Company>/5. All.csv`, fetched 2026-10-11)
- Each CSV has a `Frequency` column. Values look like a normalised score (100 = most frequent for that company, falling to about 2), not raw counts. The method is not documented. Only the first 100,000 characters of the Google, Meta, Amazon and Microsoft files were read (the files are 220k to 390k characters; sorted roughly by frequency, so the high-frequency end is covered, the long tail is not). Apple's file was read in full (35 binary-search rows).
- Google (rows with the Binary Search topic): Median of Two Sorted Arrays 73.9, Koko Eating Bananas 58.2, Split Array Largest Sum 57.6, Search in Rotated Sorted Array 57.9, Find Peak Element 56.5, Find First and Last Position 52.2, Sqrt(x) 52.0, Capacity To Ship Packages 44.8, Search a 2D Matrix 42.4, Find Minimum in Rotated Sorted Array 38.6, Time Based Key-Value Store 31.1, Kth Smallest Element in a Sorted Matrix 25.4.
- Meta: Random Pick with Weight 87.7, Find Peak Element 85.8, Find First and Last Position 73.1, Kth Missing Positive Number 68.6, Median of Two Sorted Arrays 66.8, Koko Eating Bananas 58.6, Search in Rotated Sorted Array 58.1, Kth Smallest Element in a Sorted Matrix 55.9, Sqrt(x) 48.0, Search Insert Position 46.5, Capacity To Ship Packages 46.5, Single Element in a Sorted Array 47.0, Find Minimum in Rotated Sorted Array 40.7, Binary Search 45.0, First Bad Version 45.0, Search a 2D Matrix 41.4, Search in Rotated Sorted Array II 38.5, Find the Duplicate Number 38.5, Search a 2D Matrix II 36.0, Time Based Key-Value Store 21.5.
- Amazon: Median of Two Sorted Arrays 76.8, Koko Eating Bananas 74.9, Search in Rotated Sorted Array 71.6, Find First and Last Position 60.8, Find Peak Element 60.4, Capacity To Ship Packages 59.2, Single Element in a Sorted Array 57.9, Search a 2D Matrix 57.7, Find the Duplicate Number 55.7, Split Array Largest Sum 52.4, Search a 2D Matrix II 50.7, Time Based Key-Value Store 47.7, Find Minimum in Rotated Sorted Array 47.3, Sqrt(x) 57.0, Search Insert Position 56.5, Binary Search 43.6, First Bad Version 38.9, Search in Rotated Sorted Array II 40.8, Minimum Number of Days to Make m Bouquets 42.5.
- Microsoft: Median of Two Sorted Arrays 75.2, Search in Rotated Sorted Array 68.5, Koko Eating Bananas 64.9, Find Peak Element 62.0, Single Element in a Sorted Array 59.7, Search Insert Position 57.0, Find First and Last Position 53.8, Search a 2D Matrix 52.8, Find Minimum in Rotated Sorted Array 50.0, Binary Search 47.3, Sqrt(x) 45.8, Find the Duplicate Number 45.8, Split Array Largest Sum 45.0, Capacity To Ship Packages 42.4, Search a 2D Matrix II 41.5, Time Based Key-Value Store 32.8, First Bad Version 27.3, Kth Smallest Element in a Sorted Matrix 25.0, Find Minimum in Rotated Sorted Array II 25.0.
- Apple (full file): Time Based Key-Value Store 68.0, Median of Two Sorted Arrays 63.7, Find First and Last Position 63.7, Snapshot Array 61.2, Search a 2D Matrix II 56.8, Sqrt(x) 51.0, Search in Rotated Sorted Array 48.7, Find Peak Element 39.4, Capacity To Ship Packages 35.0, Kth Smallest Element in a Sorted Matrix 35.0, Find Minimum in Rotated Sorted Array 29.5, Search a 2D Matrix 29.5, Random Pick with Weight 29.5, First Bad Version 22.0, Koko Eating Bananas 22.0, Binary Search 22.0.
- The Binary Search topic tag in these CSVs also catches problems that belong to other topics (sliding window, two pointers, DP, graphs, trees): Max Consecutive Ones III, Minimum Size Subarray Sum, Two Sum II, Subarray Product Less Than K, Longest Increasing Subsequence, Maximum Profit in Job Scheduling, Russian Doll Envelopes, Reverse Pairs, Count of Smaller Numbers After Self, Count Complete Tree Nodes, Closest Binary Search Tree Value, Swim in Rising Water, Path With Minimum Effort, Search Suggestions System, Design Hit Counter, My Calendar I/II, Missing Number, Intersection of Two Arrays.

### Educative blog "10 common binary search interview questions" (fetched 2026-10-11; company names are the article's own claims, no numbers)
- Search Insert Position (E; Amazon, Facebook), First and Last Position (M; Google, Microsoft), Peak Element (M; Google), Single Element in a Sorted Array (M; Amazon, Google), Find Minimum in Rotated Sorted Array (M; Amazon, Facebook), Search in Rotated Sorted Array (M; Google, Amazon, Microsoft), Smallest Missing Positive (M; Facebook), Find the Duplicate Number (M; Amazon, Google), Median of Two Sorted Arrays (H), Kth Smallest in a Sorted Matrix (H per article; LeetCode labels it Medium; Google, Microsoft).

### techinterview.org "Binary Search Interview Patterns" (fetched 2026-10-11)
- Pattern grouping: standard (find target), boundary (first/last occurrence), binary search on answer (Koko, Capacity to Ship, Bouquets, Median of Two Sorted Arrays), rotated array (I and II), 2D matrix (flatten, or staircase from the top-right corner).
- Claims binary search "appears in roughly 10-15% of FAANG coding interviews" with no cited source. Treat as unverified.

### Other search-summary signals (pages not opened)
- A 2025 LeetCode discuss recap (page returned 403) is summarised in search results as listing Microsoft's top topic as Binary Search and Strings, and "Binary Search on Answer" as a trending pattern. Meta's top topics in that recap were trees and graph traversal, not binary search.

## Caveats
- Frequency numbers are normalised scores from an unofficial GitHub repo built from LeetCode company tags; the underlying counts and time window are not stated. They are a signal, not ground truth. The Educative article's company names are blog claims.
- No source gave a mid-level (E4/L4/SDE-2) breakdown for binary search specifically.
- Binary-search weight at Meta looks lower than at Google/Amazon/Microsoft: the Meta rows are dominated by problems tagged with binary search for secondary reasons (Random Pick with Weight, Max Consecutive Ones III).

## Could not be fetched
- techinterviewhandbook.org/algorithms/binary-search (404), leetcode.com/discuss/post/7417074 (403), igotanoffer.com binary search article (403), neetcode.io/roadmap (title only, JS-rendered).

## Sources
- [Grind 75](https://crackr.dev/grind75)
- [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems)
- [Educative: 10 common binary search interview questions](https://educative.io/blog/binary-search-interview-questions)
- [techinterview.org: Binary Search Interview Patterns](https://www.techinterview.org/post/3233460596/binary-search-interview-patterns/)
- [NeetCode 150 list (LeetCode discuss)](https://leetcode.com/discuss/post/5808617/heres-the-list-of-neetcodes-top-150-ques-rydm/)
- [LeetCode discuss: most asked 2025](https://leetcode.com/discuss/post/7417074/)
