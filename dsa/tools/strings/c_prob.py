import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import probs_a, probs_b
from probs_a import PROBS
from lib import *

HERE = os.path.dirname(os.path.abspath(__file__))
SCORES = json.load(open(os.path.join(HERE, 'scores.json')))
BY = {p['key']: p for p in PROBS}
CSV_TITLE = {'vwa': 'Valid Word Abbreviation', 'lps': 'Longest Palindromic Substring', 'atoi': 'String to Integer (atoi)', 'roman': 'Roman to Integer',
             'revwords': 'Reverse Words in a String', 'firstuniq': 'First Unique Character in a String', 'customsort': 'Custom Sort String',
             'shifted': 'Group Shifted Strings', 'addstr': 'Add Strings', 'mulstr': 'Multiply Strings', 'zigzag': 'Zigzag Conversion',
             'lcp': 'Longest Common Prefix', 'compress': 'String Compression', 'strstr': 'Find the Index of the First Occurrence in a String',
             'merge': 'Merge Strings Alternately', 'addbin': 'Add Binary', 'pals': 'Palindromic Substrings', 'version': 'Compare Version Numbers',
             'codec': 'Encode and Decode Strings', 'justify': 'Text Justification'}
TYPE_NAME = {'A': 'Two cursors over two strings', 'B': 'Expand around a centre', 'C': 'Parse once with a little state',
             'D': 'Count or normalise, then group or look up', 'E': 'Build the answer by position or digit',
             'F': 'Rewrite in place with read/write cursors', 'G': 'Compare prefixes, search for a substring'}
# solved order and final type letters
ORDER = ['vwa', 'lps', 'atoi', 'roman', 'firstuniq', 'customsort', 'shifted', 'addstr', 'mulstr', 'zigzag', 'revwords', 'compress', 'lcp', 'strstr']
TYPE_OF = {'vwa': 'A', 'lps': 'B', 'atoi': 'C', 'roman': 'C', 'firstuniq': 'D', 'customsort': 'D', 'shifted': 'D', 'addstr': 'E', 'mulstr': 'E',
           'zigzag': 'E', 'revwords': 'F', 'compress': 'F', 'lcp': 'G', 'strstr': 'G',
           'merge': 'A', 'pals': 'B', 'version': 'C', 'codec': 'C', 'addbin': 'E', 'justify': 'E'}
NUM = {k: i + 1 for i, k in enumerate(ORDER)}
TWIST = {'lps', 'mulstr'}

def scores(key):
    d = SCORES[CSV_TITLE[key]]
    return ', '.join(f'{c} {v}' for c, v in d.items())

def provenance(key):
    n = len(SCORES[CSV_TITLE[key]])
    extra = {'atoi': ' Also on the Grind 75 Strings section.',
             'lps': ' Also on the Grind 75 Strings section and in the Blind 75 String section (community copy); deferred here from the Two Pointers notes.',
             'pals': ' Also in the Blind 75 String section (community copy).',
             'codec': ' Also in the Blind 75 String section (community copy). LeetCode Premium problem.',
             'revwords': ' Deferred here from the Two Pointers notes, where it was listed as a Google two-pointer problem.',
             'merge': ' Deferred here from the Two Pointers notes.',
             'shifted': ' LeetCode Premium problem.',
             'vwa': ' LeetCode Premium problem.'}.get(key, '')
    return f'Frequently asked: listed by {n} of the 6 companies read (company-tag scores: {scores(key)}).{extra}'

# ---------------------------------------------------------------------------------------------
# Hand-written teaching text for the 14 solved problems
# ---------------------------------------------------------------------------------------------
M = {}
M['vwa'] = dict(
    problem='A **word** (lowercase letters) and an **abbreviation** `abbr` (lowercase letters and digit runs, where a digit run is a number saying "skip this many letters"). Return `true` if `abbr` is a valid abbreviation of `word`. A number may not have a leading zero and may not be zero ("01" and "0" are invalid). Each digit run is **one** number: replaced pieces cannot touch, so "s55n" means skipping 55 letters, not 5 then 5.',
    example='`word = "internationalization"`, `abbr = "i12iz4n"` -> `true`. `word = "apple"`, `abbr = "a2e"` -> `false` (skips "pp" then expects "e" but the word has "l" before it).',
    recognise='Two strings that must stay in step, one of them compressed. Each cursor has its own stride: a letter moves both by 1, a number moves `word` by that many and `abbr` by its digit count.',
    skill='Type A: two cursors, a digit-run parser, and an end condition that checks **both** cursors reached the end.',
    brute_why='Expand the abbreviation into a pattern with one `?` per skipped letter, then compare. Correct, but the pattern can be as long as the numbers say, not as long as the input: an abbreviation like "1000000000" asks for a billion `?`. The Java version has to guard against that.',
    brute_cost='O(n + sum of the numbers) time and space',
    observation='You never need the expanded pattern. Moving `i` forward by the number gives exactly the same alignment, in O(1) per number instead of O(number).',
    opt_cost='O(n + m) time, O(1) space (n = len(word), m = len(abbr))',
    say='"Two cursors, i on word and j on abbr. A letter must match and moves both. A digit run: reject a leading zero, parse the whole number, jump i. At the end both cursors must be exactly at the end, so a number that overshoots the word fails."')
M['lps'] = dict(
    problem='Given a string `s`, return its longest palindromic substring (if several have the same length, the leftmost).',
    example='`"babad"` -> `"bab"` (`"aba"` is also valid; this page returns the leftmost). `"cbbd"` -> `"bb"`.',
    recognise='"Longest palindromic substring", n up to 1000. A palindrome is mirror-symmetric around a centre, so the centre is what you enumerate. The DP table version works but needs O(n²) memory.',
    skill='Type B: enumerate centres (odd and even), grow outwards while the mirror characters match. This also teaches why the loop "stops one step too far".',
    brute_why='Check every substring (n² of them) with an O(n) reverse-and-compare. The work is repeated: "abcba" is checked as a whole, then "bcb", then "c", re-doing the comparisons that are already known to be true inside.',
    brute_cost='O(n³) time, O(n) space for the copies',
    observation='A palindrome contains a smaller palindrome around the same centre. So start at each of the 2n - 1 centres and grow outwards: each growth step re-uses everything the previous step proved.',
    opt_cost='O(n²) time, O(1) space. Manacher\'s algorithm is O(n) but is rarely expected.',
    say='"There are 2n - 1 centres: n single characters for odd lengths and n - 1 gaps for even lengths. From each centre I expand while the two ends match, then record the longest. Worst case, a string of one repeated letter, is O(n²), which is fine for n = 1000."')
M['atoi'] = dict(
    problem='Implement `myAtoi(s)`: skip leading spaces, read an optional `+` or `-`, read digits until the first non-digit, and return the number clamped to the signed 32-bit range [-2^31, 2^31 - 1]. If no digits are read, return 0.',
    example='`"   -42"` -> `-42`. `"4193 with words"` -> `4193`. `"words and 987"` -> `0`. `"-91283472332"` -> `-2147483648`.',
    recognise='A formal list of steps in the statement: that is a **state machine** written in prose. Each step is a short loop, in order, and the order is the algorithm.',
    skill='Type C: scan once, one loop per phase, and **clamp before overflowing** (the check goes before `result * 10 + d`, not after).',
    brute_why='A regex finds the number in one line. It is a good reference to test against, and not slower, but interviewers often ban library parsing and the question is really testing whether you can write the steps and the overflow check yourself.',
    brute_cost='O(n) time, O(1) space',
    observation='Four phases in a fixed order: spaces, sign, digits, clamp. Overflow must be detected **before** it happens: in Java the int silently wraps, so test `result > (MAX - d) / 10` first.',
    opt_cost='O(n) time, O(1) space',
    say='"I\'ll write it as four small loops in the order the statement gives. For overflow I compare result against (INT_MAX - d) / 10 before multiplying, so I never need a wider type. For a negative sign I return INT_MIN, because the same check also catches 2147483648."')
M['roman'] = dict(
    problem='Convert a Roman numeral (I, V, X, L, C, D, M with the six subtractive pairs IV, IX, XL, XC, CD, CM) to an integer between 1 and 3999.',
    example='`"III"` -> `3`. `"LVIII"` -> `58`. `"MCMXCIV"` -> `1994`.',
    recognise='A lookup table plus a rule that depends on the **next** character (one-character lookahead).',
    skill='Type C: one pass with a lookahead rule. "Smaller before larger means subtract" replaces six special cases.',
    brute_why='Rewrite each subtractive pair as repeated letters (IV -> IIII) and add everything. Correct, but six special cases to remember and a second copy of the string.',
    brute_cost='O(n) time, O(n) space',
    observation='A symbol is subtracted exactly when the next symbol is bigger. One comparison covers all six pairs.',
    opt_cost='O(n) time, O(1) space',
    say='"Left to right. If this value is smaller than the next one it is part of a subtractive pair, so subtract it, otherwise add it. The last character has no next one, so it is always added."')
M['firstuniq'] = dict(
    problem='Return the index of the first character in `s` that appears exactly once, or -1.',
    example='`"leetcode"` -> `0`. `"loveleetcode"` -> `2`. `"aabb"` -> `-1`.',
    recognise='"First" plus "appears exactly once": you need counts **and** the original order. A count table gives the first, a second pass over the string gives the second.',
    skill='Type D: count first, then scan in the original order. A frequency table loses order; the second pass restores it.',
    brute_why='For each index, count how many times that letter appears in the whole string. The same letter is counted again every time it appears.',
    brute_cost='O(n²) time, O(1) space',
    observation='Counting once is enough. Counts tell you which letters are unique; the string itself still holds the order.',
    opt_cost='O(n) time, O(1) space for a fixed alphabet (O(k) in general for k distinct characters)',
    say='"Two passes: build a count of every character, then walk the string again and return the first index whose count is 1. Order comes from the second pass, uniqueness from the first."')
M['customsort'] = dict(
    problem='`order` has distinct lowercase letters. Reorder `s` so that its letters appear in the same relative order as in `order`. Letters not in `order` may go anywhere (this page puts them at the end, in their original order).',
    example='`order = "cba"`, `s = "abcd"` -> `"cbad"` (any valid answer is accepted, e.g. `"dcba"`).',
    recognise='"Sort by a custom order" over a tiny alphabet. When the key space is small and known, **counting beats comparison sorting**.',
    skill='Type D: replace sorting by counting. Emit each letter of `order` as many times as it occurs, then the leftovers.',
    brute_why='Sort `s` with a key function (rank in `order`). It works and is two lines, but it costs a comparison sort and an `order.index` lookup per comparison.',
    brute_cost='O(n log n) time (plus the key lookups), O(n) space',
    observation='There are at most 26 distinct keys. Count how many of each, then write them out in key order: no comparisons needed.',
    opt_cost='O(n + k) time and O(n) output (k = len(order))',
    say='"I count the letters of s. Then for each letter in order I append it count times and zero its count. Anything not in order is appended in original order at the end. No sorting needed because the key set is tiny."')
M['shifted'] = dict(
    problem='Two strings are in the same **shift group** if one can be turned into the other by shifting every letter by the same amount (wrapping z -> a). Group a list of strings into shift groups.',
    example='`["abc","bcd","acef","xyz","az","ba","a","z"]` -> groups `["abc","bcd","xyz"]`, `["acef"]`, `["az","ba"]`, `["a","z"]` (group order is free).',
    recognise='"Same up to a transformation" is a **canonical form** problem: find a key that is equal for every member of a group. Same family as Group Anagrams, with a different key.',
    skill='Type D: normalise each string to a signature (each letter\'s distance from the first letter, mod 26), then group by signature in a hash map.',
    brute_why='Compare each string with a representative of each existing group, trying all 26 rotations. The same comparison is repeated for every pair.',
    brute_cost='O(N² · L · 26) time worst case (N strings of length L)',
    observation='Two strings are shifts of each other exactly when their letter-to-first-letter distances match. That distance list is a key, so equal keys mean the same group and a hash map groups in one pass.',
    opt_cost='O(N · L) time and space',
    say='"I need a key that every member of a group shares. Subtract the first letter from every letter and take mod 26: shifting all letters changes the first letter by the same amount, so the differences do not change. Then it is group-by-key. The mod matters: \'az\' and \'ba\' only match with it."')
M['addstr'] = dict(
    problem='Add two non-negative integers given as decimal strings, returning the sum as a string, **without** converting the whole strings to integers.',
    example='`"11" + "123"` -> `"134"`. `"99" + "1"` -> `"100"`. `"0" + "0"` -> `"0"`.',
    recognise='Numbers too big for a built-in integer, so you do what a child does on paper: right to left, one column at a time, with a carry.',
    skill='Type E: build the output one position at a time from the least significant end, loop while **either** string has digits **or** a carry remains.',
    brute_why='`int(a) + int(b)` is a one-liner in Python (and `BigInteger` in Java), but the problem forbids it, and in Python 3.11+ converting a string with more than 4300 digits raises `ValueError` by default.',
    brute_cost='Not allowed by the problem; conversion of a long string is itself super-linear in CPython',
    observation='Column addition needs only the current digit of each string and one carry (0 or 1). The loop condition must include the carry, or the final extra digit is lost.',
    opt_cost='O(max(n, m)) time, O(max(n, m)) space for the output',
    say='"Two cursors from the right, one carry. Each column: sum the two digits and the carry, write sum % 10, carry sum / 10. The loop runs while either string has digits left or the carry is non-zero, so 99 + 1 produces its leading 1. I build the digits in reverse and reverse once at the end."')
M['mulstr'] = dict(
    problem='Multiply two non-negative integers given as strings and return the product as a string, without converting to integers.',
    example='`"2" * "3"` -> `"6"`. `"123" * "456"` -> `"56088"`.',
    recognise='The same "no big-int" restriction, but now it is long multiplication. The question is where each partial product lands.',
    skill='Type E: a **position formula**. Digit `i` of `a` times digit `j` of `b` contributes to column `i + j + 1` (and its carry to `i + j`). Looks like a hard big-number problem; it is one formula and a leading-zero strip.',
    brute_why='Convert both to integers and multiply (forbidden, and the reference for testing). The by-hand method of adding n shifted partial products also works but needs the add routine from problem 8.',
    brute_cost='Not allowed by the problem',
    observation='A product of an n-digit and an m-digit number has at most n + m digits. Keep an array of that size, add each digit-by-digit product into its column, and push the carry one column left.',
    opt_cost='O(n · m) time, O(n + m) space',
    say='"The result has at most n + m digits. For each pair of digits I add their product into slot i + j + 1, keep the remainder there and push the carry into i + j. At the end I skip leading zeros, with a special case for a zero input so I do not return an empty string."')
M['zigzag'] = dict(
    problem='Write `s` in a zigzag pattern on `numRows` rows (down the rows, then diagonally up), then read the rows left to right.',
    example='`s = "PAYPALISHIRING"`, `numRows = 3` -> `"PAHNAPLSIIGYIR"`.',
    recognise='A described layout. You do **not** need to draw the layout: only to know which row each character falls into.',
    skill='Type E: the row index bounces between 0 and `numRows - 1`. Keep one buffer per row and a direction.',
    brute_why='Fill a 2D grid with the real zigzag positions and read it row by row. It makes the picture literal, but allocates rows x n cells for n characters.',
    brute_cost='O(numRows · n) time and space',
    observation='Only the row of each character matters. The row goes 0, 1, ..., last, last - 1, ..., 1, 0, ... so a counter that flips direction at the two ends gives every row.',
    opt_cost='O(n) time, O(n) space',
    say='"I just track which row the next character goes to: it increases until the bottom row, then decreases until the top. One list per row, append, then concatenate. If numRows is 1 there is no bounce, so I return s directly."')
M['revwords'] = dict(
    problem='Reverse the order of the words in `s`. Words are separated by one or more spaces; the output has exactly one space between words and none at the start or end.',
    example='`"  the sky  is blue "` -> `"blue is sky the"`.',
    recognise='Words, spaces, "reverse the order". The traps are the messy spaces. A follow-up often asks for O(1) extra space on a **mutable** array.',
    skill='Type F: scanning from the right to cut words without `split`, and the three-step in-place version (reverse everything, reverse each word, squeeze the spaces).',
    brute_why='`" ".join(reversed(s.split()))` is correct and fine in real code. Interviewers may ask you to avoid `split`, or to do it in place, to see whether you can handle the spacing yourself.',
    brute_cost='O(n) time, O(n) space',
    observation='Walk from the right end: skip spaces, mark the end of a word, walk to its start, take the slice. For O(1) space on a char array: reversing the whole string puts the words in the right order but backwards, so reverse each word back, compacting spaces with a write cursor.',
    opt_cost='O(n) time. O(n) space for the output; the in-place char-array version is O(1) extra space',
    say='"From the right: skip spaces, remember where the word ends, scan left to its start, append the slice. Because I skip runs of spaces, the output spacing is right by construction. For constant extra space, I reverse the whole array, then reverse each word and compact with a write cursor."')
M['compress'] = dict(
    problem='Given a `char[]`, compress it **in place**: for each run of equal characters write the character, and the run length if it is greater than 1 (a length of 10 or more is written as separate digit characters). Return the new length.',
    example='`["a","a","b","b","c","c","c"]` -> returns `6`, array starts `["a","2","b","2","c","3"]`. A run of twelve `a` becomes `"a","1","2"`.',
    recognise='"In place", "return the new length", a char array. The writing position must never overtake the reading position.',
    skill='Type F: the read/write cursor pair from the Arrays topic, applied to runs. Digits of a multi-digit count each take one slot.',
    brute_why='Build the compressed string in a new buffer, then copy it back. Correct, but it uses O(n) extra space, which the problem asks you to avoid.',
    brute_cost='O(n) time, O(n) extra space',
    observation='The compressed form of a run is never longer than the run itself (a run of 1 writes 1 char, a run of 2 writes 2 chars, longer runs write fewer). So `write <= read` always, and overwriting is safe.',
    opt_cost='O(n) time, O(1) extra space',
    say='"Two cursors. read measures a run, write puts the character and then the digits of the count, one per slot, only if the count is greater than 1. write never passes read because a run never compresses to something longer, so I can overwrite safely."')
M['lcp'] = dict(
    problem='Return the longest common prefix of an array of strings, or `""` if there is none.',
    example='`["flower","flow","flight"]` -> `"fl"`. `["dog","racecar","car"]` -> `""`.',
    recognise='"Common prefix" across **all** strings. The answer is limited by the shortest string and by the first column where any two strings disagree.',
    skill='Type G: scan column by column (vertical scan) and stop at the first disagreement.',
    brute_why='Try every prefix length of the first word and test it against every word. Each test slices and compares whole prefixes again.',
    brute_cost='O(L · S) time worst case (L = length of first word, S = total characters)',
    observation='Prefixes grow one character at a time, so stop at the first column where something differs. No prefix is ever tested twice.',
    opt_cost='O(S) time worst case (S = total characters), O(1) extra space',
    say='"Column by column from the left. At column i every word must have a character and it must equal the first word\'s. At the first failure I return the first word up to i. If I run off the first word, the whole first word is the prefix."')
M['strstr'] = dict(
    problem='Return the index of the first occurrence of `needle` in `haystack`, or -1 (needle is non-empty).',
    example='`"sadbutsad"`, `"sad"` -> `0`. `"leetcode"`, `"leeto"` -> `-1`.',
    recognise='"Find a substring". In an interview the expected first answer is the brute force; **KMP** is the follow-up when they say "can you do better than O(n·m)?".',
    skill='Type G: the brute force with its worst case, then KMP: when a mismatch happens, reuse what the matched part already told you (the longest border) instead of restarting.',
    brute_why='Try every start position and compare character by character. On `"aaaa...a"` searched for `"aaa...ab"` every start matches almost all of the needle before failing, re-comparing the same letters again and again.',
    brute_cost='O(n · m) time, O(1) space',
    observation='When the first k characters of the needle matched and the next one fails, the matched text is known. The longest prefix of the needle that is also a suffix of the matched part (a **border**) says where to resume, without moving back in the haystack.',
    opt_cost='O(n + m) time, O(m) space',
    say='"First brute force, O(n·m). To do better I precompute, for each prefix of the needle, the longest proper border (lps). Then I scan the haystack once; on a mismatch I fall back to lps[k - 1] instead of restarting. k rises at most once per character, so the falls are bounded and the total is O(n + m)."')

def prob_card(key):
    p = BY[key]; m = M[key]; t = TYPE_OF[key]; n = NUM[key]
    pr = lambda role: p['py_' + role][0]
    jv = lambda role: p['java_' + role][0]
    bar = p['key']
    h = (f'<details class="card problem" id="p{n}"><summary><div class="problem-header"><div class="problem-num t{t}">{n}</div><div>'
         f'<h4 class="problem-title">{esc(p["title"])}</h4><div class="pill-row">{pill("Type " + t, "c-accent")}{pill(p["diff"], DIFF_COLOR[p["diff"]])}'
         f'{pill("LeetCode " + str(p["lc"]), mono=True)}{pill("Look-alike with a twist", "c-orange") if key in TWIST else ""}</div></div></div><span class="reveal-hint"><span class="closed">Show</span><span class="opened">Hide</span></span></summary>')
    h += P('**Where it is reported.** ' + provenance(key))
    h += P('**Problem.** ' + m['problem']) + P('**Example.** ' + m['example'])
    h += P('**Recognise before coding.** ' + m['recognise']) + P('**Skill it teaches.** ' + m['skill'])
    h += step(1, 'Brute force' if key not in ('atoi',) else 'Reference solution (brute force)')
    h += P(m['brute_why'])
    h += code_block(pr('brute'), jv('brute'))
    h += P('**Cost:** ' + m['brute_cost'] + '.')
    h += '<button type="button" class="reveal-btn">Show the observation and the optimal solution</button><div class="reveal-zone">'
    h += step(2, 'Observation') + P(m['observation'])
    h += step(3, 'Optimal solution') + code_block(pr('opt'), jv('opt')) + P('**Cost:** ' + m['opt_cost'] + '.')
    if key == 'revwords':
        h += step(4, 'Follow-up: O(1) extra space on a mutable array')
        h += P('Strings are immutable in Python and Java, so this version works on a list of characters / a `char[]`. It is verified like the others.')
        h += code_block(p['py_opt2'][0], p['java_opt2'][0])
        h += P('**Cost:** O(n) time, O(1) extra space (the caller owns the array).')
    h += P('**Say aloud.** ' + m['say'])
    h += '</div></details>'
    return h

# ---------------------------------------------------------------------------------------------
# Practice (Part 14) and Appendix A
# ---------------------------------------------------------------------------------------------
PRACTICE = ['merge', 'addbin', 'pals', 'version', 'codec', 'justify']
PR = {}
PR['merge'] = dict(task='Given two strings, merge them by adding letters in alternating order, starting with `word1`. If one string is longer, append the rest at the end.',
    think=['Which of your two cursors needs to be able to run out first? What do you do when it does?', 'Can you find the length of the common part first, so the tail handling is just two slices?', 'What do you return for "ab" and ""? (The constraints say both are non-empty; what would your code do anyway?)'],
    idea='Type A. Interleave the common part, then append whichever tail is left. Only one of the two tails is non-empty, so appending both is safe.')
PR['addbin'] = dict(task='Given two binary strings, return their sum as a binary string. No big-integer conversion.',
    think=['Which problem in Part 7 is this one a copy of? What changes: the base, the digit values, the carry?', 'Does the loop condition include the carry? What is `"1" + "1"`?', 'Could you do it with a single index into each string if you pad? Is it worth it?'],
    idea='Type E. Same as Add Strings with base 2: the carry is `total // 2` and the digit is `total % 2`.')
PR['pals'] = dict(task='Count the palindromic substrings of `s` (substrings with different start or end positions count separately).',
    think=['Which Part 7 problem is the sibling of this one? What do you do at the moment a palindrome is found, instead of recording the longest?', 'For `"aaa"`, how many are there, and which centres find them?', 'What is the worst-case input for your approach and what is its cost?'],
    idea='Type B. The same 2n - 1 centres; every successful expansion step is one more palindrome, so add 1 per step instead of tracking the longest.')
PR['version'] = dict(task='Compare two version strings such as "1.01" and "1.001". Revisions are separated by dots; compare them as integers left to right; a missing revision counts as 0. Return -1, 0 or 1.',
    think=['What is the trap with `"1.0"` against `"1"`? With `"1.01"` against `"1.001"`?', 'Can you avoid `split` and parse one revision at a time with two cursors?', 'What if the strings have a different number of revisions? How does your loop condition handle it?'],
    idea='Type C (and a Type A cursor pair). Loop while either string has characters left; parse one revision from each (defaulting to 0) and compare. No `split` is needed.')
PR['codec'] = dict(task='Design `encode(list of strings) -> string` and `decode(string) -> list of strings` so that the round trip is exact for **any** strings, including empty strings and strings that contain your delimiter.',
    think=['Why does joining with a delimiter fail? Give a concrete list that breaks it.', 'Could you escape the delimiter? What new problem does that create?', 'What if every string is prefixed with its length? How do you know where the length ends?'],
    idea='Type C (format design plus parsing). Prefix each string with its length and a separator: the decoder reads the length, then takes exactly that many characters, so the data can never be confused with the format.')
PR['justify'] = dict(task='Given words and a `maxWidth`, format the text so that every line has exactly `maxWidth` characters, fully justified (extra spaces distributed as evenly as possible, left slots first). The last line, and any line with a single word, is left-justified.',
    think=['Greedy line packing: how many words fit on a line, counting one space per gap as the minimum?', 'With `chars` letters and `gaps` gaps, what are the base space per gap and the number of gaps that get one extra? (`divmod`.)', 'Which two cases need left-justification, and what is the shared rule for the padding?'],
    idea='Type E (stretch). Pack greedily, then distribute `space, extra = divmod(maxWidth - chars, gaps)` so the first `extra` gaps get one more space. Special-case the last line and single-word lines.')

def practice_card(key):
    p = BY[key]; pr = PR[key]; t = TYPE_OF[key]
    h = f'<div class="card"><h4>{esc(p["title"])} ({p["lc"]})</h4><div class="pill-row">{pill(p["diff"] if p["diff"]!="Hard" else "Hard (stretch)", DIFF_COLOR[p["diff"]])}{pill("Type " + t, "c-accent")}{pill("LeetCode " + str(p["lc"]), mono=True)}</div>'
    h += P('**Provenance.** ' + provenance(key))
    h += P('**Task.** ' + pr['task']) + P('**Think about:**') + UL(pr['think']) + '</div>'
    return h

def appendix_a_card(key):
    p = BY[key]; pr = PR[key]
    if key == 'codec':
        h = f'<details class="card"><summary><strong>{esc(p["title"])}</strong> &middot; LeetCode {p["lc"]}</summary>'
        h += P('**Idea.** ' + pr['idea'])
        h += P('The tempting version, shown only so you can see how it fails. `decode_naive(encode_naive(["a#b", "c"]))` returns `["a", "b", "c"]`, not the original list (run, see Appendix B).')
        h += code_block(p['py_brute'][0], '// the naive version fails the same way in Java: any delimiter that can occur inside the data is ambiguous.\n// Skip it and read the length-prefix version below.')
        h += P('The length-prefix version. The decoder takes the **first** `#` after the current position, so `#` inside the text can never be mistaken for a separator.')
        h += code_block(p['py_opt'][0], p['java_opt'][0])
        h += P('**Cost:** O(total characters) time and space for both directions. **Follow-up:** the length is a decimal number, so very long strings use more digits; a fixed 4-byte binary length is the usual production choice.')
        return h + '</details>'
    h = f'<details class="card"><summary><strong>{esc(p["title"])}</strong> &middot; LeetCode {p["lc"]}</summary>'
    h += P('**Idea.** ' + pr['idea'])
    h += P('Brute force (the reference it was tested against):')
    h += code_block(p['py_brute'][0], p['java_brute'][0])
    h += P('Optimal:')
    h += code_block(p['py_opt'][0], p['java_opt'][0])
    costs = {'merge': 'O(n + m) time and space.', 'addbin': 'O(max(n, m)) time and space.', 'pals': 'O(n²) time, O(1) space (brute force O(n³)).',
             'version': 'O(n + m) time, O(1) space (the brute force splits and is O(n + m) space).',
             'justify': 'O(total characters) time and O(output) space.'}
    h += P('**Cost:** ' + costs[key])
    return h + '</details>'
