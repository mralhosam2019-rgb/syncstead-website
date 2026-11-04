"""Header menu (dropdowns): Platform and Solutions open mega panels, Resources and Company simple lists.
Used by gen.py and by the one-off script that updates the existing pages. Behaviour lives in /assets/nav.js."""

I = {
    "core": '<circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 4.5a3.5 3.5 0 0 1 0 7M18 14c2 .8 3 3 3 6"/>',
    "payroll": '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h4"/>',
    "time": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "talent": '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/>',
    "org": '<rect x="9" y="3" width="6" height="5" rx="1"/><rect x="3" y="16" width="6" height="5" rx="1"/><rect x="15" y="16" width="6" height="5" rx="1"/><path d="M12 8v4M6 16v-4h12v4"/>',
    "mobile": '<rect x="7" y="2.5" width="10" height="19" rx="2"/><path d="M11 18h2"/>',
}
CARET = '<svg class="caret" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'

T = {
    "en": dict(
        platform="Platform", solutions="Solutions", packages="Packages", resources="Resources", company="Company",
        g_core="Core", g_people="People &amp; experience", g_role="By role", g_size="By company size", g_calc="Free calculators",
        mods=[("core", "Core HR", "Employee files, requests and documents"),
              ("payroll", "Payroll", "GOSI, end of service, bank and Mudad files"),
              ("time", "Attendance &amp; leave", "Shifts, check-ins and leave balances"),
              ("talent", "Talent", "Hiring, onboarding, performance and rewards"),
              ("org", "Organization design", "Org chart, and test changes before making them"),
              ("mobile", "Self-service &amp; mobile", "Requests and payslips on every phone")],
        roles=[("lead", "Leadership", "Workforce, cost and Saudization in one view"),
               ("hr", "HR teams", "Every HR process in Arabic and English"),
               ("fin", "Finance &amp; payroll", "Payroll you can reconcile to the riyal"),
               ("it", "IT &amp; security", "Single sign-on, data separation, hosting options")],
        sizes=[("200 – 1,000 employees", "Live in weeks with ready Saudi settings"),
               ("1,000+ employees and groups", "Several companies, approval paths, flexible hosting")],
        card_eyebrow="See it live", card_title="See Syncstead with your own structure", card_text="20 minutes, Arabic and English, no commitment.",
        card_btn="Request a demo", unsure="Not sure where to start?", unsure_text="We’ll show you with your own structure.",
        all_platform="See the whole platform", trust="Trust &amp; security", calcs="Free calculators",
        res=[("articles", "Articles", "Guides on Saudi labour law and payroll")],
        calc_links=[("end-of-service-calculator", "End of service"), ("leave-balance-calculator", "Leave balance"),
                    ("overtime-calculator", "Overtime pay"), ("final-settlement-calculator", "Final settlement")],
        profile="Company profile (PDF)", faq="FAQ",
        comp=[("about", "About"), ("why-syncstead", "Why Syncstead"), ("trust", "Trust &amp; security"), ("contact", "Contact")],
        pdf="EN"),
    "ar": dict(
        platform="المنصة", solutions="الحلول", packages="الباقات", resources="الموارد", company="الشركة",
        g_core="الأساسيات", g_people="الموظفون والتجربة", g_role="حسب الدور", g_size="حسب حجم الشركة", g_calc="حاسبات مجانية",
        mods=[("core", "الموارد البشرية الأساسية", "ملفات الموظفين والطلبات والمستندات"),
              ("payroll", "الرواتب", "التأمينات ونهاية الخدمة وملفات البنك ومدد"),
              ("time", "الحضور والإجازات", "الورديات والبصمة وأرصدة الإجازات"),
              ("talent", "المواهب", "التوظيف والتهيئة والأداء والمكافآت"),
              ("org", "التصميم التنظيمي", "الهيكل التنظيمي وتجربة التغييرات قبل تنفيذها"),
              ("mobile", "الخدمة الذاتية والجوال", "الطلبات وقسائم الرواتب على كل جوال")],
        roles=[("lead", "القيادة", "القوى العاملة والتكلفة والتوطين في شاشة واحدة"),
               ("hr", "فرق الموارد البشرية", "كل إجراءات الموارد البشرية بالعربية والإنجليزية"),
               ("fin", "المالية والرواتب", "رواتب تطابقها حتى آخر ريال"),
               ("it", "تقنية المعلومات والأمان", "الدخول الموحد وفصل البيانات وخيارات الاستضافة")],
        sizes=[("من 200 إلى 1,000 موظف", "تشغيل خلال أسابيع بإعدادات سعودية جاهزة"),
               ("أكثر من 1,000 موظف ومجموعات الشركات", "عدة شركات ومسارات موافقات واستضافة مرنة")],
        card_eyebrow="شاهدها مباشرة", card_title="شاهد سينكستيد على هيكل شركتك", card_text="20 دقيقة، بالعربية والإنجليزية، دون التزام.",
        card_btn="اطلب عرضًا", unsure="لست متأكدًا من أين تبدأ؟", unsure_text="سنعرضها لك على هيكل شركتك.",
        all_platform="تعرّف على المنصة كاملة", trust="الأمان والثقة", calcs="الحاسبات المجانية",
        res=[("articles", "المقالات", "أدلة في نظام العمل السعودي والرواتب")],
        calc_links=[("end-of-service-calculator", "مكافأة نهاية الخدمة"), ("leave-balance-calculator", "رصيد الإجازة"),
                    ("overtime-calculator", "أجر العمل الإضافي"), ("final-settlement-calculator", "المخالصة النهائية")],
        profile="الملف التعريفي (PDF)", faq="الأسئلة الشائعة",
        comp=[("about", "من نحن"), ("why-syncstead", "لماذا سينكستيد"), ("trust", "الأمان والثقة"), ("contact", "تواصل معنا")],
        pdf="AR"),
}

SECTION_OF = {"platform": "platform", "packages": "packages", "resources": "resources", "articles": "resources",
              "about": "company", "why-syncstead": "company", "trust": "company", "contact": "company"}


def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[name]}</svg>'


def nav(lang, slug=""):
    t = T[lang]
    u = lambda s: f"/{lang}/" + (f"{s}/" if s else "")
    top = (slug or "").split("/")[0]
    if top.endswith("-calculator"):
        top = "resources"
    cur = SECTION_OF.get(top, "")
    on = lambda k: ' data-current="true"' if cur == k else ""

    def btn(key, label):
        return f'<button type="button" class="mt" aria-expanded="false" aria-controls="m-{key}"{on(key)}>{label}{CARET}</button>'

    def mod(key, name, desc):
        return f'<a class="mm" href="{u("platform")}#{key}"><span class="mi-ico">{icon(key)}</span><span><b>{name}</b><small>{desc}</small></span></a>'

    mods = t["mods"]
    platform = (
        f'<div class="mi">{btn("platform", t["platform"])}<div class="mp mega" id="m-platform"><div class="mega-in">'
        f'<div class="mcol"><span class="mh">{t["g_core"]}</span>{"".join(mod(*m) for m in mods[:3])}</div>'
        f'<div class="mcol"><span class="mh">{t["g_people"]}</span>{"".join(mod(*m) for m in mods[3:])}</div>'
        f'<a class="mcard" href="{u("demo")}?from=menu-platform"><span class="mh">{t["card_eyebrow"]}</span><b>{t["card_title"]}</b><small>{t["card_text"]}</small><span class="btn sm">{t["card_btn"]}</span></a>'
        f'</div><div class="mfoot"><a href="{u("platform")}"><b>{t["all_platform"]} {"←" if lang == "ar" else "→"}</b></a><a href="{u("trust")}">{t["trust"]}</a><a href="{u("packages")}">{t["packages"]}</a><a href="{u("resources")}">{t["calcs"]}</a></div></div></div>'
    )
    roles = "".join(f'<a class="mm" href="{u("")}#role-{k}"><span><b>{n}</b><small>{d}</small></span></a>' for k, n, d in t["roles"])
    sizes = "".join(f'<a class="mm" href="{u("packages")}"><span><b>{n}</b><small>{d}</small></span></a>' for n, d in t["sizes"])
    solutions = (
        f'<div class="mi">{btn("solutions", t["solutions"])}<div class="mp mega" id="m-solutions"><div class="mega-in two">'
        f'<div class="mcol"><span class="mh">{t["g_role"]}</span>{roles}</div>'
        f'<div class="mcol soft"><span class="mh">{t["g_size"]}</span>{sizes}'
        f'<a class="mcta" href="{u("demo")}?from=menu-solutions"><span><b>{t["unsure"]}</b><small>{t["unsure_text"]}</small></span><span class="btn sm">{t["card_btn"]}</span></a></div>'
        f'</div></div></div>'
    )
    packages = f'<a class="mt" href="{u("packages")}"{on("packages")}>{t["packages"]}</a>'
    res_links = "".join(f'<a class="mm" href="{u(s)}"><span><b>{n}</b><small>{d}</small></span></a>' for s, n, d in t["res"])
    calcs = "".join(f'<a href="{u(s)}">{n}</a>' for s, n in t["calc_links"])
    resources = (
        f'<div class="mi">{btn("resources", t["resources"])}<div class="mp drop" id="m-resources">{res_links}'
        f'<span class="mh">{t["g_calc"]}</span>{calcs}<hr>'
        f'<a href="/assets/docs/Syncstead-Company-Profile-{t["pdf"]}.pdf">{t["profile"]}</a><a href="{u("resources")}#faq">{t["faq"]}</a></div></div>'
    )
    company = (
        f'<div class="mi">{btn("company", t["company"])}<div class="mp drop" id="m-company">'
        + "".join(f'<a href="{u(s)}">{n}</a>' for s, n in t["comp"])
        + "</div></div>"
    )
    return platform + solutions + packages + resources + company
