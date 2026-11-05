"""New articles built from the end-of-service article template, so they share its header, footer,
styles and analytics. Run from the repository root:  python3 tools/articles.py
Each article: slug -> {lang: dict(title, desc, h1, date_label, read, lead, body)}; body is the HTML
between the lead paragraph and the end of the page div."""
import os, re, json

SITE = "https://www.syncstead.com.sa"
TEMPLATE_SLUG = "end-of-service"

ARTICLES = {}
from articles_content import ARTICLES  # noqa: E402  (content lives in its own file)


def build_one(slug, lang, c, date_iso):
    tpl = open(os.path.join(lang, "articles", TEMPLATE_SLUG, "index.html"), encoding="utf-8").read()
    crumb = "Articles" if lang == "en" else "المقالات"
    main = f'''<main id="main" class="w"><div class="page">
<p class="crumb"><a href="/{lang}/articles/">{crumb}</a></p>
<h1>{c["h1"]}</h1>
<p class="meta">{c["date_label"]} · {c["read"]}</p>
<p class="lead">{c["lead"]}</p>
{c["body"]}
</div></main>'''
    s = re.sub(r'<main id="main" class="w">.*?</main>', lambda _: main, tpl, flags=re.S)
    s = re.sub(r"<title>.*?</title>", f"<title>{c['title']}</title>", s, flags=re.S)
    s = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda m: m.group(1) + c["desc"], s)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + c["title"], s)
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": c["h1"], "datePublished": date_iso,
          "inLanguage": lang, "author": {"@type": "Organization", "name": "Syncstead"},
          "publisher": {"@type": "Organization", "name": "Syncstead"},
          "mainEntityOfPage": f"{SITE}/{lang}/articles/{slug}/"}
    s = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "Article".*?</script>',
               lambda _: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>", s, count=1, flags=re.S)
    s = s.replace(f"/articles/{TEMPLATE_SLUG}/", f"/articles/{slug}/")  # canonical, hreflang, language switch
    path = os.path.join(lang, "articles", slug, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(s)
    return path


def add_to_index(slug, lang, c):
    p = os.path.join(lang, "articles", "index.html")
    s = open(p, encoding="utf-8").read()
    if f'/articles/{slug}/"' in s:
        return
    read = "Read →" if lang == "en" else "اقرأ ←"
    card = f'<a class="article-card" href="/{lang}/articles/{slug}/"><h2>{c["h1"]}</h2><p>{c["desc"]}</p><span>{read}</span></a>\n'
    s = s.replace('<div class="article-list">\n', '<div class="article-list">\n' + card, 1)
    open(p, "w", encoding="utf-8").write(s)


def add_to_sitemap(slug):
    p = "sitemap.xml"
    s = open(p, encoding="utf-8").read()
    if f"/articles/{slug}/" in s:
        return
    rows = ""
    for lang in ("ar", "en"):
        u = f"{SITE}/{lang}/articles/{slug}/"
        rows += (f'<url><loc>{u}</loc><xhtml:link rel="alternate" hreflang="ar" href="{SITE}/ar/articles/{slug}/"/>'
                 f'<xhtml:link rel="alternate" hreflang="en" href="{SITE}/en/articles/{slug}/"/></url>\n')
    s = s.replace("</urlset>", rows + "</urlset>")
    open(p, "w", encoding="utf-8").write(s)


if __name__ == "__main__":
    for slug, spec in ARTICLES.items():
        for lang in ("en", "ar"):
            print(build_one(slug, lang, spec[lang], spec["date"]))
            add_to_index(slug, lang, spec[lang])
        add_to_sitemap(slug)
