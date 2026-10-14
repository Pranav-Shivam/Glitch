public class Tk {
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
}