#!/usr/bin/env python3
"""One-off SEO head injector for Broker Gateway static pages.
Inserts analytics.js, canonical, OpenGraph/Twitter, and JSON-LD after <title>.
Idempotent: skips files that already contain the marker."""
import re, html

BASE = "https://zhangcindy29-code.github.io/loanbridge-preview/"
OG_IMAGE = BASE + "assets/broker1.jpg"
MARKER = "<!-- seo:start -->"
ORG = "Broker Gateway"

# Organization block reused as publisher/provider
ORG_LD = {
    "@type": "FinancialService",
    "name": ORG,
    "url": BASE,
    "image": OG_IMAGE,
    "areaServed": "Sydney, NSW, Australia",
    "description": "Sydney mortgage brokers serving the Chinese, Cantonese and Vietnamese community in their own language — broker matching, property management, conveyancing and settlement support.",
    "knowsLanguage": ["en", "zh", "yue", "vi"],
    "serviceType": ["Mortgage broking", "Property management", "Conveyancing"],
}

PAGES = {
    "index.html": {
        "url": BASE,
        "og_type": "website",
        "desc": "Sydney mortgage brokers serving the Chinese, Cantonese & Vietnamese community in your language. Free broker matching, up to 12 months free property management, plus home loan, conveyancing & settlement support — one team, end to end.",
        "search_console": True,
        "ld": [
            {"@context": "https://schema.org", **ORG_LD},
            {"@context": "https://schema.org", "@type": "WebSite", "name": ORG, "url": BASE},
        ],
    },
    "property-management.html": {
        "url": BASE + "property-management.html",
        "og_type": "website",
        "ld": [{"@context": "https://schema.org", "@type": "Service",
                "name": "Up to 12 Months Free Property Management",
                "provider": {**ORG_LD}, "areaServed": "Sydney, NSW, Australia", "url": BASE + "property-management.html"}],
    },
    "buying-guide.html": {
        "url": BASE + "buying-guide.html",
        "og_type": "article",
        "ld": [{"@context": "https://schema.org", "@type": "WebPage",
                "name": "Sydney Home Buying & Loan Pitfalls Guide",
                "url": BASE + "buying-guide.html", "publisher": {**ORG_LD}}],
    },
}

ARTICLES = [
    "article-first-home-buyer-nsw.html",
    "article-refinancing-guide.html",
    "article-investment-vs-owner-occupier.html",
    "article-self-employed-home-loans.html",
    "article-stamp-duty-lmi.html",
    "article-construction-finance.html",
]
for a in ARTICLES:
    PAGES[a] = {"url": BASE + a, "og_type": "article", "is_article": True}

import json
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
DESC_RE = re.compile(r'<meta name="description" content="(.*?)"\s*/?>', re.S)

def ld_to_script(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=2) + '\n</script>'

for fn, cfg in PAGES.items():
    with open(fn, encoding="utf-8") as f:
        src = f.read()
    if MARKER in src:
        print(f"skip (already injected): {fn}")
        continue
    m = TITLE_RE.search(src)
    title = html.unescape(m.group(1)).strip() if m else ORG
    dm = DESC_RE.search(src)
    desc = cfg.get("desc") or (dm.group(1) if dm else ORG_LD["description"])
    url = cfg["url"]

    block = [MARKER]
    if cfg.get("search_console"):
        block.append('<!-- Google Search Console: 用"HTML 标记"验证时,把 Google 给的 <meta name="google-site-verification" ...> 粘到下面这行 -->')
    if cfg.get("desc") and not dm:
        block.append(f'<meta name="description" content="{html.escape(desc, quote=True)}"/>')
    block += [
        f'<link rel="canonical" href="{url}"/>',
        f'<meta property="og:site_name" content="{ORG}"/>',
        f'<meta property="og:type" content="{cfg["og_type"]}"/>',
        f'<meta property="og:title" content="{html.escape(title, quote=True)}"/>',
        f'<meta property="og:description" content="{html.escape(desc, quote=True)}"/>',
        f'<meta property="og:url" content="{url}"/>',
        f'<meta property="og:image" content="{OG_IMAGE}"/>',
        '<meta name="twitter:card" content="summary_large_image"/>',
        f'<meta name="twitter:title" content="{html.escape(title, quote=True)}"/>',
        f'<meta name="twitter:description" content="{html.escape(desc, quote=True)}"/>',
        f'<meta name="twitter:image" content="{OG_IMAGE}"/>',
        '<script src="analytics.js"></script>',
    ]

    if cfg.get("is_article"):
        ld = {"@context": "https://schema.org", "@type": "Article",
              "headline": title, "description": desc, "url": url, "image": OG_IMAGE,
              "inLanguage": "en", "datePublished": "2025-06-11", "dateModified": "2025-06-11",
              "author": {"@type": "Organization", "name": ORG},
              "publisher": {"@type": "Organization", "name": ORG, "logo": {"@type": "ImageObject", "url": OG_IMAGE}},
              "mainEntityOfPage": url}
        block.append(ld_to_script(ld))
    else:
        for obj in cfg.get("ld", []):
            block.append(ld_to_script(obj))
    block.append("<!-- seo:end -->")

    insert = "\n" + "\n".join(block) + "\n"
    new = src[:m.end()] + insert + src[m.end():]
    with open(fn, "w", encoding="utf-8") as f:
        f.write(new)
    print(f"injected: {fn}")
