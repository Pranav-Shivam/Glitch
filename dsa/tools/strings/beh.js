(function(){
 var r=[];
 function vis(el){return el.offsetParent!==null;}
 function step(name,f){try{r.push(name+': '+f());}catch(e){r.push(name+': ERROR '+e);}}
 step('open tab 7',function(){document.querySelector('.nav-tab[data-tab="tab-p7"]').click();return 'p7 visible='+vis(document.getElementById('tab-p7'))+' p1 visible='+vis(document.getElementById('tab-p1'));});
 var d=document.getElementById('p3'); d.open=true; var zone=d.querySelector('.reveal-zone');
 step('practice mode on',function(){var pm=document.getElementById('practice-mode'); pm.checked=true; pm.dispatchEvent(new Event('change'));return 'zone visible='+vis(zone);});
 step('reveal click',function(){d.querySelector('.reveal-btn').click();return 'zone visible='+vis(zone);});
 step('java toggle',function(){document.getElementById('lang-java').click();var panes=[].slice.call(d.querySelectorAll('pre.pane')).filter(vis).map(function(p){return p.dataset.l});return 'visible panes='+panes.join(',')+' body lang='+document.body.getAttribute('data-lang');});
 step('checklist',function(){document.querySelector('.nav-tab[data-tab="tab-p13"]').click();var c=document.getElementById('chk-1'); c.checked=true; c.dispatchEvent(new Event('change'));return 'progress='+document.getElementById('prog-text').textContent+' saved='+localStorage.getItem('dsa-checks-strings-v1');});
 step('counts',function(){return 'tabs='+document.querySelectorAll('.nav-tab').length+' sections='+document.querySelectorAll('.section').length;});
 step('xref',function(){document.querySelector('.nav-tab[data-tab="tab-p1"]').click();var a=document.querySelector('a.xref[href="#part-10"]');a.click();return 'tab-p10 visible='+vis(document.getElementById('tab-p10'));});
 var out=document.createElement('pre'); out.style.cssText='position:fixed;top:0;left:0;right:0;bottom:0;background:#fff;color:#000;z-index:99999;padding:20px;font:15px monospace;white-space:pre-wrap'; out.textContent=r.join(String.fromCharCode(10)); document.body.appendChild(out);
})();
