import io, contextlib, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import *
import c_prob, c_text1, c_text2, c_text3, c_text4, toolkit
from c_prob import BY

DSA = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(DSA, 'Strings_Notes_v1.html')

# ---- 1. run the Part 2 toolkit examples and the hand traces; stop if the text and the output differ
for title, code, expected in toolkit.PY_EX:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): exec(code, {})
    assert buf.getvalue().strip() == expected, (title, buf.getvalue())
JB = os.path.join(os.environ.get('JAVA_HOME', r'C:\Program Files\Java\jdk-27'), 'bin')
os.makedirs(os.path.join(HERE, 'tk'), exist_ok=True)
open(os.path.join(HERE, 'tk', 'Tk.java'), 'w', encoding='utf8').write(toolkit.JAVA_EX)
subprocess.run([JB + r'\javac.exe', '-encoding', 'UTF-8', '-d', os.path.join(HERE, 'tk'), os.path.join(HERE, 'tk', 'Tk.java')], check=True)
r = subprocess.run([JB + r'\java.exe', '-cp', os.path.join(HERE, 'tk'), 'Tk'], capture_output=True, text=True, encoding='utf8')
assert r.stdout.strip() == toolkit.JAVA_EXPECT, r.stdout
ns = {}
exec(BY['strstr']['py_opt'][0], ns); assert ns['str_str']('abababc', 'ababc') == 2 and ns['str_str']('abababc', 'ababd') == -1
exec(BY['lcp']['py_opt'][0], ns); assert ns['longest_common_prefix'](['flower', 'flow', 'flight']) == 'fl'
exec(BY['lps']['py_opt'][0], ns); assert ns['longest_palindrome']('abba') == 'abba'
exec(BY['atoi']['py_opt'][0], ns); assert ns['my_atoi']('  -42x') == -42 and ns['my_atoi']('2147483648') == 2147483647
exec(BY['addstr']['py_opt'][0], ns); assert ns['add_strings']('99', '1') == '100'
exec(BY['compress']['py_opt'][0], ns); c = list('aabbb'); n = ns['compress'](c); assert n == 4 and ''.join(c[:n]) == 'a2b3'
exec(BY['vwa']['py_opt'][0], ns); assert ns['valid_abbr']('hello', 'h3o') is True
exec(BY['firstuniq']['py_opt'][0], ns); assert ns['first_uniq']('aabc') == 2
exec(BY['mulstr']['py_opt'][0], ns); assert ns['multiply']('123', '456') == '56088'
exec(BY['zigzag']['py_opt'][0], ns); assert ns['zigzag']('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
exec(BY['shifted']['py_opt'][0], ns)
g = ns['group_shifted'](["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
assert sorted(map(sorted, g)) == sorted(map(sorted, [["abc", "bcd", "xyz"], ["acef"], ["az", "ba"], ["a", "z"]]))
exec(BY['customsort']['py_opt'][0], ns); assert ns['custom_sort']('cba', 'abcd') == 'cbad'
exec(BY['revwords']['py_opt'][0], ns); assert ns['reverse_words']('  the sky  is blue ') == 'blue is sky the'
exec(BY['roman']['py_opt'][0], ns); assert ns['roman_to_int']('MCMXCIV') == 1994
print('toolkit, traces and problem examples verified')

# ---- 2. results from the test harness and the claims scripts
py_results = json.load(open(os.path.join(HERE, 'py_results.json')))
java_lines = {}
for line in open(os.path.join(HERE, 'java_results.txt'), encoding='utf8'):
    m = re.match(r'JAVA (\w+):(\w+) pass=(\d+)', line)
    if m: java_lines[(m.group(1), m.group(2))] = int(m.group(3))
assert not any(l.startswith('JAVAFAIL') for l in open(os.path.join(HERE, 'java_results.txt'), encoding='utf8'))
for k, r in py_results.items():
    for role, cnt in r['py'].items():
        assert cnt == r['n'], (k, role)
        assert java_lines[(k, role)] == r['n'], (k, role)
claims_py = open(os.path.join(HERE, 'claims_py.txt'), encoding='utf8').read()
claims_java = open(os.path.join(HERE, 'claims_java.txt'), encoding='utf8').read()
claims2_py = open(os.path.join(HERE, 'claims2_py.txt'), encoding='utf8').read()
claims2_java = open(os.path.join(HERE, 'claims2_java.txt'), encoding='utf8').read()

# ---- 3. comparison with sibling notes (regex counts on the files as they are now)
def stats(fn):
    t = open(os.path.join(DSA, fn), encoding='utf8').read()
    return [len(re.findall(r'class="card problem"', t)), len(re.findall(r'class="card pattern"', t)), len(re.findall(r'type="checkbox" id="chk-', t)), round(os.path.getsize(os.path.join(DSA, fn)) / 1024)]
sib = {'Binary Search': 'Binary_Search_Notes_v1.html', 'Queue and Deque': 'Queue_Notes_v1.html', 'Stack': 'Stack-Mastery-Notes_v2.html', 'Hashing': 'Hashing_Notes_v1.html'}
rows = []
mine_prev = [14, 7, 36, None]
for name, fn in sib.items():
    s = stats(fn); rows.append([name] + [str(x) for x in s])
views_path = os.path.join(HERE, 'views.html')
views = open(views_path, encoding='utf8').read() if os.path.exists(views_path) else '<p>(views not yet checked)</p>'
size_path = OUT
cmp_rows = rows

# ---- 4. page
cl = Checklist()
p13 = c_text3.part13(cl)
n_chk = cl.n
parts = [c_text1.part1(), c_text1.part2(), c_text1.part3(), c_text2.part4(), c_text2.part5(), c_text2.part6(), c_text3.part7(), c_text3.part8(),
         c_text3.part9(), c_text3.part10(), c_text3.part11(), c_text3.part12(), p13, c_text4.part14(), c_text4.part15()]

def compare_html(my_kb):
    t = table(['Notes', 'Solved problems', 'Pattern cards', 'Checklist items', 'File size (KB)'],
              [['**Strings (this page)**', '14', '7', str(n_chk), str(my_kb)]] + cmp_rows)
    return t + P('Counts are regex counts on the files as they are now (not a quality measure). There were no earlier Strings notes to compare content with; the sibling pages are the depth reference. This page has fewer pattern cards than Binary Search because the string types overlap more with earlier topics, and its problems are more varied (parsing, arithmetic, layout) than the one-predicate shape of binary search. Part 7 here rests on a weaker evidence base than Binary Search (one dataset, see Appendix C).')

NAV = [('tab-p1', '1 First Principles'), ('tab-p2', '2 Toolkit'), ('tab-p3', '3 Complexity'), ('tab-p4', '4 Patterns'), ('tab-p5', '5 Recognition'),
       ('tab-p6', '6 Brute to Optimal'), ('tab-p7', '7 Problems'), ('tab-p8', '8 Method'), ('tab-p9', '9 Edge Cases'), ('tab-p10', '10 Mistakes'),
       ('tab-p11', '11 Templates'), ('tab-p12', '12 Mental Model'), ('tab-p13', '13 Checklist'), ('tab-p14', '14 Practice'), ('tab-p15', '15 Build Track'), ('tab-appx', 'Appendices')]

def build(my_kb):
    appx = c_text4.appendix(py_results, java_lines, claims_py, claims_java, claims2_py, claims2_java, {'compare': compare_html(my_kb), 'views': views})
    nav = ''.join(f'<button type="button" class="nav-tab{" active" if i == 0 else ""}" data-tab="{t}">{l}</button>' for i, (t, l) in enumerate(NAV))
    hero = ('<div class="hero"><div class="hero-tag">DSA Mastery Series &middot; Topic 7</div><h1>Strings</h1>'
            '<p>A string is an array of characters you cannot edit in place, and the questions asked about it are different: parse it, compare or normalise it, rebuild it, or find a smaller string inside it. Nearly all of them are one pass with a couple of cursors and a small state, which turns re-scanning and re-copying (O(n&sup2;) or O(n&sup3;)) into O(n). The skill that matters is saying what the characters you have already passed have turned into.</p>'
            '<div class="hero-meta"><div class="hero-badge">Prev: <span><a href="Binary_Search_Notes_v1.html">Binary Search</a></span></div><div class="hero-badge">Next: <span>Recursion</span></div>'
            '<div class="hero-badge">Patterns: <span>7 types (A to G)</span></div><div class="hero-badge">Problems: <span>14 solved + 6 practice</span></div><div class="hero-badge">Code: <span>Python and Java</span></div></div></div>'
            '<p class="hero-note">Built from <code class="nw">dsa_prompt.md</code> Parts 1 to 15. There were no earlier Strings notes. Every solution (brute force and optimal, Python and Java) was run against each other on thousands of random, constraint-respecting inputs, and every claim about a bug or a cost was reproduced with a failing input or a measurement. Results are in Appendix B. Problem choice is based on research retrieved 2026-10-13 (Appendix C); the evidence is thinner than for earlier topics. Pick a language once in the top bar and every code block follows.</p>')
    body = ''
    for i, (tid, _) in enumerate(NAV):
        content = (hero if i == 0 else '') + (parts[i] if i < 15 else appx)
        hid = '' if i == 0 else ' hidden'
        body += f'<section class="section" id="{tid}"{hid}><div class="page-wrap">\n{content}\n</div></section>\n'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Strings Notes (v1, from dsa_prompt.md)</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="assets/dsa.css">
</head>
<body data-key="strings-v1">
<header class="masthead" id="masthead">
  <div class="topbar">
    <div class="topbar-title"><b>Strings</b> &middot; DSA Mastery Notes</div>
    <div class="seg" role="group" aria-label="Code language">
      <button type="button" class="lang-global" data-l="py" id="lang-py">Python</button>
      <button type="button" class="lang-global" data-l="java" id="lang-java">Java</button>
    </div>
    <button type="button" class="theme-btn" id="theme-btn">Theme</button>
  </div>
  <nav class="nav-tabs" id="nav" aria-label="Sections">
    {nav}
  </nav>
</header>

<main>
{body}</main>
<script src="assets/dsa.js"></script>
</body>
</html>
'''

html_text = build(0)
kb = round(len(html_text.encode('utf8')) / 1024)
html_text = build(kb)
kb2 = round(len(html_text.encode('utf8')) / 1024)
if kb2 != kb: html_text = build(kb2)
open(OUT, 'w', encoding='utf8', newline='\n').write(html_text)
print('written', OUT, len(html_text.encode('utf8')) // 1024, 'KB; checklist items', n_chk)
