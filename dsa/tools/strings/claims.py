import time, sys
out = []
def say(*a): out.append(' '.join(str(x) for x in a)); print(out[-1])

say("C1 split(' ') keeps empty strings:", repr(' '.join(reversed("a  b".split(' ')))), "(correct: 'b a')")
# C3 vwa without zero check
def vwa_bad(word, abbr):
    i = j = 0
    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            num = 0
            while j < len(abbr) and abbr[j].isdigit(): num = num*10+int(abbr[j]); j += 1
            i += num
        else:
            if word[i] != abbr[j]: return False
            i += 1; j += 1
    return i == len(word) and j == len(abbr)
say("C3 abbr without zero check: vwa_bad('a','01') =", vwa_bad('a','01'), "(correct: False)")
# C4 add strings drop carry
def add_bad(a, b):
    i, j, carry, out_ = len(a)-1, len(b)-1, 0, []
    while i >= 0 or j >= 0:
        t = carry + (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0)
        i -= 1; j -= 1
        out_.append(str(t % 10)); carry = t // 10
    return ''.join(reversed(out_))
say("C4 add without final carry: add_bad('99','1') =", add_bad('99','1'), "(correct: '100')")
# C5 multiply no strip
def mul_bad(a, b):
    res = [0]*(len(a)+len(b))
    for i in range(len(a)-1,-1,-1):
        for j in range(len(b)-1,-1,-1):
            p = int(a[i])*int(b[j]) + res[i+j+1]
            res[i+j+1] = p % 10; res[i+j] += p//10
    return ''.join(map(str,res))
say("C5 multiply without stripping zeros: mul_bad('2','3') =", mul_bad('2','3'), "(correct: '6')")
# C6 shifted without mod
def key_bad(s): return tuple(ord(c)-ord(s[0]) for c in s)
def key_ok(s): return tuple((ord(c)-ord(s[0]))%26 for c in s)
say("C6 shift key without %26: 'az' vs 'ba' keys equal?", key_bad('az')==key_bad('ba'), key_bad('az'), key_bad('ba'), "| with %26:", key_ok('az')==key_ok('ba'))
# C7 compress writing str(run) as one slot
def comp_bad(chars):
    w = r = 0
    while r < len(chars):
        ch = chars[r]; s = r
        while r < len(chars) and chars[r] == ch: r += 1
        chars[w] = ch; w += 1
        if r - s > 1: chars[w] = str(r - s); w += 1     # one slot for a multi-digit count
    return w
say("C7 compress count in one slot: comp_bad(list('a'*12)) =", comp_bad(list('a'*12)), "(correct: 3, i.e. 'a12')")
# C8 odd centres only
def lps_odd(s):
    best = ''
    for c in range(len(s)):
        l = r = c
        while l >= 0 and r < len(s) and s[l] == s[r]: l -= 1; r += 1
        if r-l-1 > len(best): best = s[l+1:r]
    return best
say("C8 odd centres only: lps_odd('abba') =", repr(lps_odd('abba')), "(correct: 'abba')")
# C9 isdigit
try:
    say("C9 '\u00b2'.isdigit() =", '\u00b2'.isdigit(), "; int('\u00b2') ->", end='') if False else None
    int('\u00b2')
except ValueError as e:
    say("C9 '\u00b2'.isdigit() =", '\u00b2'.isdigit(), "but int('\u00b2') raises ValueError")
# C11 timing
def t(f):
    s = time.perf_counter(); f(); return time.perf_counter() - s
N = 200000
def concat():
    s = ''
    for i in range(N): s += 'x'
def join():
    p = []
    for i in range(N): p.append('x')
    ''.join(p)
say(f"C11a Python: s += 'x' x{N}: {t(concat):.3f}s ; list+join: {t(join):.3f}s (CPython can optimise += when nothing else references s; do not rely on it)")
def concat_shared():
    s = ''; keep = []
    for i in range(N // 4):
        s += 'x'; keep.append(s)       # keeps a second reference, defeating the in-place optimisation
say(f"C11b Python: s += 'x' x{N//4} while another reference to s exists: {t(concat_shared):.3f}s")
big = 'x' * 100000
def slicing():
    s = big
    while s: s = s[1:]
def indexing():
    for i in range(len(big)): big[i]
say(f"C11c Python: `s = s[1:]` loop on 100000 chars: {t(slicing):.3f}s ; index loop: {t(indexing):.3f}s")
# C12 comparison counts
def brute_count(h, n):
    c = 0
    for i in range(len(h)-len(n)+1):
        j = 0
        while j < len(n):
            c += 1
            if h[i+j] != n[j]: break
            j += 1
    return c
def kmp_count(h, n):
    m = len(n); lps = [0]*m; k = 0; c = 0
    for i in range(1,m):
        while k and n[i] != n[k]: k = lps[k-1]; c += 1
        c += 1
        if n[i] == n[k]: k += 1
        lps[i] = k
    k = 0
    for ch in h:
        while k and ch != n[k]: k = lps[k-1]; c += 1
        c += 1
        if ch == n[k]: k += 1
        if k == m: return c
    return c
h, n = 'a'*10000, 'a'*4999 + 'b'
say("C12 worst case h='a'*10000, needle='a'*4999+'b': brute char comparisons", brute_count(h,n), "; KMP comparisons", kmp_count(h,n))
open('claims_py.txt','w',encoding='utf8').write('\n'.join(out))
