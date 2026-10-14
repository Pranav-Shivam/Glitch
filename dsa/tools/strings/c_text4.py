import json, os, re
from lib import *
from c_prob import BY, NUM, ORDER, PRACTICE, practice_card, appendix_a_card, HERE

def part14():
    h = '<h2 id="part-14"><span class="part-no">Part 14</span>Final Practice</h2>'
    h += P('No solutions here. None of these is solved in [[#part-7|Part 7]]. Verified solutions are in [[#appendix-a|Appendix A]], to be read only after an honest attempt. Try each with a timer (15 to 20 minutes for the Mediums). Two of them (Merge Strings Alternately, Palindromic Substrings) are the siblings of solved problems; Encode and Decode Strings has no sibling and tests whether you can design a format.')
    for k in PRACTICE: h += practice_card(k)
    return h

def part15():
    h = '<h2 id="part-15"><span class="part-no">Part 15</span>Practical Build Track</h2>'
    h += P('Anthropic, OpenAI, Stripe and Netflix tend to ask realistic tasks with levels that escalate. In those tasks strings are rarely the puzzle; they are the input you must parse safely and the output you must format. No solutions unless you ask. (Tries, Backtracking and Greedy have no natural exercise here; they are used in the Practical Build topic later.)')
    h += '<div class="card"><h3>Exercise 1: Access-log analyser ("which endpoints are failing?")</h3>'
    h += P('**Scenario.** A web service writes one line per request, for example `203.0.113.7 - - [13/Oct/2026:10:00:01 +0000] "GET /api/users?id=7 HTTP/1.1" 200 512 "Mozilla/5.0 (X11; Linux)"`. Operations wants answers without loading a database.')
    h += table(['Level', 'Requirement (each adds to the previous)'], [
        ['1', 'Parse a line into `ip`, `timestamp`, `method`, `path`, `status`, `bytes`, `user_agent`. The request and the user agent are in quotes and contain spaces; a quote can be escaped as `\\"`. A malformed line must be **counted and skipped**, never crash the run.'],
        ['2', 'Normalise paths (drop the query string, collapse `//`, resolve `.` and `..`) and report the top-k paths by request count and the count per status class (2xx, 4xx, 5xx).'],
        ['3', 'The input arrives in **chunks** of arbitrary size that can split a line (even inside a quoted field). Process it as a stream with bounded memory, and support a filter such as `status >= 500 and path startswith /api`.']], cls='design')
    h += P('**What this exercises.** Type C (a character-level tokenizer with a "inside quotes" state), Type D (counting by a normalised key), Type F (a carry-over buffer for the partial last line). Justify: hand-written tokenizer versus regex (a regex is shorter, but quoted fields with escapes and catastrophic backtracking are the risks) versus `split(" ")` (breaks on the first space inside quotes); `Counter` plus a heap for top-k (the heap arrives in a later topic; sorting is the first answer).')
    h += UL(['**Test:** a normal line; a user agent with spaces and a parenthesis; an escaped quote; a path with `?a=1`, `//` and `..`; an empty line; a line missing the status; a chunk boundary in the middle of a field.',
             '**Edge cases:** empty input, a single huge line, non-UTF-8 bytes, `status` not a number, `bytes` as `-`, two lines separated by `\\r\\n`, a trailing line without a newline.',
             '**Interviewer extensions (stated, not solved):** how much memory does the count table use for a million distinct paths (and what do you do about it), multi-threaded reading of several files (merging counters), a log line injection attack (a user agent that contains a newline), and timestamps in different time zones.'])
    h += '</div>'
    h += '<div class="card"><h3>Exercise 2: Template renderer ("Hi {{name}}, you have {{count}} new messages")</h3>'
    h += P('**Scenario.** A notification service renders messages from templates and a dictionary of values.')
    h += table(['Level', 'Requirement (each adds to the previous)'], [
        ['1', '`render(template, values)` replaces every `{{key}}` with `values[key]`. Decide and document what happens for an unknown key (leave it, empty string, or raise).'],
        ['2', 'Allow spaces (`{{ name }}`), defaults (`{{name|friend}}`) and an escape (`\\{{` is a literal `{{`). A value that itself contains `{{count}}` must **not** be substituted again.'],
        ['3', 'Compile the template once into tokens and reuse it for a million renders; add a maximum output size, and an option to wrap the output at a given width without breaking words (greedy, left-aligned: the easy half of Text Justification).']], cls='design')
    h += P('**What this exercises.** Type C (a one-pass tokenizer), Type E (build the output in a list, join once), Type G (finding `{{`). Justify: a single left-to-right pass versus repeated `str.replace` (which re-substitutes values that contain braces and depends on the order of keys), compiled tokens versus re-parsing, and why the output is built in a list.')
    h += UL(['**Test:** no placeholders; adjacent placeholders `{{a}}{{b}}`; an unclosed `{{`; an escaped `\\{{`; a value containing `{{b}}`; a default used and not used; Unicode values; an empty template.',
             '**Edge cases:** a template ending in `{`, `{{}}`, `{{ | x }}`, nested braces `{{{a}}}`, very long values, wrapping when a single word is longer than the width.',
             '**Interviewer extensions (stated, not solved):** is the compiled template safe to share between threads (immutable tokens: yes; a mutable cache: lock it), untrusted templates (size and depth limits), HTML escaping of values, and how the design changes if the templates are loaded from a database and change at runtime.'])
    h += '</div>'
    return h

def appendix(py_results, java_lines, claims_py, claims_java, claims2_py, claims2_java, extra):
    h = '<h2 id="appendix-a"><span class="part-no">Appendix</span>Appendix A: Practice solutions (read only after an honest attempt)</h2>'
    h += callout('warn', 'Spoilers', '<p>These are the verified solutions to the six [[#part-14|Part 14]] problems. Every one was run against a reference in both Python and Java (<a class="xref" href="#appendix-b">Appendix B</a>). Close this section until you have tried each problem with a timer.</p>'.replace('[[#part-14|Part 14]]', '<a class="xref" href="#part-14">Part 14</a>'))
    for k in PRACTICE: h += appendix_a_card(k)

    h += '<h2 id="appendix-b"><span class="part-no">Appendix</span>Appendix B: What was verified and how</h2>'
    h += H3('Brute force versus optimal, random tests')
    h += P('One source of truth: the Python and Java code in this page comes from one data file; the test harness and this page were generated from it, so the code you read is the code that ran. Each optimal solution was compared with its brute force on random, constraint-respecting inputs: valid abbreviations and mutated ones, strings over two or three letters (many palindromes and repeats), random strings of spaces, signs, digits and letters (plus a share of numbers beyond the 32-bit range) for atoi, **every** Roman numeral from 1 to 3999, numbers without leading zeros for Add Strings, Multiply Strings and Add Binary, runs of up to 101 characters for String Compression, periodic strings for strStr, word lists with `maxWidth` at least the longest word for Text Justification, and lists of strings (possibly empty lists, empty strings, commas, tabs, backslashes, `#`, `:` and an accented letter) for Encode and Decode. Python 3.11.9 and Java 27 (JDK at `C:\\Program Files\\Java\\jdk-27`). Seeds are fixed, so a run repeats. The harness ran the Java brute force **and** the Java optimal solution and compared both with the Python brute force (for the round-trip problem, the original list).')
    rows = []
    order = ORDER + PRACTICE
    for k in order:
        p = BY[k]; r = py_results[k]
        roles = [x for x in ('brute', 'opt', 'opt2') if x in r['py']]
        py_ok = ' / '.join(f"{x}: {r['py'][x]}" for x in roles)
        jv = ' / '.join(f"{x}: {java_lines[(k, x)]}" for x in roles if (k, x) in java_lines)
        rows.append([p['title'], str(r['n']), py_ok, jv])
    h += table(['Problem', 'Cases', 'Python cases passed (role: count)', 'Java cases passed (role: count)'], rows)
    h += P('For Encode and Decode Strings only the optimal solution round-trips are counted; the naive delimiter version was shown to fail on `["a#b", "c"]` (it decodes to `["a", "b", "c"]`). `opt2` is the in-place Reverse Words follow-up.')
    h += H3('Every claim about a bug or a cost, with the output that proves it')
    h += pre_block('Python, bug demonstrations and first cost measurements (claims.py)', claims_py) + pre_block('Java, bug demonstrations and first cost measurements (Claims.java)', claims_java)
    h += P('A second round measured the cost claims in Parts 2 and 3 that were first stated from general knowledge: that a slice or substring copies, that string hashes are cached, that `insert(0, x)` is slow, and what the worst-case substring search really costs.')
    h += pre_block('Python (claims2.py)', claims2_py) + pre_block('Java (Claims2.java)', claims2_java)
    h += P('**Still not measured here** (standard facts, not tested on this machine): that string comparison stops at the first difference, that `StringBuilder` growth is amortised O(1) by doubling (its speed is measured above, the doubling is not inspected), and the O(n) cost of `split`, `strip` and `lower`. The CPython `in` operator is much faster than the naive O(n·m) on the worst case tested; the page states O(n·m) for the naive search and notes the difference.')
    h += P('The timing figures are one run on the author\'s machine and vary by machine; the character-comparison counts for strStr do not. The CPython `+=` result (fast when nothing else references the string, slow otherwise) is an implementation detail and may differ in other interpreters.')
    h += H3('Runnable examples in Part 2')
    h += P('The nine Python examples and the Java program in [[#part-2|Part 2]] were executed when this page was built; the page builder compares the printed output with the text shown and stops if they differ.')
    h += H3('How this page compares with the sibling notes')
    h += extra['compare']
    h += H3('Views checked and not checked')
    h += extra['views']

    h += '<h2 id="appendix-c"><span class="part-no">Appendix</span>Appendix C: Sources and honesty notes</h2>'
    h += P('Research retrieved **2026-10-13**, saved as `research/dsa-strings-problem-frequency-20261013.md`. Earlier calibration data comes from the local cache (`research/dsa-company-interview-calibration-2026.md`, `research/dsa-roadmap-gaps-20261011.md`, 2026-10-04 and 2026-10-11).')
    h += UL(['[[https://github.com/liquidslr/leetcode-company-wise-problems|liquidslr/leetcode-company-wise-problems]]: per-company all-time CSVs (`<Company>/5. All.csv`) for Google, Meta, Amazon, Microsoft, Apple and Uber, read in full. The source of every "company-tag score" in this page. Normalised, method undocumented.',
             '[[https://github.com/Sugapriyan-P-K/blind75|Blind 75 list (community copy on GitHub)]]: a String section with ten problems (Longest Substring Without Repeating Characters, Longest Repeating Character Replacement, Minimum Window Substring, Valid Anagram, Group Anagrams, Valid Parentheses, Valid Palindrome, Longest Palindromic Substring, Palindromic Substrings, Encode and Decode Strings). Fetched 2026-10-14; a third-party copy, not the original post.',
             '[[https://crackr.dev/grind75|Grind 75]]: a Strings section with eight problems (Valid Palindrome, Valid Anagram, Longest Palindrome, Longest Substring Without Repeating Characters, String to Integer (atoi), Longest Palindromic Substring, Find All Anagrams, Minimum Window Substring). The page shows no LeetCode numbers.',
             'Tech Interview Handbook cheatsheet and an Amazon candidate-report table, as recorded in `research/dsa-roadmap-gaps-20261011.md` (secondary: a local file, not re-fetched).'])
    h += callout('warn', 'Honest limits', '<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in [
        'Only one frequency dataset (six unofficial company CSVs) backs most of the problem choices. "Frequently asked" here means "listed by several of the six companies", not "asked at your interview". Only String to Integer, Longest Palindromic Substring, Palindromic Substrings and Encode and Decode Strings are also on a curated list that was fetched (Grind 75 or the Blind 75 community copy). NeetCode 150 was not checked (its site is JS-rendered).',
        'Three problems are LeetCode Premium (Valid Word Abbreviation, Group Shifted Strings, Encode and Decode Strings). Their statements were cross-checked on 2026-10-14 against web-search summaries of mirror sites (doocs, walkccc, NeetCode, algo.monster): the rules match (no leading zeros, a number is one digit run; shifting wraps z to a; the decoder must restore the list exactly, with any characters). The LeetCode pages themselves were not read, and the mirrors differ slightly in wording, so a small detail could still differ.',
        'No source gave a mid-level (E4/L4/SDE-2) breakdown for strings, and X (Twitter) has no usable data. The claim that Anthropic, OpenAI and Stripe use strings inside build tasks is inferred from general build-style reports, not from string-specific evidence.',
        'The types A to G and the problem order are my own grouping, not an industry standard. The problems with unique-answer ambiguity (Longest Palindromic Substring, Custom Sort String, Group Shifted Strings) are tested against the deterministic rule stated in each problem (leftmost longest; unlisted letters at the end in original order; groups compared as sets).'])
        + '</ul>')
    h += H3('Master deferral list for this topic')
    h += table(['Direction', 'Problems', 'Status'], [
        ['Received from earlier topics', 'Longest Palindromic Substring (5), Reverse Words in a String (151), Merge Strings Alternately (1768)', 'Solved (5, 151) and practice (1768) in this page'],
        ['Sent to Recursion (next)', 'Integer to English Words (273)', 'Practice there'],
        ['Sent to Tries, Trees, Heaps', 'Implement Trie (208), Word Search II (212), Design Add and Search Words (211), Serialize and Deserialize Binary Tree (297), Top K Frequent Words (692)', 'Deferred, see Part 7'],
        ['Sent to Backtracking', 'Generate Parentheses (22), Letter Combinations (17), Word Search (79), Palindrome Partitioning (131), Remove Invalid Parentheses (301), Expression Add Operators (282)', 'Deferred'],
        ['Sent to Graphs', 'Word Ladder (127), Alien Dictionary (269), Accounts Merge (721), Evaluate Division (399), Open the Lock (752)', 'Deferred'],
        ['Sent to Dynamic Programming', 'Edit Distance (72), LCS (1143), Word Break (139), Decode Ways (91), Regular Expression Matching (10), Interleaving String (97)', 'Deferred'],
        ['Sent to Greedy', 'Minimum Add to Make Parentheses Valid (921) (already deferred by the Stack notes)', 'Deferred'],
        ['Sent to Practical Build (topic 19)', 'Design In-Memory File System (588), Encode and Decode TinyURL (535)', 'Deferred'],
        ['Optional', 'Valid Number (65), Rabin-Karp, Z-algorithm, Manacher', 'Optional extras']])
    return h

def pre_block(title, text):
    return H5(title) + f'<pre class="diagram">{esc(text)}</pre>'
