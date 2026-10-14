# Strings notes: generator and tests

Everything needed to rebuild `dsa/Strings_Notes_v1.html` and to re-run the tests behind it. The page is generated from one data file, so the code you read in the notes is the code that was tested.

Needs Python 3.11 with `pygments`, a JDK (set `JAVA_HOME`, default `C:\Program Files\Java\jdk-27`), and for screenshots Microsoft Edge.

Run from this folder, in this order:

1. `python fetch_scores.py` (optional): re-downloads the six company CSVs and rewrites `scores.json`. The committed `scores.json` is what the page used (retrieved 2026-10-13).
2. `python run_tests.py`: runs every brute force and optimal solution, in Python and Java, on thousands of random inputs. Writes `py_results.json` and `java_results.txt` (read by the build). Any mismatch is printed as FAIL.
3. `claims.py`, `Claims.java`, `claims2.py`, `Claims2.java`: the bug demonstrations and cost benchmarks quoted in the notes. Their saved outputs (`claims_py.txt`, `claims_java.txt`, `claims2_py.txt`, `claims2_java.txt`) are committed because the timings quoted in Parts 2, 3 and 10 come from that run; re-running gives different timings on another machine. Compile and run the Java ones with `javac -d out Claims.java Claims2.java` and `java -Dstdout.encoding=UTF-8 -cp out Claims` (and `Claims2`).
4. `python build.py`: checks the Part 2 examples and the hand traces, checks the test results (stops on any failure) and writes `../../Strings_Notes_v1.html`.
5. `python validate.py ../../Strings_Notes_v1.html`: tag balance, duplicate ids, broken `#` links, tab/section match.
6. Optional: `shoot.py` (screenshots into `shots/`) and `beh.py` (scripted click test, writes `shots/behaviour.png`). They open a temporary copy of the page, injecting theme, language and a click script.

Files: `probs_a.py` and `probs_b.py` hold all code (Python and Java, brute force and optimal) and the random-input generators; `c_prob.py` the per-problem teaching text; `c_text1.py` to `c_text4.py` the other parts; `lib.py` the HTML helpers; `toolkit.py` the Part 2 examples with their expected output; `views.html` the "views checked" note for Appendix B.

Limits: `claims*.txt` timings are machine-specific; `scores.json` is third-party data (unofficial, normalised, method undocumented).
