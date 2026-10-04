# Most-asked array problems at large tech companies

- **Retrieved:** 2026-10-04
- **Question:** Which array problems are most commonly asked at Meta, Amazon, Google and similar companies?
- **Used for:** the "How to choose the problems" rule in `dsa/das_prompt.md`, and the Arrays notes problem set.

## Problems that recurred across sources

Two Sum, Best Time to Buy and Sell Stock, Contains Duplicate, Product of Array Except Self, Maximum Subarray, Maximum Product Subarray, 3Sum, Container With Most Water, Trapping Rain Water, Subarray Sum Equals K, Merge Intervals, Majority Element, Rotate Array, First Missing Positive, Move Zeroes, Jump Game, Single Number, Remove Element, Missing Number, Plus One, Search in Rotated Sorted Array, Maximum Consecutive Ones, Toeplitz Matrix.

## Curated lists

- **Blind 75 array section (10):** Two Sum, Best Time to Buy and Sell Stock, Contains Duplicate, Product of Array Except Self, Maximum Subarray, Maximum Product Subarray, Find Minimum in Rotated Sorted Array, Search in Rotated Sorted Array, 3Sum, Container With Most Water. The list was compiled by an experienced Meta engineer.
- **Tech Interview Handbook, week 1 (sequences):** Two Sum, Contains Duplicate, Best Time to Buy and Sell Stock, Valid Anagram, Valid Parentheses, Maximum Subarray, Product of Array Except Self, 3Sum, Merge Intervals, Group Anagrams. Optional: Maximum Product Subarray, Search in Rotated Sorted Array. The author's reasoning: arrays and strings are the most common interview question types, and many questions are mashes of these core techniques.
- **Meta top-30 list (Verve Copilot), array items:** Toeplitz Matrix, Move Zeroes, First Duplicate, Maximum Consecutive Ones, First Missing Positive, Container With Most Water, Jump Game, Subarray Sum Equals K, Single Number, Two Sum, Trapping Rain Water.
- **Amazon list (Design Gurus), array-flavoured:** Biggest Island, K Closest Points to the Origin, Number of Islands, Top K Frequent Numbers, Merge Intervals. Others on the list: tree, linked list, heap, graph and sliding-window problems.

## Company frequency numbers (low reliability)

From a third-party summary, method not explained:
- Subarray Sum Equals K: 81% frequency at Meta, 72.9% at Amazon.
- Merge Intervals: 72% at Meta.
- Product of Array Except Self: 67.5% at Amazon.
- Two Sum: 100% at Amazon.

Treat as a signal only.

## Where each belongs in the DSA roadmap

Roadmap: Arrays, Hashing, Two Pointers, Sliding Window, Stack, Binary Search, Linked List, Trees, Tries, Heaps, Backtracking, Graphs, Dynamic Programming.

| Problem | Belongs to |
|---|---|
| Two Sum, Contains Duplicate, Group Anagrams, Valid Anagram, First Duplicate | Hashing |
| 3Sum, Container With Most Water | Two Pointers |
| Search in Rotated Sorted Array, Find Minimum in Rotated Sorted Array | Binary Search |
| Valid Parentheses, Basic Calculator II, Min Remove to Make Valid Parentheses | Stack |
| Kth Largest, K Closest Points, Top K Frequent | Heaps |
| Number of Islands, Biggest Island | Graphs |
| **Merge Intervals** | **No topic in the roadmap (intervals/sorting)** |
| **Jump Game** | **No topic (greedy / DP)** |
| **Single Number** | **No topic (bit manipulation)** |

## Observations
- Meta mid-level most-reported problems are mostly strings, stacks, trees, graphs, not arrays. Arrays are the foundation inside harder problems.
- Gaps in the roadmap: intervals, greedy, bit manipulation, math.

## Not retrievable
- `leetcode.com/discuss/post/6017658/` (HTTP 403).
- `interviewsolver.com/interview-questions/meta` (no data returned).

## Sources
- [25 Array Problems To Revise Before Interviews (LeetCode Discuss)](https://leetcode.com/discuss/post/7452139/25-array-problems-to-revise-before-inter-8l98/)
- [Blind 75 overview (LeetCode Discuss)](https://leetcode.com/discuss/post/8343565/blind-75-the-only-leetcode-list-most-int-eodf/)
- [Tech Interview Handbook, best practice questions](https://www.techinterviewhandbook.org/best-practice-questions/)
- [Amazon interview questions (Design Gurus)](https://www.designgurus.io/blog/amazon-14-question)
- [Meta top 30 LeetCode questions (Verve Copilot)](https://www.vervecopilot.com/hot-blogs/meta-leetcode-interview-questions)
- [Meta E4 guide (Hello Interview)](https://www.hellointerview.com/guides/meta/e4)
