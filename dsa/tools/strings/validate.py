import sys, re, collections
from html.parser import HTMLParser
path = sys.argv[1]
src = open(path, encoding='utf8').read()
VOID = {'meta','link','br','hr','img','input'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack=[]; s.ids=collections.Counter(); s.hrefs=[]; s.tabs=[]; s.errors=[]; s.checks=0
    def handle_starttag(s, tag, attrs):
        a = dict(attrs)
        if 'id' in a: s.ids[a['id']] += 1
        if tag == 'a' and a.get('href','').startswith('#'): s.hrefs.append(a['href'][1:])
        if tag == 'button' and 'data-tab' in a: s.tabs.append(a['data-tab'])
        if tag == 'input' and a.get('type') == 'checkbox' and str(a.get('id','')).startswith('chk-'): s.checks += 1
        if tag not in VOID: s.stack.append((tag, s.getpos()))
    def handle_endtag(s, tag):
        if tag in VOID: return
        if not s.stack or s.stack[-1][0] != tag:
            s.errors.append(f'mismatch </{tag}> at {s.getpos()} stack top {s.stack[-1] if s.stack else None}')
            # try to recover
            for i in range(len(s.stack)-1, -1, -1):
                if s.stack[i][0] == tag: del s.stack[i:]; break
        else: s.stack.pop()
p = P(); p.feed(src)
print('unclosed:', p.stack[:5]); print('errors:', p.errors[:5])
print('duplicate ids:', [k for k,v in p.ids.items() if v>1])
print('broken # links:', sorted({h for h in p.hrefs if h and h not in p.ids}))
secs = re.findall(r'<section class="section" id="([^"]+)"', src)
print('tabs without section:', [t for t in p.tabs if t not in secs], '| sections without tab:', [s for s in secs if s not in p.tabs])
print('sections', len(secs), 'tabs', len(p.tabs), 'checkboxes', p.checks, 'problem cards', len(re.findall(r'class="card problem"', src)), 'pattern cards', len(re.findall(r'class="card pattern"', src)))
print('details open/close', src.count('<details'), src.count('</details>'))
print('unconverted markup:', re.findall(r'\[\[[^\]]*\]\]|\*\*[^*<]{1,30}\*\*', src)[:5])
