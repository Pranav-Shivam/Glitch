public class Claims2 {
  static long sink;
  public static void main(String[] a) {
    int n = 200000;
    String big = "x".repeat(n);
    long t0 = System.nanoTime(); String s = big; while (!s.isEmpty()) s = s.substring(1); long t1 = System.nanoTime();
    long c = 0; for (int i = 0; i < n; i++) c += big.charAt(i); long t2 = System.nanoTime(); sink = c;
    System.out.printf("L1 Java: s = s.substring(1) loop on %d chars: %.3fs ; index loop: %.4fs%n", n, (t1 - t0) / 1e9, (t2 - t1) / 1e9);
    StringBuilder sb0 = new StringBuilder(); for (int i = 0; i < 5_000_000; i++) sb0.append((char) ('a' + i % 26));
    String big2 = sb0.toString();
    long h0 = System.nanoTime(); int h = big2.hashCode(); long h1 = System.nanoTime(); int h2 = big2.hashCode(); long h3 = System.nanoTime(); sink += h + h2;
    System.out.printf("L2 Java: hashCode of a 5,000,000-char string, first call %.3f ms, second call %.5f ms%n", (h1 - h0) / 1e6, (h3 - h1) / 1e6);
    int N = 100000;
    long i0 = System.nanoTime(); StringBuilder sb = new StringBuilder(); for (int i = 0; i < N; i++) sb.insert(0, 'x'); long i1 = System.nanoTime();
    StringBuilder sb2 = new StringBuilder(); for (int i = 0; i < N; i++) sb2.append('x'); long i2 = System.nanoTime();
    System.out.printf("L3 Java: StringBuilder.insert(0, c) x%d: %.3fs ; append x%d: %.4fs%n", N, (i1 - i0) / 1e9, N, (i2 - i1) / 1e9);
    String hay = "a".repeat(100000), nd = "a".repeat(50000) + "b";
    long s0 = System.nanoTime(); int r = hay.indexOf(nd); long s1 = System.nanoTime(); sink += r;
    System.out.printf("L4 Java: indexOf worst case ('a'*50000+'b' in 'a'*100000): %.3fs (result %d)%n", (s1 - s0) / 1e9, r);
  }
}
