#!/usr/bin/env python3
"""Builds the Syncstead website (v2) in Arabic and English from one template.
Run from the repository root:  python3 tools/gen.py
Pages: home, platform, packages, why-syncstead, trust, about, resources, contact
(+ the end-of-service calculator and privacy pages keep their content and get the new header and footer)."""
import json, os, re

SITE = "https://www.syncstead.com.sa"
BOOK = "https://calendar.google.com/calendar/u/0/appointments/schedules/AcZssZ2sW2kQ_5vAHw4p-v_kQ_gorsm-WFrjHmKt5hXqJT4UEJEq7yGhmZTgFgKtR7djox9nANAhFusb"
WA = "https://wa.me/966553179126"
# --- Demo requests and measurement (fill in once, then rebuild) ---
# FORM_URL: the web app address of tools/demo-requests.gs after it is deployed from alhosam@syncstead.com.sa.
#           Empty = the form falls back to opening the visitor's email app.
FORM_URL = ""
# CF_TOKEN: the Cloudflare Web Analytics site token. Empty = no analytics script.
CF_TOKEN = ""
V = "6"

ICONS = {
  "law": '<path d="M12 3v18M5 7h14M7 7l-3 7a3 3 0 0 0 6 0L7 7zM17 7l-3 7a3 3 0 0 0 6 0l-3-7zM8 21h8"/>',
  "layers": '<path d="M12 3 2 8l10 5 10-5-10-5z"/><path d="m2 13 10 5 10-5"/><path d="m2 17.5 10 5 10-5"/>',
  "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
  "shield": '<path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6l-8-3z"/><path d="m9 12 2 2 4-4"/>',
  "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.5a6.5 6.5 0 0 1 3.5 5.5"/>',
  "pay": '<rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 9v.01M18 15v.01"/>',
  "time": '<rect x="3" y="4.5" width="18" height="16" rx="2"/><path d="M3 9.5h18M8 2.5v4M16 2.5v4M8 14h3"/>',
  "star": '<path d="m12 3 2.7 5.6 6.1.8-4.4 4.3 1.1 6.1L12 17l-5.5 2.8 1.1-6.1L3.2 9.4l6.1-.8L12 3z"/>',
  "org": '<rect x="9" y="2.5" width="6" height="5" rx="1"/><rect x="2.5" y="16.5" width="6" height="5" rx="1"/><rect x="15.5" y="16.5" width="6" height="5" rx="1"/><path d="M12 7.5v4.5M5.5 16.5V12h13v4.5"/>',
  "flow": '<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.5 6H15a3 3 0 0 1 0 6H9a3 3 0 0 0 0 6h6.5"/>',
  "flag": '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
  "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
  "lock": '<rect x="4" y="10.5" width="16" height="10.5" rx="2"/><path d="M8 10.5V7a4 4 0 0 1 8 0v3.5"/>',
  "phone": '<rect x="6.5" y="2.5" width="11" height="19" rx="2.2"/><path d="M11 18.5h2"/>',
  "server": '<rect x="3" y="3.5" width="18" height="7" rx="1.5"/><rect x="3" y="13.5" width="18" height="7" rx="1.5"/><path d="M7 7h.01M7 17h.01"/>',
  "cloud": '<path d="M7 18a4.5 4.5 0 0 1-.5-9A6 6 0 0 1 18 9.5a4 4 0 0 1-.5 8.5z"/>',
  "file": '<path d="M14 2.5H6.5a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V8z"/><path d="M14 2.5V8h5.5M8.5 13h7M8.5 17h5"/>',
  "key": '<circle cx="8" cy="15" r="4"/><path d="m11 12 9-9M17 6l3 3M14.5 8.5l2 2"/>',
  "calc": '<rect x="5" y="2.5" width="14" height="19" rx="2"/><path d="M8.5 6.5h7M8.5 11h.01M12 11h.01M15.5 11h.01M8.5 14.5h.01M12 14.5h.01M15.5 14.5h.01M8.5 18h.01M12 18h3.5"/>',
  "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
  "db": '<ellipse cx="12" cy="5.5" rx="8" ry="3"/><path d="M4 5.5v13c0 1.7 3.6 3 8 3s8-1.3 8-3v-13M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
}
def ic(n): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'
MARK = '<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="7" fill="#14B8A6"/><path d="M21 10c-1-2-3-3-5-3-3 0-5 1.6-5 4 0 6 10 3 10 9 0 2.5-2.5 4-5.5 4-2.5 0-4.5-1-5.5-3" fill="none" stroke="#1B2A4A" stroke-width="3" stroke-linecap="round"/></svg>'
WA_ICON = '<svg viewBox="0 0 32 32" aria-hidden="true"><path fill="#fff" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6a10.6 10.6 0 0 1-5.4-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.6.1-.2 0-.4 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.9 1 3.9.8a3.3 3.3 0 0 0 2.2-1.5 2.7 2.7 0 0 0 .2-1.5c-.1-.2-.3-.3-.6-.4z"/></svg>'

PAGES = ["", "platform", "packages", "why-syncstead", "trust", "about", "resources", "contact", "demo", "demo/next"]
NAV = {
  "en": [("platform", "Platform"), ("packages", "Packages"), ("why-syncstead", "Why Syncstead"), ("trust", "Trust & security"), ("about", "About"), ("resources", "Resources"), ("contact", "Contact")],
  "ar": [("platform", "المنصة"), ("packages", "الباقات"), ("why-syncstead", "لماذا سينكستيد"), ("trust", "الأمان والثقة"), ("about", "من نحن"), ("resources", "الموارد"), ("contact", "تواصل معنا")],
}
T = {
  "en": dict(book="Request a demo", book20="Request a demo", assure="20 minutes · no commitment · a Saudi company · reply within one working day", wa="WhatsApp us", menu="Menu", other="عربي", otherlang="ar", otherlabel="التبديل إلى العربية",
             tagline="Saudi human capital management platform: HR, payroll and talent in one bilingual system.",
             legal="Syncstead Company (SJSC) · CR 7055468719 · Riyadh, Saudi Arabia · © 2026", company="Company", product="Product", help="Get in touch",
             calc="End-of-service calculator", privacy="Privacy", profile="Company profile (PDF)", home="Home",
             cta_t="See Syncstead with your own structure.", cta_p="A 20-minute call, then a demo set up around how your organization works. A tailored proposal follows the first meeting.",
             skip="Skip to content", img="en"),
  "ar": dict(book="اطلب عرضًا", book20="اطلب عرضًا تجريبيًا", assure="20 دقيقة · دون التزام · شركة سعودية · نرد خلال يوم عمل واحد", wa="راسلنا على واتساب", menu="القائمة", other="English", otherlang="en", otherlabel="Switch to English",
             tagline="منصة سعودية لإدارة رأس المال البشري: الموارد البشرية والرواتب والمواهب في نظام واحد ثنائي اللغة.",
             legal="شركة سينكستيد (شركة مساهمة مبسطة) · السجل التجاري 7055468719 · الرياض، المملكة العربية السعودية · © 2026", company="الشركة", product="المنتج", help="تواصل معنا",
             calc="حاسبة مكافأة نهاية الخدمة", privacy="الخصوصية", profile="الملف التعريفي (PDF)", home="الرئيسية",
             cta_t="شاهد سينكستيد بهيكل منشأتك.", cta_p="مكالمة قصيرة مدتها 20 دقيقة، ثم عرض مُعدّ حول طريقة عمل منشأتك. يصلكم عرض مخصص بعد اللقاء الأول.",
             skip="انتقل إلى المحتوى", img="ar"),
}

def url(lang, slug): return f"/{lang}/" + (f"{slug}/" if slug else "")

def header(lang, slug):
    t = T[lang]
    nav = "".join(f'<a href="{url(lang, s)}"{" aria-current=\"page\"" if s == slug else ""}>{n}</a>' for s, n in NAV[lang])
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<header><div class="w">
<a class="logo" href="{url(lang, "")}">{MARK}SYNCSTEAD</a>
<nav class="main" id="nav" aria-label="Main">{nav}</nav>
<div class="tools"><a class="lang" hreflang="{t["otherlang"]}" lang="{t["otherlang"]}" href="{url(t["otherlang"], slug)}" aria-label="{t["otherlabel"]}">{t["other"]}</a><a class="btn sm" href="{url(lang, "demo")}?from={slug or "home"}">{t["book"]}</a>
<button class="menu-btn" aria-label="{t["menu"]}" aria-expanded="false" aria-controls="nav" onclick="var n=document.getElementById('nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">☰</button></div>
</div></header>'''

def footer(lang, slug=""):
    t = T[lang]; n = dict(NAV[lang]); wa = wa_link(lang, slug)
    pdf = f"/assets/docs/Syncstead-Company-Profile-{'AR' if lang == 'ar' else 'EN'}.pdf"
    return f'''<footer><div class="w">
<div class="cols">
<div><a class="logo" href="{url(lang, "")}">{MARK}SYNCSTEAD</a><p style="margin-top:14px;font-size:14px;color:var(--onnavy);max-width:320px">{t["tagline"]}</p></div>
<div><h4>{t["product"]}</h4><a href="{url(lang, "platform")}">{n["platform"]}</a><a href="{url(lang, "packages")}">{n["packages"]}</a><a href="{url(lang, "why-syncstead")}">{n["why-syncstead"]}</a><a href="{url(lang, "trust")}">{n["trust"]}</a></div>
<div><h4>{t["company"]}</h4><a href="{url(lang, "about")}">{n["about"]}</a><a href="{url(lang, "resources")}">{n["resources"]}</a><a href="{url(lang, "end-of-service-calculator")}">{t["calc"]}</a><a href="{pdf}">{t["profile"]}</a></div>
<div><h4>{t["help"]}</h4><a href="{url(lang, "demo")}">{t["book"]}</a><a href="mailto:info@syncstead.com.sa">info@syncstead.com.sa</a><a href="{wa}" target="_blank" rel="noopener">WhatsApp</a><a href="{url(lang, "privacy")}">{t["privacy"]}</a></div>
</div>
<div class="legal"><span>{t["legal"]}</span><span>syncstead.com.sa</span></div>
</div></footer>
<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="{t["wa"]}">{WA_ICON}</a>
<script src="/assets/fit.js?v={V}" defer></script>
<script>try{{var u=new URLSearchParams(location.search);['utm_source','utm_medium','utm_campaign'].forEach(function(k){{if(u.get(k))sessionStorage.setItem(k,u.get(k))}});if(!sessionStorage.getItem('first_ref'))sessionStorage.setItem('first_ref',document.referrer||'direct')}}catch(e){{}}</script>'''

def head(lang, slug, title, desc, schema=None):
    CF = (f"\n<script defer src=\"https://static.cloudflareinsights.com/beacon.min.js\" data-cf-beacon='{{\"token\": \"{CF_TOKEN}\"}}'></script>") if CF_TOKEN else ""
    NOINDEX = '\n<meta name="robots" content="noindex">' if slug == "demo/next" else ""
    other = "ar" if lang == "en" else "en"
    img = f"{SITE}/assets/img/v2/desk-dashboard-{lang}.jpg"
    ld = [{"@type": "Organization", "name": "Syncstead", "alternateName": "سينكستيد", "url": f"{SITE}/", "email": "info@syncstead.com.sa",
           "telephone": "+966553179126", "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"}}]
    if schema: ld += schema
    return f'''<!doctype html>
<html lang="{lang}" dir="{'rtl' if lang == 'ar' else 'ltr'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{url(lang, slug)}">
<link rel="alternate" hreflang="ar" href="{SITE}{url('ar', slug)}">
<link rel="alternate" hreflang="en" href="{SITE}{url('en', slug)}">
<link rel="alternate" hreflang="x-default" href="{SITE}{url('ar', slug)}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{url(lang, slug)}">
<meta property="og:image" content="{img}">
<meta property="og:locale" content="{'ar_SA' if lang == 'ar' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1B2A4A">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/site.css?v={V}">{CF}{NOINDEX}
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": ld}, ensure_ascii=False)}</script>
</head>
<body>'''

def page(lang, slug, title, desc, body, schema=None):
    return head(lang, slug, title, desc, schema) + "\n" + header(lang, slug) + f'\n<main id="main">\n{body}\n</main>\n' + footer(lang, slug) + "\n</body>\n</html>\n"

def img(lang, name, alt=""):
    return f'<img src="/assets/img/v2/{name}-{lang}.jpg" alt="{alt}" loading="lazy" width="1600" height="1000">'

def laptop(lang, name, alt=""):
    return f'<div class="laptop"><div class="scr">{img(lang, name, alt)}</div><div class="base"></div></div>'

def phone(lang, name, alt=""):
    return f'<div class="phone"><img src="/assets/img/v2/{name}-{lang}.jpg" alt="{alt}" loading="lazy" width="390" height="844"></div>'

WA_TOPIC = {
  "en": {"": "Syncstead", "platform": "the Syncstead platform", "packages": "Syncstead packages and a proposal", "why-syncstead": "Syncstead", "trust": "Syncstead security and hosting",
         "about": "Syncstead", "resources": "Syncstead", "contact": "Syncstead", "demo": "a Syncstead demo", "demo/next": "a Syncstead demo", "end-of-service-calculator": "end of service in Syncstead", "privacy": "Syncstead"},
  "ar": {"": "سينكستيد", "platform": "منصة سينكستيد", "packages": "باقات سينكستيد وعرض سعر", "why-syncstead": "سينكستيد", "trust": "الأمان والاستضافة في سينكستيد",
         "about": "سينكستيد", "resources": "سينكستيد", "contact": "سينكستيد", "demo": "عرض تجريبي لسينكستيد", "demo/next": "عرض تجريبي لسينكستيد", "end-of-service-calculator": "نهاية الخدمة في سينكستيد", "privacy": "سينكستيد"},
}
def wa_link(lang, slug=""):
    from urllib.parse import quote
    topic = WA_TOPIC[lang].get(slug, WA_TOPIC[lang][""])
    msg = f"Hello, I'd like to know more about {topic}." if lang == "en" else f"مرحبًا، أرغب في معرفة المزيد عن {topic}."
    return f"{WA}?text={quote(msg)}"

CTA = {
  "en": {"": ("See Syncstead with your own structure.", "Request a demo"), "platform": ("See it set up around your organization.", "See it with your own structure"),
         "packages": ("Not sure which package fits?", "Get a proposal for your size"), "why-syncstead": ("Compare us on your own terms.", "Request a demo"),
         "trust": ("Have your IT team's questions answered.", "Request our security overview"), "about": ("Talk to the founder directly.", "Request a demo"),
         "resources": ("Calculate end of service for every employee, automatically.", "See it in Syncstead"), "contact": None},
  "ar": {"": ("شاهد سينكستيد بهيكل منشأتك.", "اطلب عرضًا تجريبيًا"), "platform": ("شاهده مُعدًّا حول منشأتك.", "شاهده بهيكل منشأتك"),
         "packages": ("لست متأكدًا من الباقة المناسبة؟", "احصل على عرض يناسب حجمكم"), "why-syncstead": ("قارن بنفسك وبمعاييرك.", "اطلب عرضًا تجريبيًا"),
         "trust": ("إجابات لأسئلة فريق تقنية المعلومات لديكم.", "اطلب ملخص الأمان"), "about": ("تحدث مع المؤسس مباشرة.", "اطلب عرضًا تجريبيًا"),
         "resources": ("احسب نهاية الخدمة لكل موظف تلقائيًا.", "شاهدها في سينكستيد"), "contact": None},
}
INTEREST = {"packages": "proposal", "trust": "security", "resources": "eos"}

def cta(lang, slug=""):
    t = T[lang]; c = CTA[lang].get(slug, CTA[lang][""])
    if not c: return ""
    q = f"?from={slug or 'home'}" + (f"&interest={INTEREST[slug]}" if slug in INTEREST else "")
    return f'''<section class="tight"><div class="w"><div class="ctaband">
<div><h2 style="color:#fff">{c[0]}</h2><p>{t["cta_p"]}</p></div>
<div class="acts"><a class="btn" href="{url(lang, "demo")}{q}">{c[1]}</a><a class="btn ghost" href="{wa_link(lang, slug)}" target="_blank" rel="noopener">{t["wa"]}</a><p class="assure">{t["assure"]}</p></div>
</div></div></section>'''

from content import CONTENT  # noqa: E402  (page bodies per language)

def build():
    written = []
    for lang in ("en", "ar"):
        for slug in PAGES:
            c = CONTENT[lang][slug or "home"]
            body = c["body"](lang) + cta(lang, slug) if c.get("cta", True) else c["body"](lang)
            html = page(lang, slug, c["title"], c["desc"], body, c.get("schema"))
            path = os.path.join(lang, slug, "index.html") if slug else os.path.join(lang, "index.html")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w").write(html); written.append(path)
        # Calculator and privacy: keep their content, new header, footer and styles.
        for slug in ("end-of-service-calculator", "privacy"):
            path = os.path.join(lang, slug, "index.html")
            s = open(path).read()
            s = re.sub(r'<link rel="stylesheet" href="/assets/style\.css[^"]*">', f'<link rel="stylesheet" href="/assets/site.css?v={V}">', s)
            s = re.sub(r'(<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?)[^"]*"', r'\1family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap"', s)
            s = re.sub(r'(?:<a class="skip".*?</a>\s*)?<header>.*?</header>', header(lang, slug), s, flags=re.S)
            s = re.sub(r'<main class="w">', '<main id="main" class="w">', s)
            s = re.sub(r'\n<script defer src="https://static\.cloudflareinsights\.com[^\n]*', '', s)
            if CF_TOKEN: s = s.replace('</head>', f'<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon=\'{{"token": "{CF_TOKEN}"}}\'></script>\n</head>', 1)
            s = re.sub(r'<footer>.*?</footer>\s*(?:<a class="wa-float".*?</a>)?', footer(lang, slug), s, flags=re.S)
            open(path, "w").write(s); written.append(path)
    # Sitemap
    rows = []
    for slug in [x for x in PAGES if x != "demo/next"] + ["end-of-service-calculator", "privacy"]:
        for lang in ("ar", "en"):
            rows.append(f'<url><loc>{SITE}{url(lang, slug)}</loc><xhtml:link rel="alternate" hreflang="ar" href="{SITE}{url("ar", slug)}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}{url("en", slug)}"/></url>')
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")
    print("\n".join(written))

if __name__ == "__main__":
    import sys; sys.path.insert(0, os.path.dirname(__file__)); build()
