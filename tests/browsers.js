// Cross-browser test of the website: Chrome (Chromium), Firefox, Safari (WebKit), on desktop, iPhone,
// iPad and Android sizes. Runs in GitHub Actions against a local copy of the site on port 8765.
const pw = require('playwright');
const fs = require('fs');
const B = 'http://localhost:8765';
const pages = ['', 'platform/', 'packages/', 'why-syncstead/', 'trust/', 'about/', 'resources/', 'contact/', 'demo/', 'demo/next/', 'end-of-service-calculator/', 'privacy/'];
const D = pw.devices;
const runs = [
  ['Chrome desktop', 'chromium', { viewport: { width: 1440, height: 900 } }],
  ['Edge desktop (Chromium)', 'chromium', { viewport: { width: 1280, height: 800 }, userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36 Edg/130.0' }],
  ['Firefox desktop', 'firefox', { viewport: { width: 1440, height: 900 } }],
  ['Safari desktop (WebKit)', 'webkit', { viewport: { width: 1440, height: 900 } }],
  ['Safari iPhone 13', 'webkit', D['iPhone 13']],
  ['Safari iPhone SE', 'webkit', D['iPhone SE']],
  ['Safari iPad', 'webkit', D['iPad (gen 7)']],
  ['Chrome Android (Pixel 7)', 'chromium', D['Pixel 7']],
  ['Samsung Galaxy S9+ (Chromium)', 'chromium', D['Galaxy S9+']],
  ['Firefox Android size', 'firefox', { viewport: { width: 412, height: 915 }, isMobile: false, hasTouch: true }],
];
const res = [];
(async () => {
  fs.mkdirSync('shots', { recursive: true });
  for (const [name, engine, opts] of runs) {
    const issues = [];
    const b = await pw[engine].launch();
    const phone = (opts.viewport || {}).width < 800;
    for (const lang of ['en', 'ar']) {
      const c = await b.newContext({ ...opts, locale: lang === 'ar' ? 'ar-SA' : 'en-GB' });
      const p = await c.newPage();
      p.on('pageerror', (e) => issues.push(`script error on ${p.url().replace(B, '')}: ${e.message}`));
      for (const pg of pages) {
        const r = await p.goto(`${B}/${lang}/${pg}`, { waitUntil: 'load' });
        if (!r || r.status() !== 200) issues.push(`/${lang}/${pg} → ${r && r.status()}`);
        await p.evaluate(() => document.fonts && document.fonts.ready);
        const ov = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
        if (ov > 1) issues.push(`/${lang}/${pg} scrolls sideways by ${ov}px`);
        const broken = await p.evaluate(() => [...document.images].filter((i) => i.complete && i.naturalWidth === 0 && i.loading !== 'lazy').map((i) => i.src));
        if (broken.length) issues.push(`/${lang}/${pg} broken images: ${broken.join(', ')}`);
      }
      const step = async (label, fn) => { try { await fn(); } catch (e) { issues.push(`${lang}: ${label} failed: ${String(e.message || e).split('\n')[0].slice(0, 160)}`); } };
      p.setDefaultTimeout(10000);
      // Home: role tabs
      await step('role tabs', async () => {
      await p.goto(`${B}/${lang}/`);
      await p.click('#t-fin');
      if (await p.isHidden('#p-fin')) issues.push(`${lang}: Finance tab did not open`);
      await p.reload();
      if (await p.isHidden('#p-fin')) issues.push(`${lang}: role not remembered`);
      });
      // Phone menu
      if (phone) await step('phone menu', async () => {
        await p.click('.menu-btn');
        if (!(await p.isVisible('nav.main a[href*="/trust/"]'))) issues.push(`${lang}: phone menu did not open`);
        else { await p.click('nav.main a[href*="/trust/"]'); await p.waitForURL('**/trust/'); }
      });
      // Language switch
      await step('language switch', async () => { await p.goto(`${B}/${lang}/packages/`);
      await p.click('a.lang'); await p.waitForURL(`**/${lang === 'en' ? 'ar' : 'en'}/packages/`).catch(() => issues.push(`${lang}: language switch failed`)); });
      // Demo flow
      await step('demo request', async () => {
      await p.goto(`${B}/${lang}/packages/`);
      await p.click('.pk[data-pk=enterprise] a.btn'); await p.waitForURL('**/demo/**');
      await p.click('#demo button[type=submit]');
      if (await p.isHidden('#err')) issues.push(`${lang}: empty demo form not stopped`);
      await p.fill('[name=name]', 'Test Person'); await p.fill('[name=email]', 'test@example.com'); await p.fill('[name=company]', 'Test Co');
      await p.selectOption('[name=size]', { index: 3 });
      await p.waitForTimeout(2700);
      await p.click('#demo button[type=submit]');
      await p.waitForURL('**/demo/next/**', { timeout: 10000 }).catch(() => issues.push(`${lang}: demo did not reach step 2 (${p.url()})`));
      if (!(await p.$('iframe[src*="calendar.google.com"]'))) issues.push(`${lang}: no calendar on step 2`);
      if (!/Test/.test(await p.textContent('#hi').catch(() => ''))) issues.push(`${lang}: step 2 greeting missing`);
      });
      // Calculator
      await step('calculator', async () => {
      await p.goto(`${B}/${lang}/end-of-service-calculator/`);
      await p.fill('[name=wage]', '10000'); await p.fill('[name=start]', '2020-01-01'); await p.fill('[name=end]', '2026-01-01');
      await p.click('#eos button');
      const out = (await p.textContent('#out')) || '';
      if (!/35[,٬]000|٣٥٬?٠٠٠/.test(out)) issues.push(`${lang}: calculator shows "${out.trim()}"`);
      });
      // Screenshots of home and demo
      await step('screenshots', async () => {
      const slug = name.replace(/[^a-z0-9]+/gi, '-').toLowerCase();
      await p.goto(`${B}/${lang}/`); await p.waitForTimeout(300);
      await p.screenshot({ path: `shots/${slug}-${lang}-home.png` });
      await p.goto(`${B}/${lang}/demo/`); await p.screenshot({ path: `shots/${slug}-${lang}-demo.png`, fullPage: true });
      });
      await c.close();
    }
    await b.close();
    res.push([name, issues]);
    console.log(`${issues.length ? '✗' : '✓'} ${name}: ${issues.length ? issues.length + ' issue(s)' : 'all checks passed'}`);
    for (const i of issues) console.log('   - ' + i);
  }
  const lines = res.map(([n, i]) => `${i.length ? 'FAIL' : 'PASS'} ${n}${i.length ? ': ' + i.slice(0, 4).join(' | ') : ''}`);
  fs.writeFileSync('shots/RESULTS.txt', lines.join('\n') + '\n');
  console.log(`::notice title=Browser results::${lines.join('%0A')}`);
  if (res.some(([, i]) => i.length)) process.exit(1);
})().catch((e) => { console.log(`::error title=Test crashed::${String(e).slice(0, 500)}`); process.exit(1); });
