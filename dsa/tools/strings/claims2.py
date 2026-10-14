import time, sys
out = []
def say(*a): out.append(' '.join(str(x) for x in a)); print(out[-1])
def t(f):
    s = time.perf_counter(); f(); return time.perf_counter() - s
# K1 slice copies: cost grows with slice length
for n in (1_000_000, 4_000_000):
    big = 'x' * n
    say(f"K1 Python: 2000 slices of {n} chars each (s[1:]): {t(lambda: [big[1:] for _ in range(2000)]):.3f}s")
# K2 hash caching
s = ''.join(chr(97 + i % 26) for i in range(5_000_000))
t1 = t(lambda: hash(s)); t2 = t(lambda: hash(s))
say(f"K2 Python: hash of a 5,000,000-char string, first call {t1*1000:.3f} ms, second call {t2*1000:.4f} ms")
# K3 in-search worst case
h, nd = 'a' * 100000, 'a' * 50000 + 'b'
say(f"K3 Python: ('a'*50000+'b') in ('a'*100000): {t(lambda: nd in h):.4f}s (a naive search would do about 2.5e9 comparisons)")
h2, nd2 = 'a' * 100000, 'a' * 20 + 'b'
say(f"K3b Python: short needle ('a'*20+'b') in ('a'*100000): {t(lambda: nd2 in h2):.4f}s")
# K4 list.insert(0) vs append (Python analogue of StringBuilder.insert)
N = 100000
def ins():
    l = []
    for i in range(N): l.insert(0, 'x')
def app():
    l = []
    for i in range(N): l.append('x')
say(f"K4 Python list insert(0) x{N}: {t(ins):.3f}s ; append x{N}: {t(app):.3f}s")
open('claims2_py.txt', 'w', encoding='utf8').write('\n'.join(out))
