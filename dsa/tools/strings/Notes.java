import java.util.*;
public class Notes {
static boolean validAbbrBrute(String word, String abbr) {
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
}

static boolean validAbbr(String word, String abbr) {
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
}

static String longestPalindromeBrute(String s) {
    String best = "";
    for (int i = 0; i < s.length(); i++)
        for (int j = i; j < s.length(); j++) {
            String t = s.substring(i, j + 1);
            if (t.length() > best.length() && new StringBuilder(t).reverse().toString().equals(t)) best = t;
        }
    return best;
}

static String longestPalindrome(String s) {
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
}

static int myAtoiRegex(String s) {
    java.util.regex.Matcher m = java.util.regex.Pattern.compile("^ *([+-]?)([0-9]+)").matcher(s);
    if (!m.find()) return 0;
    java.math.BigInteger v = new java.math.BigInteger(m.group(2));
    if (m.group(1).equals("-")) v = v.negate();
    if (v.compareTo(java.math.BigInteger.valueOf(Integer.MAX_VALUE)) > 0) return Integer.MAX_VALUE;
    if (v.compareTo(java.math.BigInteger.valueOf(Integer.MIN_VALUE)) < 0) return Integer.MIN_VALUE;
    return v.intValue();
}

static int myAtoi(String s) {
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
}

static int romanToIntBrute(String s) {
    String[][] pairs = {{"IV", "IIII"}, {"IX", "VIIII"}, {"XL", "XXXX"}, {"XC", "LXXXX"}, {"CD", "CCCC"}, {"CM", "DCCCC"}};
    for (String[] p : pairs) s = s.replace(p[0], p[1]);
    int[] value = {1, 5, 10, 50, 100, 500, 1000};
    int total = 0;
    for (char c : s.toCharArray()) total += value["IVXLCDM".indexOf(c)];
    return total;
}

static int romanToInt(String s) {
    java.util.Map<Character, Integer> val = java.util.Map.of(
        'I', 1, 'V', 5, 'X', 10, 'L', 50, 'C', 100, 'D', 500, 'M', 1000);
    int total = 0;
    for (int i = 0; i < s.length(); i++) {
        int cur = val.get(s.charAt(i));
        if (i + 1 < s.length() && cur < val.get(s.charAt(i + 1))) total -= cur;
        else total += cur;
    }
    return total;
}

static String reverseWordsBuiltin(String s) {
    String[] w = s.trim().split("\\s+");
    java.util.Collections.reverse(java.util.Arrays.asList(w));
    return String.join(" ", w);
}

static String reverseWords(String s) {
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
}

static String reverseWordsInPlace(char[] chars) {
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
}

static int firstUniqBrute(String s) {
    for (int i = 0; i < s.length(); i++)
        if (s.indexOf(s.charAt(i)) == s.lastIndexOf(s.charAt(i))) return i;
    return -1;
}

static int firstUniq(String s) {
    int[] count = new int[26];                           // lowercase letters only
    for (char c : s.toCharArray()) count[c - 'a']++;
    for (int i = 0; i < s.length(); i++)
        if (count[s.charAt(i) - 'a'] == 1) return i;
    return -1;
}

static String customSortBrute(String order, String s) {
    Character[] cs = new Character[s.length()];
    for (int i = 0; i < cs.length; i++) cs[i] = s.charAt(i);
    java.util.Arrays.sort(cs, java.util.Comparator.comparingInt(
        c -> order.indexOf(c) < 0 ? order.length() : order.indexOf(c)));    // object sort is stable
    StringBuilder sb = new StringBuilder();
    for (char c : cs) sb.append(c);
    return sb.toString();
}

static String customSort(String order, String s) {
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
}

static java.util.List<java.util.List<String>> groupShiftedBrute(String[] strings) {
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
}

static java.util.List<java.util.List<String>> groupShifted(String[] strings) {
    java.util.Map<String, java.util.List<String>> groups = new java.util.HashMap<>();
    for (String s : strings) {
        StringBuilder key = new StringBuilder();
        for (char c : s.toCharArray())
            key.append((c - s.charAt(0) + 26) % 26).append(',');   // +26 keeps the remainder non-negative
        groups.computeIfAbsent(key.toString(), k -> new java.util.ArrayList<>()).add(s);
    }
    return new java.util.ArrayList<>(groups.values());
}

static String addStringsBrute(String a, String b) {
    return new java.math.BigInteger(a).add(new java.math.BigInteger(b)).toString();
}

static String addStrings(String a, String b) {
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
}

static String multiplyBrute(String a, String b) {
    return new java.math.BigInteger(a).multiply(new java.math.BigInteger(b)).toString();
}

static String multiply(String a, String b) {
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
}

static String zigzagBrute(String s, int numRows) {
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
}

static String zigzag(String s, int numRows) {
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
}

static String lcpBrute(String[] strs) {
    String best = "";
    for (int k = 0; k <= strs[0].length(); k++) {
        String prefix = strs[0].substring(0, k);
        boolean all = true;
        for (String w : strs) if (!w.startsWith(prefix)) { all = false; break; }
        if (all) best = prefix;
    }
    return best;
}

static String longestCommonPrefix(String[] strs) {
    for (int i = 0; i < strs[0].length(); i++) {
        char ch = strs[0].charAt(i);
        for (int k = 1; k < strs.length; k++)
            if (i == strs[k].length() || strs[k].charAt(i) != ch) return strs[0].substring(0, i);
    }
    return strs[0];
}

static int compressBrute(char[] chars) {
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
}

static int compress(char[] chars) {
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
}

static int strStrBrute(String haystack, String needle) {
    int n = haystack.length(), m = needle.length();
    for (int i = 0; i + m <= n; i++) {
        int j = 0;
        while (j < m && haystack.charAt(i + j) == needle.charAt(j)) j++;
        if (j == m) return i;
    }
    return -1;
}

static int strStr(String haystack, String needle) {
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
}

static String mergeAlternatelyBrute(String w1, String w2) {
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < Math.max(w1.length(), w2.length()); i++) {
        if (i < w1.length()) out.append(w1.charAt(i));
        if (i < w2.length()) out.append(w2.charAt(i));
    }
    return out.toString();
}

static String mergeAlternately(String w1, String w2) {
    int n = Math.min(w1.length(), w2.length());
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < n; i++) out.append(w1.charAt(i)).append(w2.charAt(i));
    out.append(w1, n, w1.length()).append(w2, n, w2.length());
    return out.toString();
}

static String addBinaryBrute(String a, String b) {
    return new java.math.BigInteger(a, 2).add(new java.math.BigInteger(b, 2)).toString(2);
}

static String addBinary(String a, String b) {
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
}

static int countSubstringsBrute(String s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++)
        for (int j = i; j < s.length(); j++) {
            String t = s.substring(i, j + 1);
            if (new StringBuilder(t).reverse().toString().equals(t)) count++;
        }
    return count;
}

static int countSubstrings(String s) {
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
}

static int compareVersionBrute(String v1, String v2) {
    String[] a = v1.split("\\."), b = v2.split("\\.");
    int n = Math.max(a.length, b.length);
    for (int i = 0; i < n; i++) {
        int x = i < a.length ? Integer.parseInt(a[i]) : 0;
        int y = i < b.length ? Integer.parseInt(b[i]) : 0;
        if (x != y) return x < y ? -1 : 1;
    }
    return 0;
}

static int compareVersion(String v1, String v2) {
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
}

static String encode(java.util.List<String> strs) {
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
}

static java.util.List<String> fullJustifyBrute(String[] words, int maxWidth) {
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
}

static java.util.List<String> fullJustify(String[] words, int maxWidth) {
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
}

}