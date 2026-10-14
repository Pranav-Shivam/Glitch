import random, subprocess, sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
import probs_a, probs_b
from probs_a import PROBS, fmt, canon_groups

HERE = os.path.dirname(os.path.abspath(__file__))
JAVA_BIN = os.path.join(os.environ.get("JAVA_HOME", r"C:\Program Files\Java\jdk-27"), "bin")
SEEDBASE = 20261013

def spec(p, role):
    return p.get('py_' + role)

def make_caller(p, role):
    code, fname, argfn = spec(p, role)[:3]
    extra = spec(p, role)[3] if len(spec(p, role)) > 3 else None
    ns = NS
    fn = ns[fname]
    def call(f):
        args = argfn(f)
        if extra == 'inplace':
            lst = args[0]
            n = fn(lst)
            return fmt((n, ''.join(lst[:n])))
        res = fn(*args)
        if callable(extra): return extra(res)
        return fmt(res)
    return call

NS = {}
for p in PROBS:
    for role in ('brute', 'opt', 'opt2'):
        s = spec(p, role)
        if s: exec(s[0], NS)

results = {}
lines = []
for p in PROBS:
    r = random.Random(SEEDBASE + sum(map(ord, p['key'])))
    roles = [x for x in ('brute', 'opt', 'opt2') if spec(p, x) and not (p.get('roundtrip') and x == 'brute')]
    callers = {x: make_caller(p, x) for x in roles}
    rt = p.get('roundtrip')
    cases = [p['gen'](r) for _ in range(p['n'])]
    bad = []
    pass_by_role = {x: 0 for x in roles}
    for f in cases:
        if rt:
            exp = f[0]
            check = [x for x in roles if x == 'opt']
        else:
            exp = callers['brute'](f)
            check = [x for x in roles if x != 'brute']
            pass_by_role['brute'] += 1
        for x in check:
            got = callers[x](f)
            if got == exp: pass_by_role[x] += 1
            else: bad.append((x, f, exp, got))
        lines.append('\t'.join([p['key']] + f + [exp]))
    results[p['key']] = {'n': len(cases), 'py': pass_by_role, 'bad': bad[:3]}
    print(f"PY {p['key']:11s} n={len(cases)} {pass_by_role}" + (f" FAIL {bad[:2]}" if bad else ''))

# roundtrip naive must fail on a concrete input
bad_naive = NS['decode_naive'](NS['encode_naive'](['a#b', 'c']))
print('naive codec on ["a#b","c"] ->', bad_naive)
assert bad_naive != ['a#b', 'c']

open(os.path.join(HERE, 'cases.tsv'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')

# ---- Java
notes = ['import java.util.*;', 'public class Notes {']
cases = []
for p in PROBS:
    for role in ('brute', 'opt', 'opt2'):
        if p.get('roundtrip') and role == 'brute': continue
        s = p.get('java_' + role)
        if s: notes.append(s[0]); notes.append('')
notes.append('}')
open(os.path.join(HERE, 'Notes.java'), 'w', encoding='utf8').write('\n'.join(notes))

main = ['import java.io.*; import java.util.*;', 'public class Main {',
 'static String runCompress(String s, int which) { char[] c = s.toCharArray(); int n = which == 0 ? Notes.compressBrute(c) : Notes.compress(c); return n + "," + new String(c, 0, n); }',
 'static String canon(List<List<String>> groups) { List<String> gs = new ArrayList<>(); for (List<String> g : groups) { List<String> h = new ArrayList<>(g); Collections.sort(h); gs.add(String.join(",", h)); } Collections.sort(gs); return String.join("|", gs); }',
 'static String encHex(List<String> l) { StringBuilder sb = new StringBuilder(); sb.append(l.size()).append(":"); for (int i = 0; i < l.size(); i++) { if (i > 0) sb.append(","); for (byte b : l.get(i).getBytes(java.nio.charset.StandardCharsets.UTF_8)) sb.append(String.format("%02x", b)); } return sb.toString(); }',
 'static List<String> decHex(String f) { int c = f.indexOf(":"); int n = Integer.parseInt(f.substring(0, c)); List<String> out = new ArrayList<>(); if (n == 0) return out; for (String h : f.substring(c + 1).split(",", -1)) { byte[] bs = new byte[h.length() / 2]; for (int i = 0; i < bs.length; i++) bs[i] = (byte) Integer.parseInt(h.substring(2 * i, 2 * i + 2), 16); out.add(new String(bs, java.nio.charset.StandardCharsets.UTF_8)); } return out; }',
 'static Map<String,Integer> pass = new LinkedHashMap<>(); static Map<String,String> fail = new LinkedHashMap<>();',
 'static void chk(String k, String role, String exp, String got, String[] a) { String key = k + ":" + role; if (exp.equals(got)) pass.merge(key, 1, Integer::sum); else { pass.putIfAbsent(key, 0); fail.putIfAbsent(key, Arrays.toString(a) + " exp=[" + exp + "] got=[" + got + "]"); } }',
 'public static void main(String[] args) throws Exception {',
 ' BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(args[0]), "UTF-8")); String line;',
 ' while ((line = br.readLine()) != null) { String[] t = line.split("\\t", -1); String k = t[0]; String exp = t[t.length - 1]; String[] a = Arrays.copyOfRange(t, 1, t.length - 1);',
 '  switch (k) {']
for p in PROBS:
    main.append(f'   case "{p["key"]}": {{')
    for role in ('brute', 'opt', 'opt2'):
        if p.get('roundtrip') and role == 'brute': continue
        s = p.get('java_' + role)
        if s: main.append(f'    chk(k, "{role}", exp, {s[1]}, a);')
    main.append('    break; }')
main += ['   default: throw new RuntimeException(k);', '  } }', ' for (var e : pass.entrySet()) System.out.println("JAVA " + e.getKey() + " pass=" + e.getValue());',
         ' for (var e : fail.entrySet()) System.out.println("JAVAFAIL " + e.getKey() + " " + e.getValue());', '}}']
open(os.path.join(HERE, 'Main.java'), 'w', encoding='utf8').write('\n'.join(main))

javac = os.path.join(JAVA_BIN, 'javac.exe'); java = os.path.join(JAVA_BIN, 'java.exe')
c = subprocess.run([javac, '-encoding', 'UTF-8', '-d', os.path.join(HERE, 'out'), os.path.join(HERE, 'Notes.java'), os.path.join(HERE, 'Main.java')], capture_output=True, text=True)
print('javac rc', c.returncode, c.stdout[-2000:], c.stderr[-4000:])
if c.returncode == 0:
    j = subprocess.run([java, '-cp', os.path.join(HERE, 'out'), 'Main', os.path.join(HERE, 'cases.tsv')], capture_output=True, text=True, encoding='utf8')
    print(j.stdout[-6000:], j.stderr[-2000:])
    open(os.path.join(HERE, 'java_results.txt'), 'w', encoding='utf8').write(j.stdout)
json.dump({k: {'n': v['n'], 'py': v['py']} for k, v in results.items()}, open(os.path.join(HERE, 'py_results.json'), 'w'))
