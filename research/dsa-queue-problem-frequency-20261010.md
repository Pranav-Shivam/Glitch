# Queue / Deque / BFS: which problems are asked

- **Retrieved:** 2026-10-10
- **Question:** Which queue, deque and BFS-with-queue problems are asked most at large tech companies, and which belong to later topics (trees, graphs, heaps)?
- **Used for:** `dsa/Queue_Notes_v1.html` (Part 7 provenance, Appendix sources).
- **Local cache checked first:** `dsa-stack-problem-frequency-20261004.md` (Implement Queue using Stacks in Grind 75 Stack section), `dsa-java-collections-problem-frequency-20261009.md` (Sliding Window Maximum = Google list #3, Implement Stack using Queues = Apple list #7, Moving Average / Number of Recent Calls NOT in Grind 75), `dsa-company-interview-calibration-2026.md`.

## Findings

### Grind 75 (crackr.dev/grind75, fetched 2026-10-10; technique labels are the fetch tool's classification, not the site's)
- Queue/BFS standard: Binary Tree Level Order Traversal (M, Binary Tree), Binary Tree Right Side View (M), Serialize and Deserialize Binary Tree (H), Rotting Oranges (M, Graphs), 01 Matrix (M), Word Ladder (H), Minimum Height Trees (M).
- BFS or DFS: Flood Fill (E), Number of Islands (M), Clone Graph (M), Course Schedule (M), Accounts Merge (M).
- Queue interface: Implement Queue using Stacks (E, Stack section).
- No problem on the page is a pure deque problem.

### LeetCode discuss recap of 2025 (community post, via search summary, page not opened)
- Meta: trees and DFS/BFS (Number of Islands). Google: DP and graphs (Word Ladder). Uber: heaps/priority queues (Kth Largest). Salesforce: trees and BFS (Zigzag Level Order). Graph BFS/DFS said to dominate most pipelines.

### techinterview.org Top 50 by company (from the 2026-10-09 cache)
- Google: Sliding Window Maximum (monotonic deque). Apple: Implement Stack using Queues (#7), Flatten Nested List Iterator (#4).

### Search-result summaries only
- Rotting Oranges (994) described as multi-source BFS, level-order on a graph. Design Circular Queue (622) appears under a jointaro Meta interview page (page not opened).
- No source found for Number of Recent Calls (933) or Moving Average from Data Stream (346) frequency; both are NOT in Grind 75 (cache 2026-10-09).

## Caveats
- No queue-specific frequency ranking exists in what I fetched. Most queue use in interviews is BFS inside trees/graphs, which are later topics. Problems below labelled "added for pattern coverage" have no frequency source here.
- Pure-deque and ring-buffer design problems are asked less than BFS; treat them as lower weight.

## Could not be fetched / not opened
- 1point3acres Meta high-frequency thread, Scribd, Glassdoor (login/paywall or not opened).

## Sources
- [Grind 75](https://crackr.dev/grind75)
- [LeetCode discuss: most asked 2025](https://leetcode.com/discuss/post/7417074/)
- [techinterview.org live canon 2026](https://www.techinterview.org/post/3233474779/whats-still-asked-in-2026-live-canon-vs-dead-canon/)
- [Rotting Oranges guide (CodePath)](https://guides.codepath.org/compsci/Rotting-Oranges)
- [Design Circular Queue (jointaro)](https://www.jointaro.com/interviews/meta/design-circular-queue)
