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
    MailApp.sendEmail({ to: NOTIFY, subject: 'New demo request: ' + clean(p.company) + ' (' + clean(p.size) + ')', body: body, replyTo: clean(p.email) });
  } finally {
    lock.releaseLock();
  }
  return out({ ok: true });
}

function doGet() { return out({ ok: true, service: 'Syncstead demo requests' }); }
function out(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
