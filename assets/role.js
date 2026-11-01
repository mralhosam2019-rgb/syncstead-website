// "Syncstead for…" role tabs on the home page. The chosen role is remembered in this visitor's browser
// only (localStorage), reopens on return visits, and is sent with the demo request.
(function () {
  var KEY = 'syncstead_role';
  var ar = document.documentElement.lang === 'ar';
  var NAMES = ar ? { lead: 'القيادة', hr: 'الموارد البشرية', fin: 'المالية', it: 'تقنية المعلومات' } : { lead: 'Leadership', hr: 'HR', fin: 'Finance', it: 'IT' };
  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  var list = document.querySelector('.rtabs');
  if (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role=tab]'));
    function show(k, focus) {
      tabs.forEach(function (t) {
        var on = t.getAttribute('data-role') === k;
        t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
        if (on && focus) t.focus();
      });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { var k = t.getAttribute('data-role'); show(k); set(k); });
      t.addEventListener('keydown', function (e) {
        var d = (e.key === 'ArrowRight') !== ar ? 1 : (e.key === 'ArrowLeft' || e.key === 'ArrowRight') ? -1 : 0;
        if (!d) return; e.preventDefault();
        var n = tabs[(i + d + tabs.length) % tabs.length]; show(n.getAttribute('data-role'), true); set(n.getAttribute('data-role'));
      });
    });
    var saved = get(); show(saved && NAMES[saved] ? saved : tabs[0].getAttribute('data-role'));
  }
  // Demo form: send the role along
  var f = document.getElementById('demo'), r = get();
  if (f && r && NAMES[r]) {
    var h = f.querySelector('input[name=role]');
    if (!h) { h = document.createElement('input'); h.type = 'hidden'; h.name = 'role'; f.appendChild(h); }
    h.value = NAMES[r];
  }
})();
