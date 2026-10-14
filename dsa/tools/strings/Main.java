import java.io.*; import java.util.*;
public class Main {
static String runCompress(String s, int which) { char[] c = s.toCharArray(); int n = which == 0 ? Notes.compressBrute(c) : Notes.compress(c); return n + "," + new String(c, 0, n); }
static String canon(List<List<String>> groups) { List<String> gs = new ArrayList<>(); for (List<String> g : groups) { List<String> h = new ArrayList<>(g); Collections.sort(h); gs.add(String.join(",", h)); } Collections.sort(gs); return String.join("|", gs); }
static String encHex(List<String> l) { StringBuilder sb = new StringBuilder(); sb.append(l.size()).append(":"); for (int i = 0; i < l.size(); i++) { if (i > 0) sb.append(","); for (byte b : l.get(i).getBytes(java.nio.charset.StandardCharsets.UTF_8)) sb.append(String.format("%02x", b)); } return sb.toString(); }
static List<String> decHex(String f) { int c = f.indexOf(":"); int n = Integer.parseInt(f.substring(0, c)); List<String> out = new ArrayList<>(); if (n == 0) return out; for (String h : f.substring(c + 1).split(",", -1)) { byte[] bs = new byte[h.length() / 2]; for (int i = 0; i < bs.length; i++) bs[i] = (byte) Integer.parseInt(h.substring(2 * i, 2 * i + 2), 16); out.add(new String(bs, java.nio.charset.StandardCharsets.UTF_8)); } return out; }
static Map<String,Integer> pass = new LinkedHashMap<>(); static Map<String,String> fail = new LinkedHashMap<>();
static void chk(String k, String role, String exp, String got, String[] a) { String key = k + ":" + role; if (exp.equals(got)) pass.merge(key, 1, Integer::sum); else { pass.putIfAbsent(key, 0); fail.putIfAbsent(key, Arrays.toString(a) + " exp=[" + exp + "] got=[" + got + "]"); } }
public static void main(String[] args) throws Exception {
 BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(args[0]), "UTF-8")); String line;
 while ((line = br.readLine()) != null) { String[] t = line.split("\t", -1); String k = t[0]; String exp = t[t.length - 1]; String[] a = Arrays.copyOfRange(t, 1, t.length - 1);
  switch (k) {
   case "vwa": {
    chk(k, "brute", exp, String.valueOf(Notes.validAbbrBrute(a[0], a[1])), a);
    chk(k, "opt", exp, String.valueOf(Notes.validAbbr(a[0], a[1])), a);
    break; }
   case "lps": {
    chk(k, "brute", exp, Notes.longestPalindromeBrute(a[0]), a);
    chk(k, "opt", exp, Notes.longestPalindrome(a[0]), a);
    break; }
   case "atoi": {
    chk(k, "brute", exp, String.valueOf(Notes.myAtoiRegex(a[0])), a);
    chk(k, "opt", exp, String.valueOf(Notes.myAtoi(a[0])), a);
    break; }
   case "roman": {
    chk(k, "brute", exp, String.valueOf(Notes.romanToIntBrute(a[0])), a);
    chk(k, "opt", exp, String.valueOf(Notes.romanToInt(a[0])), a);
    break; }
   case "revwords": {
    chk(k, "brute", exp, Notes.reverseWordsBuiltin(a[0]), a);
    chk(k, "opt", exp, Notes.reverseWords(a[0]), a);
    chk(k, "opt2", exp, Notes.reverseWordsInPlace(a[0].toCharArray()), a);
    break; }
   case "firstuniq": {
    chk(k, "brute", exp, String.valueOf(Notes.firstUniqBrute(a[0])), a);
    chk(k, "opt", exp, String.valueOf(Notes.firstUniq(a[0])), a);
    break; }
   case "customsort": {
    chk(k, "brute", exp, Notes.customSortBrute(a[0], a[1]), a);
    chk(k, "opt", exp, Notes.customSort(a[0], a[1]), a);
    break; }
   case "shifted": {
    chk(k, "brute", exp, Main.canon(Notes.groupShiftedBrute(a[0].split(",", -1))), a);
    chk(k, "opt", exp, Main.canon(Notes.groupShifted(a[0].split(",", -1))), a);
    break; }
   case "addstr": {
    chk(k, "brute", exp, Notes.addStringsBrute(a[0], a[1]), a);
    chk(k, "opt", exp, Notes.addStrings(a[0], a[1]), a);
    break; }
   case "mulstr": {
    chk(k, "brute", exp, Notes.multiplyBrute(a[0], a[1]), a);
    chk(k, "opt", exp, Notes.multiply(a[0], a[1]), a);
    break; }
   case "zigzag": {
    chk(k, "brute", exp, Notes.zigzagBrute(a[0], Integer.parseInt(a[1])), a);
    chk(k, "opt", exp, Notes.zigzag(a[0], Integer.parseInt(a[1])), a);
    break; }
   case "lcp": {
    chk(k, "brute", exp, Notes.lcpBrute(a[0].split(",", -1)), a);
    chk(k, "opt", exp, Notes.longestCommonPrefix(a[0].split(",", -1)), a);
    break; }
   case "compress": {
    chk(k, "brute", exp, Main.runCompress(a[0], 0), a);
    chk(k, "opt", exp, Main.runCompress(a[0], 1), a);
    break; }
   case "strstr": {
    chk(k, "brute", exp, String.valueOf(Notes.strStrBrute(a[0], a[1])), a);
    chk(k, "opt", exp, String.valueOf(Notes.strStr(a[0], a[1])), a);
    break; }
   case "merge": {
    chk(k, "brute", exp, Notes.mergeAlternatelyBrute(a[0], a[1]), a);
    chk(k, "opt", exp, Notes.mergeAlternately(a[0], a[1]), a);
    break; }
   case "addbin": {
    chk(k, "brute", exp, Notes.addBinaryBrute(a[0], a[1]), a);
    chk(k, "opt", exp, Notes.addBinary(a[0], a[1]), a);
    break; }
   case "pals": {
    chk(k, "brute", exp, String.valueOf(Notes.countSubstringsBrute(a[0])), a);
    chk(k, "opt", exp, String.valueOf(Notes.countSubstrings(a[0])), a);
    break; }
   case "version": {
    chk(k, "brute", exp, String.valueOf(Notes.compareVersionBrute(a[0], a[1])), a);
    chk(k, "opt", exp, String.valueOf(Notes.compareVersion(a[0], a[1])), a);
    break; }
   case "codec": {
    chk(k, "opt", exp, Main.encHex(Notes.decode(Notes.encode(Main.decHex(a[0])))), a);
    break; }
   case "justify": {
    chk(k, "brute", exp, String.join(",", Notes.fullJustifyBrute(a[0].split(",", -1), Integer.parseInt(a[1]))), a);
    chk(k, "opt", exp, String.join(",", Notes.fullJustify(a[0].split(",", -1), Integer.parseInt(a[1]))), a);
    break; }
   default: throw new RuntimeException(k);
  } }
 for (var e : pass.entrySet()) System.out.println("JAVA " + e.getKey() + " pass=" + e.getValue());
 for (var e : fail.entrySet()) System.out.println("JAVAFAIL " + e.getKey() + " " + e.getValue());
}}