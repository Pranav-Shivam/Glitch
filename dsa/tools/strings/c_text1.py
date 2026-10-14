from lib import *
from toolkit import PY_EX, JAVA_EX, JAVA_EXPECT

def part1():
    h = '<h2 id="part-1"><span class="part-no">Part 1</span>First Principles</h2>'
    h += callout('tip', 'One-paragraph summary',
        '<p>A <strong>string</strong> is a sequence of characters, so it behaves like an array you cannot change. What makes string problems their own topic is the <strong>kind of question</strong> asked about that sequence: parse it (a number, a path, a format), compare or normalise it (palindromes, prefixes, "same up to a shift"), rebuild it (add two numbers written as text, wrap lines), or find a smaller string inside it. Nearly all of them are solved by <strong>one pass with a couple of cursors and a small piece of state</strong>, which turns the obvious "re-scan or re-copy for every position" O(n²) or O(n³) into O(n). The skill to learn is stating, in one sentence, what the characters you have already passed mean.</p>')
    h += diagram(''' A string is an array of characters you cannot assign into:

 index:   0   1   2   3   4   5   6   7   8
 char:    i   n   t   e   r   v   i   e   w          s[2:5] = "ter"   (a COPY of 3 characters)
          ^                               ^
          first                           last = s[len(s) - 1] = s[-1] in Python

 s[0] = "x"      Python: TypeError.   Java: no such syntax. To edit, copy to a list / char[] / StringBuilder.
 s + "!"         creates a NEW string of length n + 1 (copies all n characters).

 The four jobs, with the problems that do them:
   parse     "  -42abc"  -> -42            String to Integer, Roman to Integer, Valid Word Abbreviation
   compare   "abcba"     is it a palindrome? Longest Common Prefix, Group Shifted Strings
   build     "99" + "1"  -> "100"          Add Strings, Multiply Strings, Zigzag, Text Justification
   search    "sad" in "sadbutsad"          Find the Index of the First Occurrence (strStr), KMP''')
    h += H3('Why it exists and what problem it solves')
    h += UL([
        '**Text is the most common data you meet.** Logs, URLs, file paths, versions, numbers too big for an integer, user input. Every real system parses and rebuilds strings all day.',
        '**Strings have pitfalls that arrays do not.** They are immutable in Python and Java, so "just edit it" is a copy; concatenating in a loop can be quadratic; characters are not the same as numbers; and a character is not always one position (Unicode). Interviewers use string problems to see whether you know these costs.',
        '**Better than the naive scan.** Checking every substring of a string is O(n³) for palindromes; growing outwards from each centre is O(n²) with O(1) space. Restarting a substring search at every position is O(n·m); KMP is O(n + m).',
        '**Better than clever tricks.** Built-ins (`int(a) + int(b)`, `split`, regex) answer many of these in one line. Interviews often forbid them, because the point is whether you can do the work and handle the edge cases yourself.'])
    h += H3('Terms used in these notes')
    h += table(['Term', 'Meaning'], [
        ['character, code unit, code point', 'What `s[i]` gives you. In Python a `str` is a sequence of Unicode **code points**, so `len("a😀")` is 2. In Java a `char` is a 16-bit **code unit**, so the same text has `length()` 3 (the emoji is a surrogate pair). Interview problems almost always say "lowercase English letters" so you can ignore this; know it exists.'],
        ['substring vs subsequence', 'A **substring** is a contiguous slice (`"ter"` in `"interview"`). A **subsequence** may skip characters (`"iew"`). Substring problems use cursors and windows; subsequence problems usually need DP.'],
        ['prefix, suffix', 'The first k characters / the last k characters. A **border** is a string that is both a proper prefix and a suffix of the same text (`"aba"` has border `"a"`); KMP is built on borders.'],
        ['palindrome', 'Reads the same forwards and backwards. Has a **centre**: a character (odd length) or the gap between two characters (even length).'],
        ['anagram', 'Same letters with the same counts in any order. The usual key is the sorted letters or a count table.'],
        ['immutable', 'Cannot be changed after creation. Every "edit" builds a new string. `StringBuilder` (Java) and a list of characters (Python) are the mutable versions.'],
        ['signature / canonical form', 'A value that is equal for every string in a group, so that "same group" becomes "same key". The sorted letters of an anagram; the distances from the first letter for a shift group.'],
        ['delimiter, token', 'A **delimiter** separates pieces (a space, a comma, a dot). A **token** is one piece between delimiters. Parsing is turning text into tokens, then into values.'],
        ['lexicographic order', 'Dictionary order, compared character by character on character codes. `"10" < "9"` is true because `"1" < "9"`.'],
        ['carry', 'The digit passed to the next column in addition or multiplication (the 1 in "9 + 1 = 10, write 0, carry 1").']])
    h += H3('The core invariant')
    h += callout('warn', 'Write this down before every loop',
        '<p><strong>At every moment I can say, in one sentence, what the characters I have already passed have turned into.</strong> "result holds the number made by s[i..j)"; "best holds the longest palindrome among centres 0..c"; "write marks the end of the compressed output, and write &lt;= read"; "k characters of the needle currently match". If I cannot say it, the loop is a guess. Each pattern in <a class="xref" href="#part-4">Part 4</a> has its own version of this sentence, and every bug in <a class="xref" href="#part-10">Part 10</a> is a case where the sentence stopped being true (a carry dropped, a bound off by one, a leading zero let through).</p>')
    h += H3('When to use it, and when not to')
    h += table(['Use string-specific technique when...', 'Do NOT start here when...'], [
        ['one pass with a few cursors and a small state is enough (parsing, merging, in-place rewrite)', 'the question asks about **every substring in a window** with a constraint ("longest substring with at most k..."): that is **Sliding Window** (earlier topic)'],
        ['the answer is a fixed transformation of the input (reverse, shift, add, wrap)', 'it matches **brackets or nested structure**: Stack (earlier topic), or Recursion (next topic)'],
        ['you can state a key that is equal for "equivalent" strings and group by it', 'you count or group **anagrams** or check "same characters": Hashing (earlier topic)'],
        ['a palindrome or a centre is the natural frame', 'it asks for the **best subsequence** or an **edit distance** between two strings: Dynamic Programming (later)'],
        ['you search one needle in one haystack', 'you search **many words** or by prefix: a Trie (later); a **path between words**: Graph BFS (later); **all arrangements**: Backtracking (later)']])
    h += H3('Where you already meet it')
    h += UL(['**URL and path normalisation** (`../`, `//`) in every web server and file manager.',
             '**Version comparison** ("1.10" vs "1.9") in package managers, app stores and `sort -V`.',
             '**Number parsing**: `Integer.parseInt`, `int()`, CSV and JSON readers; **big-number arithmetic** in cryptography libraries.',
             '**Text wrapping and justification** in terminals, word processors and email clients.',
             '**Substring search**: `grep`, Ctrl+F, `str.find`, database `LIKE`. The two-way and KMP families sit behind them.'])
    h += H3('Interview weight for your targets (honest version)')
    h += table(['Source', 'What it says', 'How much to trust it'], [
        ['Tech Interview Handbook cheatsheet (local research, 2026-10-11)', 'String is rated **High** priority', 'Third-party, general; not company-specific'],
        ['Amazon candidate-report table (~500 questions, local research 2026-10-11)', 'String about 27% of questions, second to Array', 'Crowd-sourced, method unclear'],
        ['Meta reports (2026, local research)', 'Coding rounds lean on parsing, palindromes, calculators, anagrams; the top String items by tag score are Minimum Remove to Make Valid Parentheses, Valid Word Abbreviation, Valid Palindrome II, Basic Calculator II, Simplify Path', 'Company-tag scores from an unofficial repo; scores are normalised per company, so they cannot be compared across companies'],
        ['Grind 75 Strings section (fetched 2026-10-13) and a community copy of the Blind 75 String section (fetched 2026-10-14)', 'Grind 75: eight string problems, two of them pure-string (atoi, Longest Palindromic Substring). Blind 75: ten, including Longest Palindromic Substring, Palindromic Substrings and Encode and Decode Strings', 'Curated lists, not company data; the Blind 75 page is a third-party copy'],
        ['Anthropic, OpenAI, Stripe (practical build style)', 'Strings appear inside the task (log and config parsing, tokenising, formatting) rather than as a named puzzle', 'Inferred from the build-style reports in `research/dsa-company-interview-calibration-2026.md`; anecdotal']])
    h += P('**What it unlocks.** The cursor-and-state habit feeds **Recursion** (the next topic: parsing nested text, generating strings), **Trees** (serialisation), **Tries** (prefix problems), **Dynamic Programming** (edit distance, longest common subsequence) and the **Practical Build** track (parsers and formatters).')
    h += H3('How it relates to the topics before it')
    h += table(['Earlier topic', 'What carries over', 'Where it shows up here'], [
        ['Arrays', 'Index arithmetic, the read/write cursor, in-place rewriting', 'String Compression, Reverse Words in place'],
        ['Hashing', 'Counts and canonical keys', 'First Unique, Custom Sort, Group Shifted'],
        ['Two Pointers', 'Converging cursors, merging two sequences', 'Valid Word Abbreviation, Compare Version, Longest Common Prefix'],
        ['Sliding Window', 'A growing/shrinking range with a state', 'KMP\'s `k` and the expansion around a centre are the same "extend while valid" idea'],
        ['Stack and Queue', 'Nested structure and brackets', 'Deferred: Decode String, Basic Calculator and Simplify Path were solved there'],
        ['Binary Search', 'Stating a predicate and an invariant before the loop', 'The same discipline: write the one-sentence invariant first']])
    h += H3('Revisit block (earlier topics, no solutions here)')
    h += P('Five problems from earlier topics to re-solve before you start. Do each from a blank page, with a timer, and check against the original notes only afterwards.')
    h += table(['Problem', 'From', 'Why now'], [
        ['Valid Palindrome (125)', 'Two Pointers', 'The converging-cursor palindrome check; compare with the centre expansion in Type B'],
        ['Valid Palindrome II (680)', 'Two Pointers (Part 14)', 'Most-reported Meta string problem in the data; one allowed deletion'],
        ['Valid Anagram (242)', 'Hashing', 'The count table behind Types D and the anagram look-alikes'],
        ['Longest Substring Without Repeating Characters (3)', 'Sliding Window', 'The window problem that is most often confused with a string problem'],
        ['Valid Parentheses (20)', 'Stack', 'The bracket problem that tells you when a string needs a stack, not a counter']])
    return h

def part2():
    h = '<h2 id="part-2"><span class="part-no">Part 2</span>Language Toolkit (Python and Java)</h2>'
    h += P('Everything in the table below is a tool you will use in Parts 7 and 11. Costs are for a string of length n; k is the length of a slice or a second string. Examples in this part were **executed** when this page was built and the printed output matches what you see (<a class="xref" href="#appendix-b">Appendix B</a>).')
    h += H3('Operations and their real cost')
    h += table(['Operation', 'Python', 'Java', 'Cost', 'Trap'], [
        ['length', '`len(s)`', '`s.length()`', 'O(1)', 'Java `length()` counts UTF-16 units, Python `len` counts code points'],
        ['read a character', '`s[i]`, `s[-1]`', '`s.charAt(i)`', 'O(1)', 'Python `s[i]` is a 1-character **string**; Java `charAt` is a `char` (a number)'],
        ['slice / substring', '`s[a:b]`', '`s.substring(a, b)`', 'O(b - a) (a copy)', 'Inside a loop, `s = s[1:]` is O(n²). Measured: Python 100,000 chars 0.953 s; Java `substring(1)` loop on 200,000 chars 1.598 s versus 0.0015 s with an index (Part 3)'],
        ['concatenate once', '`s + t`', '`s + t`, `s.concat(t)`', 'O(n + k)', 'Fine once; see next row for loops'],
        ['concatenate in a loop', '`s += c`', '`s += c`', 'O(n²) in general', 'Java: measured 0.71 s for 100,000 appends vs 0.002 s with `StringBuilder`. CPython has an in-place shortcut that makes it fast **sometimes**; do not rely on it'],
        ['build from pieces', '`"".join(list)`', '`StringBuilder.append`, `String.join`', 'O(total) (append is amortised O(1))', 'Collect pieces, join once at the end'],
        ['compare', '`s == t`, `s < t`', '`s.equals(t)`, `s.compareTo(t)`', 'O(min length) worst case', 'Java: `==` compares **references**, not text'],
        ['search', '`t in s`, `s.find(t)`, `s.index(t)`', '`s.indexOf(t)`, `s.contains(t)`', 'O(n·m) worst case in general', 'Measured on the worst case (`"a"*50000+"b"` in `"a"*100000`): Java `indexOf` 0.52 s, CPython 3.11 `in` 0.5 ms (it uses a smarter algorithm). In an interview state O(n·m) for the naive search and say CPython does better. `find` returns -1, `index` raises `ValueError`'],
        ['count occurrences', '`s.count(t)`', 'no built-in', 'O(n·m) naive (CPython is faster in practice)', 'Counts **non-overlapping** matches: `"aaa".count("aa")` is 1'],
        ['split / join', '`s.split()`, `s.split(sep)`, `sep.join(parts)`', '`s.split(regex)`, `String.join(sep, parts)`', 'O(n)', 'Python `split()` drops empty strings, `split(" ")` keeps them. Java `split` takes a **regex** and drops trailing empties'],
        ['trim, case', '`strip()`, `lower()`', '`trim()`, `toLowerCase()`', 'O(n)', 'Both return new strings; the original is unchanged'],
        ['char <-> number', '`ord(c)`, `chr(n)`', '`c - \'a\'`, `(char) (\'a\' + 2)`', 'O(1)', 'Java: `\'a\' + 1` is an `int` (98), not `\'b\'`'],
        ['char tests', '`c.isdigit()`, `c.isalpha()`, `c.isalnum()`', '`Character.isDigit(c)`, `isLetter`, `isLetterOrDigit`', 'O(1)', 'Both accept non-ASCII digits (Part 10). For ASCII digits use `"0" <= c <= "9"`'],
        ['to a number', '`int(s)`', '`Integer.parseInt(s)`', 'O(n)', 'Python: more than 4300 digits raises `ValueError` (3.11+). Java: throws `NumberFormatException` on bad input and on overflow'],
        ['reverse', '`s[::-1]`, `reversed(s)`', '`new StringBuilder(s).reverse()`', 'O(n)', '`reversed(s)` is an iterator, not a string'],
        ['sort letters', '`"".join(sorted(s))`', '`char[] c = s.toCharArray(); Arrays.sort(c)`', 'O(n log n)', 'Sorted letters are an anagram key'],
        ['count letters', '`Counter(s)` or `[0] * 26`', '`int[26]` with `c - \'a\'`', 'O(n)', 'Only valid if the alphabet is lowercase letters; ask'],
        ['mutable copy', '`list(s)`, then `"".join(chars)`', '`s.toCharArray()`, `new String(chars)`', 'O(n)', 'The copy is yours to edit; the original string is untouched'],
        ['StringBuilder edits', '(list `append`, `insert`, `pop`)', '`append`, `insert(0, x)`, `setCharAt`, `deleteCharAt`', 'append O(1); insert/delete O(n)', '`sb.insert(0, c)` in a loop is O(n²): measured 0.064 s vs 0.0009 s for 100,000 `append`s (70 times slower, and the gap grows with n). Append, then `reverse()` once']])
    h += H3('Runnable examples (Python)')
    for title, code, out in PY_EX:
        h += H5(title)
        h += f'<div class="code only-py"><div class="code-bar"><div class="lang-tabs"><button type="button" class="lang-tab" data-l="py">Python</button><button type="button" class="lang-tab" data-l="java">Java</button></div><button type="button" class="copy">Copy</button></div><pre class="pane" data-l="py">{hl(code, PYL)}</pre><pre class="pane" data-l="java">{esc("// see the Java block at the end of this part")}</pre></div>'
        h += f'<pre class="diagram">{esc("output:")}\n{esc(out)}</pre>'
    h += H3('Runnable examples (Java, one program)')
    h += f'<div class="code only-java"><div class="code-bar"><div class="lang-tabs"><button type="button" class="lang-tab" data-l="py">Python</button><button type="button" class="lang-tab" data-l="java">Java</button></div><button type="button" class="copy">Copy</button></div><pre class="pane" data-l="py">{esc("# switch to Java to see the program")}</pre><pre class="pane" data-l="java">{hl(JAVA_EX, JAL)}</pre></div>'
    h += f'<pre class="diagram">{esc("output:")}\n{esc(JAVA_EXPECT)}</pre>'
    h += H3('Common interview tricks')
    h += UL(['**Frequency array for lowercase letters:** `count[ord(c) - ord("a")] += 1` (Python), `count[c - \'a\']++` (Java). Ask whether the alphabet is lowercase-only; if not, use a dict / `HashMap`.',
             '**Collect, then join:** build a list of pieces (or a `StringBuilder`) and join once. Never grow a string with `+=` in a loop in Java.',
             '**Convert to a mutable array when the problem says "in place":** `char[]` in Java; in Python the input is already a list for those problems (String Compression, Reverse String).',
             '**Digits to a value:** `ord(c) - ord("0")` / `c - \'0\'`. Never trust `isdigit()` alone if the input could be non-ASCII.',
             '**Two answers per index:** odd and even centres for palindromes; "include the carry" for the last digit; "before and after the sign" for parsers.',
             '**Sentinels:** returning `""`, `0` or `-1` for "no answer" is part of the problem statement; ask which one.'])
    return h

def part3():
    h = '<h2 id="part-3"><span class="part-no">Part 3</span>Complexity</h2>'
    h += P('Two letters cover almost everything here: **n** is the length of the string, and **L** is the length of one string when you have a list of N strings (so the total size is N·L). Costs that look free (a slice, a concatenation, a hash-map key) are not, and that is where most string complexity mistakes come from.')
    h += H3('Complexity table to memorise')
    h += table(['Task', 'Time', 'Space', 'Why'], [
        ['One pass with cursors (parse, merge, compare)', 'O(n)', 'O(1)', 'Each cursor only moves forward; each character is looked at a constant number of times'],
        ['Count characters', 'O(n)', 'O(k) (k distinct; 26 for lowercase)', 'One increment per character'],
        ['Palindromic substring by centres', 'O(n²)', 'O(1)', '2n - 1 centres, each expands up to n/2 steps, and nothing is shared between centres'],
        ['Palindromic substring, every substring', 'O(n³)', 'O(n)', 'n² substrings, O(n) check and copy each'],
        ['Substring search, brute force', 'O(n·m)', 'O(1)', 'n - m + 1 starts, up to m comparisons each'],
        ['Substring search, KMP', 'O(n + m)', 'O(m)', 'The matched-length `k` rises at most n times, so it falls at most n times'],
        ['Group N strings by a key of length L', 'O(N·L)', 'O(N·L)', 'The key is built in O(L) and hashing it is O(L)'],
        ['Group N strings by sorted letters', 'O(N·L log L)', 'O(N·L)', 'A sort per string'],
        ['Add two numbers of n and m digits', 'O(max(n, m))', 'O(max(n, m))', 'One column per digit, one carry'],
        ['Multiply two numbers of n and m digits', 'O(n·m)', 'O(n + m)', 'Every digit pair is visited once'],
        ['Build output with a list / StringBuilder', 'O(total output)', 'O(total output)', 'Append is amortised O(1)'],
        ['Build output with `s += x` in a loop', 'O(n²) worst case', 'O(n)', 'Each `+=` copies the whole string so far']])
    h += H3('Why these are what they are')
    h += UL(['**A slice is a copy.** `s[a:b]` costs O(b - a). `s = s[1:]` inside `while s:` therefore costs n + (n-1) + ... = O(n²). Measured on this machine: 100,000 characters took 0.953 s with slicing and 0.002 s with an index loop (<a class="xref" href="#appendix-b">Appendix B</a>). Move an index instead of cutting the string.',
             '**Comparing strings costs their length.** `s == t` stops at the first difference, but a worst case is O(n). A list of N strings of length L sorted with comparisons costs O(N log N · L), not O(N log N).',
             '**A string used as a dictionary key costs O(L) to hash** (and O(L) to compare when buckets collide). "O(1) lookup" for a string key really means O(L). CPython and Java both cache the hash of a string after the first computation, so asking again is cheap (measured below: 0.768 ms then 0.0006 ms in Python).',
             '**Immutable means copy.** Every "edit" of a Python or Java string copies it. One edit is fine; an edit inside a loop is quadratic. Use a list or `StringBuilder`.'])
    h += H3('The amortised arguments you should be able to say aloud')
    h += table(['Code that looks worse than it is', 'Argument', 'Real cost'], [
        ['Reverse Words: a `while` inside a `while` (skip spaces, then scan a word)', 'Both inner loops move the same cursor `i` left and never move it back. The total number of moves is at most n.', 'O(n)'],
        ['atoi: three loops one after another', 'They are sequential, not nested: each advances the same index once.', 'O(n)'],
        ['KMP: a `while k` fall-back inside a `for i` loop', '`k` increases by at most 1 per character, so across the whole scan it increases at most n times. Each fall-back decreases `k`, and `k` never goes below 0, so the total number of fall-backs is at most n.', 'O(n + m) (precompute m, scan n)'],
        ['String Compression: a `for` over the digits of the count inside the loop', 'A count has about log10(run) digits, and the sum over runs is at most the number of characters written, which is at most n.', 'O(n)'],
        ['`StringBuilder.append` in a loop', 'The internal array doubles when full; the copying cost of all doublings sums to less than 2n.', 'O(n) total, O(1) amortised per append']])
    h += callout('warn', 'Not everything is amortised',
        '<p>Expanding around centres is <strong>truly</strong> O(n²): on `"aaaa...a"` every centre expands almost to the ends, and no work is shared between centres. Do not argue it down to O(n) in an interview; say O(n²) time and O(1) space, mention Manacher\'s O(n) as an option, and move on. The brute-force substring search is also truly O(n·m), which is exactly why KMP exists.</p>')
    h += H3('Measured costs (this machine, see Appendix B)')
    h += table(['Experiment', 'Result'], [
        ['Python `s = s[1:]` loop, 100,000 characters', '0.953 s (index loop: 0.002 s)'],
        ['Python `s += "x"` 200,000 times, nothing else holds `s`', '0.009 s (CPython shortcut; list + join: 0.004 s)'],
        ['Python `s += "x"` 50,000 times while another list holds each intermediate string', '0.870 s (the shortcut is defeated, cost is quadratic)'],
        ['Java `s += "x"` 100,000 times vs `StringBuilder`', '0.712 s vs 0.002 s'],
        ['Java `s = s.substring(1)` loop, 200,000 characters', '1.598 s (index loop: 0.0015 s)'],
        ['Python slice cost grows with its length: 2000 slices `s[1:]` of a 1,000,000 and a 4,000,000 character string', '0.511 s and 3.340 s'],
        ['Hash of a 5,000,000-character string, first call then second call', 'Python 0.768 ms then 0.0006 ms; Java 2.999 ms then 0.0005 ms (the hash is cached after the first call)'],
        ['`insert(0, x)` 100,000 times versus `append`', 'Python list 0.894 s vs 0.002 s; Java `StringBuilder` 0.064 s vs 0.0009 s'],
        ['Worst-case substring search, `"a"*50000+"b"` in `"a"*100000`', 'Java `indexOf` 0.517 s; CPython `in` 0.0005 s'],
        ['strStr worst case: haystack `"a"*10000`, needle `"a"*4999 + "b"`', 'brute force 25,005,000 character comparisons; KMP 24,998']])
    return h
