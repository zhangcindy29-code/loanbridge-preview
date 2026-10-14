#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Join the Team + Partner With Us pages.

Every visible English string goes through T(en, zh), which registers its
translation, so the i18n dictionary can't drift from the copy. check_i18n()
from build_article reports anything left untranslated.

Run:  python3 _tools/build_pages.py
"""
import json
from pathlib import Path
from build_article import check_i18n, esc

OUT = Path(__file__).resolve().parent.parent
SITE = "https://mortgagebrg.com.au"
EMAIL = "service@mortgagebrg.com.au"
# Flip to True once the client approves join-the-team.html for publishing
JOIN_LIVE = True

I18N = {}


def T(en, zh):
    I18N[en] = zh
    return en


HEAD = '''<!DOCTYPE html>

<html class="scroll-smooth" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<!-- seo:start -->
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{url}"/>
<meta property="og:site_name" content="Mortgage Bridge"/>
<meta property="og:type" content="website"/>
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
{ld}
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
.dot-list li{{position:relative;padding-left:1.5rem;margin-bottom:0.55rem;line-height:1.65;}}
.dot-list li::before{{content:'';position:absolute;left:0;top:0.6rem;width:7px;height:7px;border-radius:9999px;background:#735c00;}}
</style>
</head>
<body class="bg-background text-on-surface">
<header class="sticky top-0 z-50 glass-header border-b border-outline-variant/30">
<nav class="flex justify-between items-center w-full px-5 md:px-10 max-w-5xl mx-auto h-16 md:h-20">
<a class="font-display text-base sm:text-xl md:text-2xl font-bold text-primary whitespace-nowrap" href="index.html">Mortgage Bridge</a>
<div class="flex items-center gap-3 md:gap-5">
<a class="hidden md:inline-flex items-center gap-1 text-on-surface-variant hover:text-primary text-sm font-semibold" href="index.html">
<span class="material-symbols-outlined text-base" aria-hidden="true">arrow_back</span>{home}</a>
<button data-noi18n="true" id="lang-toggle" onclick="toggleLang()" class="flex items-center gap-1.5 whitespace-nowrap px-3 md:px-4 py-2 rounded-full border border-primary text-primary font-bold hover:bg-primary/5 transition-colors text-sm">
<span class="material-symbols-outlined text-sm" aria-hidden="true">translate</span><span id="lang-toggle-label">中文</span></button>
<a href="{cta_href}" class="inline-flex whitespace-nowrap px-4 md:px-6 py-2 md:py-2.5 rounded-full bg-primary text-on-primary font-bold hover:opacity-90 transition text-sm">{cta}</a>
</div>
</nav>
</header>
<main class="max-w-5xl mx-auto px-5 md:px-10 py-10 md:py-16">
'''

TAIL = '''
<p class="text-on-surface-variant/80 text-xs mt-14 leading-relaxed">{disclaimer}</p>
</main>
<footer class="bg-primary text-on-primary py-10">
<div class="max-w-5xl mx-auto px-5 md:px-10 flex flex-col md:flex-row justify-between items-center gap-4">
<div class="font-display text-xl font-bold">Mortgage Bridge</div>
<div class="flex flex-wrap gap-x-6 gap-y-2 text-sm text-on-primary/80 justify-center">
<a class="hover:text-secondary-fixed" href="index.html">{f_home}</a>
{f_join}<a class="hover:text-secondary-fixed" href="partner-with-us.html">{f_partner}</a>
</div>
<p class="text-on-primary/60 text-sm text-center">{copy}</p>
</div>
</footer>
<script src="forms.js"></script>
<script>
(function(){{
  const I18N = {dict};
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


def icon(name, cls="text-secondary"):
    return f'<span class="material-symbols-outlined {cls}" aria-hidden="true">{name}</span>'


def hero(badge, h1, intro):
    return (f'<span class="inline-block px-3 py-1 rounded-full bg-secondary-container text-on-secondary-container text-xs font-bold mb-4">{badge}</span>'
            f'<h1 class="font-display text-3xl md:text-5xl font-bold text-primary leading-tight mb-5 max-w-3xl">{h1}</h1>'
            f'<p class="text-on-surface-variant text-lg leading-relaxed max-w-3xl">{intro}</p>')


def h2(text, id_=None):
    a = f' id="{id_}"' if id_ else ""
    return f'<h2{a} class="font-display text-2xl md:text-3xl font-bold text-primary mt-16 mb-6 scroll-mt-24">{text}</h2>'


def cards(items, cols="md:grid-cols-2"):
    out = [f'<div class="grid {cols} gap-5">']
    for ic, title, body in items:
        out.append('<div class="p-6 rounded-2xl bg-surface-container-lowest border border-outline-variant/30">'
                   f'<div class="flex items-center gap-3 mb-2">{icon(ic)}<h3 class="font-display text-lg font-bold text-primary">{title}</h3></div>'
                   f'<p class="text-on-surface-variant leading-relaxed">{body}</p></div>')
    out.append('</div>')
    return "".join(out)


def ul(items):
    return '<ul class="dot-list text-on-surface-variant">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def page(slug, title, desc, ld, body, cta, cta_href, disclaimer):
    assert len(title) <= 62, f"title too long ({len(title)}): {title}"
    assert len(desc) <= 158, f"desc too long ({len(desc)}): {desc}"
    url = f"{SITE}/{slug}.html"
    html = (HEAD.format(title=esc(title), desc=esc(desc), url=url, site=SITE,
                        ld=json.dumps(ld, ensure_ascii=False, indent=2),
                        home=T("Home", "首页"), cta=cta, cta_href=cta_href)
            + body
            + TAIL.format(disclaimer=disclaimer, f_home=T("Home", "首页"),
                          f_join=(f'<a class="hover:text-secondary-fixed" href="join-the-team.html">{T("Join the Team", "加入我们")}</a>' if JOIN_LIVE else ""),
                          f_partner=T("Partner With Us", "合作伙伴"),
                          copy=T("© 2026 Mortgage Bridge. St Leonards, Sydney NSW.", "© 2026 Mortgage Bridge。悉尼 St Leonards。"),
                          dict=json.dumps(I18N, ensure_ascii=False)))
    (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
    miss = check_i18n(html, I18N)
    print(f"{slug}.html  untranslated: {miss or 'none'}")


def webpage_ld(name, url, desc):
    return {"@context": "https://schema.org", "@type": "WebPage", "name": name, "url": url,
            "description": desc, "inLanguage": "en",
            "publisher": {"@type": "Organization", "name": "Mortgage Bridge", "url": SITE,
                          "address": {"@type": "PostalAddress", "streetAddress": "Suite 101/11 Chandos Street",
                                      "addressLocality": "St Leonards", "addressRegion": "NSW",
                                      "postalCode": "2065", "addressCountry": "AU"}}}


# ============================== JOIN THE TEAM =================================
def role(id_, title, zh_title, summary, do, bring, regarded):
    meta = [("schedule", T("Full-time", "全职")),
            ("location_on", T("St Leonards, Sydney NSW", "悉尼 St Leonards")),
            ("payments", T("Salary discussed at interview", "薪资面谈"))]
    chips = "".join(f'<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-surface-container text-on-surface-variant text-sm">'
                    f'{icon(i, "text-base text-primary")}{t}</span>' for i, t in meta)
    return (f'<article id="{id_}" class="scroll-mt-24 p-6 md:p-9 rounded-2xl bg-surface-container-lowest border border-outline-variant/30 mb-6">'
            f'<h3 class="font-display text-2xl font-bold text-primary mb-3">{T(title, zh_title)}</h3>'
            f'<div class="flex flex-wrap gap-2 mb-5">{chips}</div>'
            f'<p class="text-on-surface-variant leading-relaxed mb-6">{summary}</p>'
            '<div class="grid md:grid-cols-2 gap-x-10 gap-y-6">'
            f'<div><h4 class="font-bold text-primary mb-3">{T("What you will do", "工作内容")}</h4>{ul(do)}</div>'
            f'<div><h4 class="font-bold text-primary mb-3">{T("What you will bring", "任职要求")}</h4>{ul(bring)}'
            f'<h4 class="font-bold text-primary mt-6 mb-3">{T("Highly regarded", "加分项")}</h4>{ul(regarded)}</div>'
            '</div>'
            f'<a href="#apply" class="inline-flex items-center gap-2 mt-7 px-6 py-3 rounded-xl bg-primary text-on-primary font-bold hover:opacity-90 transition">'
            f'{T("How to apply", "如何申请")}{icon("arrow_downward", "text-base")}</a>'
            '</article>')


def join_the_team():
    body = [hero(
        T("Careers", "招聘"),
        T("Join the Mortgage Bridge team", "加入 Mortgage Bridge 团队"),
        T("We are a Sydney mortgage and property team based in St Leonards. We help home buyers, investors and business owners with home loans, refinancing and investment property, from finance to settlement through our legal partners, to property management. We serve clients in English, Mandarin, Cantonese and Vietnamese, and we are known for taking on the files others find complicated.",
          "我们是一支位于悉尼 St Leonards 的房贷与物业团队，为买房人、投资者和生意人提供房贷、转贷和投资房服务：从贷款、通过合作律师办理过户，到后续的物业管理。我们用英语、普通话、粤语和越南语服务客户，也以擅长处理别人觉得复杂的个案而著称。"))]

    body.append(h2(T("Why work with us", "为什么加入我们")))
    body.append(cards([
        ("work", T("Work that needs real skill", "真正需要专业能力的工作"),
         T("Self-employed borrowers, company and trust structures, construction and bridging finance. You will build expertise on files that genuinely need it.",
           "自雇客户、公司和信托结构、自建与过桥贷款。你会在真正需要专业判断的个案上积累经验。")),
        ("hub", T("One team, the whole journey", "一个团队，全程服务"),
         T("Lending, settlement through our legal partners and property management sit under one roof, so clients are not passed between strangers.",
           "贷款、通过合作律师办理的过户、物业管理都在同一个团队里完成，客户不必在陌生人之间来回转。")),
        ("translate", T("Serve clients in their language", "用客户的母语服务"),
         T("Many of our clients are most comfortable in Mandarin, Cantonese or Vietnamese. Your language skills are a real strength here.",
           "我们很多客户用普通话、粤语或越南语沟通最自在。在这里，你的语言能力是实实在在的优势。")),
        ("location_on", T("Based in St Leonards", "办公地点在 St Leonards"),
         T("Our office is at Suite 101/11 Chandos Street, St Leonards, close to St Leonards station on the North Shore.",
           "办公室位于 Suite 101/11 Chandos Street, St Leonards，靠近北岸的 St Leonards 火车站。")),
    ]))

    body.append(h2(T("Open roles", "在招职位"), "roles"))
    body.append(role(
        "mortgage-broker", "Mortgage Broker", "贷款经纪人 Mortgage Broker",
        T("You will advise clients on residential and investment lending, with a focus on scenarios that need real structuring skill. You will be supported by a dedicated loan processor, so you can spend your time with clients and lenders.",
          "你将为客户提供自住房和投资房贷款建议，重点处理需要专业结构设计的个案。公司配有专职贷款助理支持你，让你把时间花在客户和银行身上。"),
        [T("Meet clients, understand their goals and financial position, and recommend loan options and structures that are in their best interests, in line with the best interests duty under the National Consumer Credit Protection Act 2009 (Cth).",
           "与客户面谈，了解其目标和财务状况，按照《2009 年全国消费信贷保护法》（联邦）规定的最佳利益义务，推荐符合客户最佳利益的贷款方案与结构。"),
         T("Handle complex scenarios, including self-employed and low-doc borrowers, company and trust structures, construction and land or subdivision finance, guarantor loans and bridging finance.",
           "处理复杂个案，包括自雇和低文件（Low Doc）借款人、公司与信托结构、自建及土地或分割贷款、担保人贷款和过桥贷款。"),
         T("Help existing borrowers review and refinance their loans, including multi-property portfolios.",
           "协助现有借款人检视贷款并办理转贷，包括多套房产的贷款组合。"),
         T("Compare products across our lender panel, prepare and lodge applications, and manage them through to approval and settlement with lenders, BDMs and conveyancers.",
           "对比合作贷款机构的产品，准备并递交申请，与银行、BDM 和过户律师协作，跟进至审批和交割。"),
         T("Complete all required compliance documentation accurately and on time.",
           "准确、按时完成所有合规文件。"),
         T("Work with our property management team so investor clients have one team from finance to lease.",
           "与物业管理团队配合，让投资房客户从贷款到出租都由同一个团队服务。"),
         T("Build and maintain referral relationships with accountants, real estate agents and other professionals.",
           "建立并维护与会计师、地产中介及其他专业人士的转介绍关系。")],
        [T("Certificate IV in Finance and Mortgage Broking (FNS40821 or an earlier equivalent version).",
           "持有 Certificate IV in Finance and Mortgage Broking（FNS40821 或此前的同等版本）。"),
         T("Mortgage broking or lending experience. There is no minimum number of years.",
           "有贷款经纪或银行贷款相关经验，不限年限。"),
         T("Fluent English and at least one of Mandarin, Cantonese or Vietnamese.",
           "英语流利，并能使用普通话、粤语或越南语中的至少一种。"),
         T("Full working rights in Australia.", "拥有澳大利亚全职工作权利。")],
        [T("Diploma of Finance and Mortgage Broking Management (FNS50322).",
           "持有 Diploma of Finance and Mortgage Broking Management（FNS50322）。"),
         T("Experience with self-employed, company, trust or construction lending.",
           "有自雇、公司、信托或自建贷款的经验。"),
         T("An existing client base or referral network in Sydney.",
           "在悉尼已有客户群或转介绍渠道。")]))

    body.append(role(
        "loan-processor", "Loan Processor", "贷款助理 Loan Processor",
        T("You keep every loan file moving. You will work alongside our brokers from the first enquiry to settlement, making sure applications are complete, accurate and on time, and that clients always know where their loan is up to.",
          "你是让每一笔贷款顺利推进的人。你将与贷款经纪人并肩工作，从客户第一次咨询到交割，确保申请完整、准确、按时，并让客户随时知道贷款进展到哪一步。"),
        [T("Make first contact with new enquiries and help us keep our promise to call clients back within 12 hours.",
           "第一时间联系新咨询的客户，帮助我们兑现 12 小时内回电的承诺。"),
         T("Collect, check and organise client documents, including ID, payslips, tax returns, BAS and company financials, and follow up on anything missing.",
           "收集、核对和整理客户文件，包括身份证件、工资单、报税单、BAS 和公司财务报表，并跟进缺失的材料。"),
         T("Enter applications into our CRM and lodgement platforms and prepare servicing calculations for broker review.",
           "将申请录入 CRM 和递交平台，并准备还款能力测算供经纪人审核。"),
         T("Track applications through assessment, valuation, conditions, loan documents and settlement, and keep clients and brokers updated at each step.",
           "跟进申请的审核、估价、批贷条件、贷款文件和交割各个环节，并在每一步及时告知客户和经纪人。"),
         T("Liaise with lenders, conveyancers and our property management team.",
           "与银行、过户律师和物业管理团队沟通协调。"),
         T("Keep every client file complete and ready for compliance review.",
           "确保每份客户档案完整，随时可供合规审查。")],
        [T("Strong attention to detail and the ability to manage many files at once.",
           "做事细致，能同时处理多份档案。"),
         T("Clear written and spoken English.", "英语书面和口头表达清晰。"),
         T("Confidence with spreadsheets and online systems.", "熟练使用电子表格和各类线上系统。"),
         T("Full working rights in Australia.", "拥有澳大利亚全职工作权利。")],
        [T("Mandarin, Cantonese or Vietnamese.", "会普通话、粤语或越南语。"),
         T("Experience in mortgage processing, credit or banking operations. There is no minimum number of years.",
           "有贷款处理、信贷或银行运营相关经验，不限年限。"),
         T("Certificate IV in Finance and Mortgage Broking.", "持有 Certificate IV in Finance and Mortgage Broking。"),
         T("Experience with broker CRM or lodgement platforms, for example ApplyOnline.",
           "使用过贷款经纪 CRM 或递交平台，例如 ApplyOnline。")]))

    body.append(h2(T("How to apply", "如何申请"), "apply"))
    body.append('<div class="p-6 md:p-9 rounded-2xl bg-primary text-on-primary">'
                f'<p class="text-lg leading-relaxed mb-5">{T("Email your resume and a short cover note to the address below. Please put the role title in the subject line.", "请把简历和一段简短的求职说明发送到以下邮箱，并在邮件标题中注明申请的职位。")}</p>'
                f'<a data-noi18n="true" href="mailto:{EMAIL}?subject=Application%20-%20" class="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-secondary-container text-on-surface font-bold text-lg select-all">'
                f'<span class="material-symbols-outlined" aria-hidden="true">mail</span>{EMAIL}</a>'
                f'<p class="text-on-primary/75 text-sm mt-5">{T("All applications are treated confidentially. We review every application and will contact shortlisted candidates.", "所有申请都会严格保密。我们会认真阅读每一份申请，并联系进入下一轮的候选人。")}</p>'
                '</div>')

    title = "Careers at Mortgage Bridge | Mortgage Broker Jobs Sydney"
    desc = "Join Mortgage Bridge in St Leonards, Sydney. We are hiring a full-time Mortgage Broker and Loan Processor to help clients across Sydney."
    page("join-the-team", title, desc, webpage_ld(title, f"{SITE}/join-the-team.html", desc), "".join(body),
         T("View open roles", "查看职位"), "#roles",
         T("Mortgage Bridge is an equal opportunity employer. Applicants must have the right to work in Australia.",
           "Mortgage Bridge 是平等机会雇主。申请人须拥有在澳大利亚工作的权利。"))


# ============================== PARTNER WITH US ===============================
def partner_with_us():
    body = [hero(
        T("Partners", "合作伙伴"),
        T("Partner with Mortgage Bridge", "与 Mortgage Bridge 合作"),
        T("We work with accountants, real estate agents, buyer's agents and solicitors across Sydney. When your client needs a home loan, a refinance or a property manager, we look after them, and they remain your client.",
          "我们与悉尼各地的会计师、地产中介、买家中介和律师合作。当你的客户需要房贷、转贷或物业管理时，由我们来照顾好他们，而客户始终是你的客户。"))]

    body.append(h2(T("Who we work with", "我们与谁合作")))
    body.append(cards([
        ("calculate", T("Accountants and tax agents", "会计师与税务师"),
         T("Self-employed, company and trust clients whose lending needs careful structuring and a lender who understands their financials.",
           "自雇、公司和信托客户，他们的贷款需要精心设计结构，也需要真正看得懂其财务报表的贷款机构。")),
        ("real_estate_agent", T("Real estate and buyer's agents", "地产中介与买家中介"),
         T("Buyers who need finance in place quickly, and investors who need a property manager once they settle.",
           "需要尽快落实贷款的买家，以及交割后需要物业管理的投资者。")),
        ("gavel", T("Solicitors and conveyancers", "律师与过户律师"),
         T("Clients who need their finance arranged in time for settlement, or who are refinancing.",
           "需要在交割前落实贷款，或正在办理转贷的客户。")),
        ("construction", T("Builders and developers", "建筑商与开发商"),
         T("Clients who need construction, land or subdivision finance to move ahead with a project.",
           "需要自建、土地或分割贷款来推进项目的客户。")),
    ]))

    body.append(h2(T("Why partners refer to us", "合作伙伴为什么把客户交给我们")))
    body.append(cards([
        ("handshake", T("Your client stays your client", "客户始终是你的客户"),
         T("We only handle lending and property management. We do not do tax, sales or legal work, so there is no overlap with what you do.",
           "我们只做贷款和物业管理，不涉及报税、卖房或法律业务，和你的业务没有任何重叠。")),
        ("psychology", T("Complex files are our strength", "复杂个案是我们的强项"),
         T("Self-employed and low-doc borrowers, company and trust structures, construction and bridging finance.",
           "自雇和低文件借款人、公司和信托结构、自建与过桥贷款。")),
        ("translate", T("In your client's language", "用客户的母语沟通"),
         T("We serve clients in English, Mandarin, Cantonese and Vietnamese.",
           "我们用英语、普通话、粤语和越南语服务客户。")),
        ("schedule", T("Contact within 12 hours", "12 小时内联系客户"),
         T("We reach out to every client you introduce within 12 hours, so they are not left waiting.",
           "你介绍的每一位客户，我们都会在 12 小时内主动联系，不让客户久等。")),
        ("notifications", T("You are kept in the loop", "进度透明"),
         T("With your client's consent, we let you know at key milestones such as approval and settlement.",
           "在客户同意的前提下，我们会在审批、交割等关键节点告知你进展。")),
        ("groups", T("Client events together", "联合举办客户活动"),
         T("We are happy to co-host seminars and community events for your clients on buying, refinancing and investing.",
           "我们乐意与你联合举办讲座和社区活动，主题涵盖买房、转贷和投资。")),
    ], cols="md:grid-cols-3"))

    body.append(h2(T("How it works", "合作流程")))
    steps = [
        (T("Introduce your client", "介绍客户"),
         T("With their permission, send us their details using the form below or by email.", "在客户同意后，通过下方表格或邮件把客户信息发给我们。")),
        (T("We contact them within 12 hours", "我们在 12 小时内联系"),
         T("A broker who speaks their language gets in touch and works through their situation.", "由会说客户语言的经纪人联系客户，了解并梳理其情况。")),
        (T("We keep you updated", "随时同步进展"),
         T("With your client's consent, we update you at key milestones until settlement.", "在客户同意的前提下，我们会在各个关键节点向你同步进展，直到交割。")),
    ]
    body.append('<ol class="grid md:grid-cols-3 gap-5">' + "".join(
        f'<li class="p-6 rounded-2xl bg-surface-container-low border-t-4 border-secondary-fixed-dim">'
        f'<div data-noi18n="true" class="font-display text-3xl font-bold text-secondary mb-2">{i}</div>'
        f'<h3 class="font-display text-lg font-bold text-primary mb-2">{t}</h3>'
        f'<p class="text-on-surface-variant leading-relaxed">{b}</p></li>'
        for i, (t, b) in enumerate(steps, 1)) + '</ol>')

    body.append(h2(T("Become a partner", "成为合作伙伴"), "partner-form"))
    opts = [T("Accountant or tax agent", "会计师或税务师"), T("Real estate agent", "地产中介"),
            T("Buyer's agent", "买家中介"), T("Solicitor or conveyancer", "律师或过户律师"),
            T("Financial planner", "财务规划师"), T("Builder or developer", "建筑商或开发商"), T("Other", "其他")]
    field = "w-full px-4 py-3 rounded-xl bg-on-primary text-on-surface placeholder-on-surface-variant/60 focus:outline-none focus:ring-2 focus:ring-secondary-fixed"
    body.append(
        '<section class="p-6 md:p-9 rounded-2xl bg-primary text-on-primary">'
        f'<p class="text-on-primary/85 mb-6">{T("Tell us a little about you and we will be in touch to talk about working together.", "简单介绍一下你自己，我们会主动联系你，商谈合作。")}</p>'
        '<form data-lead-form="New partner enquiry" data-success-en="✓ Thanks! We will be in touch shortly." data-success-zh="✓ 已收到！我们会尽快与你联系。" class="grid sm:grid-cols-2 gap-4">'
        f'<input required id="p-name" name="Name" aria-label="Your name" placeholder="Your name / 姓名" class="{field}"/>'
        f'<input required id="p-company" name="Company" aria-label="Company" placeholder="Company / 公司" class="{field}"/>'
        f'<select required id="p-type" name="Profession" aria-label="Profession" class="{field} sm:col-span-2">'
        f'<option value="">{T("What do you do?", "你的职业")}</option>' + "".join(f"<option>{o}</option>" for o in opts) + '</select>'
        f'<input required id="p-email" type="email" name="Email" aria-label="Email" placeholder="Email / 邮箱" class="{field}"/>'
        f'<input required id="p-phone" name="Phone" aria-label="Phone" placeholder="Phone / 电话" class="{field}"/>'
        f'<textarea id="p-msg" name="Message" rows="3" aria-label="Message" placeholder="How would you like to work together? (optional) / 想怎样合作？（选填）" class="{field} sm:col-span-2"></textarea>'
        f'<button type="submit" class="sm:col-span-2 px-8 py-3.5 rounded-xl bg-secondary-container text-on-surface font-bold shadow-lg hover:shadow-xl transition">{T("Send partner enquiry", "提交合作申请")}</button>'
        '</form>'
        f'<p class="text-on-primary/75 text-sm mt-5">{T("Prefer email? Write to us at", "也可以发邮件给我们：")} <span data-noi18n="true" class="font-semibold select-all">{EMAIL}</span></p>'
        '</section>')

    title = "Partner With Us | Referral Partners | Mortgage Bridge"
    desc = "Accountants, real estate agents and solicitors in Sydney: refer clients for home loans, refinancing and property management. Your client stays yours."
    page("partner-with-us", title, desc, webpage_ld(title, f"{SITE}/partner-with-us.html", desc), "".join(body),
         T("Get started", "开始合作"), "#partner-form",
         T("Clients are introduced to us only with their consent. General information only; not credit advice.",
           "客户须在本人同意后才会被介绍给我们。本页内容仅为一般信息，不构成信贷建议。"))


if __name__ == "__main__":
    join_the_team()
    I18N.clear()
    partner_with_us()
