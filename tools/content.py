"""Page content for the Syncstead website, English and Arabic. Used by gen.py."""

def G():
    import gen
    return gen

BOOK = "https://calendar.google.com/calendar/u/0/appointments/schedules/AcZssZ2sW2kQ_5vAHw4p-v_kQ_gorsm-WFrjHmKt5hXqJT4UEJEq7yGhmZTgFgKtR7djox9nANAhFusb"
WA = "https://wa.me/966553179126"

# ---------------------------------------------------------------- shared text blocks, per language
TX = {
"en": {
 "caps": [("users","Core HR & employee files","platform#core"),("pay","Payroll & end of service","platform#payroll"),("time","Time, attendance & leave","platform#time"),
          ("star","Recruiting, performance & learning","platform#talent"),("org","Org design & workforce planning","platform#org"),("pay","Compensation & rewards","platform#talent"),
          ("flow","Requests, letters & approvals","platform#core"),("flag","Saudization & compliance","platform#payroll"),("chart","Reports & analytics","platform#org"),("phone","Self-service & mobile","platform#mobile")],
 "pk": [
   dict(key="Core", size="Up to 300 employees", for_="Run HR, payroll and attendance in one place.", plus="Adds to the essentials:",
        items=["Attendance and shifts","Expenses and business trips","Visas and iqama services","Org structure and job architecture","Medical insurance","Saudization","Assets","Onboarding, probation and exits","Reports"],
        sup="Email support and guided set-up"),
   dict(key="Professional", size="300 to 1,500 employees", for_="Add talent, rewards and employee services.", plus="Everything in Core, plus:", hi="For growing companies",
        items=["Recruiting and interviews","Performance and reviews","Learning","Compensation, merit and rewards","Employee relations and discipline","Help desk, news and surveys","AI assistant","Single sign-on (Microsoft, Google, Okta)"],
        sup="Priority support and an implementation manager to go-live"),
   dict(key="Enterprise", size="1,500+ employees or groups", for_="The full platform for large companies and groups.", plus="Everything in Professional, plus:",
        items=["Succession and talent pools","Org design and workforce planning","Group view across several companies","Sandbox: a private test copy of your company","API and webhooks"],
        sup="Dedicated account manager, service levels and quarterly reviews"),
 ],
 "always": ["Employees, documents and contracts","Payroll, GOSI and end of service","Bank and Mudad salary files","Leave, letters and requests","Approval paths with escalation","Employee self-service on mobile","Arabic and English, Hijri dates","2-step sign-in and audit trail","Guided set-up and training"],
 "proposal": "Request a proposal",
},
"ar": {
 "caps": [("users","الموارد البشرية الأساسية وملفات الموظفين","platform#core"),("pay","الرواتب ونهاية الخدمة","platform#payroll"),("time","الوقت والحضور والإجازات","platform#time"),
          ("star","التوظيف والأداء والتدريب","platform#talent"),("org","التصميم التنظيمي وتخطيط القوى العاملة","platform#org"),("pay","التعويضات والمكافآت","platform#talent"),
          ("flow","الطلبات والخطابات والاعتمادات","platform#core"),("flag","التوطين والامتثال","platform#payroll"),("chart","التقارير والتحليلات","platform#org"),("phone","الخدمة الذاتية والجوال","platform#mobile")],
 "pk": [
   dict(key="الأساسية", size="حتى 300 موظف", for_="الموارد البشرية والرواتب والحضور في مكان واحد.", plus="تضيف إلى الأساسيات:",
        items=["الحضور والورديات","المصروفات ورحلات العمل","التأشيرات وخدمات الإقامة","الهيكل التنظيمي والبنية الوظيفية","التأمين الطبي","التوطين","العهد","التهيئة والتجربة وإنهاء الخدمة","التقارير"],
        sup="دعم عبر البريد وتهيئة موجّهة"),
   dict(key="الاحترافية", size="من 300 إلى 1,500 موظف", for_="إضافة المواهب والمكافآت وخدمات الموظفين.", plus="كل ما في الأساسية، إضافة إلى:", hi="للمنشآت النامية",
        items=["التوظيف والمقابلات","الأداء والتقييم","التدريب","التعويضات والزيادات والمكافآت","علاقات الموظفين والانضباط","الدعم والأخبار والاستبيانات","المساعد الذكي","الدخول الموحد (مايكروسوفت، جوجل، Okta)"],
        sup="دعم بأولوية ومدير تنفيذ حتى الإطلاق"),
   dict(key="المؤسسات", size="أكثر من 1,500 موظف أو مجموعات", for_="المنصة كاملة للمنشآت الكبيرة والمجموعات.", plus="كل ما في الاحترافية، إضافة إلى:",
        items=["التعاقب الوظيفي ومجموعات المواهب","التصميم التنظيمي وتخطيط القوى العاملة","عرض موحد لعدة شركات في المجموعة","نسخة تجريبية خاصة من شركتكم","واجهة البرمجة والربط الآلي"],
        sup="مدير حساب مخصص واتفاقية مستوى خدمة ومراجعات ربع سنوية"),
 ],
 "always": ["الموظفون والوثائق والعقود","الرواتب والتأمينات ونهاية الخدمة","ملفات الرواتب للبنك ومُدد","الإجازات والخطابات والطلبات","مسارات اعتماد مع التصعيد","الخدمة الذاتية على الجوال","العربية والإنجليزية والتاريخ الهجري","التحقق بخطوتين وسجل التدقيق","تهيئة موجّهة وتدريب"],
 "proposal": "اطلب عرضًا",
}}

def ticks(items): return '<ul class="ticks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def caps_html(lang):
    g = G()
    return '<div class="caps">' + "".join(f'<a class="cap" href="/{lang}/{h.split("#")[0]}/#{h.split("#")[1]}">{g.ic(i)}{n}</a>' for i, n, h in TX[lang]["caps"]) + "</div>"

def pk_cards(lang, full=True):
    out = []
    for p in TX[lang]["pk"]:
        tag = f'<span class="tag">{p["hi"]}</span>' if p.get("hi") else ""
        lst = ticks(p["items"]) if full else ""
        out.append(f'<div class="pk{" hi" if p.get("hi") else ""}">{tag}<h3 style="font-size:24px">{p["key"]}</h3><p>{p["for_"]}</p><div class="size">{p["size"]}</div>'
                   + (f'<div class="plus">{p["plus"]}</div>{lst}<div class="sup">{p["sup"]}</div>' if full else "")
                   + f'<a class="btn{"" if p.get("hi") else " line"}" href="/{lang}/contact/">{TX[lang]["proposal"]}</a></div>')
    return '<div class="grid g3">' + "".join(out) + "</div>"

def faq(items):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)

def faq_schema(items):
    return [{"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}]

FAQ = {
"en": [
 ("Is Syncstead a Saudi company?", "Yes. Syncstead is a Saudi simplified joint stock company headquartered in Riyadh (CR 7055468719)."),
 ("How long does it take to go live?", "Usually 4 to 16 weeks depending on size: discovery, set-up and data import, one or two payrolls in parallel, then go-live with 30 days of close support."),
 ("Which package is right for us?", "Core suits companies up to 300 employees, Professional 300 to 1,500, and Enterprise larger companies and groups. The system recommends a package for your size, and you can upgrade in one click at any time without moving data."),
 ("Can you import our existing data?", "Yes. We import your employee list, structure and balances from Excel or from your current HR system, and check them with you before go-live."),
 ("Where is our data hosted?", "Today on a secure cloud managed by Syncstead. A move to a Saudi cloud region is planned, and large organizations can host Syncstead on their own servers by agreement."),
 ("How does it handle GOSI and end of service?", "Syncstead calculates GOSI contributions and end-of-service awards under the Saudi Labour Law and prepares the salary files for your bank or Mudad upload each month. Direct connections to government platforms are on our roadmap."),
 ("Can our admin make changes without Syncstead?", "Yes. Your admin manages approval workflows, leave types, pay items, letter templates and the org structure directly. On Enterprise, a private sandbox lets you test changes before making them live."),
 ("Is it in Arabic and on mobile?", "Yes. Every screen works in Arabic and English, and employees and managers use it from their phones."),
 ("How do I get pricing?", "We send a clear written proposal after the first meeting, based on your headcount and the package that fits."),
],
"ar": [
 ("هل سينكستيد شركة سعودية؟", "نعم. سينكستيد شركة مساهمة مبسطة سعودية مقرها الرياض (السجل التجاري 7055468719)."),
 ("كم يستغرق التشغيل؟", "عادة من 4 إلى 16 أسبوعًا حسب الحجم: الاستكشاف، ثم الإعداد واستيراد البيانات، ثم دورة رواتب أو دورتان بالتوازي، ثم التشغيل مع 30 يومًا من الدعم القريب."),
 ("ما الباقة المناسبة لنا؟", "الأساسية للمنشآت حتى 300 موظف، والاحترافية من 300 إلى 1,500، والمؤسسات للمنشآت الأكبر والمجموعات. يقترح النظام الباقة المناسبة لحجمكم، ويمكنكم الترقية بضغطة واحدة في أي وقت دون نقل بيانات."),
 ("هل يمكنكم استيراد بياناتنا الحالية؟", "نعم. نستورد قائمة الموظفين والهيكل والأرصدة من إكسل أو من نظامكم الحالي، ونراجعها معكم قبل التشغيل."),
 ("أين تُستضاف بياناتنا؟", "حاليًا على سحابة آمنة تديرها سينكستيد، والانتقال إلى منطقة سحابية سعودية مخطط له، ويمكن للمنشآت الكبيرة استضافة سينكستيد على خوادمها الداخلية بالاتفاق."),
 ("كيف يتعامل النظام مع التأمينات ونهاية الخدمة؟", "يحتسب سينكستيد اشتراكات التأمينات ومكافأة نهاية الخدمة وفق نظام العمل السعودي، ويجهّز ملفات الرواتب للبنك أو لرفعها في مُدد كل شهر. الربط المباشر مع المنصات الحكومية ضمن خطتنا."),
 ("هل يستطيع مسؤول النظام لدينا إجراء التغييرات دون الرجوع إليكم؟", "نعم. يدير مسؤول النظام مسارات الاعتماد وأنواع الإجازات وبنود الرواتب وقوالب الخطابات والهيكل التنظيمي مباشرة. وفي باقة المؤسسات تتيح النسخة التجريبية الخاصة اختبار التغييرات قبل تطبيقها."),
 ("هل النظام بالعربية ويعمل على الجوال؟", "نعم. كل شاشة تعمل بالعربية والإنجليزية، ويستخدمه الموظفون والمدراء من جوالاتهم."),
 ("كيف نحصل على الأسعار؟", "نرسل عرضًا مكتوبًا واضحًا بعد اللقاء الأول، بحسب عدد موظفيكم والباقة المناسبة."),
]}

# ---------------------------------------------------------------- HOME
def home(lang):
    g = G(); en = lang == "en"
    return f'''<section class="navy hero"><div class="w">
<div style="padding-bottom:56px">
<div class="eyebrow">{"Saudi human capital management" if en else "منصة سعودية لإدارة رأس المال البشري"}</div>
<h1 style="margin-top:14px">{"One platform for your people, <em>built for Saudi&nbsp;Arabia.</em>" if en else "منصة واحدة لموظفيك، <em>صُمّمت للمملكة العربية السعودية.</em>"}</h1>
<p class="lead">{"HR, payroll, attendance, talent and organization design in one bilingual system, with Saudi labour law at its core. For companies of 200 to 20,000 employees." if en else "الموارد البشرية والرواتب والحضور والمواهب والتصميم التنظيمي في نظام واحد ثنائي اللغة، ونظام العمل السعودي في صميمه. للمنشآت من 200 إلى 20,000 موظف."}</p>
<div class="cta"><a class="btn" href="{BOOK}" target="_blank" rel="noopener">{"Book a 20-min demo" if en else "احجز عرضًا في 20 دقيقة"}</a><a class="btn ghost" href="/{lang}/platform/">{"Explore the platform" if en else "تعرّف على المنصة"}</a></div>
<div class="facts"><span>{"A Saudi company" if en else "شركة سعودية"}</span><span>{"Arabic & English on every screen" if en else "العربية والإنجليزية في كل شاشة"}</span><span>{"Live in weeks" if en else "التشغيل في أسابيع"}</span></div>
</div>
<div class="devices">{g.laptop(lang, "desk-dashboard", "Syncstead dashboard" if en else "لوحة التحكم في سينكستيد")}{g.phone(lang, "phone-home")}</div>
</div></section>

<section><div class="w">
<div class="head"><div class="eyebrow">{"What changes" if en else "ما الذي يتغير"}</div><h2>{"Control of your workforce, cost and compliance." if en else "سيطرة على القوى العاملة والتكلفة والامتثال."}</h2></div>
<div class="grid g3">
<div class="card"><div class="ico">{g.ic("layers")}</div><h3>{"One system of record" if en else "مصدر واحد لبيانات الموظفين"}</h3><p>{"Employees, payroll, attendance, talent and structure in one place, so every report agrees and nothing is typed twice." if en else "الموظفون والرواتب والحضور والمواهب والهيكل في مكان واحد، فتتطابق كل التقارير ولا يُدخل شيء مرتين."}</p></div>
<div class="card"><div class="ico">{g.ic("chart")}</div><h3>{"Cost before every decision" if en else "التكلفة قبل كل قرار"}</h3><p>{"A raise, a hire or a restructure shows its cost and Saudization effect before anyone approves it." if en else "الزيادة أو التعيين أو إعادة الهيكلة تظهر تكلفتها وأثرها على التوطين قبل أن يعتمدها أحد."}</p></div>
<div class="card"><div class="ico">{g.ic("law")}</div><h3>{"Saudi compliance by default" if en else "امتثال للأنظمة السعودية تلقائيًا"}</h3><p>{"Labour law, GOSI, end of service and Nitaqat are built in and kept current, without a customization project." if en else "نظام العمل والتأمينات ونهاية الخدمة ونطاقات مدمجة وتُحدَّث، دون مشروع تخصيص."}</p></div>
</div></div></section>

<section class="soft"><div class="w">
<div class="head"><div class="eyebrow">{"The platform" if en else "المنصة"}</div><h2>{"Every people process, hire to retire." if en else "كل إجراءات الموارد البشرية، من التعيين حتى نهاية الخدمة."}</h2><p class="lead">{"Ten capability areas on one platform. Choose the package that fits your size today and grow without changing systems." if en else "عشرة مجالات على منصة واحدة. اختر الباقة المناسبة لحجمك اليوم، وانمُ دون تغيير النظام."}</p></div>
{caps_html(lang)}
<div style="margin-top:28px"><a class="btn line" href="/{lang}/platform/">{"See every capability" if en else "شاهد كل المجالات"} →</a></div>
</div></section>

<section class="navy"><div class="w">
<div class="head"><div class="eyebrow">{"Proof" if en else "الإثبات"}</div><h2>{"Tested at the size of the Kingdom's largest groups." if en else "مُختبر بحجم أكبر المجموعات في المملكة."}</h2><p class="lead">{"Before offering Syncstead to large employers, we test it on full-size models of real Saudi groups, with every branch, grade and shift." if en else "قبل أن نقدم سينكستيد لكبار أصحاب العمل، نختبره على نماذج بالحجم الكامل لمجموعات سعودية حقيقية، بكل فروعها ودرجاتها ووردياتها."}</p></div>
<div class="stats">
<div><div class="num">60,916</div><p>{"payslips recalculated independently, matched to the riyal" if en else "مسير راتب أُعيد احتسابها بشكل مستقل وطابقت حتى آخر ريال"}</p></div>
<div><div class="num">24</div><p>{"modules, from core HR to succession planning" if en else "وحدة، من الموارد البشرية الأساسية حتى التعاقب الوظيفي"}</p></div>
<div><div class="num">2</div><p>{"languages, equal on every screen and report" if en else "لغتان متساويتان في كل شاشة وتقرير"}</p></div>
<div><div class="num">4–16</div><p>{"weeks from contract to the first live payroll" if en else "أسبوعًا من العقد حتى أول مسير رواتب فعلي"}</p></div>
</div></div></section>

<section><div class="w">
<div class="head"><div class="eyebrow">{"Packages" if en else "الباقات"}</div><h2>{"Three packages. One platform. Upgrade in one click." if en else "ثلاث باقات. منصة واحدة. الترقية بضغطة."}</h2></div>
{pk_cards(lang, full=False)}
<div style="margin-top:24px"><a class="btn line" href="/{lang}/packages/">{"Compare packages" if en else "قارن الباقات"} →</a></div>
</div></section>

<section class="soft"><div class="w">
<div class="grid g2" style="align-items:center;gap:48px">
<div><div class="eyebrow">{"Trust" if en else "الثقة"}</div><h2>{"The controls your auditors and IT team expect." if en else "الضوابط التي يتوقعها المدققون وفريق تقنية المعلومات."}</h2>
{ticks(["Each company's data kept fully separate","Role-based access and confidential pay","Single sign-on and 2-step sign-in","Full audit trail of every change","Hosting on our cloud, in the Kingdom (planned) or on your own servers"] if en else ["فصل كامل لبيانات كل منشأة","صلاحيات حسب الدور ورواتب سرية","دخول موحد وتحقق بخطوتين","سجل تدقيق كامل لكل تغيير","الاستضافة على سحابتنا، أو داخل المملكة (مخطط له)، أو على خوادمكم"])}
<p style="margin-top:20px"><a href="/{lang}/trust/">{"Trust & security" if en else "الأمان والثقة"} →</a></p></div>
<div class="shot">{g.img(lang, "desk-saudization")}</div>
</div></div></section>'''

# ---------------------------------------------------------------- PLATFORM
def platform(lang):
    g = G(); en = lang == "en"
    def feat(id_, eb, h, p, items, visual):
        return f'<div class="feature" id="{id_}"><div class="txt"><div class="eyebrow">{eb}</div><h2>{h}</h2><p class="lead">{p}</p>{ticks(items)}</div><div>{visual}</div></div>'
    F = []
    F.append(feat("payroll", "Payroll & compliance" if en else "الرواتب والامتثال",
        "Payroll you can reconcile to the riyal." if en else "رواتب تُطابق حتى آخر ريال.",
        "Prepare, approve, send to the bank and mark as paid, with checks before anything is approved." if en else "الإعداد والاعتماد والإرسال للبنك وتسجيل الدفع، مع فحوصات قبل أي اعتماد.",
        ["GOSI, overtime, loans and sick-leave tiers","End of service and leave pay at exit","Salary files for your bank or Mudad upload","Finance journals for SAP, Oracle, Dynamics, Odoo and more","Saudization and Nitaqat tracking, with what moves your band","Two approvers before payroll can be paid"] if en else
        ["التأمينات والعمل الإضافي والسلف وشرائح الإجازة المرضية","نهاية الخدمة وبدل الإجازات عند المغادرة","ملفات الرواتب للبنك أو لرفعها في مُدد","قيود المالية لأنظمة SAP وOracle وDynamics وOdoo وغيرها","متابعة التوطين ونطاقات وما يحرك نطاقك","معتمِدان قبل صرف الرواتب"],
        f'<div class="shot">{g.img(lang, "desk-payroll-run")}</div>'))
    F.append(feat("time", "Time & attendance" if en else "الوقت والحضور",
        "Attendance and leave that run themselves." if en else "حضور وإجازات تعمل تلقائيًا.",
        "Shifts, work sites and leave policies set once, then applied to every employee." if en else "الورديات ومواقع العمل وسياسات الإجازات تُعدّ مرة واحدة، ثم تُطبق على كل موظف.",
        ["Check-in from the phone at a set work site","Fingerprint devices feed attendance","Overtime from attendance into payroll","Leave policies, balances and Saudi public holidays"] if en else
        ["التحضير من الجوال في موقع العمل المحدد","أجهزة البصمة تغذي الحضور","العمل الإضافي من الحضور إلى الرواتب","سياسات الإجازات وأرصدتها والعطل الرسمية"],
        f'<div class="phones" style="max-width:420px;grid-template-columns:1fr 1fr">{g.phone(lang, "phone-home")}{g.phone(lang, "phone-leave")}</div>'))
    F.append(feat("talent", "Talent & rewards" if en else "المواهب والمكافآت",
        "Hire, grow and reward, with the cost shown first." if en else "وظّف وطوّر وكافئ، والتكلفة ظاهرة أولًا.",
        "Every raise and promotion shows its monthly cost before approval." if en else "كل زيادة وترقية تظهر تكلفتها الشهرية قبل الاعتماد.",
        ["Careers page, candidates, interviews and offers","Performance reviews with calibration","Learning and certificates","Merit cycles with budgets, bonuses and rewards","Succession plans and talent pools (Enterprise)"] if en else
        ["صفحة الوظائف والمرشحون والمقابلات والعروض","تقييم الأداء مع المعايرة","التدريب والشهادات","دورات الزيادة بميزانياتها والحوافز والمكافآت","خطط التعاقب ومجموعات المواهب (المؤسسات)"],
        f'<div class="shot">{g.img(lang, "desk-compensation")}</div>'))
    F.append(feat("org", "Organization & insight" if en else "التنظيم والتحليلات",
        "See your organization, and test changes before making them." if en else "شاهد منشأتك، وجرّب التغييرات قبل تنفيذها.",
        "Org chart, job architecture and grades, with restructure modeling and priced manpower plans." if en else "الهيكل التنظيمي والبنية الوظيفية والدرجات، مع نمذجة إعادة الهيكلة وخطط قوى عاملة مسعّرة.",
        ["Live org chart and reporting lines","Restructure modeling with cost and layers (Enterprise)","Workforce plans priced by department (Enterprise)","Headcount, cost, turnover and Saudization reports, exported to Excel"] if en else
        ["هيكل تنظيمي مباشر وخطوط الإشراف","نمذجة إعادة الهيكلة مع التكلفة والمستويات (المؤسسات)","خطط قوى عاملة مسعّرة لكل إدارة (المؤسسات)","تقارير العدد والتكلفة والدوران والتوطين مع التصدير إلى إكسل"],
        f'<div class="shot">{g.img(lang, "desk-org")}</div>'))
    F.append(feat("core", "Core HR & services" if en else "الموارد البشرية الأساسية والخدمات",
        "Every employee file and request in one place." if en else "كل ملف موظف وكل طلب في مكان واحد.",
        "Records, documents with expiry alerts and approval paths you design." if en else "السجلات والوثائق مع تنبيهات الانتهاء، ومسارات اعتماد تصممها أنت.",
        ["Contracts, documents, visas and iqama services","Onboarding, probation and exits","Letters, expenses and business trips","Approval paths with delegation and escalation","Help desk, news and surveys"] if en else
        ["العقود والوثائق وخدمات التأشيرات والإقامة","التهيئة والتجربة وإنهاء الخدمة","الخطابات والمصروفات ورحلات العمل","مسارات اعتماد مع الإنابة والتصعيد","مكتب الدعم والأخبار والاستبيانات"],
        f'<div class="shot">{g.img(lang, "desk-dashboard")}</div>'))
    F.append(feat("mobile", "Employees & managers" if en else "الموظفون والمدراء",
        "Self-service on every phone." if en else "خدمة ذاتية على كل جوال.",
        "Employees request and track; managers approve in one tap; an AI assistant answers questions on leave and pay." if en else "يطلب الموظفون ويتابعون، ويعتمد المدراء بلمسة واحدة، ويجيب المساعد الذكي عن الإجازات والرواتب.",
        ["Leave, letters, payslips and requests","One-tap approvals for managers","Alerts on the phone","AI assistant, off until your administrator agrees"] if en else
        ["الإجازات والخطابات والقسائم والطلبات","اعتماد بلمسة واحدة للمدراء","تنبيهات على الجوال","المساعد الذكي، لا يعمل إلا بموافقة مسؤول النظام"],
        f'<div class="phones">{g.phone(lang, "phone-leave")}{g.phone(lang, "phone-mgr-approvals")}{g.phone(lang, "phone-home")}</div>'))
    return f'''<section class="navy" style="padding-bottom:56px"><div class="w"><div class="eyebrow">{"The platform" if en else "المنصة"}</div>
<h1 style="margin-top:12px;max-width:900px">{"Every people process, from hire to retire, in one system." if en else "كل إجراءات الموارد البشرية، من التعيين حتى نهاية الخدمة، في نظام واحد."}</h1>
<p class="lead">{"One employee record feeds payroll, attendance, talent and planning, so the numbers agree everywhere." if en else "سجل موظف واحد يغذي الرواتب والحضور والمواهب والتخطيط، فتتطابق الأرقام في كل مكان."}</p>
<div style="margin-top:32px">{caps_html(lang)}</div></div></section>
<section style="padding-top:8px"><div class="w">{"".join(F)}</div></section>'''

# ---------------------------------------------------------------- PACKAGES
def packages(lang):
    g = G(); en = lang == "en"
    from gen import ic
    MOD = [
     ("Attendance & shifts","الحضور والورديات",1),("Expenses & trips","المصروفات والرحلات",1),("Visas & iqama services","التأشيرات وخدمات الإقامة",1),("Org structure & job architecture","الهيكل التنظيمي والبنية الوظيفية",1),
     ("Medical insurance","التأمين الطبي",1),("Saudization","التوطين",1),("Assets","العهد",1),("Onboarding, probation & exits","التهيئة والتجربة وإنهاء الخدمة",1),("Reports","التقارير",1),
     ("AI assistant","المساعد الذكي",2),("Recruiting & interviews","التوظيف والمقابلات",2),("Performance & reviews","الأداء والتقييم",2),("Learning","التدريب",2),
     ("Compensation, merit & rewards","التعويضات والزيادات والمكافآت",2),("Employee relations & discipline","علاقات الموظفين والانضباط",2),("Help desk, news & surveys","الدعم والأخبار والاستبيانات",2),
     ("Succession & talent pools","التعاقب الوظيفي ومجموعات المواهب",3),("Org design & workforce planning","التصميم التنظيمي وتخطيط القوى العاملة",3),
    ]
    FEAT = [("Single sign-on (Microsoft, Google, Okta)","الدخول الموحد (مايكروسوفت، جوجل، Okta)",2),("Group view across companies","العرض الموحد لعدة شركات",3),("Sandbox (test copy of your company)","النسخة التجريبية من شركتكم",3),("API & webhooks","واجهة البرمجة والربط الآلي",3)]
    names = [p["key"] for p in TX[lang]["pk"]]
    def row(label, lvl): return f'<tr><td>{label}</td>' + "".join(f'<td class="{"y" if lvl <= i else "n"}">{"✓" if lvl <= i else "—"}</td>' for i in (1, 2, 3)) + "</tr>"
    rows = f'<tr class="grp"><td colspan="4">{"Included in every package" if en else "مشمول في كل الباقات"}</td></tr>' + "".join(row(a, 1) for a in TX[lang]["always"])
    rows += f'<tr class="grp"><td colspan="4">{"Modules" if en else "الوحدات"}</td></tr>' + "".join(row(a if en else b, l) for a, b, l in MOD)
    rows += f'<tr class="grp"><td colspan="4">{"Capabilities" if en else "الإمكانات"}</td></tr>' + "".join(row(a if en else b, l) for a, b, l in FEAT)
    sup = [p["sup"] for p in TX[lang]["pk"]]
    rows += f'<tr class="grp"><td colspan="4">{"Support" if en else "الدعم"}</td></tr><tr><td></td>' + "".join(f'<td style="font-size:14px;text-align:center">{s}</td>' for s in sup) + "</tr>"
    return f'''<section class="navy" style="padding-bottom:56px"><div class="w"><div class="eyebrow">{"Packages" if en else "الباقات"}</div>
<h1 style="margin-top:12px;max-width:900px">{"Three packages. One platform. Switch in one click." if en else "ثلاث باقات. منصة واحدة. التبديل بضغطة."}</h1>
<p class="lead">{"Every package runs on the same system, so moving up never means a migration. Modules open the moment you upgrade, and your data stays exactly where it is." if en else "كل الباقات تعمل على النظام نفسه، فالانتقال إلى الأعلى لا يعني نقل بيانات. تُفتح الوحدات فور الترقية وتبقى بياناتك في مكانها."}</p></div></section>
<section><div class="w">{pk_cards(lang)}
<p style="margin-top:20px;font-size:14px">{"Pricing is per active employee per month, set out in a written proposal after our first meeting." if en else "التسعير لكل موظف نشط شهريًا، ويُوضَّح في عرض مكتوب بعد لقائنا الأول."}</p></div></section>
<section class="soft"><div class="w"><div class="head"><div class="eyebrow">{"Compare" if en else "المقارنة"}</div><h2>{"Everything in each package." if en else "كل ما تتضمنه كل باقة."}</h2></div>
<div class="scroll"><table class="cmp"><thead><tr><th></th>{"".join(f'<th class="c">{n}</th>' for n in names)}</tr></thead><tbody>{rows}</tbody></table></div></div></section>
<section><div class="w"><div class="grid g3">
<div class="card"><div class="ico">{ic("check")}</div><h3>{"Recommended for your size" if en else "الباقة الأنسب لحجمكم"}</h3><p>{"The system suggests the package that fits your headcount and structure." if en else "يقترح النظام الباقة المناسبة لعدد موظفيكم وهيكلكم."}</p></div>
<div class="card"><div class="ico">{ic("layers")}</div><h3>{"Upgrade in one click" if en else "الترقية بضغطة واحدة"}</h3><p>{"Request it from your Admin center; new modules open straight away." if en else "اطلبها من لوحة مسؤول الشركة، وتُفتح الوحدات الجديدة فورًا."}</p></div>
<div class="card"><div class="ico">{ic("db")}</div><h3>{"Nothing is ever lost" if en else "لا يضيع شيء أبدًا"}</h3><p>{"Changing package keeps every record, setting and history." if en else "تغيير الباقة يحفظ كل السجلات والإعدادات والتاريخ."}</p></div>
</div>
</div></section>'''

# ---------------------------------------------------------------- WHY
def why(lang):
    g = G(); en = lang == "en"
    R = [("law","Saudi rules built in, not bolted on","Labour-law calculations, GOSI, end of service, Nitaqat and Hijri dates are part of the core. Rule updates reach you without a customization project.","الأنظمة السعودية في صميمه","حسابات نظام العمل والتأمينات ونهاية الخدمة ونطاقات والتاريخ الهجري جزء من النظام، فتصلك التحديثات دون مشروع تخصيص."),
         ("chart","Every decision shows its cost first","A raise, a hire or a restructure shows its cost and Saudization effect before it is approved.","تكلفة كل قرار أمامك قبل اعتماده","الزيادة أو التعيين أو إعادة الهيكلة تظهر تكلفتها وأثرها على التوطين قبل الاعتماد."),
         ("layers","Packages sized to you, one platform","Start on the package that fits and move up in one click as you grow, with no migration.","باقات تناسب حجمكم على منصة واحدة","ابدأ بالباقة المناسبة وانتقل إلى الأعلى بضغطة واحدة مع نموك، دون نقل بيانات."),
         ("shield","Governance by design","Approval paths you set, a complete audit trail, role-based access and confidential pay for executives.","حوكمة مدمجة منذ التصميم","مسارات اعتماد تحددها أنت، وسجل تدقيق كامل، وصلاحيات حسب الدور، ورواتب سرية للإدارة العليا."),
         ("clock","Live in weeks, not months","Your structure is built from your staff list, and payroll runs in parallel and is reconciled before you switch.","التشغيل في أسابيع لا أشهر","يُبنى هيكلك من قائمة موظفيك، وتُشغَّل الرواتب بالتوازي وتُطابق قبل الانتقال."),
         ("users","Built by HR practitioners","Designed around how Saudi HR, finance and leadership teams decide, approve and report. You work directly with the founder.","صممه مختصون في الموارد البشرية","مصمم وفق طريقة قرار واعتماد وتقارير فرق الموارد البشرية والمالية والقيادة في المنشآت السعودية، وتعمل مباشرة مع المؤسس.")]
    cards = "".join(f'<div class="card"><div class="ico">{g.ic(i)}</div><h3>{a if en else c}</h3><p>{b if en else d}</p></div>' for i, a, b, c, d in R)
    C = [("Saudi regulation","Built into the core","Through partners and customization","Mostly covered","الأنظمة السعودية","مدمجة في صميم النظام","عبر شركاء وتخصيص","مغطاة غالبًا"),
         ("Arabic and English","Equal, on every screen","Often English first","Varies","العربية والإنجليزية","متساويتان في كل شاشة","الإنجليزية أولًا غالبًا","تتفاوت"),
         ("Packages","Three, sized by headcount; switch in one click","Licensed module by module","Tiers and paid add-ons","الباقات","ثلاث حسب عدد الموظفين، والتبديل بضغطة","ترخيص لكل وحدة","مستويات وإضافات مدفوعة"),
         ("Cost of decisions","Shown before every raise, hire or restructure","Separate planning tools","Rarely offered","تكلفة القرارات","ظاهرة قبل كل زيادة أو تعيين أو إعادة هيكلة","أدوات تخطيط منفصلة","نادرًا ما تتوفر"),
         ("Approval paths","Yours to design, with stand-ins and escalation","Flexible, set up by consultants","Fixed or basic","مسارات الاعتماد","تصممها أنت، مع الإنابة والتصعيد","مرنة، يعدّها مستشارون","ثابتة أو بسيطة"),
         ("Hosting","Our cloud, in the Kingdom (planned) or your own servers","Vendor cloud","Vendor cloud","الاستضافة","سحابتنا، أو داخل المملكة (مخطط له)، أو خوادمكم","سحابة المزوّد","سحابة المزوّد"),
         ("Time to go live","Weeks, with a parallel payroll run","Often several months","Weeks","مدة التشغيل","أسابيع، مع دورة رواتب موازية","عدة أشهر غالبًا","أسابيع")]
    head = ("Syncstead","Global ERP suites","Typical HR apps") if en else ("سينكستيد","أنظمة ERP العالمية","تطبيقات الموارد البشرية المعتادة")
    rows = "".join(f'<tr><td style="font-weight:600">{r[0] if en else r[4]}</td><td class="us">{r[1] if en else r[5]}</td><td>{r[2] if en else r[6]}</td><td>{r[3] if en else r[7]}</td></tr>' for r in C)
    return f'''<section class="navy" style="padding-bottom:56px"><div class="w"><div class="eyebrow">{"Why Syncstead" if en else "لماذا سينكستيد"}</div>
<h1 style="margin-top:12px;max-width:900px">{"Enterprise depth, without the enterprise project." if en else "عمق الأنظمة الكبرى، دون مشروعها الطويل."}</h1>
<p class="lead">{"Six reasons Saudi leadership teams choose Syncstead." if en else "ستة أسباب تجعل قيادات المنشآت السعودية تختار سينكستيد."}</p></div></section>
<section><div class="w"><div class="grid g3">{cards}</div></div></section>
<section class="soft"><div class="w"><div class="head"><div class="eyebrow">{"How we compare" if en else "كيف نقارن"}</div><h2>{"Syncstead next to the usual options." if en else "سينكستيد مقارنة بالخيارات المعتادة."}</h2></div>
<div class="scroll"><table class="cmp"><thead><tr><th></th><th class="us">{head[0]}</th><th>{head[1]}</th><th>{head[2]}</th></tr></thead><tbody>{rows}</tbody></table></div>
<p style="margin-top:12px;font-size:14px">{"Comparison reflects typical offers in the Saudi market and may differ by provider." if en else "تعكس المقارنة العروض المعتادة في السوق السعودي، وقد تختلف من مزود لآخر."}</p></div></section>
<section class="navy"><div class="w"><div class="head"><div class="eyebrow">{"Proof" if en else "الإثبات"}</div><h2>{"Accuracy you can check." if en else "دقة يمكنك التحقق منها."}</h2></div>
<div class="grid g3">
<div><div class="num">60,916</div><p style="margin-top:6px">{"payslips recalculated independently in our scale tests, matched to the riyal" if en else "مسير راتب أُعيد احتسابها بشكل مستقل في اختبارات الحجم الكبير، وطابقت حتى آخر ريال"}</p></div>
<div><div class="num">{"Exact" if en else "دقة تامة"}</div><p style="margin-top:6px">{"leave pay and end of service at exit, including unpaid-leave rules" if en else "في بدل الإجازات ونهاية الخدمة عند المغادرة، بما فيها قواعد الإجازة غير المدفوعة"}</p></div>
<div><div class="num">{"Separate" if en else "لكل منشأة"}</div><p style="margin-top:6px">{"nightly checks for each company, so one large client never slows another" if en else "فحوصات ليلية مستقلة، فلا تبطئ منشأة كبيرة غيرها"}</p></div>
</div></div></section>'''

# ---------------------------------------------------------------- TRUST
def trust(lang):
    g = G(); en = lang == "en"
    S = [("lock","Access","Role-based access for every user, confidential pay for executives, and admin rights held by a named account owner.","الوصول","صلاحيات حسب الدور لكل مستخدم، ورواتب سرية للإدارة العليا، وصلاحيات الإدارة لدى مالك حساب محدد."),
         ("key","Sign-in","2-step sign-in that admins can require, and single sign-on with Microsoft, Google or Okta.","تسجيل الدخول","تحقق بخطوتين يمكن إلزامه، ودخول موحد عبر مايكروسوفت أو جوجل أو Okta."),
         ("shield","Separation","Each company's data kept fully separate from every other company.","الفصل","فصل كامل لبيانات كل منشأة عن غيرها."),
         ("file","Audit trail","Every change and approval recorded: who, what and when.","سجل التدقيق","كل تغيير واعتماد مسجل: من وماذا ومتى."),
         ("pay","Payroll control","Two approvers before payroll can be paid, with checks against labour-law limits.","ضبط الرواتب","معتمِدان قبل صرف الرواتب، مع فحص حدود نظام العمل."),
         ("db","Backups","Encrypted connections, daily backups and a full company backup on demand in open formats.","النسخ الاحتياطي","اتصالات مشفرة، ونسخ احتياطية يومية، ونسخة كاملة للمنشأة عند الطلب بصيغ مفتوحة.")]
    cards = "".join(f'<div class="card"><div class="ico">{g.ic(i)}</div><h3>{a if en else c}</h3><p>{b if en else d}</p></div>' for i, a, b, c, d in S)
    return f'''<section class="navy" style="padding-bottom:56px"><div class="w"><div class="eyebrow">{"Trust & security" if en else "الأمان والثقة"}</div>
<h1 style="margin-top:12px;max-width:900px">{"Built for the questions your IT and procurement teams will ask." if en else "مصمم للأسئلة التي سيطرحها فريقا تقنية المعلومات والمشتريات لديكم."}</h1>
<p class="lead">{"Security, data protection and hosting, explained plainly." if en else "الأمان وحماية البيانات والاستضافة، بوضوح."}</p></div></section>
<section><div class="w"><div class="head"><div class="eyebrow">{"Security controls" if en else "ضوابط الأمان"}</div><h2>{"The controls your auditors expect." if en else "الضوابط التي يتوقعها المدققون."}</h2></div><div class="grid g3">{cards}</div></div></section>
<section class="soft" id="hosting"><div class="w"><div class="head"><div class="eyebrow">{"Hosting" if en else "الاستضافة"}</div><h2>{"Hosting that fits your policies." if en else "استضافة تناسب سياساتكم."}</h2></div>
<div class="grid g3">
<div class="card"><span class="st">{"Available" if en else "متاح"}</span><div class="ico">{g.ic("cloud")}</div><h3>{"Secure cloud" if en else "سحابة آمنة"}</h3><p>{"Managed by Syncstead, with daily backups, monitoring and updates included." if en else "تديرها سينكستيد، مع نسخ احتياطية يومية ومراقبة وتحديثات مشمولة."}</p></div>
<div class="card"><span class="st pl">{"Planned" if en else "مخطط له"}</span><div class="ico">{g.ic("flag")}</div><h3>{"Hosted in the Kingdom" if en else "استضافة داخل المملكة"}</h3><p>{"Moving to a Saudi cloud region, in line with national data regulations." if en else "الانتقال إلى منطقة سحابية سعودية، وفق الأنظمة الوطنية للبيانات."}</p></div>
<div class="card"><span class="st">{"By agreement" if en else "بالاتفاق"}</span><div class="ico">{g.ic("server")}</div><h3>{"On your own servers" if en else "على خوادمكم الداخلية"}</h3><p>{"For large organizations that require hosting inside their own network. The system runs as a standard container." if en else "للمنشآت الكبيرة التي تشترط الاستضافة داخل شبكتها، ويعمل النظام كحاوية قياسية."}</p></div>
</div></div></section>
<section><div class="w"><div class="grid g2" style="gap:48px;align-items:start">
<div><div class="eyebrow">{"Data protection" if en else "حماية البيانات"}</div><h2>{"Your data, under your control." if en else "بياناتك تحت سيطرتك."}</h2>
{ticks(["Designed around the Personal Data Protection Law (PDPL)","Data processing agreement signed before any real data is loaded","AI features stay off until your administrator switches them on","Test copies use made-up names, ID numbers and pay","Your full data available to export at any time"] if en else ["مصمم وفق نظام حماية البيانات الشخصية","اتفاقية معالجة بيانات تُوقَّع قبل تحميل أي بيانات حقيقية","مزايا الذكاء الاصطناعي لا تعمل إلا بتفعيل من مسؤول النظام","النسخ التجريبية تستخدم أسماء وأرقام هويات ورواتب وهمية","بياناتك كاملة متاحة للتصدير في أي وقت"])}</div>
<div><div class="eyebrow">{"Saudi company" if en else "شركة سعودية"}</div><h2>{"A local partner you can hold to account." if en else "شريك محلي يمكنك مساءلته."}</h2>
<p class="lead">{"Syncstead is a Saudi simplified joint stock company headquartered in Riyadh, CR 7055468719. Contracts, support and service levels are under Saudi law." if en else "سينكستيد شركة مساهمة مبسطة سعودية مقرها الرياض، السجل التجاري 7055468719. العقود والدعم واتفاقيات مستوى الخدمة وفق الأنظمة السعودية."}</p>
<p style="margin-top:16px;font-size:14px">{"Direct connections to government platforms are on our roadmap. Today, Syncstead prepares the files your team uploads." if en else "الربط المباشر مع المنصات الحكومية ضمن خطتنا، ويجهّز سينكستيد حاليًا الملفات التي يرفعها فريقكم."}</p></div>
</div></div></section>'''

# ---------------------------------------------------------------- ABOUT
def about(lang):
    g = G(); en = lang == "en"
    msg = (["Saudi companies are changing how they manage people. Saudization targets, evolving labour regulations and leadership teams that expect every decision to come with its cost.",
            "Yet many HR teams still run payroll on spreadsheets, or wait months while global systems are customized for Saudi rules. I founded Syncstead to close that gap.",
            "After years advising Saudi organizations on HR and governance, I built the platform I wanted my clients to have: Saudi regulation at its core, Arabic and English as equals, and governance designed in from the first screen.",
            "Our commitment is simple: payroll you can trust to the riyal, decisions with their cost in front of you, and a partner who understands how your organization works."] if en else
           ["تتغير طريقة إدارة المنشآت السعودية لموظفيها: مستهدفات التوطين، وتحديثات نظام العمل، وقيادات تتوقع أن يأتي كل قرار ومعه تكلفته.",
            "ومع ذلك ما زالت فرق كثيرة تدير الرواتب بجداول إكسل، أو تنتظر أشهرًا حتى تُخصَّص الأنظمة العالمية للأنظمة السعودية. أسست سينكستيد لسد هذه الفجوة.",
            "بعد سنوات من تقديم الاستشارات للمنشآت السعودية في الموارد البشرية والحوكمة، بنيت المنصة التي تمنيت أن تكون لدى عملائي: الأنظمة السعودية في صميمها، والعربية والإنجليزية على قدم المساواة، والحوكمة مدمجة منذ الشاشة الأولى.",
            "التزامنا واضح: رواتب دقيقة حتى آخر ريال، وقرارات تكلفتها أمامك قبل اعتمادها، وشريك يفهم طريقة عمل منشأتك."])
    facts = ([("Company","Syncstead · سينكستيد"),("Legal form","Saudi simplified joint stock company"),("Commercial registration","7055468719"),("Headquarters","Riyadh, Saudi Arabia"),("Built for","Saudi companies of 200 to 20,000 employees, and groups")] if en else
             [("الشركة","سينكستيد · Syncstead"),("الكيان النظامي","شركة مساهمة مبسطة سعودية"),("السجل التجاري","7055468719"),("المقر","الرياض، المملكة العربية السعودية"),("لمن صُممت","المنشآت السعودية من 200 إلى 20,000 موظف، والمجموعات")])
    vals = ([("Accuracy","Payroll and entitlements calculated by the law, and checked."),("Clarity","Plain screens, plain proposals, no surprises."),("Partnership","You work directly with the people who build the system."),("Trust","Your data protected, separated and always yours.")] if en else
            [("الدقة","رواتب ومستحقات تُحتسب وفق النظام وتُراجَع."),("الوضوح","شاشات واضحة وعروض واضحة ودون مفاجآت."),("الشراكة","تعمل مباشرة مع من يبنون النظام."),("الثقة","بياناتك محمية ومفصولة وملك لك دائمًا.")])
    return f'''<section class="navy" style="padding-bottom:56px"><div class="w"><div class="eyebrow">{"About Syncstead" if en else "من نحن"}</div>
<h1 style="margin-top:12px;max-width:900px">{"A Saudi company, built by HR practitioners." if en else "شركة سعودية، صممها مختصون في الموارد البشرية."}</h1>
<p class="lead">{"Our mission: give every Saudi organization full control of its workforce, cost and compliance, in one system its people actually enjoy using." if en else "رسالتنا: أن تمتلك كل منشأة سعودية سيطرة كاملة على قواها العاملة وتكلفتها وامتثالها، في نظام واحد يستمتع موظفوها باستخدامه."}</p></div></section>
<section><div class="w"><div class="grid g2" style="grid-template-columns:1.5fr 1fr;gap:56px;align-items:start">
<div class="msg"><div class="eyebrow">{"A message from our CEO" if en else "كلمة الرئيس التنفيذي"}</div><h2>{"Your people decisions deserve the same rigour as your financial ones." if en else "قرارات الموارد البشرية تستحق الدقة نفسها التي تحظى بها القرارات المالية."}</h2>
<div class="quote" style="margin-top:24px">{"&ldquo;" if en else "&rdquo;"}</div>{"".join(f"<p>{p}</p>" for p in msg)}
<p style="margin-top:28px;opacity:1"><strong style="color:var(--fg)">{"Al Hosam Al Ghamdi" if en else "الحسام الغامدي"}</strong><br><span style="font-size:15px;color:var(--muted)">{"Founder & CEO" if en else "المؤسس والرئيس التنفيذي"}</span></p></div>
<div class="card" style="background:var(--soft)"><div class="eyebrow">{"At a glance" if en else "لمحة سريعة"}</div><dl class="facts-list">{"".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in facts)}</dl></div>
</div></div></section>
<section class="soft"><div class="w"><div class="head"><div class="eyebrow">{"Our values" if en else "قيمنا"}</div><h2>{"What you can expect from us." if en else "ما الذي يمكنك أن تتوقعه منا."}</h2></div>
<div class="grid g4">{"".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in vals)}</div></div></section>
<section id="founding-partners"><div class="w"><div class="grid g2" style="gap:48px;align-items:center">
<div><div class="eyebrow">{"Founding Partners Program" if en else "برنامج الشركاء المؤسسين"}</div><h2>{"Join early, on preferred terms." if en else "انضم مبكرًا بشروط تفضيلية."}</h2>
<p class="lead">{"A limited number of companies join as founding partners, with preferred founding terms, full set-up and training, and direct access to the founder. In return, we ask for your feedback and, once you are live, a reference." if en else "عدد محدود من المنشآت تنضم كشركاء مؤسسين، بشروط تأسيس تفضيلية، وتهيئة كاملة وتدريب، وتواصل مباشر مع المؤسس. وفي المقابل نطلب ملاحظاتكم، ثم توصيتكم بعد التشغيل."}</p></div>
<div class="shot">{g.img(lang, "desk-org")}</div></div></div></section>'''

# ---------------------------------------------------------------- RESOURCES
def resources(lang):
    g = G(); en = lang == "en"
    return f'''<section class="navy" style="padding-bottom:56px"><div class="w"><div class="eyebrow">{"Resources" if en else "الموارد"}</div>
<h1 style="margin-top:12px;max-width:900px">{"Tools and answers for Saudi HR teams." if en else "أدوات وإجابات لفرق الموارد البشرية السعودية."}</h1></div></section>
<section><div class="w"><div class="grid g2" style="gap:48px;align-items:start">
<div><div class="eyebrow">{"Free tool" if en else "أداة مجانية"}</div><h2>{"End-of-service calculator" if en else "حاسبة مكافأة نهاية الخدمة"}</h2><p class="lead">{"Estimate an employee's end-of-service award under the Saudi Labour Law, for termination or resignation." if en else "احسب تقديريًا مكافأة نهاية الخدمة للموظف وفق نظام العمل السعودي، عند إنهاء العقد أو الاستقالة."}</p>
<a class="btn" style="margin-top:20px" href="/{lang}/end-of-service-calculator/">{g.ic("calc")}{"Open the calculator" if en else "افتح الحاسبة"}</a></div>
<div class="downloads"><div class="eyebrow">{"Downloads" if en else "التنزيلات"}</div>
<a href="/assets/docs/Syncstead-Company-Profile-EN.pdf">{g.ic("file")}<span>{"Company profile, English" if en else "الملف التعريفي، بالإنجليزية"}<small>PDF · 6 {"pages" if en else "صفحات"}</small></span></a>
<a href="/assets/docs/Syncstead-Company-Profile-AR.pdf">{g.ic("file")}<span>{"Company profile, Arabic" if en else "الملف التعريفي، بالعربية"}<small>PDF · 6 {"pages" if en else "صفحات"}</small></span></a></div>
</div></div></section>
<section class="soft" id="faq"><div class="w" style="max-width:860px"><div class="head"><div class="eyebrow">{"FAQ" if en else "الأسئلة الشائعة"}</div><h2>{"Questions we are often asked." if en else "أسئلة تصلنا كثيرًا."}</h2></div>{faq(FAQ[lang])}</div></section>'''

# ---------------------------------------------------------------- CONTACT
def contact(lang):
    g = G(); en = lang == "en"
    L = (dict(name="Full name", email="Work email", company="Company", size="Number of employees", choose="Choose", phone="Mobile (optional)", send="Request a demo",
              note='This opens your email app with the details filled in. See our <a href="/en/privacy/">privacy notice</a>.', ok="Thank you. Your email app should now be open. Press send and we will reply within one working day.",
              subj="Demo request: ", lines=["Name: ", "Work email: ", "Company: ", "Employees: ", "Mobile: "]) if en else
         dict(name="الاسم الكامل", email="البريد الإلكتروني للعمل", company="المنشأة", size="عدد الموظفين", choose="اختر", phone="الجوال (اختياري)", send="اطلب عرضًا",
              note='يفتح هذا تطبيق البريد لديك والتفاصيل معبأة. اطلع على <a href="/ar/privacy/">إشعار الخصوصية</a>.', ok="شكرًا لك. يُفترض أن تطبيق البريد مفتوح الآن، اضغط إرسال وسنرد خلال يوم عمل واحد.",
              subj="طلب عرض: ", lines=["الاسم: ", "البريد: ", "المنشأة: ", "عدد الموظفين: ", "الجوال: "]))
    js_lines = json.dumps(L["lines"], ensure_ascii=False)
    return f'''<section class="navy" style="padding-bottom:56px"><div class="w"><div class="eyebrow">{"Contact" if en else "تواصل معنا"}</div>
<h1 style="margin-top:12px;max-width:900px">{"Let's talk about your organization." if en else "لنتحدث عن منشأتك."}</h1>
<p class="lead">{"Book a 20-minute call, message us on WhatsApp, or send your details and we will reply within one working day." if en else "احجز مكالمة مدتها 20 دقيقة، أو راسلنا على واتساب، أو أرسل بياناتك وسنرد خلال يوم عمل واحد."}</p></div></section>
<section><div class="w"><div class="grid g2" style="gap:48px;align-items:start;grid-template-columns:1fr 1.2fr">
<div>
<div class="card"><div class="ico">{g.ic("time")}</div><h3>{"Book a demo" if en else "احجز عرضًا"}</h3><p>{"Pick a time that suits you in our calendar." if en else "اختر الوقت المناسب لك من تقويمنا."}</p><a class="btn" style="margin-top:14px" href="{BOOK}" target="_blank" rel="noopener">{"Book a 20-min demo" if en else "احجز عرضًا في 20 دقيقة"}</a></div>
<div class="card" style="margin-top:16px"><div class="ico">{g.ic("phone")}</div><h3>WhatsApp</h3><p dir="ltr" style="text-align:start">+966 55 317 9126</p><a class="btn line" style="margin-top:14px" href="{WA}" target="_blank" rel="noopener">{"WhatsApp us" if en else "راسلنا على واتساب"}</a></div>
<div class="card" style="margin-top:16px"><div class="ico">{g.ic("file")}</div><h3>{"Email" if en else "البريد الإلكتروني"}</h3><p><a href="mailto:info@syncstead.com.sa">info@syncstead.com.sa</a></p><p style="font-size:14px">{"Riyadh, Saudi Arabia" if en else "الرياض، المملكة العربية السعودية"}</p></div>
</div>
<div class="card"><h3>{"Send your details" if en else "أرسل بياناتك"}</h3>
<form id="demo" novalidate>
<div class="two"><label>{L["name"]}<input name="name" autocomplete="name" required></label><label>{L["email"]}<input name="email" type="email" autocomplete="email" required></label></div>
<div class="two"><label>{L["company"]}<input name="company" autocomplete="organization" required></label><label>{L["size"]}<select name="size" required><option value="">{L["choose"]}</option><option>200–499</option><option>500–999</option><option>1,000–2,499</option><option>2,500+</option></select></label></div>
<label>{L["phone"]}<input name="phone" type="tel" autocomplete="tel" inputmode="tel"></label>
<button class="btn" type="submit">{L["send"]}</button>
<p style="font-size:13px;margin-top:12px">{L["note"]}</p>
<div class="ok" id="ok" hidden>{L["ok"]}</div>
</form></div>
</div></div></section>
<script>
document.getElementById('demo').addEventListener('submit',function(e){{
e.preventDefault();var f=e.target;if(!f.checkValidity()){{f.reportValidity();return;}}
var d=new FormData(f),L={js_lines};
var body=L[0]+d.get('name')+'\\n'+L[1]+d.get('email')+'\\n'+L[2]+d.get('company')+'\\n'+L[3]+d.get('size')+'\\n'+L[4]+(d.get('phone')||'-');
location.href='mailto:info@syncstead.com.sa?subject='+encodeURIComponent('{L["subj"]}'+d.get('company'))+'&body='+encodeURIComponent(body);
document.getElementById('ok').hidden=false;}});
</script>'''

import json  # noqa: E402

def meta(en_t, en_d, ar_t, ar_d): return {"en": (en_t, en_d), "ar": (ar_t, ar_d)}
M = {
 "home": meta("Syncstead | Saudi HCM platform: HR, payroll and talent", "One bilingual platform for HR, payroll, attendance, talent and organization design, built around Saudi labour law, for companies of 200+ employees.",
              "سينكستيد | منصة سعودية لإدارة رأس المال البشري", "منصة واحدة ثنائية اللغة للموارد البشرية والرواتب والحضور والمواهب والتصميم التنظيمي، مبنية على نظام العمل السعودي، للمنشآت من 200 موظف فأكثر."),
 "platform": meta("Platform | Syncstead", "Payroll and compliance, attendance, talent and rewards, organization design and employee self-service in one Saudi HCM platform.",
                  "المنصة | سينكستيد", "الرواتب والامتثال والحضور والمواهب والمكافآت والتصميم التنظيمي والخدمة الذاتية في منصة سعودية واحدة."),
 "packages": meta("Packages | Syncstead", "Core, Professional and Enterprise: three packages on one platform, sized by headcount, with one-click upgrades.",
                  "الباقات | سينكستيد", "الأساسية والاحترافية والمؤسسات: ثلاث باقات على منصة واحدة حسب عدد الموظفين، مع الترقية بضغطة واحدة."),
 "why-syncstead": meta("Why Syncstead | Syncstead", "Saudi rules built in, the cost of every decision shown first, governance by design, and go-live in weeks.",
                       "لماذا سينكستيد | سينكستيد", "الأنظمة السعودية مدمجة، وتكلفة كل قرار ظاهرة أولًا، وحوكمة مدمجة، وتشغيل في أسابيع."),
 "trust": meta("Trust & security | Syncstead", "Security controls, data protection under the PDPL, and hosting options: our cloud, in the Kingdom (planned) or your own servers.",
               "الأمان والثقة | سينكستيد", "ضوابط الأمان، وحماية البيانات وفق نظام حماية البيانات الشخصية، وخيارات الاستضافة."),
 "about": meta("About | Syncstead", "Syncstead is a Saudi company headquartered in Riyadh, built by HR and governance practitioners.",
               "من نحن | سينكستيد", "سينكستيد شركة سعودية مقرها الرياض، صممها مختصون في الموارد البشرية والحوكمة."),
 "resources": meta("Resources | Syncstead", "Free end-of-service calculator, company profile downloads and answers to common questions.",
                   "الموارد | سينكستيد", "حاسبة مكافأة نهاية الخدمة المجانية، وتنزيل الملف التعريفي، وإجابات الأسئلة الشائعة."),
 "contact": meta("Contact | Syncstead", "Book a demo, message us on WhatsApp or email info@syncstead.com.sa.",
                 "تواصل معنا | سينكستيد", "احجز عرضًا، أو راسلنا على واتساب، أو عبر البريد info@syncstead.com.sa."),
}
BODY = {"home": home, "platform": platform, "packages": packages, "why-syncstead": why, "trust": trust, "about": about, "resources": resources, "contact": contact}

CONTENT = {}
for lang in ("en", "ar"):
    CONTENT[lang] = {}
    for k, fn in BODY.items():
        t, d = M[k][lang]
        CONTENT[lang][k] = {"title": t, "desc": d, "body": fn, "cta": k != "contact"}
        if k in ("resources",):
            CONTENT[lang][k]["schema"] = faq_schema(FAQ[lang])
