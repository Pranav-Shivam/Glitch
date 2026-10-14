from lib import *
from c_prob import BY, NUM, TYPE_NAME, ORDER, TYPE_OF, prob_card
from c_text2 import code_of

def part7():
    h = '<h2 id="part-7"><span class="part-no">Part 7</span>Representative Problems</h2>'
    h += P('Fourteen solved problems, grouped by pattern type (the number is the order in this file, not the difficulty). Every solution, brute force and optimal, in Python and in Java, was run against each other on 3999 to 6000 random, constraint-respecting inputs. Results and every claim about a bug are in <a class="xref" href="#appendix-b">Appendix B</a>. The brute force is always visible; in **Practice mode** the observation and the optimal code stay hidden until you press the button.')
    h += '<div class="toolbar"><label for="practice-mode"><input type="checkbox" id="practice-mode"> Practice mode</label><span>Hides the observation and the optimal solution until you ask, so you look for the idea from the brute force first.</span></div>'
    h += H3('How these problems were chosen (research first)')
    h += P('Local cache checked first (`research/`): no strings file existed, so the web was searched on 2026-10-13 and the findings saved as `research/dsa-strings-problem-frequency-20261013.md`. The main source is the per-company all-time CSVs of the GitHub repo `liquidslr/leetcode-company-wise-problems`, read in full for Google, Meta, Amazon, Microsoft, Apple and Uber (scores are normalised so 100 = the most frequent problem for that company; method undocumented). I kept the String-tagged problems, ranked them by how many of the six companies list them, and removed the ones whose technique belongs to another topic. Two curated lists were fetched as a second source (Grind 75 Strings section; a community copy of the Blind 75 String section). **This is a weaker standard than earlier topics:** only atoi, Longest Palindromic Substring, Palindromic Substrings and Encode and Decode Strings appear in both a curated list and the company data. The rest are "listed by N of 6 companies" in a single unofficial dataset, so treat the ranking as a signal. Interviewers rarely reuse a problem word for word, so the pattern matters more than the title.')
    h += callout('tip', 'Look-alikes that need a twist',
        '<p>Three problems here look like something they are not. <strong>Problem 2</strong> (Longest Palindromic Substring) looks like a brute-force or DP problem; centre expansion is the interview answer. <strong>Problem 9</strong> (Multiply Strings) looks like hard big-number arithmetic; it is one position formula. <strong>Problem 7</strong> (Group Shifted Strings) looks like Group Anagrams, but the key is a difference list modulo 26, not sorted letters. Problems 2 and 9 carry a "Look-alike with a twist" label. <a class="xref" href="#part-5">Part 5</a> lists the look-alikes that belong to other topics.</p>')
    h += H3('Coverage check against the research')
    h += table(['Frequently asked problem', 'Handled', 'Where / why'], [
        ['Longest Common Prefix (14), Roman to Integer (13), String to Integer (8), Longest Palindromic Substring (5), Zigzag Conversion (6)', 'Solved', 'Problems [[#p13|13]], [[#p4|4]], [[#p3|3]], [[#p2|2]], [[#p10|10]] (all listed by 5 or 6 of 6 companies)'],
        ['Reverse Words in a String (151), String Compression (443), Find the Index of the First Occurrence (28), First Unique Character (387)', 'Solved', 'Problems [[#p11|11]], [[#p12|12]], [[#p14|14]], [[#p5|5]]'],
        ['Valid Word Abbreviation (408), Custom Sort String (791), Group Shifted Strings (249), Add Strings (415), Multiply Strings (43)', 'Solved', 'Problems [[#p1|1]], [[#p6|6]], [[#p7|7]], [[#p8|8]], [[#p9|9]] (Meta-heavy scores)'],
        ['Merge Strings Alternately (1768), Palindromic Substrings (647), Add Binary (67), Compare Version Numbers (165), Encode and Decode Strings (271), Text Justification (68)', 'Practice', '[[#part-14|Part 14]]; solutions in [[#appendix-a|Appendix A]]'],
        ['Valid Palindrome (125), Valid Palindrome II (680)', 'Earlier topic', 'Two Pointers; both are in the Revisit block of [[#part-1|Part 1]]'],
        ['Valid Number (65), Integer to English Words (273)', 'Not solved', 'See "Outside the roadmap" below'],
        ['Goat Latin (824), Fizz Buzz (412), Reverse Vowels of a String (345), Reverse String (344)', 'Not solved', 'Easy simulation or two-pointer exercises; same skills as problems 1, 11 and 12']])
    h += H3('Frequently asked, but the technique belongs elsewhere')
    h += table(['Problem', 'Goes to', 'Why'], [
        ['Longest Substring Without Repeating (3), Minimum Window Substring (76), Longest Repeating Character Replacement (424), Permutation in String (567), Find All Anagrams (438), Substring with Concatenation of All Words (30)', 'Sliding Window (earlier topic)', 'A window with a validity condition'],
        ['Group Anagrams (49), Valid Anagram (242), Ransom Note (383)', 'Hashing (earlier topic)', 'Count table / sorted-letters key'],
        ['Valid Parentheses (20), Decode String (394), Basic Calculator (224), Basic Calculator II (227), Simplify Path (71), Minimum Remove to Make Valid Parentheses (1249), Remove All Adjacent Duplicates (1047)', 'Stack (earlier topic)', 'Nesting or "undo the last thing"'],
        ['Minimum Add to Make Parentheses Valid (921)', 'Greedy (later topic)', 'A single counter is enough; the Stack notes already deferred it'],
        ['Edit Distance (72), Longest Common Subsequence (1143), Word Break (139), Decode Ways (91), Regular Expression Matching (10), Interleaving String (97), Longest Palindromic Subsequence (516), Palindromic Substrings as a DP table', 'Dynamic Programming (later)', 'Overlapping sub-problems on prefixes'],
        ['Generate Parentheses (22), Letter Combinations of a Phone Number (17), Word Search (79), Remove Invalid Parentheses (301), Palindrome Partitioning (131), Expression Add Operators (282), Word Break II (140)', 'Backtracking (later)', 'Generate all answers by trying and undoing choices'],
        ['Implement Trie (208), Word Search II (212), Design Add and Search Words (211), Design Search Autocomplete System (642)', 'Tries (later)', 'Shared prefixes'],
        ['Word Ladder (127), Alien Dictionary (269), Open the Lock (752), Accounts Merge (721), Evaluate Division (399), Reconstruct Itinerary (332)', 'Graphs (later)', 'Strings are nodes or labels in a graph'],
        ['Serialize and Deserialize Binary Tree (297), Construct Binary Tree from String (536)', 'Trees (later)', 'The traversal is the topic'],
        ['Top K Frequent Words (692)', 'Heaps (later)', 'Select the top k with a comparator'],
        ['Design In-Memory File System (588), Encode and Decode TinyURL (535)', 'Practical Build track (topic 19)', 'Design exercises that use strings as keys and paths'],
        ['Time Based Key-Value Store (981)', 'Binary Search (earlier topic)', 'Solved there']])
    h += H3('Outside the roadmap')
    h += table(['Problem / technique', 'Suggested place', 'Why'], [
        ['Valid Number (65)', 'After this topic as a stretch', 'A finite-state machine with many cases (sign, digits, dot, exponent). Meta tag score 68.2, but Google 18.0, Amazon 26.5, Microsoft 16.1. LeetCode rates it Hard'],
        ['Integer to English Words (273)', 'Recursion (next topic), as practice', 'Recursive chunking by thousands; LeetCode Hard; Apple, Microsoft, Amazon tag scores 46 to 53'],
        ['Rabin-Karp (rolling hash), Z-algorithm, Manacher\'s algorithm', 'Optional extras (roadmap)', 'KMP is shown in problem 14; the others are rarely expected at a 3 to 4 year level'],
        ['Find the Closest Palindrome (564)', 'Skip unless a target company asks', 'Hard math over candidate palindromes; Uber 81 but the other five companies 8 to 18']])

    groups = {}
    for k in ORDER: groups.setdefault(TYPE_OF[k], []).append(k)
    for t in 'ABCDEFG':
        h += f'<h3 class="group-title">Type {t}: {TYPE_NAME[t]}</h3>'
        for k in groups[t]: h += prob_card(k)
    return h

def part8():
    h = '<h2 id="part-8"><span class="part-no">Part 8</span>Problem-Solving Method</h2>'
    h += P('A repeatable ten-step process. The right-hand column is what to **say aloud**, which is what interviewers score along with the code.')
    h += table(['Step', 'Question to ask', 'Example of what to say'], [
        ['1. Understand the input', 'What characters can appear: lowercase only, any ASCII, Unicode? Can it be empty? Is it one string or a list?', '"Lowercase English letters only, length 1 to 1000, so I can use a 26-slot count array."'],
        ['2. Identify constraints', 'How long can the string be? Is O(n²) fine?', '"n up to 1000, so O(n²) is 10^6 operations: fine. At 10^5 I would need O(n)."'],
        ['3. Clarify edge cases', 'Spaces at the ends or repeated? Leading zeros? A sign? What do I return for no answer: -1, 0, empty?', '"If there are no digits, return 0, and if the number is out of range, clamp. Is that right?"'],
        ['4. Brute force', 'What is the obvious loop and its cost?', '"Check every substring with a reverse-and-compare: O(n³)."'],
        ['5. Find the bottleneck', 'What does the brute force re-do?', '"It re-compares the inside of a palindrome every time it checks a longer one."'],
        ['6. Recognise the pattern', 'Parse? Centre? Count and group? Carry? Read/write? Prefix or needle?', '"This is a palindrome question, so I enumerate centres: 2n - 1 of them."'],
        ['7. Design it', 'Write the five-line sheet below before the loop', '"State is l and r, invariant is s[l+1..r-1] is a palindrome, step is widen while ends match."'],
        ['8. State complexity', 'Time and space, with the reason', '"O(n²) time because each centre can expand up to n/2; O(1) space."'],
        ['9. Code', 'Write the loop from the template; name variables for their meaning', '(Writes it, narrating each update. Uses a list or StringBuilder to build output.)'],
        ['10. Test', 'Empty/one char, all the same char, the largest value, a case with the answer at the end, a case with no answer', '"I will trace "abba" for the even centre, "a" for one char, and "aaa" for repeated characters."']])
    h += H3('The five-line write-down (do this before typing the loop)')
    h += diagram(''' 1. Alphabet and size       lowercase? digits? spaces? unicode?   n up to ?
 2. State                   which cursors, which counters, which output container
 3. Invariant               "what the characters I have passed have turned into"   (one sentence)
 4. Step per character      what happens for a letter / a digit / a space / the end
 5. End and return          what must be true when the loop stops; what to return when there is no answer''')
    h += H3('Worked interview walkthrough: String to Integer (atoi)')
    h += table(['Minutes', 'What you do', 'What you say'], [
        ['0-2', 'Read, restate, ask', '"So: skip spaces, one optional sign, read digits until a non-digit, clamp to 32-bit, 0 if no digits. Does \'+-5\' give 0? And is a space after the sign allowed?" (Per the statement: yes 0, no.)'],
        ['2-3', 'Constraints and brute force', '"The input is up to 200 characters, so anything linear is fine. A regex would do it, but I will write the phases myself."'],
        ['3-5', 'Design', '"Four phases in order: spaces, sign, digits, clamp. State: index i, sign, result. Overflow: I will check before multiplying, with result > (INT_MAX - d) / 10, so I never need a wider type."'],
        ['5-10', 'Code', 'Writes `my_atoi`, narrating each loop. Leaves the clamp for a negative sign returning INT_MIN, because 2147483648 also triggers the same check.'],
        ['10-13', 'Test', '"\'   -42\' -> -42. \'42abc\' -> 42. \'abc\' -> 0. \'-\' -> 0. \'2147483648\' -> 2147483647. \'-2147483649\' -> -2147483648. Empty string -> 0."'],
        ['13-15', 'Complexity and follow-ups', '"O(n) time, O(1) space. If you want me to accept whitespace like tabs, or a decimal point, only the first loop or a new phase changes."']])
    h += P('The same shape works for every problem here: **clarify the alphabet and the failure answer, name the invariant, code with the template, trace the smallest and the nastiest input.**')
    return h

def part9():
    h = '<h2 id="part-9"><span class="part-no">Part 9</span>Edge Cases</h2>'
    h += P('Run through this list automatically before you say "done". The last column says which pattern the case breaks.')
    h += table(['Edge case', 'Example', 'Why it matters', 'Breaks'], [
        ['Empty string', '`""`', 'Loops that assume `s[0]` exist; `strs[0]` in LCP; functions that return a slice', 'All; Types B, G'],
        ['One character', '`"a"`', 'The smallest palindrome; the smallest valid abbreviation; the loop body runs once', 'B, C'],
        ['All characters the same', '`"aaaa"`', 'Worst case for expansion (O(n²) really) and for brute-force search; zero unique letters', 'B, D, G'],
        ['Leading, trailing and repeated spaces', '`"  a  b "`', '`split(" ")` creates empty strings; output must have single spaces', 'C, F'],
        ['Sign only, no digits', '`"-"`, `"+"`', 'Result must be 0, not an error', 'C'],
        ['Leading zeros in a number', '`"007"`, abbr `"01"`', 'Fine for atoi; **invalid** in an abbreviation or version rule; strip them from a product', 'A, C, E'],
        ['Overflow at the boundary', '`"2147483648"`, `"-2147483649"`', 'Check before multiplying; Java wraps silently', 'C'],
        ['Final carry', '`"99" + "1"`', 'Loop must continue while the carry is non-zero', 'E'],
        ['Unequal lengths', '`"1"` and `"99999"`', 'Missing digit counts as 0; tails of merges', 'A, E'],
        ['Zero as an input', '`"0" * "123"`', 'The product array would be all zeros: return `"0"`, not `""`', 'E'],
        ['Even-length palindrome', '`"abba"`, `"cbbd"`', 'Only the gap between two characters is a centre', 'B'],
        ['Needle longer than haystack, or equal', '`"ab"`, `"abc"`', 'Loop bounds `n - m + 1` may be negative or zero', 'G'],
        ['Periodic strings', '`"abababab"`', 'The case where KMP\'s fall-back is used and brute force is slow', 'G'],
        ['Run length of 10 or more', '`"a"` x 12', 'The count takes several characters', 'F'],
        ['Delimiter inside the data', '`"a#b"`', 'Joining with a delimiter is ambiguous', 'C (format design)'],
        ['Case and non-letters', '`"A man, a plan"`', 'Decide: ignore or keep? Say it out loud', 'B, D'],
        ['Non-ASCII', 'accents, emoji', 'Python `len` counts code points, Java `length()` counts UTF-16 units', 'Any with indexes'],
        ['No valid answer', 'no unique character, no match', 'What do I return: -1, `""`, `0`? Read the statement', 'D, G']])
    return h

def part10():
    h = '<h2 id="part-10"><span class="part-no">Part 10</span>Common Mistakes</h2>'
    h += P('Every "this gives the wrong answer" below was **reproduced with a failing input** and is listed in <a class="xref" href="#appendix-b">Appendix B</a>.')
    h += H3('Conceptual mistakes')
    h += table(['Mistake', 'Failing example', 'How to avoid it'], [
        ['Only odd centres for palindromes', '`"abba"` returns `"a"`', 'Always try `(c, c)` **and** `(c, c + 1)`'],
        ['Dropping the final carry', '`add("99", "1")` returns `"00"`', 'Loop `while i >= 0 or j >= 0 or carry`'],
        ['No leading-zero strip on a product', '`multiply("2", "3")` returns `"06"`', 'Skip zeros but keep one digit; special-case a zero input'],
        ['Letting a leading zero through', '`valid_abbr("a", "01")` returns `true`, should be `false`', 'Test `abbr[j] == "0"` before parsing a number'],
        ['Shift key without `% 26`', '`"az"` and `"ba"` get keys `(0, 25)` and `(0, -1)` and are not grouped', 'Take the difference modulo 26']])
    h += H3('Python mistakes')
    h += table(['Mistake', 'What happens', 'How to avoid it'], [
        ['`s.split(" ")` instead of `s.split()`', '`" ".join(reversed("a  b".split(" ")))` is `"b  a"` (two spaces), not `"b a"`', 'Use `split()` with no argument, or scan manually'],
        ['`isdigit()` for "is this an ASCII digit?"', '`"²".isdigit()` is `True`, but `int("²")` raises `ValueError`', 'Test `"0" <= c <= "9"`'],
        ['`s = s[1:]` inside a loop', '100,000 characters take 0.953 s versus 0.002 s with an index', 'Move an index, not the string'],
        ['`s += c` in a loop, relied on to be fast', 'CPython sometimes makes it fast (0.009 s for 200,000) and sometimes not (0.870 s for 50,000 when something else holds the string)', 'Collect in a list, then `"".join`'],
        ['`int(a) + int(b)` for big numbers', '`int("1" * 5000)` raises `ValueError` (the 4300-digit limit, Python 3.11+)', 'Do column arithmetic; the problem forbids the shortcut anyway']])
    h += H3('Java mistakes')
    h += table(['Mistake', 'What happens', 'How to avoid it'], [
        ['`==` on strings', '`new String("ab") == "ab"` is `false`, `.equals` is `true`', 'Always `equals`'],
        ['Overflow in parsing', 'Without the pre-check, `myAtoi("2147483648")` returns -2147483648 (wrapped), not 2147483647', 'Compare with `(MAX - d) / 10` before multiplying'],
        ['`split("\\\\s+")` on text that starts with a space', '`" a b".split("\\\\s+")` has 3 elements and the first is empty', '`trim()` first, or scan manually'],
        ['`split(",")` drops trailing empty strings', '`"a,b,,".split(",")` has 2 elements; `split(",", -1)` has 4', 'Pass `-1` when empties matter'],
        ['`\'a\' + 1 + ""` versus `"" + \'a\' + 1`', '`"98"` versus `"a1"`', 'Cast `(char)` or start the expression with a string'],
        ['`Character.isDigit` on non-ASCII digits', 'It is `true` for the Arabic-Indic digit 3 and `c - \'0\'` gives 1587', 'Test `c >= \'0\' && c <= \'9\'`'],
        ['`s += "x"` in a loop', '0.712 s for 100,000 appends versus 0.002 s with `StringBuilder`', '`StringBuilder`, then `toString()`']])
    h += H3('Complexity mistakes')
    h += UL(['Calling expand-around-centre O(n). It is O(n²); say so.',
             'Forgetting that a slice, a `substring` or a string used as a map key costs its length.',
             'Calling the brute-force substring search O(n) because the code "looks like one loop". The inner comparison loop makes it O(n·m): 25,005,000 comparisons on the worst case against 24,998 for KMP.',
             'Saying KMP is O(n·m) because of the `while` inside the `for`. The fall-backs are paid for by the increases of `k` (Part 3).'])
    h += H3('Boundary mistakes')
    h += UL(['**The loop stops one step too far.** After expanding around a centre the palindrome is `s[l+1 .. r-1]`, not `s[l .. r]`.',
             '**`i` can pass the end.** In Valid Word Abbreviation a number can send `i` beyond `len(word)`; the final check `i == len(word)` rejects it, but only if you do not index `word[i]` first.',
             '**Compression count in one slot.** A run of 12 written with one `chars[write] = str(12)` returns length 2, not 3 (reproduced).',
             '**Off-by-one in `n - m + 1`.** The last valid start of a needle is `n - m`, so `range(n - m + 1)`; for `m > n` the range is empty, which is correct.'])
    h += H3('Interview reasoning mistakes')
    h += UL(['Starting to code before asking what to return when there is no answer.',
             'Using a library call the interviewer banned (`int()`, `BigInteger`, `split`, regex) without asking. Ask: "May I use...?"',
             'Writing `if s[i] in "0123456789"` for a digit check and forgetting that `"" in "0123456789"` is true (empty slices).',
             'Not testing the even-length, empty and carry cases, because the first example passed.',
             'Presenting a hash-map or sorted-key solution as O(n) without mentioning the O(L) key cost.'])
    return h

def part11():
    h = '<h2 id="part-11"><span class="part-no">Part 11</span>Interview Templates</h2>'
    h += P('The minimum set to remember, as a recall sheet. Every template is **taken from a solution that was run** against a brute force ([[#part-7|Part 7]], [[#appendix-b|Appendix B]]). Together they cover Types A to G.')
    items = [
        ('T1 Two cursors over two strings (Type A)', 'vwa', 'Valid Word Abbreviation (408); Compare Version Numbers (165); Merge Strings Alternately (1768)', 'O(n + m) / O(1)', 'The final check: `i == len(word) and j == len(abbr)`. Both cursors must end together.'),
        ('T2 Expand around a centre (Type B)', 'lps', 'Longest Palindromic Substring (5); Palindromic Substrings (647)', 'O(n²) / O(1)', 'The bounds after the loop: the palindrome is `s[l+1 .. r-1]`. And do not forget the even centre `(c, c + 1)`.'),
        ('T3 Parse with phases and clamp (Type C)', 'atoi', 'String to Integer (8); the number parsing inside Compare Version and Encode/Decode', 'O(n) / O(1)', 'The clamp test goes **before** `result * 10 + d`: `result > (INT_MAX - d) // 10`.'),
        ('T4 Count, then scan (Type D)', 'firstuniq', 'First Unique Character (387); Custom Sort String (791); Ransom Note (383)', 'O(n) / O(1)', 'Pass 2 runs over the **string**, not over the table, or the order is lost.'),
        ('T5 Group by a signature (Type D)', 'shifted', 'Group Shifted Strings (249); Group Anagrams (49) with a different key', 'O(N·L) / O(N·L)', 'The key must be equal exactly when strings are equivalent: the `% 26`.'),
        ('T6 Column arithmetic with a carry (Type E)', 'addstr', 'Add Strings (415); Add Binary (67)', 'O(max(n, m)) / O(max(n, m))', 'The loop condition includes the carry: `while i >= 0 or j >= 0 or carry`.'),
        ('T7 Read/write cursors (Type F)', 'compress', 'String Compression (443); Remove Duplicates and Move Zeroes (Arrays)', 'O(n) / O(1)', 'The count is written as separate digit characters, one per slot, and only if the run is longer than 1.'),
        ('T8 Vertical scan (Type G)', 'lcp', 'Longest Common Prefix (14)', 'O(S) / O(1)', 'Stop when `i == len(w)` **or** `w[i] != ch`; do not index past the end of a short word.'),
        ('T9 KMP (Type G)', 'strstr', 'Find the Index of the First Occurrence (28); Repeated Substring Pattern (459, same table)', 'O(n + m) / O(m)', 'Both loops: `while k and mismatch: k = lps[k - 1]`. The fall-back uses `lps[k - 1]`, not `lps[k]`.')]
    for title, key, applies, cx, line in items:
        h += f'<div class="card"><h3>{inline(title)}</h3>{code_of(key)}'
        h += P('**Applies to:** ' + applies + ' &nbsp; **Complexity:** ' + cx + ' (time / space)').replace('&amp;nbsp;', '&nbsp;')
        h += P('**The line people most often get wrong:** ' + line) + '</div>'
    return h

def part12():
    h = '<h2 id="part-12"><span class="part-no">Part 12</span>Mental Model</h2>'
    h += diagram(''' When I see  a STRING and the words "parse", "convert", "palindrome", "prefix", "in place", "as strings", "group by"
        |
        v
 Think about  what the characters I have already passed have turned into (the one-sentence invariant)
        |
        v
 Because  a cursor or two plus a small state replaces re-scanning, re-copying and re-comparing
        |
        v
 Use  the type: A two cursors / B centres / C phases / D count-or-key / E carry / F read-write / G prefix-or-KMP
      and build the answer in a list or StringBuilder, join once
        |
        v
 Expected complexity:  O(n) for one pass,  O(n^2) for centres,  O(n + m) for KMP,  O(n*m) for long multiplication''')
    h += H3('The core idea in one picture')
    h += diagram(''' s = "  -42x"

   skip spaces    sign     digits        stop
   [ ][ ]         [-]      [4][2]       [x]
    0  1           2        3  4         5
    i ------------>i------->i-->i------->i        i only moves right: each character is read once

 eliminated:  re-reading, slicing, converting to a number type, regex
 kept:        i, sign, result            (result = value of the digits so far, already clamped)
 reused:      the same loop shape for parsing, merging, comparing, rewriting''')
    h += H3('Three sentences to recite before an interview')
    h += OL(['Strings are immutable, so I **move indexes, not strings**, and I build output in a list or `StringBuilder` and join once.',
             'Before the loop I say, in one sentence, **what the characters I have passed have turned into**; every update must keep that sentence true.',
             'I always ask **what to return when there is no answer** and test the empty, one-character, all-same and carry cases.'])
    h += H3('You are ready to move to Recursion when you can...')
    h += UL(['Write templates T1 to T9 from memory in Python and Java and explain every line, including the clamp in T3, the `% 26` in T5, the carry in the loop condition of T6 and the `lps[k - 1]` in T9.',
             'State the one-sentence invariant of each type and the amortised argument for KMP, unprompted.',
             'Classify an unseen string problem into a type A to G, or into "not this topic" (window, stack, DP, backtracking, trie, graph), within about a minute, and say why.',
             'Solve Longest Palindromic Substring, String to Integer, Add Strings and String Compression without looking at a template, and Reverse Words with the in-place follow-up.',
             'Describe a case where you reached for `s += c`, `s[1:]` or a delimiter and found it wrong (quadratic cost, or ambiguous data), and what you switched to.',
             'Explain why strings of nested or repeated structure (Decode String, Basic Calculator, Generate Parentheses) point to **recursion**, which is the next topic.'])
    return h

def part13(cl):
    h = '<h2 id="part-13"><span class="part-no">Part 13</span>Mastery Checklist (self-assessment)</h2>'
    h += P('Tick an item only when you can do it **without notes**. Nothing is ticked for you. Ticks are saved in this browser (key `strings-v1`).')
    h += '<div class="progress-wrap"><div class="progress-label"><span>Progress</span><span id="prog-text">0 / 0</span></div><div class="progress-outer"><div class="progress-inner" id="prog-bar"></div></div></div>'
    h += cl.group('Level 1: Fundamentals', 'Can I explain the concept?', [
        'I can explain in two sentences what makes a string problem different from an array problem (immutability, the cost of copies, characters vs numbers).',
        'I can state the one-sentence invariant for each of the seven types (A to G).',
        'I can explain the difference between a substring and a subsequence and say which one needs DP.',
        'I can explain a palindrome\'s centre and why there are 2n - 1 of them.',
        'I can explain what a border is and how it lets KMP skip re-reading the haystack.',
        'I can say how this topic relates to Hashing, Two Pointers, Sliding Window and Stack, and what it leads to (Recursion, Trees, Tries, DP).'])
    h += cl.group('Level 2: Python and Java', 'Can I implement the basic operations and templates without looking?', [
        'I can write T1 to T5 from memory in Python and Java.',
        'I can write T6 (carry) and T7 (read/write) from memory, including the digit-by-digit count write.',
        'I can write the KMP `lps` table and the search loop from memory in both languages.',
        'I can state when `==` is wrong in Java, what `split` does with trailing empties, and what `\'a\' + 1` is.',
        'I can build a string with a list + `join` in Python and a `StringBuilder` in Java, and say what `insert(0, c)` costs.',
        'I can parse digits with `ord(c) - ord("0")` / `c - \'0\'` and explain why I avoid `isdigit()` / `Character.isDigit` for ASCII-only input.'])
    h += cl.group('Level 3: Complexity', 'Can I explain time and space, including the amortised argument?', [
        'I can explain why `s = s[1:]` in a loop and `s += c` in a Java loop are O(n²).',
        'I can explain why a string map key costs O(L), and the cost of grouping N strings of length L.',
        'I can give the amortised argument for KMP (k rises at most n times, so it falls at most n times).',
        'I can explain why Reverse Words with nested `while` loops is O(n).',
        'I can say why expand-around-centre is truly O(n²) and what Manacher changes.',
        'I can compute the cost of Add Strings (O(max(n, m))) and Multiply Strings (O(n·m)) and say why.'])
    h += cl.group('Level 4: Patterns', 'Can I recognise the major patterns and the look-alikes?', [
        'I can read a statement and name its type (A to G) within about a minute.',
        'I can say which of Valid Parentheses, Longest Substring Without Repeating, Group Anagrams, Edit Distance and Word Ladder are not this topic, and what each needs instead.',
        'I can tell Longest Palindromic Substring (centres) from Valid Palindrome (converging cursors) and say why each fits.',
        'I can tell "single counter" from "stack" for a bracket problem and say what makes the difference.',
        'I can say when KMP is the answer and when the brute force with a stated O(n·m) is acceptable.'])
    h += cl.group('Level 5: Problem Solving', 'Can I solve representative Easy and Medium problems?', [
        'I can solve Valid Word Abbreviation and explain why the check at the end needs both cursors.',
        'I can solve Longest Palindromic Substring and explain the bounds after the loop.',
        'I can solve String to Integer including the overflow check, without a template.',
        'I can solve First Unique Character, Custom Sort String and Group Shifted Strings and explain what makes each key valid.',
        'I can solve Add Strings and Multiply Strings and explain the carry and the position formula.',
        'I can solve String Compression and Reverse Words (with the in-place follow-up) and explain why `write <= read`.',
        'I can solve Longest Common Prefix and strStr (brute force, then KMP).'])
    h += cl.group('Level 6: Interview Ready', 'Can I explain my approach aloud and solve an unfamiliar problem?', [
        'I can solve a representative medium (for example String to Integer) in about 15 to 20 minutes, including stating brute force, complexity and one test.',
        'I can write a correct solution without running it, and trace the empty, one-character and carry cases by hand.',
        'I can answer a follow-up that changes a constraint (non-ASCII input, a library is banned, O(1) extra space, the input arrives in chunks).',
        'I can solve the Part 14 set without hints and read Appendix A only afterwards.',
        'I can describe a case where my first idea (a delimiter, `split`, `int()`) was wrong and what I used instead.',
        'I can say honestly which string problems I would defer or skip in an interview (Valid Number, DP-based ones) and why.'])
    return h
