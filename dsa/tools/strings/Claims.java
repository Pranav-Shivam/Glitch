public class Claims {
  static int atoiBad(String s) { int i=0,n=s.length(); while(i<n&&s.charAt(i)==' ')i++; int sign=1; if(i<n&&(s.charAt(i)=='+'||s.charAt(i)=='-')){sign=s.charAt(i)=='-'?-1:1;i++;} int r=0; while(i<n&&s.charAt(i)>='0'&&s.charAt(i)<='9'){ r=r*10+(s.charAt(i)-'0'); i++; } return sign*r; }
  public static void main(String[] a) {
    System.out.println("J1 atoi without pre-check: atoiBad(\"2147483648\") = " + atoiBad("2147483648") + " (correct: 2147483647)");
    String x = new String("ab"); String y = "ab";
    System.out.println("J2 new String(\"ab\") == \"ab\": " + (x == y) + " ; equals: " + x.equals(y));
    System.out.println("J3 \" a b\".split(\"\\s+\").length = " + " a b".split("\s+").length + " first=[" + " a b".split("\s+")[0] + "] (correct: 2 words)");
    char c = 'a';
    System.out.println("J4 'a' + 1 + \"\" = \"" + ('a' + 1 + "") + "\" ; \"\" + 'a' + 1 = \"" + ("" + 'a' + 1) + "\" ; (char)(c + 1) = " + (char)(c + 1));
    System.out.println("J5 Character.isDigit('\u0663') = " + Character.isDigit('\u0663') + " ; '\u0663' - '0' = " + ('\u0663' - '0'));
    int N = 100000;
    long t0 = System.nanoTime(); String s = ""; for (int i = 0; i < N; i++) s += "x"; long t1 = System.nanoTime();
    StringBuilder sb = new StringBuilder(); for (int i = 0; i < N; i++) sb.append("x"); long t2 = System.nanoTime();
    System.out.printf("J6 Java: s += \"x\" x%d: %.3fs ; StringBuilder: %.3fs%n", N, (t1 - t0) / 1e9, (t2 - t1) / 1e9);
    System.out.println("J7 \"a,b,,\".split(\",\").length = " + "a,b,,".split(",").length + " ; split(\",\", -1).length = " + "a,b,,".split(",", -1).length);
  }
}
