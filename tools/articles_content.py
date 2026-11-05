"""Article content for tools/articles.py. Facts checked against the sources linked at the end of each article."""

MUDAD_SRC_EN = ('<p class="note">For general information, not legal advice. Sources: '
 '<a href="https://www.hrsd.gov.sa/media-center/news/769565" target="_blank" rel="noopener">Ministry of Human Resources (Mudad launch, Nov 2020)</a>, '
 '<a href="https://hrsd.gov.sa/en/ministry-services/services/wage-protection-file-upload-service" target="_blank" rel="noopener">Ministry service: wage protection file upload</a>, '
 '<a href="https://www.deloitte.com/middle-east/en/services/tax/perspectives/update-on-wage-protection-system-file-uploading-period.html" target="_blank" rel="noopener">Deloitte (30-day upload period)</a>, '
 '<a href="https://gulfnews.com/world/gulf/saudi/saudi-arabia-flags-unreasonable-wages-and-delayed-payments-as-payroll-violations-1.500233626" target="_blank" rel="noopener">Gulf News (alerts and violations, Aug 2025)</a>, '
 '<a href="https://saudigazette.com.sa/article/632102/SAUDI-ARABIA/Mudad-launches-new-update-on-calculating-wage-protection-compliance-rates" target="_blank" rel="noopener">Saudi Gazette (compliance rate)</a>.</p>')
MUDAD_SRC_AR = MUDAD_SRC_EN.replace("For general information, not legal advice. Sources:", "للاسترشاد العام وليست استشارة قانونية. المصادر:") \
 .replace("Ministry of Human Resources (Mudad launch, Nov 2020)", "وزارة الموارد البشرية: تدشين مدد (نوفمبر 2020)") \
 .replace("Ministry service: wage protection file upload", "خدمة رفع ملف حماية الأجور") \
 .replace("Deloitte (30-day upload period)", "Deloitte: مهلة 30 يوماً") \
 .replace("Gulf News (alerts and violations, Aug 2025)", "Gulf News: التنبيهات والمخالفات (أغسطس 2025)") \
 .replace("Saudi Gazette (compliance rate)", "Saudi Gazette: نسبة الالتزام")

ARTICLES = {
 "mudad-wage-protection": {
  "date": "2026-11-05",
  "en": dict(
   title="Mudad and the Wage Protection Program: employer guide | Syncstead",
   desc="Mudad upload deadline, alert timeline, violations, compliance rate and penalties for salary delays under the Saudi Wage Protection Program.",
   h1="Mudad and the Wage Protection Program: a practical guide for employers",
   date_label="5 November 2026", read="5 min read",
   lead="What payroll teams need to upload the wage protection file on time, keep the compliance rate up and avoid service suspensions.",
   body="""<h2>What is Mudad?</h2>
<p>Mudad is the Ministry of Human Resources and Social Development's platform for managing and protecting private-sector wages. It has been the official interface of the Wage Protection Program since 1 November 2020. The program covered more than 900,000 establishments and 8.5 million employees at the end of 2024.</p>
<p>After a wage file is uploaded, the establishment sees its compliance rate, violations and alerts straight away, and the file is checked against social insurance data.</p>
<h2>Upload deadline: 30 days</h2>
<p>From 1 March 2025 the Ministry cut the period for uploading the wage protection file from 60 days to <strong>30 days</strong>. Set your internal payroll cutoff a few days earlier so there is time to fix errors.</p>
<h2>Alerts when the file is late</h2>
<table><thead><tr><th>When</th><th>What happens</th></tr></thead><tbody>
<tr><td>Due date</td><td>Initial reminder</td></tr>
<tr><td>Day 10</td><td>Second notice</td></tr>
<tr><td>Day 15</td><td>Final warning</td></tr>
<tr><td>Day 20</td><td>Inspection request. The employer has 10 days to justify the delay; the employee has 3 days to accept or reject it, and the reason is accepted if there is no reply.</td></tr></tbody></table>
<h2>What counts as a violation</h2>
<ul><li>Unreasonably high or low wages compared with prevailing levels.</li>
<li>Deductions above half of an employee's pay.</li>
<li>Basic wage not recorded for more than 90 days.</li>
<li>Wages not paid, or payment not documented.</li></ul>
<h2>If salaries are delayed</h2>
<table><thead><tr><th>Delay</th><th>Effect</th></tr></thead><tbody>
<tr><td>Two consecutive months</td><td>Ministry services suspended, except issuing and renewing work permits</td></tr>
<tr><td>More than 3 months</td><td>All services suspended; employees may move to another employer without consent</td></tr></tbody></table>
<h2>How the compliance rate is calculated</h2>
<p>Compliance rate = compliant workers ÷ covered workers × 100. Some groups are excluded, including workers on probation, those posted outside Saudi Arabia and those who did not complete a full month.</p>
<h2>How to upload the file</h2>
<ol><li>Sign in to Mudad and select your establishment.</li>
<li>Open "Upload Files", then "Upload New File".</li>
<li>Choose the wage type and month, select the file and confirm. It is processed immediately.</li>
<li>Check the result under "Compliance Information".</li></ol>
<div class="article-cta"><h3>Mudad-ready files, every month</h3><p>Syncstead runs payroll and produces ready files for Mudad and bank upload, in Arabic and English.</p><a class="btn" href="/en/demo/?from=article-mudad">Request a demo</a> <a class="btn line" href="/en/final-settlement-calculator/">Free settlement calculator</a></div>
""" + MUDAD_SRC_EN,
  ),
  "ar": dict(
   title="منصة مدد وبرنامج حماية الأجور: دليل أصحاب العمل | سينكستيد",
   desc="مهلة رفع ملف حماية الأجور في مدد، جدول التنبيهات، المخالفات، نسبة الالتزام وعواقب تأخير الرواتب في السعودية.",
   h1="منصة مدد وبرنامج حماية الأجور: الدليل العملي لأصحاب العمل",
   date_label="5 نوفمبر 2026", read="قراءة 5 دقائق",
   lead="ما يحتاجه فريق الرواتب لرفع ملف حماية الأجور في موعده، والحفاظ على نسبة الالتزام، وتجنّب إيقاف الخدمات.",
   body="""<h2>ما هي منصة مدد؟</h2>
<p>مدد منصة وزارة الموارد البشرية والتنمية الاجتماعية لإدارة الأجور وحمايتها في القطاع الخاص، وهي الواجهة الرسمية لبرنامج حماية الأجور منذ 1 نوفمبر 2020. وكان البرنامج يغطي أكثر من 900 ألف منشأة و8.5 مليون موظف بنهاية 2024.</p>
<p>بعد رفع ملف الأجور تظهر للمنشأة نسبة الالتزام والمخالفات والتنبيهات مباشرة، ويُطابَق الملف مع بيانات التأمينات الاجتماعية.</p>
<h2>مهلة الرفع: 30 يوماً</h2>
<p>اعتباراً من 1 مارس 2025 خفّضت الوزارة مهلة رفع ملف حماية الأجور من 60 يوماً إلى <strong>30 يوماً</strong>. اجعل موعد إقفال الرواتب الداخلي قبلها بأيام حتى يبقى وقت لتصحيح الأخطاء.</p>
<h2>التنبيهات عند التأخر في رفع الملف</h2>
<table><thead><tr><th>متى</th><th>ماذا يحدث</th></tr></thead><tbody>
<tr><td>يوم الاستحقاق</td><td>تذكير أولي</td></tr>
<tr><td>اليوم 10</td><td>إشعار ثانٍ</td></tr>
<tr><td>اليوم 15</td><td>إنذار نهائي</td></tr>
<tr><td>اليوم 20</td><td>طلب تفتيش. للمنشأة 10 أيام لتبرير التأخير، وللموظف 3 أيام لقبول التبرير أو رفضه، ويُعتمد التبرير إذا لم يرد.</td></tr></tbody></table>
<h2>ما الذي يُسجَّل كمخالفة</h2>
<ul><li>أجور غير منطقية، مرتفعة جداً أو منخفضة جداً مقارنة بالمستويات السائدة.</li>
<li>استقطاعات تتجاوز نصف أجر الموظف.</li>
<li>عدم تسجيل الأجر الأساسي لأكثر من 90 يوماً.</li>
<li>عدم صرف الأجور أو عدم توثيق صرفها.</li></ul>
<h2>عند تأخير الرواتب</h2>
<table><thead><tr><th>مدة التأخير</th><th>الأثر</th></tr></thead><tbody>
<tr><td>شهران متتاليان</td><td>إيقاف خدمات الوزارة، باستثناء إصدار وتجديد رخص العمل</td></tr>
<tr><td>أكثر من 3 أشهر</td><td>إيقاف جميع الخدمات، ويحق للموظفين الانتقال إلى صاحب عمل آخر دون موافقة المنشأة</td></tr></tbody></table>
<h2>كيف تُحسب نسبة الالتزام</h2>
<p>نسبة الالتزام = عدد العمال الملتزَم بهم ÷ عدد العمال المشمولين × 100. ويُستثنى بعض الفئات، منها العاملون تحت التجربة، والمنتدبون خارج المملكة، ومن لم يكملوا شهراً كاملاً.</p>
<h2>خطوات رفع الملف</h2>
<ol><li>سجّل الدخول إلى مدد واختر المنشأة.</li>
<li>افتح «رفع الملفات» ثم «رفع ملف جديد».</li>
<li>حدّد نوع الأجر والشهر، واختر الملف وأكّد. تتم المعالجة فوراً.</li>
<li>راجع النتيجة من «معلومات الالتزام».</li></ol>
<div class="article-cta"><h3>ملفات جاهزة لمدد كل شهر</h3><p>سينكستيد يدير الرواتب ويُصدر ملفات جاهزة للرفع على مدد وللبنك، بالعربية والإنجليزية.</p><a class="btn" href="/ar/demo/?from=article-mudad">اطلب عرضاً توضيحياً</a> <a class="btn line" href="/ar/final-settlement-calculator/">حاسبة المخالصة المجانية</a></div>
""" + MUDAD_SRC_AR,
  ),
 },
}

# ---------------------------------------------------------------- Payroll guide
PAY_SRC_EN = ('<p class="note">For general information, not legal advice. Sources: '
 '<a href="https://www.hrsd.gov.sa/knowledge-centre/articles/313" target="_blank" rel="noopener">Ministry of Human Resources (overtime)</a>, '
 '<a href="https://www.hrsd.gov.sa/en/knowledge-centre/articles/325" target="_blank" rel="noopener">Ministry of Human Resources (sick leave)</a>, '
 '<a href="https://www.gosi.gov.sa/GOSIOnline/FAQ_Employer&amp;locale=en_US" target="_blank" rel="noopener">GOSI employer FAQ</a>, '
 '<a href="https://www.argaam.com/en/article/articledetail/id/1824657" target="_blank" rel="noopener">Argaam (new GOSI rates)</a>, '
 '<a href="https://www.deloitte.com/middle-east/en/services/tax/perspectives/update-on-wage-protection-system-file-uploading-period.html" target="_blank" rel="noopener">Deloitte (Mudad 30 days)</a>.</p>')
PAY_SRC_AR = PAY_SRC_EN.replace("For general information, not legal advice. Sources:", "للاسترشاد العام وليست استشارة قانونية. المصادر:") \
 .replace("Ministry of Human Resources (overtime)", "وزارة الموارد البشرية: العمل الإضافي") \
 .replace("Ministry of Human Resources (sick leave)", "وزارة الموارد البشرية: الإجازة المرضية") \
 .replace("GOSI employer FAQ", "التأمينات الاجتماعية: أسئلة أصحاب العمل") \
 .replace("Argaam (new GOSI rates)", "أرقام: نسب التأمينات الجديدة") \
 .replace("Deloitte (Mudad 30 days)", "Deloitte: مهلة مدد 30 يوماً")

GOSI_TABLE_EN = """<table><thead><tr><th>Employee</th><th>Employee share</th><th>Employer share</th></tr></thead><tbody>
<tr><td>Saudi, registered before 3 July 2024</td><td>9.75%</td><td>11.75%</td></tr>
<tr><td>Saudi, first registered on or after 3 July 2024 (from July 2026)</td><td>10.75%</td><td>12.75%</td></tr>
<tr><td>Non-Saudi</td><td>0%</td><td>2%</td></tr></tbody></table>"""
GOSI_TABLE_AR = """<table><thead><tr><th>الموظف</th><th>حصة الموظف</th><th>حصة صاحب العمل</th></tr></thead><tbody>
<tr><td>سعودي مسجل قبل 3 يوليو 2024</td><td>9.75%</td><td>11.75%</td></tr>
<tr><td>سعودي أول تسجيل له في 3 يوليو 2024 أو بعده (من يوليو 2026)</td><td>10.75%</td><td>12.75%</td></tr>
<tr><td>غير سعودي</td><td>0%</td><td>2%</td></tr></tbody></table>"""

ARTICLES["payroll-saudi-arabia"] = {
  "date": "2026-11-05",
  "en": dict(
   title="How to run payroll in Saudi Arabia: monthly checklist | Syncstead",
   desc="A monthly payroll checklist for Saudi companies: wage components, overtime, sick leave, deductions, GOSI contributions and the Mudad wage protection file.",
   h1="How to run payroll in Saudi Arabia: a monthly checklist",
   date_label="5 November 2026", read="6 min read",
   lead="Eight steps that take a Saudi payroll run from attendance to the bank transfer, with the rules that apply at each step.",
   body="""<h2>1. Confirm each employee's wage</h2>
<p>Under the Labour Law the wage is the actual wage: basic pay plus allowances such as housing and transport. Keep the basic wage and each allowance as separate items, because different rules use different parts of the wage.</p>
<h2>2. Add overtime</h2>
<p>Each overtime hour is paid at the hourly wage plus 50% of the basic hourly wage (Article 107). Hours worked on official holidays and Eids count as overtime. Common practice divides the monthly wage by 30 days and by 8 hours to get the hourly wage. The Ministry cites a limit of 720 overtime hours a year.</p>
<p><a href="/en/overtime-calculator/">Open the overtime calculator</a></p>
<h2>3. Apply leave and absences</h2>
<ul><li><strong>Annual leave:</strong> 21 days a year, 30 days after 5 consecutive years (Article 109).</li>
<li><strong>Sick leave:</strong> within one year, whether continuous or not: first 30 days at full pay, next 60 days at 75%, next 30 days unpaid (Article 117).</li>
<li><strong>Maternity leave:</strong> 12 weeks at full pay since the 2025 amendments.</li></ul>
<h2>4. Apply deductions</h2>
<p>Deduct loans, advances and penalties only where the law allows. Deductions above half of an employee's pay are flagged as a violation in Mudad.</p>
<h2>5. Calculate GOSI contributions</h2>
<p>Contributions are based on basic pay plus housing allowance, between SAR 1,500 (SAR 400 for non-Saudis) and SAR 45,000 a month.</p>
""" + GOSI_TABLE_EN + """
<p><a href="/en/gosi-calculator/">Open the GOSI calculator</a></p>
<h2>6. Work out net pay</h2>
<p>Net pay = wage + overtime and other earnings − unpaid leave − deductions − the employee's GOSI share. Accrue the end-of-service award for each employee every month so the liability is always known.</p>
<h2>7. Upload the wage protection file to Mudad</h2>
<p>Upload the file within 30 days (the period since 1 March 2025). Mudad checks it against GOSI data and shows your compliance rate straight away. <a href="/en/articles/mudad-wage-protection/">Read the Mudad guide</a></p>
<h2>8. Pay and keep records</h2>
<p>Pay salaries by bank transfer through the wage protection system and give each employee a payslip. Keep payroll records for every month.</p>
<div class="article-cta"><h3>Run payroll in one place</h3><p>Syncstead handles payroll, GOSI, leave and end of service, with ready files for Mudad and bank upload, in Arabic and English.</p><a class="btn" href="/en/demo/?from=article-payroll">Request a demo</a> <a class="btn line" href="/en/final-settlement-calculator/">Free settlement calculator</a></div>
""" + PAY_SRC_EN,
  ),
  "ar": dict(
   title="كيف تُعدّ مسير الرواتب في السعودية: قائمة شهرية | سينكستيد",
   desc="قائمة شهرية لإعداد مسير الرواتب في الشركات السعودية: مكونات الأجر، العمل الإضافي، الإجازات، الاستقطاعات، اشتراكات التأمينات وملف حماية الأجور في مدد.",
   h1="كيف تُعدّ مسير الرواتب في السعودية: قائمة شهرية",
   date_label="5 نوفمبر 2026", read="قراءة 6 دقائق",
   lead="ثماني خطوات تأخذ مسير الرواتب من الحضور إلى التحويل البنكي، مع القواعد التي تنطبق في كل خطوة.",
   body="""<h2>1. تأكد من أجر كل موظف</h2>
<p>الأجر في نظام العمل هو الأجر الفعلي: الأجر الأساسي مضافاً إليه البدلات مثل السكن والنقل. احتفظ بالأجر الأساسي وكل بدل كبنود منفصلة، لأن القواعد المختلفة تعتمد على أجزاء مختلفة من الأجر.</p>
<h2>2. أضف العمل الإضافي</h2>
<p>تُدفع كل ساعة إضافية بأجر الساعة مضافاً إليه 50% من الأجر الأساسي للساعة (المادة 107). وتُعد ساعات العمل في الأعياد والعطلات الرسمية ساعات إضافية. والممارسة الشائعة قسمة الأجر الشهري على 30 يوماً ثم على 8 ساعات لاستخراج أجر الساعة. وتشير الوزارة إلى حد أقصى قدره 720 ساعة إضافية في السنة.</p>
<p><a href="/ar/overtime-calculator/">افتح حاسبة العمل الإضافي</a></p>
<h2>3. طبّق الإجازات والغياب</h2>
<ul><li><strong>الإجازة السنوية:</strong> 21 يوماً في السنة، و30 يوماً بعد 5 سنوات متصلة (المادة 109).</li>
<li><strong>الإجازة المرضية:</strong> خلال السنة الواحدة متصلة أو متقطعة: أول 30 يوماً بأجر كامل، ثم 60 يوماً بثلاثة أرباع الأجر، ثم 30 يوماً دون أجر (المادة 117).</li>
<li><strong>إجازة الوضع:</strong> 12 أسبوعاً بأجر كامل منذ تعديلات 2025.</li></ul>
<h2>4. طبّق الاستقطاعات</h2>
<p>اقتطع السلف والقروض والجزاءات في الحدود التي يسمح بها النظام فقط. والاستقطاع الذي يتجاوز نصف أجر الموظف يُسجَّل مخالفة في مدد.</p>
<h2>5. احسب اشتراكات التأمينات الاجتماعية</h2>
<p>تُحسب الاشتراكات على الأجر الأساسي مضافاً إليه بدل السكن، بين 1,500 ريال (400 ريال لغير السعوديين) و45,000 ريال شهرياً.</p>
""" + GOSI_TABLE_AR + """
<p><a href="/ar/gosi-calculator/">افتح حاسبة التأمينات</a></p>
<h2>6. احسب صافي الراتب</h2>
<p>صافي الراتب = الأجر + العمل الإضافي والمستحقات الأخرى − الإجازات غير المدفوعة − الاستقطاعات − حصة الموظف في التأمينات. واحسب مخصص مكافأة نهاية الخدمة لكل موظف شهرياً حتى يبقى الالتزام معروفاً دائماً.</p>
<h2>7. ارفع ملف حماية الأجور على مدد</h2>
<p>ارفع الملف خلال 30 يوماً (المهلة المعمول بها منذ 1 مارس 2025). تطابق مدد الملف مع بيانات التأمينات وتعرض نسبة الالتزام مباشرة. <a href="/ar/articles/mudad-wage-protection/">اقرأ دليل مدد</a></p>
<h2>8. اصرف الرواتب واحتفظ بالسجلات</h2>
<p>اصرف الرواتب بالتحويل البنكي عبر نظام حماية الأجور، وسلّم كل موظف قسيمة راتبه. واحتفظ بسجلات الرواتب لكل شهر.</p>
<div class="article-cta"><h3>مسير الرواتب في مكان واحد</h3><p>سينكستيد يدير الرواتب والتأمينات والإجازات ونهاية الخدمة، مع ملفات جاهزة للرفع على مدد وللبنك، بالعربية والإنجليزية.</p><a class="btn" href="/ar/demo/?from=article-payroll">اطلب عرضاً توضيحياً</a> <a class="btn line" href="/ar/final-settlement-calculator/">حاسبة المخالصة المجانية</a></div>
""" + PAY_SRC_AR,
  ),
}

# ---------------------------------------------------------------- Labour law hub
LAW_SRC_EN = ('<p class="note">For general information, not legal advice. Sources: '
 '<a href="https://www.uqn.gov.sa/details?p=25379" target="_blank" rel="noopener">Umm Al-Qura gazette (2025 amendments)</a>, '
 '<a href="https://hrsd.gov.sa/ar/knowledge-centre/articles/312" target="_blank" rel="noopener">Ministry of Human Resources (work conditions)</a>, '
 '<a href="https://www.hrsd.gov.sa/en/knowledge-centre/articles/325" target="_blank" rel="noopener">Ministry of Human Resources (sick leave)</a>, '
 '<a href="https://www.kslaw.com/insights/articles/amendments-to-the-saudi-labor-law-approved" target="_blank" rel="noopener">King &amp; Spalding</a>, '
 '<a href="https://tamimi.com/news/key-amendments-to-saudi-arabias-labour-law" target="_blank" rel="noopener">Al Tamimi &amp; Company</a>.</p>')
LAW_SRC_AR = LAW_SRC_EN.replace("For general information, not legal advice. Sources:", "للاسترشاد العام وليست استشارة قانونية. المصادر:") \
 .replace("Umm Al-Qura gazette (2025 amendments)", "جريدة أم القرى: تعديلات 2025") \
 .replace("Ministry of Human Resources (work conditions)", "وزارة الموارد البشرية: شروط العمل") \
 .replace("Ministry of Human Resources (sick leave)", "وزارة الموارد البشرية: الإجازة المرضية")

ARTICLES["saudi-labour-law"] = {
  "date": "2026-11-05",
  "en": dict(
   title="Saudi Labour Law 2026: key rules for employers | Syncstead",
   desc="The Saudi Labour Law rules employers use most, updated for the February 2025 amendments: hours, overtime, leave, maternity, probation, notice and end of service.",
   h1="Saudi Labour Law 2026: the key rules for employers",
   date_label="5 November 2026", read="6 min read",
   lead="The rules HR teams apply every month, with the article number and what changed in the amendments that took effect in February 2025.",
   body="""<h2>Working time</h2>
<table><thead><tr><th>Rule</th><th>What the law says</th><th>Article</th></tr></thead><tbody>
<tr><td>Normal hours</td><td>Up to 8 hours a day or 48 a week</td><td>98</td></tr>
<tr><td>Ramadan (Muslim employees)</td><td>Up to 6 hours a day or 36 a week</td><td>98</td></tr>
<tr><td>Weekly rest</td><td>Friday, paid, at least 24 hours in a row; can be moved for some workers after notifying the Labour Office</td><td>104</td></tr>
<tr><td>Overtime</td><td>Hourly wage plus 50% of the basic wage; holidays and Eids count as overtime. Since 2025 the parties can agree on paid time off instead.</td><td>107</td></tr></tbody></table>
<h2>Leave</h2>
<table><thead><tr><th>Leave</th><th>Entitlement</th><th>Article</th></tr></thead><tbody>
<tr><td>Annual</td><td>21 days a year; 30 days after 5 consecutive years. Unused leave is paid when employment ends.</td><td>109, 111</td></tr>
<tr><td>Sick</td><td>Within one year, continuous or not: 30 days full pay, then 60 days at 75%, then 30 days unpaid</td><td>117</td></tr>
<tr><td>Maternity</td><td><strong>12 weeks at full pay</strong> (10 weeks before 2025); 6 weeks must be taken after the birth</td><td>151</td></tr>
<tr><td>Paternity</td><td>3 days at full pay, taken within 7 days of the birth</td><td>113</td></tr>
<tr><td>Marriage</td><td>5 days at full pay</td><td>113</td></tr>
<tr><td>Bereavement</td><td>5 days for a spouse, ascendant or descendant (for example a parent, grandparent, child or grandchild); <strong>3 days for a brother or sister</strong> (new in 2025)</td><td>113</td></tr>
<tr><td>Hajj</td><td>10 to 15 days including the Eid al-Adha holiday, once, after 2 consecutive years of service</td><td>114</td></tr>
<tr><td>Exams</td><td>Paid for exam days in a year the student is not repeating; request at least 15 days ahead</td><td>115</td></tr></tbody></table>
<h2>Contracts and ending employment</h2>
<table><thead><tr><th>Rule</th><th>What the law says</th><th>Article</th></tr></thead><tbody>
<tr><td>Probation</td><td>Must be stated in the contract and cannot exceed <strong>180 days</strong> in total (changed in 2025)</td><td>53</td></tr>
<tr><td>Notice (open-ended contracts, monthly paid)</td><td><strong>At least 30 days</strong> from the employee and <strong>at least 60 days</strong> from the employer (changed in 2025)</td><td>75</td></tr>
<tr><td>Resignation</td><td>For fixed-term contracts: treated as accepted if the employer does not reply within 30 days; the employer can postpone acceptance by up to 60 days if business needs require it, with written reasons; the employee can withdraw within 7 days if not yet accepted (new in 2025)</td><td>79 bis</td></tr>
<tr><td>End-of-service award</td><td>Half a month's wage for each of the first 5 years, a month's wage for each year after; reduced on resignation</td><td>84, 85</td></tr></tbody></table>
<h2>Free tools</h2>
<ul><li><a href="/en/end-of-service-calculator/">End-of-service calculator</a></li>
<li><a href="/en/leave-balance-calculator/">Annual leave balance calculator</a></li>
<li><a href="/en/overtime-calculator/">Overtime pay calculator</a></li>
<li><a href="/en/gosi-calculator/">GOSI contribution calculator</a></li></ul>
<div class="article-cta"><h3>Keep every rule up to date automatically</h3><p>Syncstead applies leave, overtime, GOSI and end-of-service rules in payroll, in Arabic and English.</p><a class="btn" href="/en/demo/?from=article-labour-law">Request a demo</a></div>
""" + LAW_SRC_EN,
  ),
  "ar": dict(
   title="نظام العمل السعودي 2026: أهم القواعد لأصحاب العمل | سينكستيد",
   desc="أكثر قواعد نظام العمل السعودي استخداماً بعد تعديلات فبراير 2025: ساعات العمل، العمل الإضافي، الإجازات، إجازة الوضع، فترة التجربة، الإشعار ونهاية الخدمة.",
   h1="نظام العمل السعودي 2026: أهم القواعد لأصحاب العمل",
   date_label="5 نوفمبر 2026", read="قراءة 6 دقائق",
   lead="القواعد التي تطبقها فرق الموارد البشرية كل شهر، مع رقم المادة وما تغيّر في التعديلات النافذة منذ فبراير 2025.",
   body="""<h2>وقت العمل</h2>
<table><thead><tr><th>القاعدة</th><th>ما ينص عليه النظام</th><th>المادة</th></tr></thead><tbody>
<tr><td>ساعات العمل</td><td>حتى 8 ساعات يومياً أو 48 ساعة أسبوعياً</td><td>98</td></tr>
<tr><td>رمضان (للمسلمين)</td><td>حتى 6 ساعات يومياً أو 36 ساعة أسبوعياً</td><td>98</td></tr>
<tr><td>الراحة الأسبوعية</td><td>يوم الجمعة بأجر كامل ولمدة 24 ساعة متصلة على الأقل، ويجوز تغييره لبعض العمال بعد إبلاغ مكتب العمل</td><td>104</td></tr>
<tr><td>العمل الإضافي</td><td>أجر الساعة مضافاً إليه 50% من الأجر الأساسي، وتُعد الأعياد والعطلات الرسمية عملاً إضافياً. ومنذ 2025 يجوز الاتفاق على إجازة مدفوعة بدلاً من الأجر.</td><td>107</td></tr></tbody></table>
<h2>الإجازات</h2>
<table><thead><tr><th>الإجازة</th><th>الاستحقاق</th><th>المادة</th></tr></thead><tbody>
<tr><td>السنوية</td><td>21 يوماً في السنة، و30 يوماً بعد 5 سنوات متصلة. ويُدفع أجر الأيام غير المستخدمة عند انتهاء الخدمة.</td><td>109، 111</td></tr>
<tr><td>المرضية</td><td>خلال السنة الواحدة متصلة أو متقطعة: 30 يوماً بأجر كامل، ثم 60 يوماً بثلاثة أرباع الأجر، ثم 30 يوماً دون أجر</td><td>117</td></tr>
<tr><td>الوضع</td><td><strong>12 أسبوعاً بأجر كامل</strong> (كانت 10 أسابيع قبل 2025)، منها 6 أسابيع إلزامية بعد الولادة</td><td>151</td></tr>
<tr><td>المولود (للأب)</td><td>3 أيام بأجر كامل، تُؤخذ خلال 7 أيام من الولادة</td><td>113</td></tr>
<tr><td>الزواج</td><td>5 أيام بأجر كامل</td><td>113</td></tr>
<tr><td>الوفاة</td><td>5 أيام لوفاة الزوج أو أحد الأصول أو الفروع، و<strong>3 أيام لوفاة الأخ أو الأخت</strong> (جديد في 2025)</td><td>113</td></tr>
<tr><td>الحج</td><td>من 10 إلى 15 يوماً شاملة إجازة عيد الأضحى، مرة واحدة، بعد سنتين متصلتين من الخدمة</td><td>114</td></tr>
<tr><td>الامتحانات</td><td>بأجر كامل لأيام الامتحان في السنة غير المعادة، ويُقدَّم الطلب قبل 15 يوماً على الأقل</td><td>115</td></tr></tbody></table>
<h2>العقود وانتهاء العلاقة</h2>
<table><thead><tr><th>القاعدة</th><th>ما ينص عليه النظام</th><th>المادة</th></tr></thead><tbody>
<tr><td>فترة التجربة</td><td>يجب النص عليها في العقد، ولا تزيد في مجموعها على <strong>180 يوماً</strong> (تعديل 2025)</td><td>53</td></tr>
<tr><td>الإشعار (العقود غير محددة المدة، الأجر الشهري)</td><td><strong>30 يوماً على الأقل</strong> من العامل و<strong>60 يوماً على الأقل</strong> من صاحب العمل (تعديل 2025)</td><td>75</td></tr>
<tr><td>الاستقالة</td><td>في العقود محددة المدة: تُعد مقبولة إذا لم يرد صاحب العمل خلال 30 يوماً، ويجوز له تأجيل القبول حتى 60 يوماً إذا اقتضت مصلحة العمل ذلك مع بيان الأسباب كتابةً، وللعامل سحبها خلال 7 أيام ما لم تُقبل (جديد في 2025)</td><td>79 مكرر</td></tr>
<tr><td>مكافأة نهاية الخدمة</td><td>أجر نصف شهر عن كل سنة من السنوات الخمس الأولى، وأجر شهر عن كل سنة بعدها، وتُخفض عند الاستقالة</td><td>84، 85</td></tr></tbody></table>
<h2>أدوات مجانية</h2>
<ul><li><a href="/ar/end-of-service-calculator/">حاسبة مكافأة نهاية الخدمة</a></li>
<li><a href="/ar/leave-balance-calculator/">حاسبة رصيد الإجازة السنوية</a></li>
<li><a href="/ar/overtime-calculator/">حاسبة أجر العمل الإضافي</a></li>
<li><a href="/ar/gosi-calculator/">حاسبة اشتراكات التأمينات</a></li></ul>
<div class="article-cta"><h3>قواعد محدّثة تلقائياً</h3><p>سينكستيد يطبق قواعد الإجازات والعمل الإضافي والتأمينات ونهاية الخدمة داخل مسير الرواتب، بالعربية والإنجليزية.</p><a class="btn" href="/ar/demo/?from=article-labour-law">اطلب عرضاً توضيحياً</a></div>
""" + LAW_SRC_AR,
  ),
}
