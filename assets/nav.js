// Header menus: Platform and Solutions open wide panels, Resources and Company small lists.
// Laptop: open on hover (short delay) or click; Esc, a click outside or moving away closes them.
// Phone and tablet (menu button): each section opens like an accordion inside the full menu.
(function () {
  var nav = document.getElementById('nav');
  if (!nav) return;
  var items = Array.prototype.slice.call(nav.querySelectorAll('.mi'));
  var wide = window.matchMedia('(min-width: 1121px) and (hover: hover)');
  var timer;
  function close(except) {
    items.forEach(function (it) {
      if (it === except) return;
      it.classList.remove('open');
      var b = it.querySelector('.mt'); if (b) b.setAttribute('aria-expanded', 'false');
    });
  }
  function open(it) {
    close(it);
    it.classList.add('open');
    it.querySelector('.mt').setAttribute('aria-expanded', 'true');
  }
  items.forEach(function (it) {
    var b = it.querySelector('.mt');
    b.addEventListener('click', function () {
      if (it.classList.contains('open')) { it.classList.remove('open'); b.setAttribute('aria-expanded', 'false'); } else open(it);
    });
    it.addEventListener('mouseenter', function () { if (!wide.matches) return; clearTimeout(timer); timer = setTimeout(function () { open(it); }, 120); });
    it.addEventListener('mouseleave', function () { if (!wide.matches) return; clearTimeout(timer); timer = setTimeout(function () { close(); }, 200); });
    it.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { close(); b.focus(); }
      if (e.key === 'ArrowDown' && e.target === b) { e.preventDefault(); open(it); var f = it.querySelector('.mp a'); if (f) f.focus(); }
    });
  });
  document.addEventListener('click', function (e) { if (!nav.contains(e.target)) close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  wide.addEventListener && wide.addEventListener('change', function () { close(); });
})();
