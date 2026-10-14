# Practice problems (Part 14, solutions in Appendix A). Same registry as probs_a.
from probs_a import add, rs, gen_num

def bin_num(r, lo=1, hi=14):
    L = r.randint(lo, hi)
    if L == 1: return r.choice('01')
    return '1' + ''.join(r.choice('01') for _ in range(L - 1))

# ------------------------------------------------------------ Merge Strings Alternately
add(key='merge', title='Merge Strings Alternately', lc=1768, diff='Easy', typ='E', n=4000, practice=True,
    gen=lambda r: [rs(r, 'abc', 1, 7), rs(r, 'xyz', 1, 7)],
    py_brute=('''def merge_alternately_brute(word1, word2):
    out = []
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            out.append(word1[i])
        if i < len(word2):
            out.append(word2[i])
    return "".join(out)''', 'merge_alternately_brute', lambda f: (f[0], f[1])),
    py_opt=('''def merge_alternately(word1, word2):
    n = min(len(word1), len(word2))
    out = [word1[i] + word2[i] for i in range(n)]       # interleave the common part
    out.append(word1[n:])                               # at most one of these two tails is non-empty
    out.append(word2[n:])
    return "".join(out)''', 'merge_alternately', lambda f: (f[0], f[1])),
    java_brute=('''static String mergeAlternatelyBrute(String w1, String w2) {
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < Math.max(w1.length(), w2.length()); i++) {
        if (i < w1.length()) out.append(w1.charAt(i));
        if (i < w2.length()) out.append(w2.charAt(i));
    }
    return out.toString();
}''', 'Notes.mergeAlternatelyBrute(a[0], a[1])'),
    java_opt=('''static String mergeAlternately(String w1, String w2) {
    int n = Math.min(w1.length(), w2.length());
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < n; i++) out.append(w1.charAt(i)).append(w2.charAt(i));
    out.append(w1, n, w1.length()).append(w2, n, w2.length());
    return out.toString();
}''', 'Notes.mergeAlternately(a[0], a[1])'))

# ------------------------------------------------------------ Add Binary
add(key='addbin', title='Add Binary', lc=67, diff='Easy', typ='D', n=4000, practice=True,
    gen=lambda r: [bin_num(r), bin_num(r)],
    py_brute=('''def add_binary_brute(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]''', 'add_binary_brute', lambda f: (f[0], f[1])),
    py_opt=('''def add_binary(a, b):
    i, j, carry = len(a) - 1, len(b) - 1, 0
    out = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        out.append(str(total % 2))
        carry = total // 2
    return "".join(reversed(out))''', 'add_binary', lambda f: (f[0], f[1])),
    java_brute=('''static String addBinaryBrute(String a, String b) {
    return new java.math.BigInteger(a, 2).add(new java.math.BigInteger(b, 2)).toString(2);
}''', 'Notes.addBinaryBrute(a[0], a[1])'),
    java_opt=('''static String addBinary(String a, String b) {
    int i = a.length() - 1, j = b.length() - 1, carry = 0;
    StringBuilder out = new StringBuilder();
    while (i >= 0 || j >= 0 || carry != 0) {
        int total = carry;
        if (i >= 0) total += a.charAt(i--) - '0';
        if (j >= 0) total += b.charAt(j--) - '0';
        out.append(total % 2);
        carry = total / 2;
    }
    return out.reverse().toString();
}''', 'Notes.addBinary(a[0], a[1])'))

# ------------------------------------------------------------ Palindromic Substrings
add(key='pals', title='Palindromic Substrings', lc=647, diff='Medium', typ='B', n=4000, practice=True,
    gen=lambda r: [rs(r, r.choice(['ab', 'abc', 'a']), 1, 14)],
    py_brute=('''def count_substrings_brute(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            t = s[i:j + 1]
            if t == t[::-1]:
                count += 1
    return count''', 'count_substrings_brute', lambda f: (f[0],)),
    py_opt=('''def count_substrings(s):
    count = 0
    for c in range(len(s)):
        for l, r in ((c, c), (c, c + 1)):       # odd centre, even centre
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1                      # every successful step is one more palindrome
                l -= 1
                r += 1
    return count''', 'count_substrings', lambda f: (f[0],)),
    java_brute=('''static int countSubstringsBrute(String s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++)
        for (int j = i; j < s.length(); j++) {
            String t = s.substring(i, j + 1);
            if (new StringBuilder(t).reverse().toString().equals(t)) count++;
        }
    return count;
}''', 'String.valueOf(Notes.countSubstringsBrute(a[0]))'),
    java_opt=('''static int countSubstrings(String s) {
    int count = 0;
    for (int c = 0; c < s.length(); c++)
        for (int parity = 0; parity < 2; parity++) {
            int l = c, r = c + parity;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                count++;
                l--;
                r++;
            }
        }
    return count;
}''', 'String.valueOf(Notes.countSubstrings(a[0]))'))

# ------------------------------------------------------------ Compare Version Numbers
def gen_ver(r):
    def v():
        segs = [str(r.randint(0, 12)) for _ in range(r.randint(1, 4))]
        segs = [('0' * r.randint(0, 2)) + x for x in segs]
        return '.'.join(segs)
    a = v()
    b = a if r.random() < .3 else v()
    if r.random() < .3: b += '.0' * r.randint(1, 2)
    return [a, b]
add(key='version', title='Compare Version Numbers', lc=165, diff='Medium', typ='B', n=6000, practice=True, gen=gen_ver,
    py_brute=('''def compare_version_brute(v1, v2):
    a = [int(x) for x in v1.split(".")]
    b = [int(x) for x in v2.split(".")]
    n = max(len(a), len(b))
    a += [0] * (n - len(a))                     # a missing revision counts as 0
    b += [0] * (n - len(b))
    for x, y in zip(a, b):
        if x != y:
            return -1 if x < y else 1
    return 0''', 'compare_version_brute', lambda f: (f[0], f[1])),
    py_opt=('''def compare_version(v1, v2):
    i = j = 0
    while i < len(v1) or j < len(v2):           # keep going while EITHER string has revisions left
        x = 0
        while i < len(v1) and v1[i] != ".":     # parse one revision of v1; stays 0 if v1 has run out
            x = x * 10 + int(v1[i])
            i += 1
        y = 0
        while j < len(v2) and v2[j] != ".":
            y = y * 10 + int(v2[j])
            j += 1
        if x != y:
            return -1 if x < y else 1
        i += 1                                  # step over the "."
        j += 1
    return 0''', 'compare_version', lambda f: (f[0], f[1])),
    java_brute=('''static int compareVersionBrute(String v1, String v2) {
    String[] a = v1.split("\\\\."), b = v2.split("\\\\.");
    int n = Math.max(a.length, b.length);
    for (int i = 0; i < n; i++) {
        int x = i < a.length ? Integer.parseInt(a[i]) : 0;
        int y = i < b.length ? Integer.parseInt(b[i]) : 0;
        if (x != y) return x < y ? -1 : 1;
    }
    return 0;
}''', 'String.valueOf(Notes.compareVersionBrute(a[0], a[1]))'),
    java_opt=('''static int compareVersion(String v1, String v2) {
    int i = 0, j = 0;
    while (i < v1.length() || j < v2.length()) {
        int x = 0, y = 0;
        while (i < v1.length() && v1.charAt(i) != '.') x = x * 10 + (v1.charAt(i++) - '0');
        while (j < v2.length() && v2.charAt(j) != '.') y = y * 10 + (v2.charAt(j++) - '0');
        if (x != y) return x < y ? -1 : 1;
        i++;
        j++;
    }
    return 0;
}''', 'String.valueOf(Notes.compareVersion(a[0], a[1]))'))

# ------------------------------------------------------------ Encode and Decode Strings (round trip)
CODEC_ALPHA = 'ab#12:5 ,' + chr(9) + chr(92) + chr(233)
def codec_enc(lst):      # test-file field: count, then each string as hex of its UTF-8 bytes
    return str(len(lst)) + ':' + ','.join(w.encode('utf8').hex() for w in lst)
def codec_dec(field):
    n, rest = field.split(':', 1)
    return [] if int(n) == 0 else [bytes.fromhex(h).decode('utf8') for h in rest.split(',')]
def gen_codec(r):
    return [codec_enc([rs(r, CODEC_ALPHA, 0, 7) for _ in range(r.randint(0, 6))])]
add(key='codec', title='Encode and Decode Strings', lc=271, diff='Medium', typ='F', n=5000, practice=True, premium=True, roundtrip=True,
    gen=gen_codec,
    py_brute=('''def encode_naive(strs):
    return "#".join(strs)                       # the tempting version: a delimiter

def decode_naive(s):
    return s.split("#")                         # breaks when a string contains "#" (or is the only empty string)''', 'codec_naive', lambda f: (codec_dec(f[0]),)),
    py_opt=('''def encode(strs):
    return "".join(str(len(s)) + "#" + s for s in strs)     # 3#abc2#xy: length first, then the text

def decode(s):
    out, i = [], 0
    while i < len(s):
        j = s.index("#", i)                     # the FIRST "#" after i ends the length, whatever the text holds
        n = int(s[i:j])
        out.append(s[j + 1:j + 1 + n])          # take exactly n characters, never scan for a delimiter
        i = j + 1 + n
    return out

def codec_roundtrip(strs):
    return decode(encode(strs))''', 'codec_roundtrip', lambda f: (codec_dec(f[0]),), codec_enc),
    java_brute=('''// naive version omitted in Java: the failure is identical (a delimiter that can appear in the data)
static String codecNaive() { return ""; }''', '""'),
    java_opt=('''static String encode(java.util.List<String> strs) {
    StringBuilder sb = new StringBuilder();
    for (String s : strs) sb.append(s.length()).append('#').append(s);
    return sb.toString();
}
static java.util.List<String> decode(String s) {
    java.util.List<String> out = new java.util.ArrayList<>();
    int i = 0;
    while (i < s.length()) {
        int j = s.indexOf('#', i);
        int n = Integer.parseInt(s.substring(i, j));
        out.add(s.substring(j + 1, j + 1 + n));
        i = j + 1 + n;
    }
    return out;
}''', 'Main.encHex(Notes.decode(Notes.encode(Main.decHex(a[0]))))'))

# ------------------------------------------------------------ Text Justification
def gen_just(r):
    words = [rs(r, 'abcde', 1, 5) for _ in range(r.randint(1, 9))]
    return [','.join(words), str(r.randint(max(len(w) for w in words), 14))]
add(key='justify', title='Text Justification', lc=68, diff='Hard', typ='F', n=5000, practice=True, gen=gen_just,
    py_brute=('''def full_justify_brute(words, max_width):
    lines, i = [], 0
    while i < len(words):
        line = [words[i]]
        used = len(words[i])
        i += 1
        while i < len(words) and used + 1 + len(words[i]) <= max_width:   # +1: one space per gap, at least
            used += 1 + len(words[i])
            line.append(words[i])
            i += 1
        last = i == len(words)
        if last or len(line) == 1:
            lines.append(" ".join(line).ljust(max_width))                 # left-justified
        else:
            gaps = [1] * (len(line) - 1)
            spare = max_width - used
            g = 0
            while spare > 0:                    # hand out spare spaces one at a time, left to right, round robin
                gaps[g % len(gaps)] += 1
                g += 1
                spare -= 1
            lines.append("".join(w + " " * k for w, k in zip(line, gaps + [0])))
    return lines''', 'full_justify_brute', lambda f: (f[0].split(','), int(f[1]))),
    py_opt=('''def full_justify(words, max_width):
    lines, i = [], 0
    while i < len(words):
        j, chars = i, 0                         # greedily pack words i..j-1; chars = letters only
        while j < len(words) and chars + len(words[j]) + (j - i) <= max_width:   # (j - i) = minimum gaps
            chars += len(words[j])
            j += 1
        line = words[i:j]
        gaps = j - i - 1
        if j == len(words) or gaps == 0:        # last line, or a single word: left-justify
            text = " ".join(line)
            lines.append(text + " " * (max_width - len(text)))
        else:
            space, extra = divmod(max_width - chars, gaps)   # every gap gets space; the first `extra` get one more
            text = ""
            for k, w in enumerate(line[:-1]):
                text += w + " " * (space + (1 if k < extra else 0))
            lines.append(text + line[-1])
        i = j
    return lines''', 'full_justify', lambda f: (f[0].split(','), int(f[1]))),
    java_brute=('''static java.util.List<String> fullJustifyBrute(String[] words, int maxWidth) {
    java.util.List<String> lines = new java.util.ArrayList<>();
    int i = 0;
    while (i < words.length) {
        java.util.List<String> line = new java.util.ArrayList<>();
        line.add(words[i]);
        int used = words[i].length();
        i++;
        while (i < words.length && used + 1 + words[i].length() <= maxWidth) {
            used += 1 + words[i].length();
            line.add(words[i]);
            i++;
        }
        StringBuilder sb = new StringBuilder();
        if (i == words.length || line.size() == 1) {
            sb.append(String.join(" ", line));
            while (sb.length() < maxWidth) sb.append(' ');
        } else {
            int[] gaps = new int[line.size() - 1];
            java.util.Arrays.fill(gaps, 1);
            for (int spare = maxWidth - used, g = 0; spare > 0; spare--, g++) gaps[g % gaps.length]++;
            for (int k = 0; k < line.size(); k++) {
                sb.append(line.get(k));
                if (k < gaps.length) for (int t = 0; t < gaps[k]; t++) sb.append(' ');
            }
        }
        lines.add(sb.toString());
    }
    return lines;
}''', 'String.join(",", Notes.fullJustifyBrute(a[0].split(",", -1), Integer.parseInt(a[1])))'),
    java_opt=('''static java.util.List<String> fullJustify(String[] words, int maxWidth) {
    java.util.List<String> lines = new java.util.ArrayList<>();
    int i = 0;
    while (i < words.length) {
        int j = i, chars = 0;
        while (j < words.length && chars + words[j].length() + (j - i) <= maxWidth) chars += words[j++].length();
        int gaps = j - i - 1;
        StringBuilder sb = new StringBuilder();
        if (j == words.length || gaps == 0) {            // last line or single word: left-justify
            for (int k = i; k < j; k++) { if (k > i) sb.append(' '); sb.append(words[k]); }
            while (sb.length() < maxWidth) sb.append(' ');
        } else {
            int space = (maxWidth - chars) / gaps, extra = (maxWidth - chars) % gaps;
            for (int k = i; k < j - 1; k++) {
                sb.append(words[k]);
                for (int t = 0; t < space + (k - i < extra ? 1 : 0); t++) sb.append(' ');
            }
            sb.append(words[j - 1]);
        }
        lines.add(sb.toString());
        i = j;
    }
    return lines;
}''', 'String.join(",", Notes.fullJustify(a[0].split(",", -1), Integer.parseInt(a[1])))'))
