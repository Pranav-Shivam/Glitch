# Java Collections for interviews: which problems and questions come up

- **Retrieved:** 2026-10-09
- **Question:** Which problems where the *choice of Java collection* is the crux (PriorityQueue, TreeMap, ArrayDeque, LinkedHashMap, HashMap+ArrayList, comparators) are asked most at large tech companies, and which conceptual Collections questions recur?
- **Used for:** `dsa/Java_Collections_Notes_v1.html` (Part 7 provenance labels, Appendix B sources).
- **Local cache checked first:** `dsa-hashing-problem-frequency-2026.md` (2026-10-09) for hash problems (380 Insert Delete GetRandom ~59.5% on one Apple table, method unknown; LRU 146 no frequency data); `dsa-stack-problem-frequency-20261004.md` (Min Stack, Queue using Stacks in Grind 75); `dsa-company-interview-calibration-2026.md`.

## Findings

### Grind 75 (crackr.dev/grind75, fetched)
- Heap (4): K Closest Points to Origin (M), Task Scheduler (M), Find Median from Data Stream (H), Merge k Sorted Lists (H).
- Linked List section contains LRU Cache (M). Binary Search section contains Time Based Key-Value Store (M). Arrays contains Merge Intervals (M) and Insert Interval (M). Stack contains Implement Queue using Stacks (E) and Min Stack (M).
- NOT in Grind 75: Insert Delete GetRandom O(1), Top K Frequent Elements, Kth Largest Element in an Array, Meeting Rooms II, Group Anagrams, Moving Average, Number of Recent Calls.

### techinterview.org "Top 50 most asked by company" (fetched; 62 unique problems, method not stated)
- Amazon list: Two Sum (1), LRU Cache (2, hash map + doubly linked list), Merge Intervals (3), K Closest Points to Origin (5, heap or quickselect), Reorder Data in Log Files (7, custom sort).
- Google list: Sliding Window Maximum (3, monotonic deque), Merge K Sorted Lists (4, heap), Median from Data Stream (10, two heaps).
- Meta list: Subarray Sum Equals K, Dot Product of Two Sparse Vectors, Random Pick with Weight, Nested List Weight Sum.
- Apple list: Flatten Nested List Iterator (4), Implement Stack using Queues (7).
- Microsoft list: Group Anagrams (9, sorted-chars key), Min Stack (10).
- Blind 75 / NeetCode weeks: Top K Frequent (wk1), Kth Largest Element (wk4), LRU Cache (wk3).
- Not in that article: Meeting Rooms II, Insert Delete GetRandom, Time Based KV Store, Sort Characters by Frequency, Top K Frequent Words.

### Search-result summaries only (pages not opened)
- An Amazon candidate report (via search summary) describes a heap question on dynamically retrieving top-k, where the choice of min-heap vs max-heap was the focus.
- Meta candidate reports mention Median of Data Stream with trouble balancing two heaps.
- Heap-pattern guides (techinterview.org heap patterns, DEV Community) state: Kth Largest uses a min-heap of size k; K Closest uses a max-heap of size k keyed by squared distance; Top K Frequent uses a count map plus a size-k heap, or bucket sort O(n).
- No source found for Top K Frequent Words, Meeting Rooms II or TreeMap-specific questions.

### Conceptual Java Collections questions (search summaries from prep sites, representative not ranked)
- HashMap internals (buckets, load factor 0.75, resize, treeification), HashMap vs ConcurrentHashMap, fail-fast vs fail-safe iterators, synchronized vs concurrent collections, Comparable vs Comparator, ArrayList vs LinkedList, Iterator vs ListIterator, why map keys should be immutable, how TreeMap keeps order.
- Summary also states from general knowledge (not verified here): treeify at bucket size >= 8 with table >= 64, else resize. Notes verify behaviour by running Java where possible, otherwise label as not run.

## Caveats
- Crowd-sourced prep-site lists, no stated methods, no counts for this topic. Treat as a signal.
- Company ties come from one aggregator article; several problems (Top K Frequent Words, Meeting Rooms II, Time Based KV Store as a company ask) have no source here, so they are labelled "added for pattern coverage" or "in Grind 75 only".
- Conceptual-question list is from vendor/prep blog summaries, not interview logs.

## Could not be fetched
- `mintlify.com/sparktsao/Questions100/problems/top-frequency` returned a 308 redirect to `mintlify.wiki`; not followed.
- Scribd, Glassdoor, 1point3acres results appeared in search but were not opened (login/paywall).

## Sources
- [Grind 75 (crackr.dev)](https://crackr.dev/grind75)
- [Top 50 most asked problems by company (techinterview.org)](https://www.techinterview.org/post/3233474385/coding-interview-top-50-most-asked-problems-by-company-google-amazon-meta-apple-microsoft-blind-75-neetcode-150/)
- [Heap and Priority Queue Interview Patterns (techinterview.org)](https://techinterview.org/heap-priority-queue-interview-patterns/)
- [DSA heap key questions (DEV Community)](https://dev.to/nozibul_islam_113b1d5334f/dsa-heap-key-questions-and-challenges-3a55)
- [Java Collection Framework interview questions (kaashivinfotech)](https://www.kaashivinfotech.com/blog/?p=22551)
- [Java interview questions (bosscoderacademy)](https://www.bosscoderacademy.com/blog/java-interview-questions)
- Local: `research/dsa-hashing-problem-frequency-2026.md`, `research/dsa-stack-problem-frequency-20261004.md`, `research/dsa-company-interview-calibration-2026.md`
