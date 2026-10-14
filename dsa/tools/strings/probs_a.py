# Problems 1-14 (solved in Part 7). One source of truth: code strings here feed both the test harness and the notes page.
import random, string

def fmt(x):
    if isinstance(x, bool): return 'true' if x else 'false'
    if isinstance(x, (list, tuple)): return ','.join(fmt(i) for i in x)
    return str(x)

def rs(r, alpha, lo, hi):
    return ''.join(r.choice(alpha) for _ in range(r.randint(lo, hi)))

PROBS = []
def add(**kw): PROBS.append(kw)

# ---------------------------------------------------------------- 1 Valid Word Abbreviation
def gen_vwa(r):
    w = rs(r, 'abc', 1, 9)
    # build an abbreviation of w, then maybe mutate it
    out, i = '', 0
    while i < len(w):
        if r.random() < 0.5:
            k = r.randint(1, len(w) - i)
            out += ('0' if r.random() < 0.08 else '') + str(k); i += k
        else:
            out += w[i]; i += 1
    if r.random() < 0.45 and out:
        p = r.randrange(len(out)); out = out[:p] + r.choice('abc0123') + out[p + 1:]
    if r.random() < 0.1: out += r.choice('12a')
    if not out: out = 'a'
    return [w, out]

add(key='vwa', title='Valid Word Abbreviation', lc=408, diff='Easy', typ='A', n=5000, gen=gen_vwa,
    py_brute=('''def valid_abbr_brute(word, abbr):
    # expand every number into that many wildcards, then compare character by character
    pattern, j = [], 0
    while j < len(abbr):
        if "0" <= abbr[j] <= "9":
            if abbr[j] == '0':
                return False                   # leading zero (also rejects a lone "0")
            k = j
            while k < len(abbr) and "0" <= abbr[k] <= "9":
                k += 1
            pattern.extend('?' * int(abbr[j:k]))
            j = k
        else:
            pattern.append(abbr[j])
            j += 1
    if len(pattern) != len(word):
        return False
    return all(p == '?' or p == c for p, c in zip(pattern, word))''', 'valid_abbr_brute', lambda f: (f[0], f[1])),
    py_opt=('''def valid_abbr(word, abbr):
    i = j = 0                                  # i walks word, j walks abbr
    while i < len(word) and j < len(abbr):
        if "0" <= abbr[j] <= "9":
            if abbr[j] == '0':
                return False                   # no leading zeros, and no zero-length skip
            num = 0
            while j < len(abbr) and "0" <= abbr[j] <= "9":
                num = num * 10 + int(abbr[j])
                j += 1
            i += num                           # skip num letters of word
        else:
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1
    return i == len(word) and j == len(abbr)   # both must end together''', 'valid_abbr', lambda f: (f[0], f[1])),
    java_brute=('''static boolean validAbbrBrute(String word, String abbr) {
    StringBuilder pattern = new StringBuilder();
    int j = 0;
    while (j < abbr.length()) {
        char c = abbr.charAt(j);
        if ((c >= '0' && c <= '9')) {
            if (c == '0') return false;                  // leading zero
            int k = j;
            long num = 0;
            while (k < abbr.length() && (abbr.charAt(k) >= '0' && abbr.charAt(k) <= '9')) {
                num = num * 10 + (abbr.charAt(k) - '0');
                k++;
            }
            if (num > word.length()) return false;       // would not fit anyway; avoids a huge pattern
            for (long t = 0; t < num; t++) pattern.append('?');
            j = k;
        } else {
            pattern.append(c);
            j++;
        }
    }
    if (pattern.length() != word.length()) return false;
    for (int i = 0; i < word.length(); i++)
        if (pattern.charAt(i) != '?' && pattern.charAt(i) != word.charAt(i)) return false;
    return true;
}''', 'String.valueOf(Notes.validAbbrBrute(a[0], a[1]))'),
    java_opt=('''static boolean validAbbr(String word, String abbr) {
    int i = 0, j = 0;                                    // i walks word, j walks abbr
    while (i < word.length() && j < abbr.length()) {
        char c = abbr.charAt(j);
        if ((c >= '0' && c <= '9')) {
            if (c == '0') return false;                  // no leading zeros
            long num = 0;                                // long: ten digits do not fit in an int
            while (j < abbr.length() && (abbr.charAt(j) >= '0' && abbr.charAt(j) <= '9')) {
                num = num * 10 + (abbr.charAt(j) - '0');
                j++;
            }
            i += num;                                    // compound assignment narrows back to int
        } else {
            if (word.charAt(i) != c) return false;
            i++;
            j++;
        }
    }
    return i == word.length() && j == abbr.length();
}''', 'String.valueOf(Notes.validAbbr(a[0], a[1]))'))

# ---------------------------------------------------------------- 2 Longest Palindromic Substring
add(key='lps', title='Longest Palindromic Substring', lc=5, diff='Medium', typ='B', n=5000,
    gen=lambda r: [rs(r, r.choice(['ab', 'abc', 'aab']), 1, 13)],
    py_brute=('''def longest_palindrome_brute(s):
    best = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            t = s[i:j + 1]
            if t == t[::-1] and len(t) > len(best):    # strict >: keep the leftmost longest
                best = t
    return best''', 'longest_palindrome_brute', lambda f: (f[0],)),
    py_opt=('''def longest_palindrome(s):
    best_l, best_r = 0, 0                       # inclusive bounds of the best palindrome so far
    for c in range(len(s)):
        for l, r in ((c, c), (c, c + 1)):       # odd centre, then even centre
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # loop stopped one step too far: palindrome is s[l+1 .. r-1]
            if (r - 1) - (l + 1) > best_r - best_l:
                best_l, best_r = l + 1, r - 1
    return s[best_l:best_r + 1]''', 'longest_palindrome', lambda f: (f[0],)),
    java_brute=('''static String longestPalindromeBrute(String s) {
    String best = "";
    for (int i = 0; i < s.length(); i++)
        for (int j = i; j < s.length(); j++) {
            String t = s.substring(i, j + 1);
            if (t.length() > best.length() && new StringBuilder(t).reverse().toString().equals(t)) best = t;
        }
    return best;
}''', 'Notes.longestPalindromeBrute(a[0])'),
    java_opt=('''static String longestPalindrome(String s) {
    int bestL = 0, bestR = 0;                            // inclusive bounds of the best palindrome so far
    for (int c = 0; c < s.length(); c++) {
        for (int parity = 0; parity < 2; parity++) {    // 0 = odd centre, 1 = even centre
            int l = c, r = c + parity;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                l--;
                r++;
            }
            if ((r - 1) - (l + 1) > bestR - bestL) {    // palindrome is s[l+1 .. r-1]
                bestL = l + 1;
                bestR = r - 1;
            }
        }
    }
    return s.substring(bestL, bestR + 1);
}''', 'Notes.longestPalindrome(a[0])'))

# ---------------------------------------------------------------- 3 atoi
def gen_atoi(r):
    if r.random() < 0.15:
        return [r.choice(['', ' ', '  ']) + r.choice(['', '+', '-']) + str(r.randint(2**30, 2**33)) + r.choice(['', 'x', ' 5'])]
    return [rs(r, ' +-0123456789a.', 0, 14)]
add(key='atoi', title='String to Integer (atoi)', lc=8, diff='Medium', typ='B', n=6000, gen=gen_atoi,
    py_brute=('''import re

def my_atoi_regex(s):
    m = re.match(r" *([+-]?)([0-9]+)", s)       # an independent reference: let a regex find the number
    if not m:
        return 0
    v = int(m.group(2)) * (-1 if m.group(1) == "-" else 1)
    return max(-2**31, min(2**31 - 1, v))''', 'my_atoi_regex', lambda f: (f[0],)),
    py_opt=('''def my_atoi(s):
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    i, n = 0, len(s)
    while i < n and s[i] == " ":                # 1. skip leading spaces
        i += 1
    sign = 1
    if i < n and s[i] in "+-":                  # 2. one optional sign
        sign = -1 if s[i] == "-" else 1
        i += 1
    result = 0
    while i < n and "0" <= s[i] <= "9":         # 3. digits, stop at the first non-digit
        d = ord(s[i]) - ord("0")
        if result > (INT_MAX - d) // 10:        # 4. result * 10 + d would pass INT_MAX: clamp now
            return INT_MAX if sign == 1 else INT_MIN
        result = result * 10 + d
        i += 1
    return sign * result''', 'my_atoi', lambda f: (f[0],)),
    java_brute=('''static int myAtoiRegex(String s) {
    java.util.regex.Matcher m = java.util.regex.Pattern.compile("^ *([+-]?)([0-9]+)").matcher(s);
    if (!m.find()) return 0;
    java.math.BigInteger v = new java.math.BigInteger(m.group(2));
    if (m.group(1).equals("-")) v = v.negate();
    if (v.compareTo(java.math.BigInteger.valueOf(Integer.MAX_VALUE)) > 0) return Integer.MAX_VALUE;
    if (v.compareTo(java.math.BigInteger.valueOf(Integer.MIN_VALUE)) < 0) return Integer.MIN_VALUE;
    return v.intValue();
}''', 'String.valueOf(Notes.myAtoiRegex(a[0]))'),
    java_opt=('''static int myAtoi(String s) {
    int i = 0, n = s.length();
    while (i < n && s.charAt(i) == ' ') i++;             // 1. skip leading spaces
    int sign = 1;
    if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {   // 2. one optional sign
        sign = s.charAt(i) == '-' ? -1 : 1;
        i++;
    }
    int result = 0;                                      // stays in int: we clamp BEFORE it can overflow
    while (i < n && s.charAt(i) >= '0' && s.charAt(i) <= '9') {  // 3. digits
        int d = s.charAt(i) - '0';
        if (result > (Integer.MAX_VALUE - d) / 10)       // 4. result * 10 + d would pass MAX_VALUE
            return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
        result = result * 10 + d;
        i++;
    }
    return sign * result;
}''', 'String.valueOf(Notes.myAtoi(a[0]))'))

# ---------------------------------------------------------------- 4 Roman to Integer
def to_roman(n):
    vals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    out = ''
    for v, s in vals:
        while n >= v: out += s; n -= v
    return out
_roman_i = [0]
def gen_roman(r):
    _roman_i[0] += 1
    return [to_roman((_roman_i[0] - 1) % 3999 + 1)]
add(key='roman', title='Roman to Integer', lc=13, diff='Easy', typ='B', n=3999, gen=gen_roman, exhaustive=True,
    py_brute=('''def roman_to_int_brute(s):
    # rewrite each subtractive pair as repeated letters, then every symbol just adds
    for pair, rep in (("IV", "IIII"), ("IX", "VIIII"), ("XL", "XXXX"),
                      ("XC", "LXXXX"), ("CD", "CCCC"), ("CM", "DCCCC")):
        s = s.replace(pair, rep)
    val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    return sum(val[c] for c in s)''', 'roman_to_int_brute', lambda f: (f[0],)),
    py_opt=('''def roman_to_int(s):
    val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, ch in enumerate(s):
        if i + 1 < len(s) and val[ch] < val[s[i + 1]]:
            total -= val[ch]                    # smaller symbol before a bigger one is subtracted
        else:
            total += val[ch]
    return total''', 'roman_to_int', lambda f: (f[0],)),
    java_brute=('''static int romanToIntBrute(String s) {
    String[][] pairs = {{"IV", "IIII"}, {"IX", "VIIII"}, {"XL", "XXXX"}, {"XC", "LXXXX"}, {"CD", "CCCC"}, {"CM", "DCCCC"}};
    for (String[] p : pairs) s = s.replace(p[0], p[1]);
    int[] value = {1, 5, 10, 50, 100, 500, 1000};
    int total = 0;
    for (char c : s.toCharArray()) total += value["IVXLCDM".indexOf(c)];
    return total;
}''', 'String.valueOf(Notes.romanToIntBrute(a[0]))'),
    java_opt=('''static int romanToInt(String s) {
    java.util.Map<Character, Integer> val = java.util.Map.of(
        'I', 1, 'V', 5, 'X', 10, 'L', 50, 'C', 100, 'D', 500, 'M', 1000);
    int total = 0;
    for (int i = 0; i < s.length(); i++) {
        int cur = val.get(s.charAt(i));
        if (i + 1 < s.length() && cur < val.get(s.charAt(i + 1))) total -= cur;
        else total += cur;
    }
    return total;
}''', 'String.valueOf(Notes.romanToInt(a[0]))'))

# ---------------------------------------------------------------- 5 Reverse Words in a String
def gen_rw(r):
    while True:
        s = rs(r, 'abc  ', 1, 14)
        if s.strip(): return [s]
add(key='revwords', title='Reverse Words in a String', lc=151, diff='Medium', typ='C', n=5000, gen=gen_rw,
    py_brute=('''def reverse_words_builtin(s):
    return " ".join(reversed(s.split()))        # split() with no argument drops extra spaces''', 'reverse_words_builtin', lambda f: (f[0],)),
    py_opt=('''def reverse_words(s):
    out = []
    i = len(s) - 1
    while i >= 0:                               # walk from the right end
        while i >= 0 and s[i] == " ":           # skip spaces
            i -= 1
        if i < 0:
            break
        j = i                                   # j = last char of this word
        while i >= 0 and s[i] != " ":           # find its first char
            i -= 1
        out.append(s[i + 1:j + 1])
    return " ".join(out)''', 'reverse_words', lambda f: (f[0],)),
    java_brute=('''static String reverseWordsBuiltin(String s) {
    String[] w = s.trim().split("\\\\s+");
    java.util.Collections.reverse(java.util.Arrays.asList(w));
    return String.join(" ", w);
}''', 'Notes.reverseWordsBuiltin(a[0])'),
    java_opt=('''static String reverseWords(String s) {
    StringBuilder out = new StringBuilder();
    int i = s.length() - 1;
    while (i >= 0) {
        while (i >= 0 && s.charAt(i) == ' ') i--;        // skip spaces
        if (i < 0) break;
        int j = i;                                       // j = last char of this word
        while (i >= 0 && s.charAt(i) != ' ') i--;        // find its first char
        if (out.length() > 0) out.append(' ');
        out.append(s, i + 1, j + 1);
    }
    return out.toString();
}''', 'Notes.reverseWords(a[0])'),
    py_opt2=('''def reverse_words_in_place(chars):
    # chars is a list of characters. Reverse everything, reverse each word, squeeze spaces.
    def rev(l, r):
        while l < r:
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
    n = len(chars)
    rev(0, n - 1)
    write = 0                                   # next free slot in the compacted result
    read = 0
    while read < n:
        if chars[read] != " ":
            if write > 0:
                chars[write] = " "              # one space between words
                write += 1
            start = write
            while read < n and chars[read] != " ":
                chars[write] = chars[read]
                write += 1
                read += 1
            rev(start, write - 1)               # the word is backwards now: flip it back
        else:
            read += 1
    del chars[write:]
    return "".join(chars)''', 'reverse_words_in_place', lambda f: (list(f[0]),)),
    java_opt2=('''static String reverseWordsInPlace(char[] chars) {
    int n = chars.length;
    reverse(chars, 0, n - 1);
    int write = 0, read = 0;
    while (read < n) {
        if (chars[read] != ' ') {
            if (write > 0) chars[write++] = ' ';         // one space between words
            int start = write;
            while (read < n && chars[read] != ' ') chars[write++] = chars[read++];
            reverse(chars, start, write - 1);            // flip the (currently backwards) word back
        } else {
            read++;
        }
    }
    return new String(chars, 0, write);
}
static void reverse(char[] c, int l, int r) {
    while (l < r) { char t = c[l]; c[l++] = c[r]; c[r--] = t; }
}''', 'Notes.reverseWordsInPlace(a[0].toCharArray())'))

# ---------------------------------------------------------------- 6 First Unique Character
add(key='firstuniq', title='First Unique Character in a String', lc=387, diff='Easy', typ='C', n=5000,
    gen=lambda r: [rs(r, r.choice(['ab', 'abcd', 'abcdef']), 1, 12)],
    py_brute=('''def first_uniq_brute(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:                  # count() scans the whole string: O(n) per index
            return i
    return -1''', 'first_uniq_brute', lambda f: (f[0],)),
    py_opt=('''from collections import Counter

def first_uniq(s):
    count = Counter(s)                          # pass 1: how many times each letter occurs
    for i, ch in enumerate(s):                  # pass 2: first index whose letter occurs once
        if count[ch] == 1:
            return i
    return -1''', 'first_uniq', lambda f: (f[0],)),
    java_brute=('''static int firstUniqBrute(String s) {
    for (int i = 0; i < s.length(); i++)
        if (s.indexOf(s.charAt(i)) == s.lastIndexOf(s.charAt(i))) return i;
    return -1;
}''', 'String.valueOf(Notes.firstUniqBrute(a[0]))'),
    java_opt=('''static int firstUniq(String s) {
    int[] count = new int[26];                           // lowercase letters only
    for (char c : s.toCharArray()) count[c - 'a']++;
    for (int i = 0; i < s.length(); i++)
        if (count[s.charAt(i) - 'a'] == 1) return i;
    return -1;
}''', 'String.valueOf(Notes.firstUniq(a[0]))'))

# ---------------------------------------------------------------- 7 Custom Sort String
def gen_custom(r):
    order = ''.join(r.sample('abcdef', r.randint(1, 5)))
    return [order, rs(r, 'abcdefg', 0, 12)]
add(key='customsort', title='Custom Sort String', lc=791, diff='Medium', typ='C', n=5000, gen=gen_custom,
    py_brute=('''def custom_sort_brute(order, s):
    rank = {c: i for i, c in enumerate(order)}
    # sorted() is stable, so letters not in order (rank = len(order)) keep their original order at the end
    return "".join(sorted(s, key=lambda c: rank.get(c, len(order))))''', 'custom_sort_brute', lambda f: (f[0], f[1])),
    py_opt=('''from collections import Counter

def custom_sort(order, s):
    count = Counter(s)
    out = []
    for c in order:                             # letters named in order, in that order, all their copies
        out.append(c * count.pop(c, 0))
    in_order = set(order)
    out.extend(c for c in s if c not in in_order)   # everything else, original order
    return "".join(out)''', 'custom_sort', lambda f: (f[0], f[1])),
    java_brute=('''static String customSortBrute(String order, String s) {
    Character[] cs = new Character[s.length()];
    for (int i = 0; i < cs.length; i++) cs[i] = s.charAt(i);
    java.util.Arrays.sort(cs, java.util.Comparator.comparingInt(
        c -> order.indexOf(c) < 0 ? order.length() : order.indexOf(c)));    // object sort is stable
    StringBuilder sb = new StringBuilder();
    for (char c : cs) sb.append(c);
    return sb.toString();
}''', 'Notes.customSortBrute(a[0], a[1])'),
    java_opt=('''static String customSort(String order, String s) {
    int[] count = new int[26];
    for (char c : s.toCharArray()) count[c - 'a']++;
    StringBuilder sb = new StringBuilder();
    for (char c : order.toCharArray()) {
        for (int k = 0; k < count[c - 'a']; k++) sb.append(c);
        count[c - 'a'] = 0;                              // used up: do not emit again below
    }
    for (char c : s.toCharArray())
        if (order.indexOf(c) < 0) sb.append(c);          // everything else, original order
    return sb.toString();
}''', 'Notes.customSort(a[0], a[1])'))

# ---------------------------------------------------------------- 8 Group Shifted Strings
def gen_shift(r):
    words = []
    for _ in range(r.randint(1, 8)):
        L = r.randint(1, 4)
        if words and r.random() < 0.5:
            base = r.choice(words); k = r.randint(0, 25)
            w = ''.join(chr((ord(c) - 97 + k) % 26 + 97) for c in base)
        else:
            w = rs(r, 'abcxyz', L, L)
        words.append(w)
    return [','.join(words)]
def canon_groups(groups):
    return '|'.join(sorted(','.join(sorted(g)) for g in groups))
add(key='shifted', title='Group Shifted Strings', lc=249, diff='Medium', typ='D', n=5000, gen=gen_shift, premium=True,
    py_brute=('''def group_shifted_brute(strings):
    groups = []                                 # each group is a list; groups[i][0] is its representative
    for s in strings:
        for g in groups:
            rep = g[0]
            if len(rep) == len(s) and any(
                    "".join(chr((ord(c) - 97 + k) % 26 + 97) for c in rep) == s
                    for k in range(26)):        # try all 26 rotations of the representative
                g.append(s)
                break
        else:
            groups.append([s])
    return groups''', 'group_shifted_brute', lambda f: (f[0].split(','),), canon_groups),
    py_opt=('''from collections import defaultdict

def group_shifted(strings):
    groups = defaultdict(list)
    for s in strings:
        # signature: each letter's distance from the first letter, wrapped round the alphabet
        key = tuple((ord(c) - ord(s[0])) % 26 for c in s)
        groups[key].append(s)
    return list(groups.values())''', 'group_shifted', lambda f: (f[0].split(','),), canon_groups),
    java_brute=('''static java.util.List<java.util.List<String>> groupShiftedBrute(String[] strings) {
    java.util.List<java.util.List<String>> groups = new java.util.ArrayList<>();
    for (String s : strings) {
        boolean placed = false;
        for (java.util.List<String> g : groups) {
            String rep = g.get(0);
            if (rep.length() != s.length()) continue;
            for (int k = 0; k < 26 && !placed; k++) {
                StringBuilder sb = new StringBuilder();
                for (char c : rep.toCharArray()) sb.append((char) ('a' + (c - 'a' + k) % 26));
                if (sb.toString().equals(s)) { g.add(s); placed = true; }
            }
            if (placed) break;
        }
        if (!placed) groups.add(new java.util.ArrayList<>(java.util.List.of(s)));
    }
    return groups;
}''', 'Main.canon(Notes.groupShiftedBrute(a[0].split(",", -1)))'),
    java_opt=('''static java.util.List<java.util.List<String>> groupShifted(String[] strings) {
    java.util.Map<String, java.util.List<String>> groups = new java.util.HashMap<>();
    for (String s : strings) {
        StringBuilder key = new StringBuilder();
        for (char c : s.toCharArray())
            key.append((c - s.charAt(0) + 26) % 26).append(',');   // +26 keeps the remainder non-negative
        groups.computeIfAbsent(key.toString(), k -> new java.util.ArrayList<>()).add(s);
    }
    return new java.util.ArrayList<>(groups.values());
}''', 'Main.canon(Notes.groupShifted(a[0].split(",", -1)))'))

# ---------------------------------------------------------------- 9 Add Strings
def gen_num(r, lo=1, hi=25):
    L = r.randint(lo, hi)
    if L == 1 and r.random() < 0.3: return '0'
    return r.choice('123456789') + ''.join(r.choice('0123456789' if r.random() < .7 else '99') for _ in range(L - 1))
add(key='addstr', title='Add Strings', lc=415, diff='Easy', typ='D', n=5000, gen=lambda r: [gen_num(r), gen_num(r)],
    py_brute=('''def add_strings_brute(a, b):
    return str(int(a) + int(b))                 # Python ints are unbounded; the problem forbids this shortcut''', 'add_strings_brute', lambda f: (f[0], f[1])),
    py_opt=('''def add_strings(a, b):
    i, j, carry = len(a) - 1, len(b) - 1, 0
    out = []
    while i >= 0 or j >= 0 or carry:            # carry keeps the loop alive for a final extra digit
        total = carry
        if i >= 0:
            total += ord(a[i]) - ord("0")
            i -= 1
        if j >= 0:
            total += ord(b[j]) - ord("0")
            j -= 1
        out.append(str(total % 10))
        carry = total // 10
    return "".join(reversed(out))               # digits were produced least-significant first''', 'add_strings', lambda f: (f[0], f[1])),
    java_brute=('''static String addStringsBrute(String a, String b) {
    return new java.math.BigInteger(a).add(new java.math.BigInteger(b)).toString();
}''', 'Notes.addStringsBrute(a[0], a[1])'),
    java_opt=('''static String addStrings(String a, String b) {
    int i = a.length() - 1, j = b.length() - 1, carry = 0;
    StringBuilder out = new StringBuilder();
    while (i >= 0 || j >= 0 || carry != 0) {
        int total = carry;
        if (i >= 0) total += a.charAt(i--) - '0';
        if (j >= 0) total += b.charAt(j--) - '0';
        out.append(total % 10);
        carry = total / 10;
    }
    return out.reverse().toString();
}''', 'Notes.addStrings(a[0], a[1])'))

# ---------------------------------------------------------------- 10 Multiply Strings
add(key='mulstr', title='Multiply Strings', lc=43, diff='Medium', typ='D', n=5000, gen=lambda r: [gen_num(r, 1, 14), gen_num(r, 1, 14)],
    py_brute=('''def multiply_brute(a, b):
    return str(int(a) * int(b))                 # forbidden shortcut; also the reference for testing''', 'multiply_brute', lambda f: (f[0], f[1])),
    py_opt=('''def multiply(a, b):
    if a == "0" or b == "0":
        return "0"
    res = [0] * (len(a) + len(b))               # a product has at most len(a) + len(b) digits
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            prod = (ord(a[i]) - 48) * (ord(b[j]) - 48) + res[i + j + 1]
            res[i + j + 1] = prod % 10          # digit i of a times digit j of b lands at i + j + 1
            res[i + j] += prod // 10            # the carry goes one slot to the left
    start = 0
    while start < len(res) - 1 and res[start] == 0:   # strip leading zeros
        start += 1
    return "".join(map(str, res[start:]))''', 'multiply', lambda f: (f[0], f[1])),
    java_brute=('''static String multiplyBrute(String a, String b) {
    return new java.math.BigInteger(a).multiply(new java.math.BigInteger(b)).toString();
}''', 'Notes.multiplyBrute(a[0], a[1])'),
    java_opt=('''static String multiply(String a, String b) {
    if (a.equals("0") || b.equals("0")) return "0";
    int[] res = new int[a.length() + b.length()];
    for (int i = a.length() - 1; i >= 0; i--)
        for (int j = b.length() - 1; j >= 0; j--) {
            int prod = (a.charAt(i) - '0') * (b.charAt(j) - '0') + res[i + j + 1];
            res[i + j + 1] = prod % 10;
            res[i + j] += prod / 10;
        }
    StringBuilder sb = new StringBuilder();
    int start = 0;
    while (start < res.length - 1 && res[start] == 0) start++;
    for (int k = start; k < res.length; k++) sb.append(res[k]);
    return sb.toString();
}''', 'Notes.multiply(a[0], a[1])'))

# ---------------------------------------------------------------- 11 Zigzag Conversion
add(key='zigzag', title='Zigzag Conversion', lc=6, diff='Medium', typ='D', n=5000,
    gen=lambda r: [rs(r, string.ascii_lowercase, 1, 16), str(r.randint(1, 6))],
    py_brute=('''def zigzag_brute(s, num_rows):
    if num_rows == 1:
        return s
    cols = len(s)                               # generous: at most one column per character
    grid = [[""] * cols for _ in range(num_rows)]
    r = c = 0
    down = True
    for ch in s:
        grid[r][c] = ch
        if down:
            if r == num_rows - 1:
                down = False
                r -= 1
                c += 1
            else:
                r += 1
        else:
            if r == 0:
                down = True
                r += 1
            else:
                r -= 1
                c += 1
    return "".join("".join(row) for row in grid)''', 'zigzag_brute', lambda f: (f[0], int(f[1]))),
    py_opt=('''def zigzag(s, num_rows):
    if num_rows == 1 or num_rows >= len(s):
        return s                                # no bounce possible
    rows = [[] for _ in range(num_rows)]
    r, step = 0, 1
    for ch in s:
        rows[r].append(ch)
        if r == 0:
            step = 1                            # bounce off the top
        elif r == num_rows - 1:
            step = -1                           # bounce off the bottom
        r += step
    return "".join("".join(row) for row in rows)''', 'zigzag', lambda f: (f[0], int(f[1]))),
    java_brute=('''static String zigzagBrute(String s, int numRows) {
    if (numRows == 1) return s;
    char[][] grid = new char[numRows][s.length()];
    int r = 0, c = 0;
    boolean down = true;
    for (char ch : s.toCharArray()) {
        grid[r][c] = ch;
        if (down) {
            if (r == numRows - 1) { down = false; r--; c++; } else r++;
        } else {
            if (r == 0) { down = true; r++; } else { r--; c++; }
        }
    }
    StringBuilder sb = new StringBuilder();
    for (char[] row : grid) for (char x : row) if (x != 0) sb.append(x);
    return sb.toString();
}''', 'Notes.zigzagBrute(a[0], Integer.parseInt(a[1]))'),
    java_opt=('''static String zigzag(String s, int numRows) {
    if (numRows == 1 || numRows >= s.length()) return s;
    StringBuilder[] rows = new StringBuilder[numRows];
    for (int i = 0; i < numRows; i++) rows[i] = new StringBuilder();
    int r = 0, step = 1;
    for (char ch : s.toCharArray()) {
        rows[r].append(ch);
        if (r == 0) step = 1;
        else if (r == numRows - 1) step = -1;
        r += step;
    }
    StringBuilder out = new StringBuilder();
    for (StringBuilder row : rows) out.append(row);
    return out.toString();
}''', 'Notes.zigzag(a[0], Integer.parseInt(a[1]))'))

# ---------------------------------------------------------------- 12 Longest Common Prefix
add(key='lcp', title='Longest Common Prefix', lc=14, diff='Easy', typ='E', n=5000,
    gen=lambda r: [','.join(rs(r, r.choice(['ab', 'abc']), 0, 6) if r.random() < .5 else ('ab' * 3)[:r.randint(0, 6)] for _ in range(r.randint(1, 5)))],
    py_brute=('''def lcp_brute(strs):
    best = ""
    for k in range(len(strs[0]) + 1):           # try every prefix length of the first word
        prefix = strs[0][:k]
        if all(w.startswith(prefix) for w in strs):
            best = prefix
    return best''', 'lcp_brute', lambda f: (f[0].split(','),)),
    py_opt=('''def longest_common_prefix(strs):
    for i, ch in enumerate(strs[0]):            # vertical scan: column by column
        for w in strs[1:]:
            if i == len(w) or w[i] != ch:       # some word is too short, or disagrees at column i
                return strs[0][:i]
    return strs[0]                              # the first word is itself a prefix of all the others''', 'longest_common_prefix', lambda f: (f[0].split(','),)),
    java_brute=('''static String lcpBrute(String[] strs) {
    String best = "";
    for (int k = 0; k <= strs[0].length(); k++) {
        String prefix = strs[0].substring(0, k);
        boolean all = true;
        for (String w : strs) if (!w.startsWith(prefix)) { all = false; break; }
        if (all) best = prefix;
    }
    return best;
}''', 'Notes.lcpBrute(a[0].split(",", -1))'),
    java_opt=('''static String longestCommonPrefix(String[] strs) {
    for (int i = 0; i < strs[0].length(); i++) {
        char ch = strs[0].charAt(i);
        for (int k = 1; k < strs.length; k++)
            if (i == strs[k].length() || strs[k].charAt(i) != ch) return strs[0].substring(0, i);
    }
    return strs[0];
}''', 'Notes.longestCommonPrefix(a[0].split(",", -1))'))

# ---------------------------------------------------------------- 13 String Compression
def gen_comp(r):
    out = ''
    for _ in range(r.randint(1, 5)):
        out += r.choice('abc') * (r.choice([1, 1, 2, 3, 9, 10, 11, 12, 25, 100, 101]) if r.random() < .6 else r.randint(1, 4))
    return [out]
def comp_wrap(fn):
    def f(chars):
        n = fn(chars)
        return (n, ''.join(chars[:n]))
    return f
add(key='compress', title='String Compression', lc=443, diff='Medium', typ='E', n=5000, gen=gen_comp,
    py_brute=('''from itertools import groupby

def compress_brute(chars):
    parts = []
    for ch, grp in groupby(chars):              # groupby: runs of equal consecutive characters
        k = len(list(grp))
        parts.append(ch + (str(k) if k > 1 else ""))
    out = "".join(parts)                        # builds a second copy: O(n) extra space
    chars[:len(out)] = list(out)
    return len(out)''', 'compress_brute', lambda f: (list(f[0]),), 'inplace'),
    py_opt=('''def compress(chars):
    write = read = 0
    while read < len(chars):
        ch = chars[read]
        start = read
        while read < len(chars) and chars[read] == ch:   # measure the run
            read += 1
        chars[write] = ch                       # write the character once
        write += 1
        run = read - start
        if run > 1:
            for d in str(run):                  # then the count, one digit per slot
                chars[write] = d
                write += 1
    return write                                # write <= read always, so we never overwrite unread input''', 'compress', lambda f: (list(f[0]),), 'inplace'),
    java_brute=('''static int compressBrute(char[] chars) {
    StringBuilder sb = new StringBuilder();
    int i = 0;
    while (i < chars.length) {
        int j = i;
        while (j < chars.length && chars[j] == chars[i]) j++;
        sb.append(chars[i]);
        if (j - i > 1) sb.append(j - i);
        i = j;
    }
    for (int k = 0; k < sb.length(); k++) chars[k] = sb.charAt(k);
    return sb.length();
}''', 'Main.runCompress(a[0], 0)'),
    java_opt=('''static int compress(char[] chars) {
    int write = 0, read = 0;
    while (read < chars.length) {
        char ch = chars[read];
        int start = read;
        while (read < chars.length && chars[read] == ch) read++;     // measure the run
        chars[write++] = ch;
        int run = read - start;
        if (run > 1)
            for (char d : Integer.toString(run).toCharArray()) chars[write++] = d;
    }
    return write;
}''', 'Main.runCompress(a[0], 1)'))

# ---------------------------------------------------------------- 14 strStr
def gen_strstr(r):
    if r.random() < .3:
        p = rs(r, 'ab', 1, 3)
        return [(p * r.randint(1, 5))[:r.randint(0, 14)] + r.choice(['', 'a', 'b']), (p * 2)[:r.randint(1, 5)]]
    return [rs(r, 'ab', 0, 14), rs(r, 'ab', 1, 5)]
add(key='strstr', title='Find the Index of the First Occurrence in a String', lc=28, diff='Easy', typ='F', n=6000, gen=gen_strstr,
    py_brute=('''def str_str_brute(haystack, needle):
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):                  # every possible start
        j = 0
        while j < m and haystack[i + j] == needle[j]:
            j += 1
        if j == m:
            return i
    return -1                                   # worst case O(n * m), e.g. "aaaa...a" with "aaa...ab"''', 'str_str_brute', lambda f: (f[0], f[1])),
    py_opt=('''def str_str(haystack, needle):
    # KMP. lps[k] = length of the longest proper prefix of needle[:k+1] that is also its suffix
    m = len(needle)
    lps = [0] * m
    k = 0
    for i in range(1, m):
        while k and needle[i] != needle[k]:
            k = lps[k - 1]                      # fall back to a shorter border
        if needle[i] == needle[k]:
            k += 1
        lps[i] = k
    k = 0                                       # k = how many characters of needle currently match
    for i, ch in enumerate(haystack):           # i never moves backwards
        while k and ch != needle[k]:
            k = lps[k - 1]
        if ch == needle[k]:
            k += 1
        if k == m:
            return i - m + 1
    return -1''', 'str_str', lambda f: (f[0], f[1])),
    java_brute=('''static int strStrBrute(String haystack, String needle) {
    int n = haystack.length(), m = needle.length();
    for (int i = 0; i + m <= n; i++) {
        int j = 0;
        while (j < m && haystack.charAt(i + j) == needle.charAt(j)) j++;
        if (j == m) return i;
    }
    return -1;
}''', 'String.valueOf(Notes.strStrBrute(a[0], a[1]))'),
    java_opt=('''static int strStr(String haystack, String needle) {
    int m = needle.length();
    int[] lps = new int[m];
    for (int i = 1, k = 0; i < m; i++) {
        while (k > 0 && needle.charAt(i) != needle.charAt(k)) k = lps[k - 1];
        if (needle.charAt(i) == needle.charAt(k)) k++;
        lps[i] = k;
    }
    for (int i = 0, k = 0; i < haystack.length(); i++) {
        while (k > 0 && haystack.charAt(i) != needle.charAt(k)) k = lps[k - 1];
        if (haystack.charAt(i) == needle.charAt(k)) k++;
        if (k == m) return i - m + 1;
    }
    return -1;
}''', 'String.valueOf(Notes.strStr(a[0], a[1]))'))
