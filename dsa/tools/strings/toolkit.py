# Toolkit examples shown in Part 2. Each is run at build time and its printed output is compared with the expected text.
PY_EX = [
 ("Indexing and slicing", '''s = "interview"
print(s[0], s[-1], s[2:5], s[::-1], len(s))''', "i w ter weivretni 9"),
 ("Strings are immutable", '''s = "cat"
try:
    s[0] = "b"
except TypeError:
    print("TypeError")
chars = list(s)          # a mutable copy
chars[0] = "b"
print("".join(chars))''', "TypeError\nbat"),
 ("split with and without an argument", '''t = "  a  b "
print(t.split())
print(t.split(" "))
print(",".join(["x", "y", "z"]))''', "['a', 'b']\n['', '', 'a', '', 'b', '']\nx,y,z"),
 ("Searching", '''t = "banana"
print(t.find("an"), t.find("x"), t.count("an"), "ana" in t, t.startswith("ban"))
try:
    t.index("x")
except ValueError:
    print("index raises, find returns -1")''', "1 -1 2 True True\nindex raises, find returns -1"),
 ("Characters and numbers", '''print(ord("c") - ord("a"), chr(ord("a") + 2), int("7") + 1, "7".isdigit(), "ab1".isalnum(), "Ab".lower())''', "2 c 8 True True ab"),
 ("Counting and sorting letters", '''from collections import Counter
print(Counter("aab"))
print("".join(sorted("bca")))
counts = [0] * 26
for ch in "hello":
    counts[ord(ch) - ord("a")] += 1
print(counts[ord("l") - ord("a")])''', "Counter({'a': 2, 'b': 1})\nabc\n2"),
 ("Building a string", '''parts = []
for i in range(4):
    parts.append(str(i))
print("-".join(parts))''', "0-1-2-3"),
 ("Comparison is lexicographic, character by character", '''print("apple" < "banana", "Z" < "a", "10" < "9", "ab" < "abc")''', "True True True True"),
 ("Unicode: len counts code points", '''print(len("a\U0001F600"))''', "2"),
]
JAVA_EX = '''public class Tk {
    public static void main(String[] args) {
        String s = "interview";
        System.out.println(s.charAt(0) + " " + s.charAt(s.length() - 1) + " " + s.substring(2, 5) + " " + new StringBuilder(s).reverse() + " " + s.length());
        String a = new String("cat"), b = "cat";
        System.out.println((a == b) + " " + a.equals(b));
        char[] cs = s.toCharArray();
        java.util.Arrays.sort(cs);
        System.out.println(new String(cs));
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 4; i++) { if (i > 0) sb.append('-'); sb.append(i); }
        System.out.println(sb);
        sb.setCharAt(0, 'x'); sb.insert(0, "<"); sb.deleteCharAt(sb.length() - 1);
        System.out.println(sb);
        System.out.println("  a  b ".split(" ").length + " " + "a,b,,".split(",").length + " " + "a,b,,".split(",", -1).length);
        System.out.println(('c' - 'a') + " " + (char) ('a' + 2) + " " + Integer.parseInt("7") + 1 + " " + Character.isDigit('7') + " " + Character.isLetterOrDigit('_'));
        int[] counts = new int[26];
        for (char c : "hello".toCharArray()) counts[c - 'a']++;
        System.out.println(counts['l' - 'a']);
        System.out.println("apple".compareTo("banana") + " " + "ab".compareTo("abc") + " " + "10".compareTo("9"));
        String e = "a" + new String(Character.toChars(0x1F600));
        System.out.println(e.length() + " " + e.codePointCount(0, e.length()));
        System.out.println("banana".indexOf("an") + " " + "banana".indexOf("x") + " " + "banana".lastIndexOf("an") + " " + String.join("|", java.util.List.of("p", "q")));
    }
}'''
JAVA_EXPECT = '''i w ter weivretni 9
false true
eeiinrtvw
0-1-2-3
<x-1-2-
5 2 4
2 c 71 true false
2
-1 -1 -8
3 2
1 -1 3 p|q'''
