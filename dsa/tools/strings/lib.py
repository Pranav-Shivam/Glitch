import re, html
from pygments import highlight
from pygments.lexers import PythonLexer, JavaLexer
from pygments.formatters import HtmlFormatter

FMT = HtmlFormatter(nowrap=True)
PYL, JAL = PythonLexer(), JavaLexer()

def esc(s): return html.escape(s, quote=False)

def inline(t):
    """Tiny markup: `code`, **bold**, [[#id|label]] (in-page), [[https://..|label]] (external)."""
    t = esc(t)
    t = re.sub(r'&lt;a class="xref" href="(#[^"]+)"&gt;(.*?)&lt;/a&gt;', lambda m: '<a class="xref" href="' + m.group(1) + '">' + m.group(2) + '</a>', t)
    t = t.replace('&amp;nbsp;', '&nbsp;')
    t = re.sub(r'`([^`]+)`', lambda m: '<code class="nw">' + m.group(1) + '</code>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    def link(m):
        tgt, lab = m.group(1), m.group(2)
        if tgt.startswith('#'): return f'<a class="xref" href="{tgt}">{lab}</a>'
        return f'<a href="{tgt}">{lab}</a>'
    t = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', link, t)
    return t

def P(t, cls=None):
    a = f' class="{cls}"' if cls else ''
    return f'<p{a}>{inline(t)}</p>'
def H3(t, id=None):
    a = f' id="{id}"' if id else ''
    return f'<h3{a}>{inline(t)}</h3>'
def H4(t): return f'<h4>{inline(t)}</h4>'
def H5(t): return f'<h5>{inline(t)}</h5>'
def UL(items): return '<ul>' + ''.join(f'<li>{inline(i)}</li>' for i in items) + '</ul>'
def OL(items): return '<ol>' + ''.join(f'<li>{inline(i)}</li>' for i in items) + '</ol>'
def diagram(t): return f'<pre class="diagram">{esc(t)}</pre>'

def table(headers, rows, cls=None, raw_cols=()):
    h = ''.join(f'<th>{inline(x)}</th>' for x in headers)
    body = ''
    for r in rows:
        body += '<tr>' + ''.join(f'<td>{inline(c) if i not in raw_cols else c}</td>' for i, c in enumerate(r)) + '</tr>'
    c = f' class="{cls}"' if cls else ''
    return f'<div class="table-wrap"><table{c}><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table></div>'

def callout(kind, title, body):
    inner = body if body.startswith('<') else P(body)
    return f'<div class="callout {kind}"><strong>{inline(title)}</strong>{inner}</div>'

def hl(code, lex):
    return highlight(code.strip('\n'), lex, FMT).rstrip('\n')

def code_block(py, java, only=None):
    cls = ' only-' + only if only else ''
    bar = ('<div class="code-bar"><div class="lang-tabs"><button type="button" class="lang-tab" data-l="py">Python</button>'
           '<button type="button" class="lang-tab" data-l="java">Java</button></div><button type="button" class="copy">Copy</button></div>')
    return (f'<div class="code{cls}">{bar}<pre class="pane" data-l="py">{hl(py, PYL)}</pre>'
            f'<pre class="pane" data-l="java">{hl(java, JAL)}</pre></div>')

def pill(text, color=None, mono=False):
    c = 'pill ' + ('mono' if mono else color)
    return f'<span class="{c}">{esc(text)}</span>'

DIFF_COLOR = {'Easy': 'c-green', 'Medium': 'c-yellow', 'Hard': 'c-red'}

def step(n, title): return f'<h5 class="step" data-step="{n}"><span class="step-n">{n}</span>{inline(title)}</h5>'

class Checklist:
    def __init__(self): self.n = 0
    def group(self, level, question, items):
        out = f'<h5>{inline(level)}</h5>{P(question)}<ul class="checklist">'
        for it in items:
            self.n += 1
            out += f'<li><label><input type="checkbox" id="chk-{self.n}"><span>{inline(it)}</span></label></li>'
        return out + '</ul>'
