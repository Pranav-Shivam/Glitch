from lib import *
from c_prob import BY, NUM, TYPE_NAME, ORDER

def code_of(key, role='opt'):
    p = BY[key]
    return code_block(p['py_' + role][0], p['java_' + role][0])

def algo(items):
    return '<div class="algo-box"><div class="algo-label">5. Generic algorithm</div><ol>' + ''.join(f'<li>{inline(i)}</li>' for i in items) + '</ol></div>'

def pcard(letter, title, diff, tag, parts, solved, template_key, trace_html, complexity, space):
    what, solves, recog, intuition, algo_items, state = parts
    h = f'<div class="card pattern" id="type-{letter.lower()}"><h3>Type {letter}: {inline(title)}</h3><div class="pill-row">{pill("Type " + letter, "c-accent")}{pill(diff, DIFF_COLOR[diff])}{pill(tag, mono=True)}</div>'
    h += P('**1. What it is.** ' + what) + P('**2. What problem it solves.** ' + solves)
    h += P('**3. How to recognise it.** ' + recog) + P('**4. Intuition.** ' + intuition)
    h += algo(algo_items)
    h += P('**6. State, validity condition, step.** ' + state)
    h += P('**7. Template.** The verified code of ' + solved + ' (run against a brute force, <a class="xref" href="#appendix-b">Appendix B</a>):')
    h += code_of(template_key)
    h += P('**8. Time.** ' + complexity) + P('**9. Space.** ' + space)
    h += P('**10. A tiny example traced by hand.**') + trace_html + '</div>'
    return h

def part4():
    h = '<h2 id="part-4"><span class="part-no">Part 4</span>Core Patterns</h2>'
    h += P('Seven types, lettered so later parts can refer to them. Before coding any of them, write down five things: the **state** (cursors and what they mean), the **invariant** (the one-sentence meaning of what you have passed), the **update** for each kind of character, the **end condition** (what makes the loop stop and what must be true then), and **what to return**. Items 8 and 9 (time and space) are in the card.')
    h += table(['Type', 'Name', 'One-line idea', 'Solved here'], [
        ['A', TYPE_NAME['A'], 'One cursor per string, each with its own stride; both must end together', 'Valid Word Abbreviation'],
        ['B', TYPE_NAME['B'], 'A palindrome has a centre; grow outwards while the ends match (odd and even centres)', 'Longest Palindromic Substring'],
        ['C', TYPE_NAME['C'], 'The statement lists phases in order; one loop per phase; clamp before overflow', 'String to Integer, Roman to Integer'],
        ['D', TYPE_NAME['D'], 'Equivalent strings share a key; count or normalise once, then group or look up', 'First Unique, Custom Sort String, Group Shifted Strings'],
        ['E', TYPE_NAME['E'], 'Work from the least significant digit or from a position formula; mind the carry', 'Add Strings, Multiply Strings, Zigzag'],
        ['F', TYPE_NAME['F'], 'A write cursor that never passes the read cursor; or reverse twice', 'Reverse Words, String Compression'],
        ['G', TYPE_NAME['G'], 'Scan column by column and stop at the first difference; reuse matched text with borders', 'Longest Common Prefix, strStr (KMP)']])
    h += P('**How they relate.** C is the general single-pass scan; A is C with two strings; E is C run from the right; F is C that writes as it reads. D replaces sorting or searching by one counting pass. B and G are the two "compare" families: B compares a string with its own mirror, G compares a string with a prefix of itself (the border).')

    h += pcard('A', 'Two cursors over two strings', 'Easy', 'one cursor each, different strides', (
        'Two indexes, one per string, advancing by different amounts (1 for a letter, a whole number for a digit run). Also covers merging and comparing two sequences.',
        'Decides whether two strings match under a compression or encoding without ever expanding it, and merges or compares two sequences in O(n + m).',
        '"Valid abbreviation", "merge alternately", "compare version numbers", "is s a subsequence of t". Two inputs, and one of them is a compressed form of the other or must be consumed in step.',
        'Never build the expanded form. A skip of `num` letters is just `i += num`: the alignment is the same, the cost is O(1) instead of O(num).',
        ['`i = j = 0`.', 'While both cursors are in range: if `abbr[j]` is a digit, reject a leading zero, parse the whole number, `i += num`. Otherwise the letters must match; move both by 1.',
         'On exit, `i == len(word)` **and** `j == len(abbr)`: both must have ended together.'],
        '**State:** `i` (word), `j` (abbr). **Invariant:** `word[:i]` is exactly what `abbr[:j]` describes. **Step:** letter -> compare and advance both; digits -> parse the run, jump `i`. **Valid at the end:** both cursors at the end.'),
        'Problem [[#p1|1]] (Valid Word Abbreviation); practice: Merge Strings Alternately and Compare Version Numbers', 'vwa',
        table(['Step', 'i', 'j', 'what happens'], [['start', '0', '0', '`word = "hello"`, `abbr = "h3o"`'], ['`h` = `h`', '1', '1', 'letters match, both advance'], ['digit run `3`', '4', '2', 'parse 3, skip three letters of `word`'], ['`o` = `o`', '5', '3', 'letters match'], ['end', '5', '3', '`i == 5 == len(word)` and `j == 3 == len(abbr)` -> **true**']]),
        'O(n + m).', 'O(1).')

    h += pcard('B', 'Expand around a centre', 'Medium', 'odd and even centres', (
        'Treat every position (and every gap between positions) as a possible centre of a palindrome and grow outwards while the two ends match.',
        'Finds the longest palindromic substring, or counts all of them, in O(n²) time and O(1) space with no table.',
        '"Palindromic substring", "longest palindrome", "count palindromes", n at most about 1000 to 5000.',
        'A palindrome is its centre plus a smaller palindrome plus two equal ends. Growing outwards re-uses what the previous step proved, so no substring is re-compared from scratch.',
        ['For each centre `c` in `0..n-1`, try two starting pairs: `(c, c)` (odd length) and `(c, c + 1)` (even length).', 'While `l >= 0`, `r < n` and `s[l] == s[r]`: `l -= 1`, `r += 1`.', 'The loop stops one step too far, so the palindrome is `s[l+1 .. r-1]`; record it if it is longer than the best.'],
        '**State:** `l`, `r`, and the best bounds. **Invariant:** `s[l+1 .. r-1]` is a palindrome centred at `c`. **Step:** widen by one on both sides if the new ends match. **Valid:** after the loop, the palindrome is the span strictly inside `l` and `r`.'),
        'Problem [[#p2|2]] (Longest Palindromic Substring); practice: Palindromic Substrings', 'lps',
        table(['centre', 'start (l, r)', 'steps', 'palindrome found', 'best so far'], [
            ['0 odd', '(0, 0)', '`a` = `a`; then l = -1, stop', '`a` (0..0)', '`a`'], ['0 even', '(0, 1)', '`a` != `b`', 'none', '`a`'],
            ['1 odd', '(1, 1)', '`b`; then `a` != `b`', '`b`', '`a`'], ['1 even', '(1, 2)', '`b` = `b`; `a` = `a`; l = -1, stop', '`abba` (0..3)', '**`abba`**'],
            ['2, 3', '...', 'nothing longer than 4 fits', '', '`abba`']]) + P('Input `s = "abba"`. Note that the even centre at gap 1 is the only one that finds the answer: forgetting even centres returns `"a"` (Part 10).'),
        'O(n²) worst case (2n - 1 centres, up to n/2 steps each).', 'O(1).')

    h += pcard('C', 'Parse once with a little state', 'Medium', 'phases in order, clamp early', (
        'Read the string left to right once, with one small loop per phase named in the statement (spaces, sign, digits...), or one rule that looks one character ahead.',
        'Turns a verbal specification (atoi, Roman numerals, a version, a path) into code with no re-reading and no regex.',
        'The statement is a list of steps ("skip whitespace, then an optional sign, then digits, then stop"), or it defines a conversion table with a lookahead rule. Words like "ignore", "until the first non-digit", "return 0 if".',
        'A parser is a tiny state machine. Writing the phases in the statement\'s order, as sequential loops, is already the algorithm. Overflow is a **state** problem too: test before you multiply.',
        ['`i = 0`; skip leading spaces.', 'Read one optional sign.', 'While the character is a digit: if `result * 10 + d` would pass the limit, clamp and return; else `result = result * 10 + d`.', 'Return `sign * result`. (If there were no digits, `result` is still 0.)'],
        '**State:** `i`, `sign`, `result`. **Invariant:** `result` is the value of the digits read so far, and `result` is within range. **Step:** one digit. **Valid:** stop at the first non-digit or end of string.'),
        'Problems [[#p3|3]] (String to Integer) and [[#p4|4]] (Roman to Integer); practice: Compare Version Numbers, Encode and Decode Strings', 'atoi',
        table(['i', 'char', 'phase', 'result', 'note'], [['0, 1', '` `, ` `', 'skip spaces', '0', '`s = "  -42x"`'], ['2', '`-`', 'sign', '0', '`sign = -1`'], ['3', '`4`', 'digit', '4', '`4 > (MAX - 4) // 10`? no'], ['4', '`2`', 'digit', '42', ''], ['5', '`x`', 'stop', '42', 'not a digit'], ['end', '', '', '**-42**', '`sign * result`']]),
        'O(n).', 'O(1).')

    h += pcard('D', 'Count or normalise, then group or look up', 'Easy', 'frequency table, signature key', (
        'Pass 1 builds a table (character counts, or a canonical key per string). Pass 2 uses the table to answer in the original order, or to group.',
        'Replaces repeated scanning or comparison sorting by one counting pass, and replaces "is x equivalent to y?" by "do x and y have the same key?".',
        '"First/only/appears once", "same letters", "equivalent up to...", "group the strings that...", "sort by a given order" over a small alphabet.',
        'If two strings are equivalent, there is something they share. Compute it once per string and equality of keys does the work of all the pairwise comparisons.',
        ['Choose the table: `count[26]` for lowercase letters, a dictionary otherwise, or a key (tuple of differences, sorted letters).', 'Pass 1: fill the table (or compute each string\'s key and append the string to `groups[key]`).', 'Pass 2: walk the original order and read the table.'],
        '**State:** the table. **Invariant:** after pass 1 the table describes the whole input. **Step (pass 2):** one lookup per element. **Valid:** keys really are equal exactly when the strings are equivalent (the mod 26 in Group Shifted is what makes this true).'),
        'Problems [[#p5|5]] (First Unique), [[#p6|6]] (Custom Sort), [[#p7|7]] (Group Shifted)', 'firstuniq',
        table(['pass', 'i', 'char', 'count', 'action'], [['1', '0-3', '`a a b c`', '`a:2, b:1, c:1`', 'fill the table for `s = "aabc"`'], ['2', '0', '`a`', '2', 'not unique'], ['2', '1', '`a`', '2', 'not unique'], ['2', '2', '`b`', '1', '**return 2**']]),
        'O(n) (O(N·L) for N keyed strings).', 'O(k) for k distinct characters (O(1) for 26 letters); O(N·L) for the groups.')

    h += pcard('E', 'Build the answer by position or digit', 'Medium', 'carry, position formula, bounce', (
        'Produce the output piece by piece: digit by digit from the right with a carry, into a slot given by a formula (`i + j + 1`), or into a row picked by a bouncing counter.',
        'Does arithmetic or layout on text too long for a number type, or described by a picture, without building the picture.',
        '"Add/multiply two numbers as strings", "without converting to integer", "zigzag", "format/justify", "convert to a different layout".',
        'Do on text what you do on paper: the column rule (digit sum, remainder, carry), or find the single formula that says where each input piece goes in the output.',
        ['Decide the direction (right to left for arithmetic) and the output container (list of digits, array of rows).', 'Loop while there is **any** input left **or a carry**.', 'Compute the piece and the new carry; write the piece.', 'Reverse or strip at the end (leading zeros, reversed digits).'],
        '**State:** cursors, carry, output list. **Invariant:** the output so far is the correct answer for the columns already processed, and `carry` is what must be added to the next column. **Valid:** nothing left in either input and `carry == 0`.'),
        'Problems [[#p8|8]] (Add Strings), [[#p9|9]] (Multiply Strings), [[#p10|10]] (Zigzag); practice: Add Binary, Text Justification', 'addstr',
        table(['i', 'j', 'carry in', 'sum', 'write', 'carry out'], [['1', '0', '0', '9 + 1 = 10', '0', '1'], ['0', '-1', '1', '9 + 0 + 1 = 10', '0', '1'], ['-1', '-1', '1', '1', '1', '0']]) + P('`"99" + "1"`: digits written right to left are `0, 0, 1`; reversed -> **`"100"`**. The third row exists only because the loop also runs while `carry != 0`.'),
        'O(max(n, m)) for addition; O(n·m) for multiplication; O(n) for zigzag.', 'O(output length).')

    h += pcard('F', 'Rewrite in place with read/write cursors', 'Medium', 'write <= read, or reverse twice', (
        'A read cursor scans the input; a write cursor marks where the next output character goes. For reordering, reverse the whole thing, then each piece.',
        'Rewrites a mutable array (or builds the answer from a string) in O(n) with O(1) extra space.',
        '"In place", "O(1) extra space", "return the new length", "reverse the words", "compress".',
        'Output is never longer than the part of the input already read, so writing cannot overwrite anything unread (`write <= read`). Reversing everything and then each word puts the words in reverse order with each word the right way round.',
        ['Start `read = write = 0`.', 'Measure the next piece (a run, a word) with `read`.', 'Write its compressed or reordered form at `write` and advance `write`.', 'Return `write` (the new length), or truncate to it.'],
        '**State:** `read`, `write`. **Invariant:** `chars[:write]` is the finished output for `chars[:read]`, and `write <= read`. **Valid:** `read` reached the end.'),
        'Problems [[#p11|11]] (Reverse Words) and [[#p12|12]] (String Compression)', 'compress',
        table(['read', 'run', 'write after', 'array'], [['0', '`aa` (2)', '2', '`a 2 b b b`'], ['2', '`bbb` (3)', '4', '`a 2 b 3 b`'], ['5', 'end', '4', 'return **4** (`a2b3`)']]) + P('Input `chars = "aabbb"`.'),
        'O(n).', 'O(1) extra.')

    h += pcard('G', 'Compare prefixes, search for a substring', 'Easy', 'vertical scan, KMP border', (
        'Compare many strings column by column and stop at the first mismatch; or search one string inside another while remembering how much of the needle already matches.',
        'Finds common prefixes in O(total characters) and substring positions in O(n + m) instead of O(n·m).',
        '"Common prefix", "starts with", "first occurrence", "find the needle", "repeated pattern", "shortest palindrome by prefix".',
        'A prefix grows one character at a time, so you only need the first disagreement. In substring search, when a mismatch happens the text already matched is known; its longest border says where to resume without re-reading the haystack.',
        ['Prefix: for column `i` of the first word, check every other word has a character at `i` and it is equal; at the first failure return the prefix before `i`.', 'KMP step 1: `lps[i]` = longest proper border of `needle[:i+1]`.', 'KMP step 2: scan the haystack; `k` = matched length; on mismatch `k = lps[k-1]`; on match `k += 1`; `k == m` is a hit.'],
        '**State:** column `i` (prefix) or `k`, `lps` (KMP). **Invariant (KMP):** `needle[:k]` equals the last `k` characters of the haystack read so far, and `k` is the longest such value. **Valid:** `k == m` at index `i` means the match starts at `i - m + 1`.'),
        'Problems [[#p13|13]] (Longest Common Prefix) and [[#p14|14]] (strStr with KMP)', 'strstr',
        P('Needle `ababc`, `lps = [0, 0, 1, 2, 0]`. Haystack `abababc`:') + table(['i', 'char', 'k before', 'what happens', 'k after'], [
            ['0', 'a', '0', 'match', '1'], ['1', 'b', '1', 'match', '2'], ['2', 'a', '2', 'match', '3'], ['3', 'b', '3', 'match', '4'],
            ['4', 'a', '4', '`c` expected: mismatch, `k = lps[3] = 2`; `a` matches `needle[2]`', '3'], ['5', 'b', '3', 'match', '4'], ['6', 'c', '4', 'match, `k == 5 == m`: return `6 - 5 + 1` = **2**', '5']])
        + P('Table `lps` for `aabaaab` (computed by the verified code): `[0, 1, 0, 1, 2, 2, 3]`. For the prefix cases, "flower / flow / flight" stops at column 2 (`o` vs `i`) and returns `"fl"`.'),
        'Prefix: O(total characters). strStr: brute O(n·m), KMP O(n + m).', 'Prefix: O(1). KMP: O(m) for `lps`.')
    return h

def part5():
    h = '<h2 id="part-5"><span class="part-no">Part 5</span>Pattern Recognition</h2>'
    h += P('Read the statement for **what is being asked** and **what is the cheapest thing to remember while scanning**. The table maps phrases to a pattern; the flowchart narrows it down; the last table is the honest list of problems that look like strings but are other topics.')
    h += H3('Problem clue -> pattern -> reasoning')
    h += table(['Problem clue', 'Pattern', 'Reasoning'], [
        ['"abbreviation", "compressed form", "merge", "compare versions"', 'Type A', 'Two inputs consumed at different speeds; never expand'],
        ['"palindromic substring", "longest palindrome", "count palindromes"', 'Type B', 'A palindrome is defined by its centre; try all 2n - 1'],
        ['"skip whitespace", "optional sign", "ignore characters after", "clamp to 32-bit"', 'Type C', 'A specification written as ordered phases; one loop each, test overflow first'],
        ['"Roman numeral", "convert using this table", "depends on the next character"', 'Type C', 'Single pass with one character of lookahead'],
        ['"first unique", "appears exactly once", "most frequent letter"', 'Type D', 'Count, then scan again in order'],
        ['"sort by a given order", "arrange according to"', 'Type D', 'A small known key set: counting beats comparison sorting'],
        ['"same pattern", "shifted", "equivalent up to", "group the strings that"', 'Type D', 'Find a canonical key; group by key'],
        ['"add/multiply as strings", "without converting to integer", "big number"', 'Type E', 'Column arithmetic from the right with a carry; or a position formula'],
        ['"zigzag", "spiral", "justify", "layout"', 'Type E', 'You never need the picture, only which output slot each piece goes to'],
        ['"in place", "O(1) extra space", "return the new length", "reverse the order of words"', 'Type F', '`write <= read`; or reverse twice'],
        ['"common prefix", "starts with", "all strings share"', 'Type G', 'Column scan, stop at the first mismatch'],
        ['"find the needle", "first occurrence", "is it a substring", "repeated substring pattern"', 'Type G', 'Brute force first; KMP if asked for O(n + m)']])
    h += H3('Decision flowchart')
    h += diagram(''' Is the input ONE string, or a list/pair of strings?
 |
 +-- asks about a WINDOW (longest/shortest substring with a constraint)?   -> Sliding Window  (earlier topic)
 +-- asks about brackets / nesting / "undo the last thing"?                -> Stack           (earlier topic) / Recursion (next)
 +-- asks to COUNT or GROUP by letters or an equivalence?                  -> Hashing (earlier) or Type D
 +-- asks for a best SUBSEQUENCE, or the edit distance between two strings? -> Dynamic Programming (later)
 +-- asks for ALL strings/arrangements?                                    -> Backtracking    (later)
 +-- asks for a path between words, or an ordering of letters?             -> Graph           (later)
 +-- searches MANY words or by prefix?                                     -> Trie            (later)
 |
 +-- is a palindrome the object?            -> Type B (centres)   or converging cursors (Two Pointers, Valid Palindrome)
 +-- is it a numeric/format conversion?     -> Type C (phases)    or Type E (carry) if the numbers are huge
 +-- must it be done in place?              -> Type F
 +-- is it a single needle in a haystack?   -> Type G
 +-- two strings consumed together?         -> Type A''')
    h += H3('Keyword map for the look-alikes')
    h += table(['If you see...', 'Think...', 'Because'], [
        ['"valid parentheses", "balanced", "decode string"', 'Stack', 'The most recent unmatched open bracket decides the next close'],
        ['"minimum number of changes to make valid" with only one bracket kind', 'A counter (Greedy)', 'No stack is needed when one counter of open brackets is enough'],
        ['"anagram", "permutation of"', 'Count table / fixed window', 'Letter counts, possibly over a window of fixed length'],
        ['"all", "every", "generate", "list all valid"', 'Backtracking', 'The output is a set of strings, not one answer'],
        ['"minimum edits", "longest common subsequence", "can it be segmented"', 'Dynamic Programming', 'Overlapping sub-problems on prefixes of the strings'],
        ['"starts with" asked many times on a dictionary', 'Trie', 'Shared prefixes are stored once']])
    h += H3('Looks like this topic, but actually needs something else')
    h += table(['Looks like', 'Actually needs', 'Why'], [
        ['Longest Substring Without Repeating Characters (3)', 'Sliding Window (done)', 'A window with a validity condition; strings are only the alphabet'],
        ['Valid Parentheses (20), Decode String (394), Basic Calculator (224, 227)', 'Stack (done)', 'Nesting; the last opened thing is closed first'],
        ['Group Anagrams (49), Valid Anagram (242)', 'Hashing (done)', 'A count/sorted-letters key; Type D here is the same idea for shifts'],
        ['Edit Distance (72), Longest Common Subsequence (1143), Word Break (139), Decode Ways (91)', 'Dynamic Programming', 'Every sub-problem is a pair of prefixes; greedy and two pointers fail'],
        ['Generate Parentheses (22), Letter Combinations (17), Palindrome Partitioning (131)', 'Backtracking', 'The answer is a list of strings; you explore and undo choices'],
        ['Word Search II (212), Implement Trie (208), Design Add and Search Words (211)', 'Tries', 'Many words, shared prefixes'],
        ['Word Ladder (127), Alien Dictionary (269)', 'Graph (BFS / topological sort)', 'Strings are nodes, one-letter changes or letter order are edges'],
        ['Serialize and Deserialize Binary Tree (297)', 'Trees', 'The string is only the encoding; the traversal is the topic'],
        ['Top K Frequent Words (692)', 'Heaps', 'Count, then select the top k by a comparator'],
        ['Longest Palindromic Substring (5)', 'Looks like DP, but centre expansion is the interview answer', 'O(n²) time and O(1) space, no table; DP is O(n²) space; Manacher is O(n) but rarely expected'],
        ['Valid Number (65)', 'A finite-state machine, not clever string tricks', 'Many cases (sign, dot, exponent); write a table of states or one flag per part; beyond the 14 problems here']])
    return h

def part6():
    h = '<h2 id="part-6"><span class="part-no">Part 6</span>Brute Force -> Optimization</h2>'
    h += P('For each family the same ladder: the naive approach, what it wastes, the observation, the better approach. The full code for both ends of each ladder is in <a class="xref" href="#part-7">Part 7</a> (brute force and optimal side by side).')
    h += H3('Longest Palindromic Substring (Type B)')
    h += diagram(''' Brute force      check every substring            O(n^2) substrings x O(n) check     = O(n^3)
      |  waste:   "abcba" is compared fully, then "bcb", then "c": the inner comparisons repeat
      v
 Observation      a palindrome = equal ends + a smaller palindrome around the SAME centre
      |
      v
 Better           from each of the 2n - 1 centres, grow while the ends match       = O(n^2), O(1) space
      |
      v
 Optional         Manacher re-uses mirror information between centres               = O(n)   (rarely expected)''')
    h += H3('Substring search (Type G)')
    h += diagram(''' Brute force      try every start, compare character by character         = O(n * m)
      |  waste:   on "aaaa..a" with needle "aaa..ab" each start matches almost all of the
      |           needle, fails at the last letter, and the next start re-compares the same letters
      v
 Observation      after matching k characters and failing, the matched text is KNOWN:
      |           it equals needle[:k]; the longest prefix of the needle that is also a suffix of
      |           it (a border) tells where to resume, without moving back in the haystack
      v
 Better           KMP: lps table for the needle O(m), scan the haystack O(n)       = O(n + m)''')
    h += P('Measured on the worst case (haystack `a` x 10,000, needle `a` x 4999 + `b`): brute force 25,005,000 character comparisons, KMP 24,998 (Appendix B).')
    h += H3('The other families')
    h += table(['Problem (type)', 'Brute force', 'Why slow / wasteful', 'Observation', 'Better', 'Compare'], [
        ['First Unique (D)', 'For each index, count that letter in the whole string', 'Same letter counted again for every occurrence', 'One count table answers every question', 'Count once, scan once', 'O(n²) -> O(n)'],
        ['Custom Sort (D)', 'Sort with a key function', 'A comparison sort when the keys are at most 26 values', 'Counting needs no comparisons', 'Emit each letter of `order` `count` times, then the rest', 'O(n log n) -> O(n)'],
        ['Group Shifted (D)', 'Compare with each group\'s representative, 26 rotations', 'Repeats a comparison for every pair', 'Shift-equivalent strings share a signature', 'Group by signature in a hash map', 'O(N²·L·26) -> O(N·L)'],
        ['Add Strings (E)', '`int(a) + int(b)`', 'Forbidden; conversion of long strings is slow and limited', 'Column addition needs one digit pair and one carry', 'Right-to-left loop with carry', 'n/a -> O(max(n, m))'],
        ['Multiply Strings (E)', '`int(a) * int(b)`', 'Forbidden', 'Digit i x digit j lands in slot i + j + 1', 'Array of n + m digits, carry one slot left', 'n/a -> O(n·m)'],
        ['Zigzag (E)', 'Fill a rows x n grid, read row by row', 'Allocates and scans many empty cells', 'Only the row of each character matters', 'Row counter that bounces; one buffer per row', 'O(rows·n) -> O(n)'],
        ['String Compression (F)', 'Build a new string, copy back', 'O(n) extra space', 'Output never outruns input: `write <= read`', 'Overwrite in place', 'O(n) space -> O(1)'],
        ['Reverse Words (F)', '`split`, reverse, `join`', 'Extra lists; hides the space handling', 'Reverse all, then each word, compact spaces', 'Two cursors on a char array', 'O(n) space -> O(1) extra'],
        ['Longest Common Prefix (G)', 'Try every prefix length against every word', 'Re-slices and re-compares the same prefix', 'The prefix only grows; stop at the first mismatch', 'Vertical scan', 'O(L·S) -> O(S)'],
        ['Valid Word Abbreviation (A)', 'Expand numbers into `?` marks', 'Pattern can be far longer than the input', 'Skip is just `i += num`', 'Two cursors', 'O(n + sum) -> O(n + m)']])
    return h
