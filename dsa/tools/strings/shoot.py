import subprocess, os, sys, time
DSA = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(DSA, 'Strings_Notes_v1.html'), encoding='utf8').read()
# (name, tab, element to isolate or '', lang, theme, width, height)
shots = [
 ('v_p3', 'tab-p3', '', 'py', 'light', 1280, 1900),
 ('v_p6', 'tab-p6', '', 'py', 'dark', 1280, 1900),
 ('v_p8', 'tab-p8', '', 'py', 'light', 1280, 1700),
 ('v_p9', 'tab-p9', '', 'py', 'dark', 1280, 1500),
 ('v_p10', 'tab-p10', '', 'java', 'light', 1280, 1800),
 ('v_p11', 'tab-p11', '', 'py', 'light', 1280, 1700),
 ('v_p12', 'tab-p12', '', 'py', 'dark', 1280, 1700),
 ('v_p14', 'tab-p14', '', 'py', 'light', 1280, 1500),
 ('v_p4B_java', 'tab-p4', 'type-b', 'java', 'light', 1280, 1700),
 ('v_p1_light', 'tab-p1', '', 'py', 'light', 1280, 1400),
 ('v_p13_light', 'tab-p13', '', 'py', 'light', 1280, 1000),
 ('v_prob1_java', 'tab-p7', 'p1', 'java', 'dark', 1280, 1900),
 ('v_prob14_java', 'tab-p7', 'p14', 'java', 'light', 1280, 2200),
 ('v_prob12_java', 'tab-p7', 'p12', 'java', 'dark', 1280, 1900),
 ('v_p7_top', 'tab-p7', '', 'py', 'light', 1280, 2200),
 ('v_p2_py', 'tab-p2', '', 'py', 'dark', 1280, 2600),
]
sel = sys.argv[1:]
for name, tab, iso, lang, theme, w, h in shots:
    if sel and name not in sel: continue
    isolate = ''
    if iso:
        isolate = ("<script>(function(){var d=document.getElementById('%s');if(!d)return;var host=d.closest('.page-wrap');"
                   "if(d.tagName==='DETAILS')d.open=true;var keep=d;while(keep.parentNode!==host)keep=keep.parentNode;"
                   "Array.prototype.slice.call(host.children).forEach(function(c){if(c!==keep)c.remove();});})();</script>") % iso
    inj = f"<script>try{{localStorage.setItem('dsa-lang','{lang}');localStorage.setItem('dsa-theme','{theme}')}}catch(e){{}}</script>\n<script src=\"assets/dsa.js\"></script>{isolate}\n<script>0"
    t = src.replace('<script src="assets/dsa.js">', inj, 1)
    tmp = os.path.join(DSA, f'_view_{name}.html'); open(tmp, 'w', encoding='utf8').write(t)
    out = os.path.join(HERE, 'shots', name + '.png')
    if os.path.exists(out): os.remove(out)
    url = 'file:///' + tmp.replace(chr(92), '/') + '#' + tab
    subprocess.run([EDGE, '--headless=old', '--disable-gpu', '--user-data-dir=' + os.path.join(HERE, 'edge_ud_' + name), '--no-first-run', '--hide-scrollbars', f'--window-size={w},{h}', f'--screenshot={out}', '--virtual-time-budget=4000', url], capture_output=True, timeout=120)
    for _ in range(60):
        if os.path.exists(out) and os.path.getsize(out) > 0: time.sleep(0.5); break
        time.sleep(0.5)
    os.remove(tmp)
    print(name, os.path.exists(out) and os.path.getsize(out))
