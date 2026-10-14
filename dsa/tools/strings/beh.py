import os,subprocess,time
DSA=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')); HERE=os.getcwd()
EDGE=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
src=open(os.path.join(DSA,'Strings_Notes_v1.html'),encoding='utf8').read()
test=open('beh.js',encoding='utf8').read()
t=src.replace('</body>','<script>'+test+'</script></body>')
tmp=os.path.join(DSA,'_t_behaviour.html'); open(tmp,'w',encoding='utf8').write(t)
out=os.path.join(HERE,'shots','behaviour.png')
if os.path.exists(out): os.remove(out)
subprocess.run([EDGE,'--headless=old','--disable-gpu','--user-data-dir='+os.path.join(HERE,'edge_ud_beh4'),'--no-first-run','--window-size=1100,400',f'--screenshot={out}','--virtual-time-budget=4000','file:///'+tmp.replace(chr(92),'/')],capture_output=True,timeout=120)
for _ in range(60):
    if os.path.exists(out) and os.path.getsize(out)>0: time.sleep(0.5);break
    time.sleep(0.5)
os.remove(tmp); print(os.path.exists(out))
