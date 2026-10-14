# Strings: which problems are asked

- **Retrieved:** 2026-10-13
- **Question:** Which String problems are asked most often at large tech companies (Google, Meta, Amazon, Microsoft, Apple, Uber) for a 3-4 year engineer, and which belong to other topics?
- **Used for:** `dsa/Strings_Notes_v1.html` (Part 7 provenance, sources appendix).
- **Local cache checked first:** `dsa-roadmap-gaps-20261011.md` (Tech Interview Handbook rates String "High"; Amazon candidate-report table String 27.4%; Meta reports lean on parsing, palindromes, calculators, anagrams), `dsa-company-interview-calibration-2026.md`. No file listed string problems, so the web was searched.

## Method
- Source: github.com/liquidslr/leetcode-company-wise-problems, raw CSV `<Company>/5. All.csv` for Google, Meta, Amazon, Microsoft, Apple, Uber (fetched 2026-10-13, full files, not truncated).
- Kept rows whose `Topics` column contains "String". Ranked by number of companies listing the problem (of 6), then by summed Frequency. Frequency looks like a normalised 0-100 score per company; method undocumented.

## Findings (companies listing it / 6; Frequency per company G/Me/A/Mi/Ap/U)
- 6/6: Group Anagrams (56/59/81/70/78/60), Longest Common Prefix (73/70/73/72/76/34), Longest Substring Without Repeating Characters (72/69/84/80/67/20), Longest Palindromic Substring (70/67/78/80/51/38), Valid Parentheses (66/74/74/71/72/20), Valid Palindrome (52/83/54/60/71/48), Generate Parentheses, Roman to Integer (66/61/61/69/39/52), Letter Combinations of a Phone Number, Valid Anagram, Word Break, Word Search, Word Ladder, Minimum Window Substring, Serialize and Deserialize Binary Tree, Regular Expression Matching, Basic Calculator II (30/89/50/34/60/42), String to Integer (atoi) (44/57/54/53/43/50), Basic Calculator, Alien Dictionary, Simplify Path (37/84/44/46/22/34), Text Justification, Word Search II, Implement Trie, Valid Palindrome II (38/95/42/39/22/20), Time Based Key-Value Store.
- 5/6: Merge Strings Alternately, Reverse Words in a String, Find the Index of the First Occurrence in a String, Decode String, String Compression, Longest Repeating Character Replacement, Zigzag Conversion, Longest Valid Parentheses, First Unique Character, Edit Distance, Reverse String, Ransom Note, Integer to English Words, Palindromic Substrings, Remove All Adjacent Duplicates.
- Meta-specific top of its String list (Frequency): Minimum Remove to Make Valid Parentheses 100, Valid Word Abbreviation 96.8, Valid Palindrome II 95.1, Basic Calculator II 89.3, Simplify Path 83.7, Valid Palindrome 82.6, Valid Parentheses 73.9, Custom Sort String 72.8, Minimum Window Substring 71.9, Minimum Add to Make Parentheses Valid 71.8, Valid Number 68.2, Add Strings 63.6, Group Shifted Strings 61.4, Goat Latin 61.1, Strobogrammatic Number 50.5, Add Binary 50.1, Multiply Strings 49.3.
- Uber standouts: Alien Dictionary 95, Find the Closest Palindrome 81, Word Search 78, Design In-Memory File System 62, Basic Calculator 62.
- Many String-tagged problems belong to other topics: Sliding Window (Longest Substring..., Minimum Window, Permutation in String, Find All Anagrams), Stack (Valid Parentheses, Decode String, Min Remove, Remove Adjacent Duplicates), Hashing (Group Anagrams, Valid Anagram), DP (Edit Distance, LCS, Word Break, Decode Ways, Palindromic Substrings), Backtracking (Generate Parentheses, Letter Combinations, Word Search), Trie (Implement Trie, Word Search II), Graph (Word Ladder, Alien Dictionary).

## Caveats
- Normalised scores from an unofficial repo built from LeetCode company tags; counts and window unstated. Signal, not ground truth.
- Topic tags are LeetCode's and include secondary tags (e.g. Time Based Key-Value Store is tagged String).
- Pure-string problems (tag is only "String", or String plus Two Pointers/Math/Simulation) are a small set: atoi, Valid Number, Zigzag, Goat Latin, Valid Word Abbreviation, Reverse Words, Add Strings, Multiply Strings, String Compression, Longest Common Prefix, Roman to Integer, Valid Palindrome (I, II), Custom Sort String.
- No source gave a mid-level (E4/L4/SDE-2) breakdown for strings specifically. Uber CSV is smaller (about 60 KB), so its scores rest on fewer rows.

## Could not fetch
- Nothing new attempted beyond the CSVs. Earlier attempts (leetcode.com/discuss 403s) are in `dsa-roadmap-gaps-20261011.md`.

## Sources
- [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems)

## Update 2026-10-13 (curated lists)
- **Grind 75** (crackr.dev/grind75, fetched 2026-10-13): a "Strings" section with 8 problems: Valid Palindrome (E), Valid Anagram (E), Longest Palindrome (E), Longest Substring Without Repeating Characters (M), String to Integer (atoi) (M), Longest Palindromic Substring (M), Find All Anagrams in a String (M), Minimum Window Substring (H). No LeetCode numbers on the page. So among this topic's pure-string problems, **atoi and Longest Palindromic Substring** are on a curated list; Valid Palindrome, anagrams and the sliding-window ones belong to earlier topics.
- **Blind 75 / NeetCode 150**: a standard web search returned only generic descriptions; no page listing the string problems was confirmed. From memory (NOT verified in this session): Encode and Decode Strings and Longest Palindromic Substring are on Blind 75, Palindromic Substrings is a NeetCode 150 addition. Treat as unverified.
- **Not fetched / not found:** neetcode.io (JS-rendered, seen in earlier sessions), a Blind 75 list page.

## Sources (update)
- [Grind 75](https://crackr.dev/grind75)

## Update 2026-10-14 (Blind 75 copy, premium statements, cost benchmarks)
- **Blind 75, community copy** ([Sugapriyan-P-K/blind75](https://github.com/Sugapriyan-P-K/blind75), fetched 2026-10-14; third-party, not the original post): a "String" section of ten problems: Longest Substring Without Repeating Characters, Longest Repeating Character Replacement, Minimum Window Substring, Valid Anagram, Group Anagrams, Valid Parentheses, Valid Palindrome, **Longest Palindromic Substring, Palindromic Substrings, Encode and Decode Strings** (marked LeetCode Premium). Elsewhere in that list: Word Break (DP), Word Search (Matrix), Implement Trie, Add and Search Word, Word Search II (Tree). This **corrects the 2026-10-13 note above**: Palindromic Substrings is on the Blind 75 copy (the earlier "NeetCode addition, from memory" guess was wrong or at least unverified).
- **Premium statements cross-checked** against web-search summaries of mirror sites (doocs, walkccc, NeetCode, algo.monster, grandyang), not the LeetCode pages (paywalled): 408 Valid Word Abbreviation: replaced substrings are non-adjacent and non-empty, no leading zeros, "s55n" invalid for "substitution", example "internationalization" / "i12iz4n" true. 249 Group Shifted Strings: shift wraps z to a, group strings in the same shifting sequence, any group order, example `["abc","bcd","acef","xyz","az","ba","a","z"]` -> `[["abc","bcd","xyz"],["az","ba"],["acef"],["a","z"]]`, key = adjacent differences mod 26 ("az" and "ba" match only with the mod). 271 Encode and Decode Strings: decode must restore the list exactly, no `eval`/serialize helpers, strs[i] any of the 256 ASCII characters (NeetCode, doocs), length < 200, list length < 100, follow-up: any character set; length prefix with a delimiter ("4#neet4#code...") is the standard answer.
- **Cost benchmarks run locally** (Python 3.11.9, Java 27, Windows; outputs in `dsa/Strings_Notes_v1.html` Appendix B): slice and substring copy cost grows with length; string hash cached after the first call in both languages; `insert(0, x)` in a loop is much slower than append (Python list 0.894 s vs 0.002 s; Java StringBuilder 0.064 s vs 0.0009 s for 100,000); on the worst-case substring search ("a"*50000+"b" in "a"*100000) Java `indexOf` took 0.517 s but CPython `in` took 0.5 ms (CPython 3.10+ uses a two-way algorithm), so "O(n*m) worst case" is true of the naive algorithm and of Java here, not of CPython.
- **Not fetched / unavailable:** the LeetCode problem pages themselves, the original Blind 75 post, neetcode.io (JS-rendered), `raw.githubusercontent.com/SamirPaulb/blind75/main/README.md` (404).

## Sources (update 2026-10-14)
- [Blind 75 community copy](https://github.com/Sugapriyan-P-K/blind75)
- [doocs LeetCode 408](https://leetcode.doocs.org/en/lc/408/), [doocs 249](https://leetcode.doocs.org/en/lc/249/), [doocs 271](https://leetcode.doocs.org/en/lc/271/), [walkccc 271](https://walkccc.me/LeetCode/problems/271/), [NeetCode 271](https://neetcode.io/solutions/encode-and-decode-strings)
