// "Find your fit": an optional two-question panel on the home page. The answers stay in this visitor's
// browser only (localStorage) and personalize the site: the recommended package is marked, chosen
// capabilities move first, the Platform page opens with them, and the demo form is pre-filled.
(function () {
  var ar = document.documentElement.lang === 'ar';
  var KEY = 'syncstead_fit';
  var PKG = { s1: 'core', s2: 'professional', s3: 'enterprise', s4: 'enterprise' };
  var SIZE = ar ? { s1: 'أقل من 300', s2: '300–1,499', s3: '1,500–4,999', s4: '5,000+' } : { s1: 'Under 300', s2: '300–1,499', s3: '1,500–4,999', s4: '5,000+' };
  var PKN = ar ? { core: 'الأساسية', professional: 'الاحترافية', enterprise: 'المؤسسات' } : { core: 'Core', professional: 'Professional', enterprise: 'Enterprise' };
  var AREA = { payroll: 'payroll', saudization: 'payroll', attendance: 'time', talent: 'talent', org: 'org', self: 'mobile' };
  var PRI = ar ? { payroll: 'دقة الرواتب', saudization: 'التوطين', attendance: 'الحضور', talent: 'المواهب', org: 'التصميم التنظيمي', self: 'الخدمة الذاتية' }
               : { payroll: 'Payroll accuracy', saudization: 'Saudization', attendance: 'Attendance', talent: 'Talent', org: 'Org design', self: 'Self-service' };
  function load() { try { return JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { return null; } }
  function save(v) { try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) {} }
  function clear() { try { localStorage.removeItem(KEY); } catch (e) {} }

  function apply(fit) {
    if (!fit) return;
    var pk = PKG[fit.size];
    // Packages: mark the recommended one
    document.querySelectorAll('.pk[data-pk]').forEach(function (el) {
      var mine = el.getAttribute('data-pk') === pk;
      el.classList.toggle('hi', mine);
      var tag = el.querySelector('.tag');
      if (mine) { if (!tag) { tag = document.createElement('span'); tag.className = 'tag'; el.prepend(tag); } tag.textContent = ar ? 'الأنسب لكم' : 'Recommended for you'; }
      else if (tag) tag.remove();
      var b = el.querySelector('a.btn'); if (b) b.classList.toggle('line', !mine);
    });
    // Capabilities and platform sections: chosen areas first
    var areas = (fit.pri || []).map(function (p) { return AREA[p]; });
    document.querySelectorAll('.caps').forEach(function (box) {
      var items = Array.prototype.slice.call(box.children);
      items.forEach(function (a) { var h = (a.getAttribute('href') || '').split('#')[1]; a.classList.toggle('fit', areas.indexOf(h) > -1); });
      items.sort(function (a, b) { return (b.classList.contains('fit') ? 1 : 0) - (a.classList.contains('fit') ? 1 : 0); }).forEach(function (a) { box.appendChild(a); });
    });
    var feats = document.querySelector('.feature') && document.querySelector('.feature').parentNode;
    if (feats && !location.hash) {
      areas.slice().reverse().forEach(function (id) { var f = document.getElementById(id); if (f && f.classList.contains('feature')) feats.insertBefore(f, feats.firstChild); });
    }
    // Home: summary line
    var out = document.getElementById('fit-result');
    if (out) {
      var pri = (fit.pri || []).map(function (p) { return PRI[p]; }).join(ar ? '، ' : ', ');
      out.innerHTML = (ar ? 'لمنشأة من ' + SIZE[fit.size] + ' موظف، نوصي بباقة <b>' + PKN[pk] + '</b>' : 'For a company of ' + SIZE[fit.size] + ' employees, we recommend <b>' + PKN[pk] + '</b>')
        + (pri ? (ar ? '، مع التركيز على ' + pri + '.' : ', focused on ' + pri + '.') : '.')
        + ' <a href="' + (ar ? '/ar/packages/' : '/en/packages/') + '">' + (ar ? 'قارن الباقات' : 'Compare packages') + '</a> · <a href="#" id="fit-reset">' + (ar ? 'تغيير' : 'Change') + '</a>';
      out.hidden = false;
      var r = document.getElementById('fit-reset');
      if (r) r.addEventListener('click', function (e) { e.preventDefault(); clear(); location.reload(); });
      var form = document.getElementById('fit-form'); if (form) form.hidden = true;
    }
    // Demo form: pre-fill
    var f = document.getElementById('demo');
    if (f) {
      if (fit.size === 's4' && f.size) f.size.value = '5,000+';
      var h = f.querySelector('input[name=priorities]');
      if (!h) { h = document.createElement('input'); h.type = 'hidden'; h.name = 'priorities'; f.appendChild(h); }
      h.value = (fit.pri || []).map(function (p) { return PRI[p]; }).join(', ') + ' · ' + SIZE[fit.size];
    }
  }

  // Home panel
  var form = document.getElementById('fit-form');
  if (form) {
    form.addEventListener('change', function () {
      var on = form.querySelectorAll('input[name=pri]:checked');
      form.querySelectorAll('input[name=pri]').forEach(function (i) { i.disabled = !i.checked && on.length >= 3; });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var s = form.querySelector('input[name=size]:checked');
      if (!s) { form.querySelector('.fit-err').hidden = false; return; }
      var pri = Array.prototype.map.call(form.querySelectorAll('input[name=pri]:checked'), function (i) { return i.value; });
      var fit = { size: s.value, pri: pri };
      save(fit); apply(fit);
    });
  }
  apply(load());
})();
