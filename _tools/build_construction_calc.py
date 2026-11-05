#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""construction-loan-calculator.html. construction loan calculator 590/mo KD 3 (DataForSEO, Nov 2026);
the top 10 has no dedicated construction tool. Head, nav, footer and language script come from
refinance-calculator.html so the page stays in step with the other calculators."""
import json, re
from pathlib import Path
from build_article import check_i18n

ROOT = Path(__file__).resolve().parent.parent
SRC = (ROOT / "refinance-calculator.html").read_text(encoding="utf-8")
URL = "https://mortgagebrg.com.au/construction-loan-calculator.html"
TITLE = "Construction Loan Calculator Australia | Mortgage Bridge"
DESC = "Estimate construction loan repayments stage by stage: interest during the build, the highest monthly payment and your repayment after completion."
assert len(TITLE) <= 62 and len(DESC) <= 158

D = {"Talk to a broker": "联系顾问", "LMI calc": "LMI 计算器"}
def T(en, zh):
    D[en] = zh
    return en

FAQS = [
    ("How is interest calculated on a construction loan?", "自建贷款的利息怎么算？",
     "Usually on the amount drawn so far, not the full approved loan. Each progress payment increases the balance, so the monthly interest rises through the build. Lenders can differ, so check your loan terms.",
     "通常按已放款金额计算，而不是整笔批准额度。每次分期放款都会增加余额，所以每月利息在建房期间逐步上升。各贷款机构可能不同，请查看你的贷款条款。"),
    ("Do I use my own money first?", "要先用自己的钱吗？",
     "Often, yes. Many lenders expect your own contribution to be spent before they release loan funds. This calculator applies your savings to the earliest stages first.",
     "通常是的。很多贷款机构要求先用完你的自有资金，才开始放款。这个计算器会先把自有资金用于最早的阶段。"),
    ("Are the stage percentages fixed?", "各阶段的比例是固定的吗？",
     "No. The figures here are an example. Your building contract sets the real schedule, so enter your own percentages.",
     "不是。这里的数字只是示例，实际安排以你的建筑合同为准，可以输入你自己的比例。"),
    ("What does this calculator leave out?", "这个计算器没有计入什么？",
     "It does not include lender fees, Lenders Mortgage Insurance, variations, valuation or inspection fees, or items outside the building contract. Allow extra for these and for delays.",
     "它没有计入贷款费用、贷款保险（LMI）、工程变更、估价或查验费用，以及建筑合同以外的项目。这些费用和工期延误都要额外预留。"),
]
def field(id_, en, zh, val, prefix="$", suffix="", hint=None):
    left = f'<span data-noi18n="true" class="absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant font-semibold">{prefix}</span>' if prefix else ""
    right = f'<span data-noi18n="true" class="absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant font-semibold">{suffix}</span>' if suffix else ""
    cls = "calc-input" + (" !pl-7" if prefix else " !pl-3") + (" !pr-8" if suffix else "")
    h = f'<p class="text-xs text-on-surface-variant mt-1">{hint}</p>' if hint else ""
    return (f'<div><label class="block text-sm font-semibold text-on-surface-variant mb-1.5" for="{id_}">{T(en, zh)}</label>'
            f'<div class="relative">{left}<input data-noi18n="true" class="{cls}" id="{id_}" inputmode="decimal" type="text" value="{val}"/>{right}</div>{h}</div>')

STAGES = [("Deposit", "定金", 5), ("Base or slab", "地基或楼板", 15), ("Frame", "框架", 20), ("Lock-up", "封顶门窗", 25), ("Fixing", "内部安装", 25), ("Completion", "实际完工", 10)]
stage_inputs = "".join(
    f'<div class="flex items-center gap-3"><label class="flex-1 text-sm text-on-surface-variant" for="s{i}">{T(en, zh)}</label>'
    f'<div class="relative w-24"><input data-noi18n="true" class="calc-input !pl-3 !pr-7 !py-1.5 text-right" id="s{i}" inputmode="decimal" type="text" value="{p}"/>'
    f'<span data-noi18n="true" class="absolute right-2.5 top-1/2 -translate-y-1/2 text-on-surface-variant text-sm font-semibold">%</span></div></div>'
    for i, (en, zh, p) in enumerate(STAGES))

BODY = f'''<h1 class="font-display text-3xl md:text-4xl font-bold text-primary leading-tight">{T("Construction Loan Calculator", "自建贷款计算器")}</h1>
<p class="text-on-surface-variant mt-3 text-lg leading-relaxed">{T("A construction loan is released in stages, so your repayment changes as you build. See the interest stage by stage, the most you may pay each month during the build, and your repayment once it finishes.", "自建贷款是分阶段放款的，所以月供会随着工程变化。这里可以看到每个阶段的利息、建房期间每月最高可能付多少，以及完工后的月供。")}</p>

<section class="mt-8 rounded-2xl border border-outline-variant/40 bg-surface-container-lowest shadow-sm overflow-hidden">
<div class="p-6 md:p-8 grid md:grid-cols-2 gap-6 md:gap-8">
<div class="space-y-4">
<h2 class="font-display font-bold text-primary">{T("Your project", "你的项目")}</h2>
{field("land", "Loan already owing on the land", "土地已有贷款", "400,000", hint=T("Enter 0 if you own the land outright.", "如果土地没有贷款，请填 0。"))}
{field("build", "Building contract price", "建筑合同价", "500,000")}
{field("own", "Your own money for the build", "用于建房的自有资金", "50,000", hint=T("Applied to the earliest stages first.", "先用于最早的阶段。"))}
<div class="grid grid-cols-2 gap-3">
{field("rate", "Interest rate (example)", "利率（示例）", "6.50", prefix="", suffix="%")}
{field("months", "Build length (months)", "工期（月）", "12", prefix="")}
</div>
<div class="grid grid-cols-2 gap-3">
{field("term", "Loan term (years)", "贷款期限（年）", "30", prefix="")}
{field("rent", "Weekly rent while building", "建房期间每周房租", "0")}
</div>
</div>
<div>
<h2 class="font-display font-bold text-primary mb-1">{T("Progress payment stages", "分期付款阶段")}</h2>
<p class="text-xs text-on-surface-variant mb-3">{T("Example only. Enter the percentages from your building contract.", "仅为示例，请填写你建筑合同里的比例。")}</p>
<div class="space-y-2">{stage_inputs}</div>
<p id="pctMsg" class="text-sm font-semibold mt-3" data-noi18n="true"></p>
</div>
</div>
<div class="bg-surface-container-low border-t border-outline-variant/30 p-6 md:p-8" data-noi18n="true">
<div id="summary" class="grid sm:grid-cols-3 gap-5"></div>
<div class="overflow-x-auto mt-6"><table class="w-full text-sm min-w-[520px]"><thead id="thead"></thead><tbody id="tbody"></tbody></table></div>
<p id="note" class="text-xs text-on-surface-variant mt-3 leading-relaxed"></p>
</div>
</section>

<section id="get-review" class="my-12 p-6 md:p-8 rounded-2xl bg-primary text-on-primary scroll-mt-24">
<h2 class="font-display text-xl md:text-2xl font-bold mb-2">{T("Check this against your actual project", "按你的实际项目核对一下")}</h2>
<p class="text-on-primary/80 mb-6 text-sm md:text-base">{T("A broker will call you back within 12 hours to go through your contract, stages and lender options.", "顾问会在 12 小时内回电，和你一起看合同、分期安排和贷款方案。")}</p>
<form data-lead-form="Construction calculator lead" data-success-en="✓ Thanks! A specialist will call you within 12 hours." data-success-zh="✓ 已收到！顾问会在12小时内联系你。" class="grid sm:grid-cols-2 gap-4">
<input required id="lead-name" name="Name" aria-label="Your name" placeholder="Your name / 称呼" class="w-full px-4 py-3 rounded-xl bg-on-primary text-on-surface placeholder-on-surface-variant/60 focus:outline-none focus:ring-2 focus:ring-secondary-fixed"/>
<input required id="lead-contact" name="Contact" aria-label="Phone or WeChat" placeholder="Phone or WeChat / 电话或微信" class="w-full px-4 py-3 rounded-xl bg-on-primary text-on-surface placeholder-on-surface-variant/60 focus:outline-none focus:ring-2 focus:ring-secondary-fixed"/>
<select id="lead-type" name="Situation" aria-label="Your project" class="w-full px-4 py-3 rounded-xl bg-on-primary text-on-surface sm:col-span-2">
<option>{T("Building a new home", "新建住宅")}</option><option>{T("Knockdown rebuild", "推倒重建")}</option><option>{T("Buying land first", "先买地")}</option><option>{T("Subdivision or small development", "土地分割或小型开发")}</option><option>{T("Not sure yet", "还不确定")}</option>
</select>
<button class="sm:col-span-2 px-8 py-3.5 rounded-xl bg-secondary-container text-on-surface font-bold shadow-lg hover:shadow-xl transition" type="submit">{T("Talk about my project", "聊聊我的项目")}</button>
</form>
</section>

<h2 class="font-display text-2xl font-bold text-primary mt-12 mb-4">{T("Construction loan questions", "自建贷款常见问题")}</h2>
<div class="space-y-3">{"".join(f'<details class="rounded-xl border border-outline-variant/40 bg-surface-container-lowest p-5"><summary class="font-semibold text-primary cursor-pointer">{T(q, qz)}</summary><p class="text-sm text-on-surface-variant mt-3 leading-relaxed">{T(a, az)}</p></details>' for q, qz, a, az in FAQS)}</div>

<div class="mt-10 rounded-2xl border border-outline-variant/40 p-6 bg-surface-container-low">
<h3 class="font-display text-xl font-bold text-primary mb-2">{T("How construction loans work", "自建贷款怎么运作")}</h3>
<p class="text-on-surface-variant text-sm mb-4 leading-relaxed">{T("Progress payments, what lenders ask for, NSW insurance rules and the mistakes that delay a build.", "分期放款、贷款机构的要求、NSW 保险规定，以及会拖慢工程的常见错误。")}</p>
<a class="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-primary text-on-primary font-bold hover:opacity-90 transition text-sm" href="article-construction-finance.html">{T("Read the guide", "阅读指南")}</a>
</div>

<p class="text-on-surface-variant/85 text-xs mt-8 leading-relaxed">{T("This calculator provides general information only and produces an estimate, not a quote. It does not take into account your objectives, financial situation or needs. The interest rate and stages are examples, and actual timing, drawdowns, fees and repayments depend on your contract and lender. All loans are subject to lender approval.", "本计算器仅提供一般信息和估算，并非报价，也未考虑你的目标、财务状况或需求。利率和阶段仅为示例，实际时间、放款、费用和月供取决于你的合同和贷款机构。所有贷款均须经贷款机构批准。")}</p>
'''

CALC = r'''<script src="construction-calc.js"></script>
'''

# ---- assemble from the refinance calculator so head/nav/footer stay consistent -----------
head_end = SRC.index('<main class="max-w-4xl')
foot_start = SRC.index('</main>')
head = SRC[:head_end]
tail = SRC[foot_start:]
old_title = re.search(r"<title>(.*?)</title>", head).group(1)
old_desc = re.search(r'name="description" content="([^"]*)"', head).group(1)
head = head.replace(old_title, TITLE).replace(old_desc, DESC).replace("https://mortgagebrg.com.au/refinance-calculator.html", URL)
ld = re.findall(r'<script type="application/ld\+json">.*?</script>', head, re.S)
assert len(ld) == 2, len(ld)
web = {"@context": "https://schema.org", "@type": "WebApplication", "name": "Construction Loan Calculator", "url": URL,
       "applicationCategory": "FinanceApplication", "operatingSystem": "All", "browserRequirements": "Requires JavaScript",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "AUD"},
       "provider": {"@type": "FinancialService", "name": "Mortgage Bridge", "url": "https://mortgagebrg.com.au/"}}
faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, _, a, _ in FAQS]}
head = head.replace(ld[0], '<script type="application/ld+json">\n' + json.dumps(web, indent=2) + "\n</script>")
head = head.replace(ld[1], '<script type="application/ld+json">\n' + json.dumps(faq, ensure_ascii=False, indent=2) + "\n</script>")
FOOT = "© 2026 Mortgage Bridge Pty Ltd ABN 66 700 684 519. Expert mortgage guidance for Sydney's multicultural communities."
D[FOOT] = "© 2026 Mortgage Bridge Pty Ltd ABN 66 700 684 519。为悉尼多元文化社区提供专业房贷指导。"
tail = re.sub(r"const I18N = \{.*?\};", lambda m: "const I18N = " + json.dumps(D, ensure_ascii=False) + ";", tail, count=1, flags=re.S)
tail = tail.replace('<script src="forms.js"></script>', '<script src="forms.js"></script>\n' + CALC.strip())
html = head + '<main class="max-w-4xl mx-auto px-5 md:px-10 py-10 md:py-14">\n' + BODY + "\n" + tail
(ROOT / "construction-loan-calculator.html").write_text(html, encoding="utf-8")
print("untranslated:", check_i18n(html, D) or "none")
