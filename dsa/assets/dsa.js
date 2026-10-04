/* DSA Mastery Notes: shared behaviour (tabs, language, copy, theme, practice, checklist). Set <body data-key="slug">. */
(function () {
  var root = document.documentElement, body = document.body;
  var KEY = body.getAttribute('data-key') || 'topic';
  function save(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function load(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function $(id) { return document.getElementById(id); }
  function all(sel, el) { return [].slice.call((el || document).querySelectorAll(sel)); }

  /* masthead height feeds scroll-margin so anchors land below the sticky bar */
  var mast = $('masthead');
  function measure() { if (mast) root.style.setProperty('--mast-h', mast.offsetHeight + 'px'); }
  measure(); window.addEventListener('resize', measure);

  /* ── Tabs and in-page links ── */
  var sections = all('.section'), tabs = all('.nav-tab');
  function showTab(id) {
    sections.forEach(function (s) { s.hidden = s.id !== id; });
    tabs.forEach(function (b) {
      var on = b.dataset.tab === id;
      b.classList.toggle('active', on);
      b.setAttribute('aria-current', on ? 'page' : 'false');
      if (on) { var nav = b.parentNode; nav.scrollLeft = Math.max(0, b.offsetLeft - nav.clientWidth / 2 + b.offsetWidth / 2); }
    });
  }
  function go(id) {
    var el = id && $(id); if (!el) return false;
    var sec = el.closest('.section'); if (!sec) return false;
    showTab(sec.id);
    var det = el.closest('details'); if (det) det.open = true;
    if (el === sec) window.scrollTo(0, 0); else el.scrollIntoView({ block: 'start' });
    return true;
  }
  function remember(id) { try { history.replaceState(null, '', '#' + id); } catch (e) {} }
  tabs.forEach(function (b) {
    b.addEventListener('click', function () { go(b.dataset.tab); remember(b.dataset.tab); });
  });
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href^="#"]') : null;
    if (!a) return;
    var id = a.getAttribute('href').slice(1);
    if (go(id)) { e.preventDefault(); remember(id); }
  });
  window.addEventListener('hashchange', function () { go(location.hash.slice(1)); });
  if (!go(location.hash.slice(1))) showTab(sections.length ? sections[0].id : '');

  /* ── One language choice for every code block ── */
  var langBtns = all('.lang-tab, .lang-global');
  function setLang(l, anchor) {
    var before = anchor ? anchor.getBoundingClientRect().top : 0;
    body.setAttribute('data-lang', l);
    langBtns.forEach(function (b) {
      var on = b.dataset.l === l;
      b.classList.toggle('active', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    if (anchor) window.scrollBy(0, anchor.getBoundingClientRect().top - before);
    save('dsa-lang', l);
  }
  langBtns.forEach(function (b) {
    b.addEventListener('click', function () { setLang(b.dataset.l, b.classList.contains('lang-tab') ? b : null); });
  });
  setLang(load('dsa-lang') === 'java' ? 'java' : 'py');

  /* ── Copy ── */
  document.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('.copy') : null;
    if (!b) return;
    var pre = all('pre', b.closest('.code')).filter(function (p) { return p.offsetParent !== null; })[0];
    if (!pre) return;
    function flash(t) { b.textContent = t; setTimeout(function () { b.textContent = 'Copy'; }, 1400); }
    function selectIt() {
      var r = document.createRange(); r.selectNodeContents(pre);
      var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); flash('Selected');
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(pre.textContent).then(function () { flash('Copied'); }, selectIt);
    } else selectIt();
  });

  /* ── Theme ── */
  function currentTheme() {
    return root.getAttribute('data-theme') ||
      (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  }
  var tb = $('theme-btn');
  if (tb) tb.addEventListener('click', function () {
    var next = currentTheme() === 'light' ? 'dark' : 'light';
    root.setAttribute('data-theme', next); save('dsa-theme', next);
  });
  var savedTheme = load('dsa-theme');
  if (savedTheme === 'light' || savedTheme === 'dark') root.setAttribute('data-theme', savedTheme);

  /* ── Practice mode ── */
  var pm = $('practice-mode');
  if (pm) pm.addEventListener('change', function () {
    body.classList.toggle('practice', pm.checked);
    if (!pm.checked) all('.problem.revealed').forEach(function (c) { c.classList.remove('revealed'); });
  });
  all('.reveal-btn').forEach(function (b) {
    b.addEventListener('click', function () { b.closest('.problem').classList.add('revealed'); });
  });

  /* ── Checklist ── */
  var boxes = all('ul.checklist input');
  var checks = {}; try { checks = JSON.parse(load('dsa-checks-' + KEY) || '{}') || {}; } catch (e) { checks = {}; }
  function progress() {
    var done = boxes.filter(function (c) { return c.checked; }).length;
    var pt = $('prog-text'), pb = $('prog-bar');
    if (pt) pt.textContent = done + ' / ' + boxes.length;
    if (pb) pb.style.width = (boxes.length ? done / boxes.length * 100 : 0) + '%';
  }
  boxes.forEach(function (c) {
    if (checks[c.id]) c.checked = true;
    c.addEventListener('change', function () { checks[c.id] = c.checked; save('dsa-checks-' + KEY, JSON.stringify(checks)); progress(); });
  });
  progress();
})();
