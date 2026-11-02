/**
 * Syncstead demo requests: receives the website's demo form, saves each request as a row in a
 * Google Sheet in the company's Google Workspace, and emails the sales inbox straight away.
 *
 * Set up once (about 2 minutes), signed in as alhosam@syncstead.com.sa:
 *  1. Open https://script.google.com → New project → name it "Syncstead demo requests".
 *  2. Replace everything in Code.gs with this file and press Save.
 *  3. Run "setup" once (▶ Run, choose setup) and allow access when Google asks.
 *     It creates the "Syncstead demo requests" sheet in your Drive.
 *  4. Deploy → New deployment → type "Web app" → Execute as: Me → Who has access: Anyone → Deploy.
 *  5. Copy the Web app URL (ends in /exec) and send it to Claude: it goes into FORM_URL in tools/gen.py.
 */
const NOTIFY = 'alhosam@syncstead.com.sa';
const SHEET_NAME = 'Syncstead demo requests';
const COLUMNS = ['Received (Riyadh)', 'Name', 'Job title', 'Work email', 'Mobile', 'Company', 'Employees', 'Package', 'Current system',
  'Priorities', 'Timeline', 'Companies / branches', 'Interest', 'From page', 'Language',
  'Source (utm_source)', 'Medium (utm_medium)', 'Campaign (utm_campaign)', 'First referrer', 'Status'];
// Columns shown in the email (all except the received time and status).
const EMAIL_FROM = 1, EMAIL_TO = COLUMNS.length - 1;

function setup() {
  const ss = SpreadsheetApp.create(SHEET_NAME);
  const sh = ss.getSheets()[0];
  sh.setName('Requests');
  sh.appendRow(COLUMNS);
  sh.setFrozenRows(1);
  sh.getRange(1, 1, 1, COLUMNS.length).setFontWeight('bold').setBackground('#1B2A4A').setFontColor('#FFFFFF');
  PropertiesService.getScriptProperties().setProperty('SHEET_ID', ss.getId());
  Logger.log('Sheet ready: ' + ss.getUrl());
}

function doPost(e) {
  const p = (e && e.parameter) || {};
  const clean = (v, n) => String(v || '').replace(/[\r\n]+/g, ' ').trim().slice(0, n || 200);
  // Ignore empty or malformed submissions.
  if (!clean(p.email).includes('@') || !clean(p.name) || !clean(p.company)) return out({ ok: false });
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const id = PropertiesService.getScriptProperties().getProperty('SHEET_ID');
    const book = SpreadsheetApp.openById(id);
    let sh = book.getSheetByName('Requests');
    // When the columns change, keep older requests in their own tab and start a fresh "Requests" tab.
    if (sh.getRange(1, 1, 1, COLUMNS.length).getValues()[0].join('|') !== COLUMNS.join('|')) {
      sh.setName('Requests (before ' + Utilities.formatDate(new Date(), 'Asia/Riyadh', 'yyyy-MM-dd') + ')');
      sh = book.insertSheet('Requests', 0);
      sh.appendRow(COLUMNS);
      sh.setFrozenRows(1);
      sh.getRange(1, 1, 1, COLUMNS.length).setFontWeight('bold').setBackground('#1B2A4A').setFontColor('#FFFFFF');
    }
    const when = Utilities.formatDate(new Date(), 'Asia/Riyadh', 'yyyy-MM-dd HH:mm');
    // A leading apostrophe stops a value being read as a formula.
    const safe = (v) => (/^[=+\-@]/.test(v) ? "'" + v : v);
    const emp = p.employees || p.size;
    // The form also copies the optional answers into "interest" (for older versions of this script): drop that copy here.
    const interest = String(p.interest || '').split(/(?:^| \| )Title: /)[0];
    const vals = [when, p.name, p.title, p.email, p.phone, p.company, emp, p.package, p.system, p.priorities, p.timeline, p.entities,
      interest, p.from, p.lang, p.utm_source, p.utm_medium, p.utm_campaign, p.referrer, 'New']
      .map((v, i) => (i === 0 ? v : clean(v, i === 18 ? 300 : 200)));
    sh.appendRow(vals.map((v, i) => (i === 0 ? v : safe(v))));
    const row = vals;
    const body = COLUMNS.slice(EMAIL_FROM, EMAIL_TO).map((c, i) => c + ': ' + (row[i + EMAIL_FROM] || '-')).join('\n') + '\n\nAll requests: ' + book.getUrl();
    const v = {}; COLUMNS.forEach((c, i) => { v[c] = row[i] || ''; });
    MailApp.sendEmail({ to: NOTIFY, subject: 'New demo request: ' + clean(p.company) + ' · ' + (emp ? clean(emp) + ' employees' : '') + (p.package ? ' · ' + clean(p.package) : ''),
      body: body, htmlBody: emailHtml(v, book.getUrl()), replyTo: clean(p.email), name: 'Syncstead website' });
  } finally {
    lock.releaseLock();
  }
  return out({ ok: true });
}

/** The notification email: Syncstead header, summary, and the request grouped into sections. Inline styles for email clients. */
function emailHtml(v, sheetUrl) {
  const esc = (t) => String(t || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  const val = (t) => (t ? esc(t) : '<span style="color:#94A3B8">Not provided</span>');
  const digits = String(v['Mobile'] || '').replace(/\D/g, '').replace(/^00/, '').replace(/^0(5\d{8})$/, '966$1');
  const navy = '#1B2A4A', teal = '#14B8A6', line = '#E2E8F0', muted = '#64748B', ink = '#0F172A';
  const rowsOf = (pairs) => pairs.map(([k, x], i) =>
    '<tr><td style="padding:10px 0;border-top:' + (i ? '1px solid ' + line : '0') + ';color:' + muted + ';font-size:13px;width:170px;vertical-align:top">' + k + '</td>' +
    '<td style="padding:10px 0;border-top:' + (i ? '1px solid ' + line : '0') + ';color:' + ink + ';font-size:14px;font-weight:600">' + x + '</td></tr>').join('');
  const section = (title, pairs) =>
    '<tr><td style="padding:22px 28px 4px"><div style="font-size:11px;letter-spacing:.12em;font-weight:700;color:#0D9488;text-transform:uppercase">' + title + '</div>' +
    '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:8px;border-collapse:collapse">' + rowsOf(pairs) + '</table></td></tr>';
  const pill = (t) => t ? '<span style="display:inline-block;background:#CCFBF1;color:#115E59;border-radius:999px;padding:4px 10px;font-size:12px;font-weight:700;margin:0 6px 6px 0">' + esc(t) + '</span>' : '';
  const prios = String(v['Priorities'] || '').split(',').map((x) => x.trim()).filter(Boolean);
  const btn = (href, label, primary) => '<a href="' + href + '" style="display:inline-block;margin:0 8px 8px 0;padding:11px 18px;border-radius:999px;font-size:14px;font-weight:700;text-decoration:none;' +
    (primary ? 'background:' + teal + ';color:' + ink : 'background:#fff;color:' + ink + ';border:1px solid ' + line) + '">' + label + '</a>';
  const first = esc(String(v['Name'] || '').split(' ')[0]);
  return '<!doctype html><html><body style="margin:0;padding:0;background:#F1F5F9;font-family:Segoe UI,Arial,sans-serif">' +
    '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F1F5F9;padding:24px 12px"><tr><td align="center">' +
    '<table role="presentation" width="640" cellpadding="0" cellspacing="0" style="max-width:640px;width:100%;background:#fff;border-radius:16px;overflow:hidden;border:1px solid ' + line + '">' +
    // header
    '<tr><td style="background:' + navy + ';padding:22px 28px"><table role="presentation" cellpadding="0" cellspacing="0"><tr>' +
    '<td style="background:' + teal + ';color:' + navy + ';font-weight:800;font-size:18px;width:34px;height:34px;text-align:center;border-radius:8px">S</td>' +
    '<td style="padding-left:12px;color:#fff;font-weight:700;font-size:16px;letter-spacing:.18em">SYNCSTEAD</td></tr></table>' +
    '<div style="margin-top:18px;color:#5EEAD4;font-size:12px;font-weight:700;letter-spacing:.12em">NEW DEMO REQUEST</div>' +
    '<div style="margin-top:6px;color:#fff;font-size:24px;font-weight:700;line-height:1.25">' + esc(v['Company']) + '</div>' +
    '<div style="margin-top:6px;color:#CBD5E1;font-size:14px">' + esc(v['Name']) + (v['Job title'] ? ' · ' + esc(v['Job title']) : '') + '</div></td></tr>' +
    // summary tiles
    '<tr><td style="padding:22px 28px 0"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>' +
    ['Employees', 'Package', 'Timeline'].map((k, i) => '<td width="33%" style="' + (i ? 'padding-left:10px;' : '') + '"><div style="background:#F8FAFC;border:1px solid ' + line + ';border-radius:12px;padding:12px 14px">' +
      '<div style="color:' + muted + ';font-size:12px">' + k + '</div><div style="color:' + ink + ';font-size:18px;font-weight:700;margin-top:2px">' + (v[k] ? esc(k === 'Employees' ? Number(v[k]).toLocaleString('en-US') : v[k]) : '–') + '</div></div></td>').join('') +
    '</tr></table></td></tr>' +
    // actions
    '<tr><td style="padding:18px 28px 0">' + btn('mailto:' + esc(v['Work email']) + '?subject=' + encodeURIComponent('Your Syncstead demo') , 'Reply to ' + first, true) +
    (digits ? btn('https://wa.me/' + digits, 'WhatsApp', false) + btn('tel:+' + digits, 'Call', false) : '') + '</td></tr>' +
    section('Contact', [['Name', val(v['Name'])], ['Job title', val(v['Job title'])], ['Work email', v['Work email'] ? '<a href="mailto:' + esc(v['Work email']) + '" style="color:#0D9488">' + esc(v['Work email']) + '</a>' : val('')], ['Mobile', val(v['Mobile'])]]) +
    section('Company', [['Company', val(v['Company'])], ['Employees', val(v['Employees'] && Number(v['Employees']).toLocaleString('en-US'))], ['Matching package', val(v['Package'])], ['Companies / branches', val(v['Companies / branches'])]]) +
    section('What they need', [['Current system', val(v['Current system'])], ['Top priorities', prios.length ? prios.map(pill).join('') : val('')], ['Timeline', val(v['Timeline'])], ['Interest', val(v['Interest'])]]) +
    section('Where they came from', [['Page', val(v['From page'])], ['Language', val(v['Language'] === 'ar' ? 'Arabic' : v['Language'] === 'en' ? 'English' : v['Language'])], ['Source', val([v['Source (utm_source)'], v['Medium (utm_medium)'], v['Campaign (utm_campaign)']].filter(Boolean).join(' / '))], ['First referrer', val(v['First referrer'])]]) +
    '<tr><td style="padding:22px 28px 26px"><div style="border-top:1px solid ' + line + ';padding-top:16px;font-size:13px;color:' + muted + '">Received ' + esc(v['Received (Riyadh)']) + ' (Riyadh) · ' +
    '<a href="' + sheetUrl + '" style="color:#0D9488;font-weight:600">Open all requests</a> · Aim to reply within one working day.</div></td></tr>' +
    '</table><div style="color:#94A3B8;font-size:12px;margin-top:14px">Sent by the demo form on syncstead.com.sa</div></td></tr></table></body></html>';
}

function doGet() { return out({ ok: true, service: 'Syncstead demo requests' }); }
function out(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
