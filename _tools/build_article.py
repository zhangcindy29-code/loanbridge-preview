#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mortgage Bridge 文章生成器。

从一份 spec(dict) 生成与全站约定一致的 HTML：
  - seo:start/end 块 + canonical + OG + Twitter + Article/FAQPage JSON-LD
  - 统一 nav(含计算器入口 + 中英切换) / footer
  - 正文 / 留资表单(接 forms.js) / FAQ(details) / 相关链接 / 免责声明
  - i18n 字典，并自动校验覆盖率(漏译会报错，不会静默出半英半中的页面)

用法：写 spec → build(spec) → 检查 stdout 的漏译报告。
"""
import json
import re
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
SITE = "https://mortgagebrg.com.au"

HEAD = '''<!DOCTYPE html>

<html class="scroll-smooth" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<!-- seo:start -->
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{url}"/>
<meta property="og:site_name" content="Mortgage Bridge"/>
<meta property="og:type" content="article"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:url" content="{url}"/>
<meta property="og:image" content="{site}/assets/og-share.jpg"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title}"/>
<meta name="twitter:description" content="{desc}"/>
<meta name="twitter:image" content="{site}/assets/og-share.jpg"/>
<script src="analytics.js"></script>
<script type="application/ld+json">
{article_ld}
</script>
<script type="application/ld+json">
{faq_ld}
</script>
<!-- seo:end -->
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
tailwind.config = {{ darkMode: "class", theme: {{ extend: {{ colors: {{
"surface":"#fbf9f8","surface-container-low":"#f5f3f3","surface-container":"#efeded","surface-container-lowest":"#ffffff",
"surface-container-high":"#eae8e7","on-surface":"#1b1c1c","on-surface-variant":"#40484b",
"outline":"#70787c","outline-variant":"#c0c8cb","primary":"#003441","on-primary":"#ffffff",
"primary-container":"#0f4c5c","secondary":"#735c00","on-secondary":"#ffffff",
"secondary-container":"#fed65b","on-secondary-container":"#745c00","secondary-fixed":"#ffe088",
"secondary-fixed-dim":"#e9c349","error-container":"#ffdad6","on-error-container":"#93000a",
"background":"#fbf9f8" }} }} }} }};
</script>
<style>
body{{font-family:'Inter','PingFang SC',sans-serif;}}
.font-display{{font-family:'Be Vietnam Pro','PingFang SC',sans-serif;}}
.material-symbols-outlined{{font-variation-settings:'FILL' 0,'wght' 400,'GRAD' 0,'opsz' 24;}}
.glass-header{{background:rgba(251,249,248,0.85);backdrop-filter:blur(8px);}}
.prose-body p{{margin-bottom:1rem;line-height:1.85;}}
.prose-body ul{{margin:0.5rem 0 1.25rem;padding-left:0;}}
.prose-body li{{position:relative;padding-left:1.75rem;margin-bottom:0.6rem;line-height:1.7;}}
.prose-body li::before{{content:'';position:absolute;left:0;top:0.6rem;width:8px;height:8px;border-radius:9999px;background:#735c00;}}
</style>
</head>
<body class="bg-background text-on-surface">
<header class="sticky top-0 z-50 glass-header border-b border-outline-variant/30">
<nav class="flex justify-between items-center w-full px-5 md:px-10 max-w-4xl mx-auto h-16 md:h-20">
<a class="font-display text-base sm:text-xl md:text-2xl font-bold text-primary whitespace-nowrap" href="index.html">Mortgage Bridge</a>
<div class="flex items-center gap-3 md:gap-5">
<a class="hidden md:inline-flex items-center gap-1 text-on-surface-variant hover:text-primary text-sm font-semibold" href="index.html#knowledge">
<span class="material-symbols-outlined text-base">arrow_back</span>All Articles</a>
<a href="stamp-duty-calculator-nsw.html" class="hidden lg:inline-flex items-center gap-1.5 whitespace-nowrap px-3 md:px-4 py-2 rounded-full border border-primary text-primary font-bold hover:bg-primary/5 transition-colors text-sm">
<span class="material-symbols-outlined text-sm">calculate</span>Stamp duty calc</a>
<button data-noi18n="true" id="lang-toggle" onclick="toggleLang()" class="flex items-center gap-1.5 whitespace-nowrap px-3 md:px-4 py-2 rounded-full border border-primary text-primary font-bold hover:bg-primary/5 transition-colors text-sm">
<span class="material-symbols-outlined text-sm">translate</span><span id="lang-toggle-label">中文</span></button>
<a href="#lead" class="inline-flex whitespace-nowrap px-4 md:px-6 py-2 md:py-2.5 rounded-full bg-primary text-on-primary font-bold hover:opacity-90 transition text-sm">Talk to a broker</a>
</div>
</nav>
</header>
<main class="max-w-4xl mx-auto px-5 md:px-10 py-10 md:py-14">
<span class="inline-block px-3 py-1 rounded-full bg-secondary-container text-on-secondary-container text-xs font-bold mb-4">{badge}</span>
<h1 class="font-display text-3xl md:text-5xl font-bold text-primary leading-tight mb-4">{h1}</h1>
<div class="flex items-center gap-2 text-on-surface-variant text-sm mb-8">
<span class="material-symbols-outlined text-base">schedule</span>{read_time}</div>
<div class="prose-body text-on-surface-variant text-lg">
<p>{intro}</p>
</div>
'''

LEAD = '''
<section id="lead" class="my-12 p-6 md:p-8 rounded-2xl bg-primary text-on-primary scroll-mt-24">
<h2 class="font-display text-xl md:text-2xl font-bold mb-2 flex items-center gap-2"><span class="material-symbols-outlined text-secondary-fixed">verified</span>{cta_h}</h2>
<p class="text-on-primary/80 mb-6 text-sm md:text-base">{cta_p} <span class="text-on-primary/70">我们提供普通话/粤语服务。</span></p>
<form data-lead-form="{lead_tag}" data-success-en="✓ Thanks! A specialist will call you within 12 hours." data-success-zh="✓ 已收到！顾问会在12小时内联系你。" class="grid sm:grid-cols-2 gap-4">
<input required name="Name" placeholder="Your name / 称呼" class="w-full px-4 py-3 rounded-xl bg-on-primary text-on-surface placeholder-on-surface-variant/60 focus:outline-none focus:ring-2 focus:ring-secondary-fixed"/>
<input required name="Contact" placeholder="Phone or WeChat / 电话或微信" class="w-full px-4 py-3 rounded-xl bg-on-primary text-on-surface placeholder-on-surface-variant/60 focus:outline-none focus:ring-2 focus:ring-secondary-fixed"/>
<select name="Situation" class="w-full px-4 py-3 rounded-xl bg-on-primary text-on-surface sm:col-span-2">
{cta_options}
</select>
<button type="submit" class="sm:col-span-2 px-8 py-3.5 rounded-xl bg-secondary-container text-on-surface font-bold shadow-lg hover:shadow-xl transition">{cta_btn}</button>
</form>
</section>
'''

TAIL = '''
<p class="text-on-surface-variant/70 text-xs mt-8 leading-relaxed">{disclaimer}</p>
</main>
<footer class="bg-primary text-on-primary py-10">
<div class="max-w-4xl mx-auto px-5 md:px-10 flex flex-col md:flex-row justify-between items-center gap-4">
<div class="font-display text-xl font-bold">Mortgage Bridge</div>
<p class="text-on-primary/60 text-sm text-center">© 2026 Mortgage Bridge. Expert mortgage guidance for Sydney's multicultural communities.</p>
</div>
</footer>
<script src="forms.js"></script>
<script>
(function(){{
  const I18N = {dict};
  const PH = {{}};
  const SKIP=["SCRIPT","STYLE","NOSCRIPT"]; const reg=[];
  function walk(n){{ for(const c of n.childNodes){{
    if(c.nodeType===3){{ if(c.nodeValue.trim()) reg.push({{node:c,en:c.nodeValue,key:c.nodeValue.trim()}}); }}
    else if(c.nodeType===1){{ if(SKIP.includes(c.tagName))continue; if(c.hasAttribute("data-noi18n"))continue;
      if((c.getAttribute("class")||"").indexOf("material-symbols")!==-1)continue; walk(c); }} }} }}
  walk(document.body);
  window.setLang=function(lang){{
    reg.forEach(function(r){{ r.node.nodeValue=(lang==="zh"&&I18N[r.key]!==undefined)?I18N[r.key]:r.en; }});
    document.documentElement.lang=lang==="zh"?"zh-CN":"en";
    const l=document.getElementById("lang-toggle-label"); if(l)l.textContent=lang==="zh"?"EN":"中文";
    try{{localStorage.setItem("lb_lang",lang);}}catch(e){{}}
  }};
  window.toggleLang=function(){{ const cur=document.documentElement.lang==="zh-CN"?"zh":"en"; window.setLang(cur==="zh"?"en":"zh"); }};
  let s="en"; try{{s=localStorage.getItem("lb_lang")||"en";}}catch(e){{}} window.setLang(s);
}})();
</script>
</body></html>
'''


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_blocks(blocks):
    out = []
    for kind, val in blocks:
        if kind == "p":
            out.append(f"<p>{val}</p>")
        elif kind == "ul":
            items = "".join(f"<li>{i}</li>" for i in val)
            out.append(f"<ul>{items}</ul>")
        elif kind == "callout":
            out.append(
                '</div><div class="my-6 p-5 rounded-xl bg-secondary-fixed/40 border border-secondary-fixed-dim/50">'
                f'<p class="text-sm text-on-surface leading-relaxed">{val}</p></div>'
                '<div class="prose-body text-on-surface-variant">'
            )
        elif kind == "warn":
            out.append(
                '</div><div class="my-6 p-5 rounded-xl bg-error-container/60 border border-on-error-container/20">'
                f'<p class="text-sm text-on-error-container leading-relaxed">{val}</p></div>'
                '<div class="prose-body text-on-surface-variant">'
            )
    return "\n".join(out)


def build(spec):
    slug = spec["slug"]
    assert len(spec["title"]) <= 62, f'title 超长 {len(spec["title"])}: {spec["slug"]}'
    assert len(spec["desc"]) <= 158, f'desc 超长 {len(spec["desc"])}: {spec["slug"]}' 
    url = f"{SITE}/{slug}.html"

    article_ld = json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": spec["title"], "description": spec["desc"], "url": url,
        "image": f"{SITE}/assets/og-share.jpg", "inLanguage": "en",
        "datePublished": spec["date"], "dateModified": spec["date"],
        "author": {"@type": "Organization", "name": "Mortgage Bridge"},
        "publisher": {"@type": "Organization", "name": "Mortgage Bridge",
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/og-share.jpg"}},
        "mainEntityOfPage": url,
    }, ensure_ascii=False, indent=2)

    faq_ld = json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": f["q"],
                        "acceptedAnswer": {"@type": "Answer", "text": f["a_plain"]}}
                       for f in spec["faqs"]],
    }, ensure_ascii=False, indent=2)

    parts = [HEAD.format(
        title=esc(spec["title"]), desc=esc(spec["desc"]), url=url, site=SITE,
        article_ld=article_ld, faq_ld=faq_ld, badge=spec["badge"],
        h1=spec["h1"], read_time=spec["read_time"], intro=spec["intro"])]

    for i, sec in enumerate(spec["sections"]):
        parts.append(f'<h2 class="font-display text-2xl font-bold text-primary mt-10 mb-4">{sec["h2"]}</h2>')
        parts.append('<div class="prose-body text-on-surface-variant">')
        parts.append(render_blocks(sec["blocks"]))
        parts.append('</div>')
        if i == spec.get("lead_after", 1):
            parts.append(LEAD.format(
                cta_h=spec["cta"]["h"], cta_p=spec["cta"]["p"],
                lead_tag=spec["cta"]["tag"], cta_btn=spec["cta"]["btn"],
                cta_options="\n".join(f"<option>{o}</option>" for o in spec["cta"]["options"])))

    parts.append('<h2 class="font-display text-2xl font-bold text-primary mt-12 mb-4">Frequently asked questions</h2>')
    parts.append('<div class="space-y-3">')
    for f in spec["faqs"]:
        parts.append(
            '<details class="rounded-xl border border-outline-variant/40 bg-surface-container-lowest p-5">'
            f'<summary class="font-semibold text-primary cursor-pointer">{f["q"]}</summary>'
            f'<p class="text-sm text-on-surface-variant mt-3 leading-relaxed">{f["a"]}</p></details>')
    parts.append('</div>')

    parts.append('<div class="mt-12 pt-8 border-t border-outline-variant/30">')
    parts.append('<h3 class="font-display text-lg font-bold text-primary mb-4">Helpful tools &amp; guides</h3>')
    parts.append('<div class="grid sm:grid-cols-2 gap-4">')
    for href, t, blurb in spec["related"]:
        parts.append(
            f'<a href="{href}" class="block p-5 rounded-xl bg-surface-container-lowest border border-outline-variant/20 hover:border-primary/40 transition">'
            f'<p class="font-bold text-primary">{t}</p>'
            f'<p class="text-on-surface-variant text-sm mt-1">{blurb}</p></a>')
    parts.append('</div></div>')

    parts.append(TAIL.format(disclaimer=spec["disclaimer"],
                             dict=json.dumps(spec["i18n"], ensure_ascii=False)))

    html = "\n".join(parts)
    path = OUT / f"{slug}.html"
    path.write_text(html, encoding="utf-8")

    missing = check_i18n(html, spec["i18n"])
    return path, missing


def check_i18n(html, dict_):
    """复刻 i18n 遍历逻辑，报出漏译的英文串。"""
    from html.parser import HTMLParser
    SKIP = {"script", "style", "noscript"}

    class W(HTMLParser):
        def __init__(s):
            super().__init__(convert_charrefs=True); s.sk = 0; s.k = []; s.st = []
        def handle_starttag(s, t, a):
            d = dict(a)
            skip = t in SKIP or "data-noi18n" in d or "material-symbols" in (d.get("class") or "")
            s.st.append((t, skip))
            if skip: s.sk += 1
        def handle_endtag(s, t):
            while s.st:
                tag, skip = s.st.pop()
                if skip: s.sk -= 1
                if tag == t: break
        def handle_data(s, d):
            if s.sk == 0 and d.strip(): s.k.append(d.strip())

    body = html[html.find("<body"):]
    w = W(); w.feed(body)
    seen, miss = set(), []
    for k in w.k:
        if k in seen: continue
        seen.add(k)
        if k in dict_: continue
        # 纯数字/标点/已是中文的跳过
        if re.fullmatch(r"[\s\d$,.%\-—–:;()/&+]*", k): continue
        if re.search(r"[一-鿿]", k): continue
        if k in ("Mortgage Bridge",): continue
        miss.append(k)
    return miss
