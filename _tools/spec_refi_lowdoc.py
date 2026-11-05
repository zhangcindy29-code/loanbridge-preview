#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rewrites of the two thin articles with the most search demand (DataForSEO, Nov 2026):
refinance home loan 6,600/mo KD 8 · low doc home loan 880/mo KD 0 · self employed home loan 320/mo KD 0.

Worked refinance figures: $650,000 P&I, monthly repayments.
  6.20% 25y $4,268 (interest $630,335) · 5.70% 25y $4,070 (interest $570,872) · 5.70% 30y $3,773 (interest $708,137)
"""
from build_article import build

BASE = {
    "All Articles": "全部文章", "Stamp duty calc": "印花税计算器", "Talk to a broker": "联系顾问",
    "Frequently asked questions": "常见问题", "Helpful tools & guides": "实用工具与指南",
    "© 2026 Mortgage Bridge Pty Ltd ABN 66 700 684 519. Expert mortgage guidance for Sydney's multicultural communities.":
        "© 2026 Mortgage Bridge Pty Ltd ABN 66 700 684 519。为悉尼多元文化社区提供专业房贷指导。",
}


def maker():
    d = dict(BASE)

    def T(en, zh):
        d[en] = zh
        return en
    return d, T


def link(href, text):
    return f'<a class="font-semibold text-primary underline" href="{href}">{text}</a>'


def faq(T, qen, qzh, aen, azh):
    return {"q": T(qen, qzh), "a": T(aen, azh), "a_plain": aen}


# ============================== REFINANCE ======================================
def refinance():
    d, T = maker()
    spec = {
        "slug": "article-refinancing-guide",
        "title": "Refinance Home Loan: When It's Worth It | Mortgage Bridge",
        "desc": "When refinancing your home loan really saves money: the costs to count, how to work out break-even, and the term reset that can cost you more.",
        "date": "2026-11-05",
        "badge": T("Refinance · Australia", "转贷 · 澳洲"),
        "h1": T("Refinancing your home loan: when it actually saves you money", "转贷：什么情况下才是真的省钱"),
        "read_time": T("8 min read", "阅读约 8 分钟"),
        "intro": T("A lower monthly repayment is not the same as a cheaper loan. Refinancing can save you tens of thousands of dollars, or quietly cost you more, and the difference usually comes down to three numbers: the rate, the switching costs and the years left on the loan.",
                   "月供变低，不等于贷款变便宜。转贷可能帮你省下几万澳元，也可能在不知不觉中让你多付钱，差别通常就在三个数字：利率、转贷费用，以及贷款还剩多少年。"),
        "lead_after": 1,
        "sections": [
            {"h2": T("Four reasons people refinance", "转贷常见的四个原因"), "blocks": [
                ("ul", [T("A lower interest rate. Variable rates on the market can differ by more than two percentage points, so a loan you have not reviewed in a few years may no longer be competitive.",
                          "更低的利率。市场上的浮动利率相差可能超过两个百分点，几年没检查过的贷款，可能已经没有竞争力了。"),
                        T("Better features, such as an offset account or the ability to split the loan.",
                          "更好的功能，例如 offset 账户，或者把贷款拆分。"),
                        T("Access to equity for a renovation or the deposit on an investment property.",
                          "释放房产净值，用来装修或支付投资房首付。"),
                        T("Rolling a fixed-rate period that is ending onto a better deal, rather than drifting onto the lender's revert rate.",
                          "固定利率快到期时换到更好的方案，而不是自动转入银行的回转利率。")]),
                ("p", T("It is also worth asking your current lender for a better rate first. Sometimes one phone call gets you part of the way, without any switching costs.",
                        "也建议先问问现有银行能不能给更低的利率。有时候一个电话就能拿到一部分优惠，还不用付转贷费用。")),
            ]},
            {"h2": T("The costs to count before you switch", "转贷前要算清的费用"), "blocks": [
                ("p", T("Refinancing is not free. Which of these apply depends on your current loan and your new lender, so check each one in writing.",
                        "转贷不是免费的。下面哪些费用适用，取决于你现在的贷款和新的贷款机构，每一项都要以书面确认为准。")),
                ("ul", [T("Discharge fee: charged when you close your current loan.", "解约费（Discharge fee）：关闭现有贷款时收取。"),
                        T("Break fee: you may have to pay this if you are leaving a fixed rate early, and it can be large.", "提前解除费（Break fee）：提前退出固定利率时可能要付，金额可能不小。"),
                        T("Application or settlement fees with the new lender, although some lenders waive them.", "新贷款机构的申请费或交割费，部分机构会减免。"),
                        T("Government registration fees for changing the mortgage on the title.", "更改产权抵押登记的政府费用。"),
                        T("Lenders Mortgage Insurance, if your equity is under 20%. LMI can outweigh the savings on its own.", "贷款保险（LMI）：净值低于 20% 时可能要付，单这一项就可能抵消省下的钱。")]),
                ("warn", T("If you paid LMI on your current loan, it generally does not transfer to the new lender. Ask your current lender whether a partial refund applies, and include any new LMI in your sums.",
                           "如果现有贷款付过 LMI，一般不能转到新银行。可以问问现有银行有没有部分退款，并把新的 LMI 计入成本。")),
            ]},
            {"h2": T("How to work out your break-even", "怎么算回本时间"), "blocks": [
                ("p", T("Divide your total switching costs by your monthly saving. That tells you how many months it takes to get your money back. If you may sell or refinance again before that point, the switch may not be worth it.",
                        "用转贷总费用除以每月省下的钱，就能算出几个月回本。如果在回本之前你可能卖房或再次转贷，这次转贷可能就不划算。")),
                ("callout", T("Illustration only: on a $650,000 loan with 25 years left, moving from 6.20% to 5.70% drops the monthly repayment from about $4,268 to about $4,070, a saving of about $198 a month. With $1,500 in switching costs, you would break even in about 8 months. These rates are examples, not offers.",
                              "仅作示例：贷款 $650,000、还剩 25 年，利率从 6.20% 降到 5.70%，月供从约 $4,268 降到约 $4,070，每月省约 $198。如果转贷费用是 $1,500，大约 8 个月回本。这些利率只是示例，并非报价。")),
                ("p", link("refinance-calculator.html", T("Run your own numbers in our free refinance calculator", "用我们的免费转贷计算器算一算你的情况"))),
            ]},
            {"h2": T("The trap: resetting your loan term", "最大的坑：还款期被重置"), "blocks": [
                ("p", T("This is the mistake that makes refinancing look better than it is. Take the same loan and new rate, but stretch the remaining 25 years onto a fresh 30-year term. The repayment falls to about $3,773, so the monthly \"saving\" appears to jump to about $495.",
                        "这个错误会让转贷看起来比实际更划算。同样的贷款和新利率，如果把剩下的 25 年拉长成新的 30 年，月供会降到约 $3,773，每月“省下”的钱看起来变成约 $495。")),
                ("ul", [T("Stay on 6.20% for 25 years: about $630,000 in total interest.", "保持 6.20%、25 年：总利息约 $630,000。"),
                        T("Move to 5.70% and keep 25 years: about $571,000, roughly $59,000 less.", "转到 5.70%、仍为 25 年：约 $571,000，少付约 $59,000。"),
                        T("Move to 5.70% but reset to 30 years: about $708,000, roughly $78,000 more than not switching at all.", "转到 5.70%、但重置为 30 年：约 $708,000，比完全不转贷还多付约 $78,000。")]),
                ("p", T("A lower rate with a longer term can leave you paying more overall. When you compare offers, keep the term close to the years you have left, or keep paying your old repayment amount if your new loan allows extra repayments.",
                        "利率低了，期限却长了，总共反而可能付得更多。比较方案时，尽量让期限接近现有贷款的剩余年数；如果新贷款允许额外还款，也可以继续按原来的月供还。")),
            ]},
            {"h2": T("When refinancing may not be worth it", "什么情况下可能不值得转"), "blocks": [
                ("ul", [T("You are still in a fixed period and the break fee wipes out the saving.", "还在固定利率期内，提前解除费把省下的钱都吃掉了。"),
                        T("Your equity is under 20% and you would pay LMI again.", "净值低于 20%，要重新付 LMI。"),
                        T("Your income has dropped or changed recently. A new application means being assessed again, and you may not qualify on the same terms.", "收入最近下降或有变化。转贷要重新审核，不一定能拿到同样的条件。"),
                        T("You plan to sell before you would break even.", "打算在回本之前卖房。")]),
                ("p", T("Self-employed or running your income through a company or trust? You can still refinance, but the new lender will assess your income its own way, so it pays to check that before you apply.",
                        "如果你是自雇，或者收入经公司、信托走账，一样可以转贷，但新贷款机构会用自己的方法评估收入，申请前先确认清楚会更稳妥。")),
                ("p", link("article-self-employed-home-loans.html", T("Read our guide to self-employed and low doc home loans", "阅读我们的自雇与 Low Doc 贷款指南"))),
            ]},
            {"h2": T("Refinancing an investment property", "投资房转贷"), "blocks": [
                ("p", T("If you are refinancing to release equity for your next purchase, how the loan is set up matters as much as the rate. Our team can look at the loan with you, and if you buy an investment property through us, new clients can receive up to 12 months of free property management. Conditions apply.",
                        "如果转贷是为了释放净值买下一套房，贷款结构和利率一样重要。我们的团队可以和你一起看贷款方案；如果通过我们买投资房，新客户最多可免 12 个月物业管理费，须符合相关条件。")),
                ("p", link("property-management.html", T("See how property management works", "了解物业管理服务"))),
            ]},
        ],
        "cta": {"h": T("Find out if switching is worth it for you", "看看转贷对你是否划算"),
                "p": T("Tell us about your loan. A broker will call you back within 12 hours to go through the numbers with you.", "告诉我们你的贷款情况，顾问会在 12 小时内回电，和你一起算清楚。"),
                "tag": "Refinance guide lead", "btn": T("Request a free refinance review", "申请免费转贷评估"),
                "options": [T("I want a lower rate", "我想要更低的利率"), T("My fixed rate is ending", "固定利率快到期"),
                            T("I want to release equity", "我想释放房产净值"), T("Not sure yet", "还不确定")]},
        "faqs": [
            faq(T, "How often should I review my home loan?", "多久应该检查一次房贷？",
                "A common habit is to review your rate from time to time, and always when a fixed period is ending or your circumstances change. Reviewing does not commit you to switching.",
                "建议定期检查利率，固定利率快到期或个人情况有变化时更要看一次。检查不代表一定要转贷。"),
            faq(T, "Does refinancing affect my credit score?", "转贷会影响信用分吗？",
                "A new application normally appears on your credit file. One considered application is different from several in a short period, so it is sensible to narrow your options before you apply.",
                "新的申请通常会记录在信用档案里。一次深思熟虑的申请，和短时间内多次申请不一样，所以最好先缩小选择范围再申请。"),
            faq(T, "How long does refinancing take?", "转贷要多长时间？",
                "It varies by lender and by how complex your finances are, so allow several weeks. Your broker can give you a better idea once your lender and documents are known.",
                "因贷款机构和个人财务复杂程度而异，建议预留几周时间。确定贷款机构和文件后，顾问可以给你更具体的估计。"),
            faq(T, "Can I refinance if I am self-employed?", "自雇可以转贷吗？",
                "Yes, subject to the new lender's criteria. You will need to show your income again, usually with tax returns or, for some low doc products, alternative evidence such as BAS and bank statements.",
                "可以，但要符合新贷款机构的条件。你需要重新证明收入，通常是提供报税单；部分 Low Doc 产品可接受 BAS 和银行流水等其他材料。"),
        ],
        "related": [
            ("refinance-calculator.html", T("Refinance calculator", "转贷计算器"), T("Monthly saving, total interest and break-even.", "每月省多少、总利息和回本时间。")),
            ("article-self-employed-home-loans.html", T("Self-employed and low doc loans", "自雇与 Low Doc 贷款"), T("What lenders ask for when income is harder to prove.", "收入较难证明时，贷款机构会要什么。")),
            ("borrowing-power-calculator.html", T("Borrowing power calculator", "借款能力计算器"), T("Estimate how much you may be able to borrow.", "估算你可能借到多少。")),
            ("property-management.html", T("Property management", "物业管理"), T("Up to 12 months free for eligible new clients.", "符合条件的新客户最多免 12 个月。")),
        ],
        "disclaimer": T("This article is general information only and does not take into account your objectives, financial situation or needs. Interest rates shown are examples only and are not offers. Fees, lender criteria and policies change and vary between lenders. All loans are subject to lender approval. Sources: Moneysmart (ASIC), switching home loans, accessed November 2026.",
                        "本文仅为一般信息，未考虑你的目标、财务状况或需求。文中利率仅为示例，并非报价。费用、贷款条件和政策会变化，且因贷款机构而异。所有贷款均须经贷款机构批准。资料来源：ASIC Moneysmart“转换房贷”页面，2026 年 11 月查阅。"),
        "i18n": d,
    }
    return spec


# ============================== SELF-EMPLOYED / LOW DOC =========================
def low_doc():
    d, T = maker()
    spec = {
        "slug": "article-self-employed-home-loans",
        "title": "Self-Employed & Low Doc Home Loans Explained | Mortgage Bridge",
        "desc": "How lenders assess self-employed income, what full doc and low doc loans ask for, the real trade-offs, and how to prepare before you apply.",
        "date": "2026-11-05",
        "badge": T("Self-employed · Low doc", "自雇 · Low Doc"),
        "h1": T("Self-employed and low doc home loans: what lenders really look at", "自雇与 Low Doc 房贷：贷款机构真正看什么"),
        "read_time": T("9 min read", "阅读约 9 分钟"),
        "intro": T("Being self-employed does not stop you getting a home loan, but it does change how your income is judged. The same business can look strong to one lender and risky to another, so knowing which loan type fits your paperwork often matters more than the rate you see advertised.",
                   "自雇不代表贷不到款，但收入的评估方式不一样。同一门生意，这家贷款机构觉得很稳，另一家可能觉得有风险。所以搞清楚哪种贷款适合你手上的材料，往往比广告上的利率更重要。"),
        "lead_after": 1,
        "sections": [
            {"h2": T("Why self-employed applications feel harder", "为什么自雇申请感觉更难"), "blocks": [
                ("p", T("An employee can show a payslip. A business owner's income can move from year to year, and much of it may sit in a company or trust. Lenders still have to be satisfied that you can repay, so they look for evidence that your income is real and stable.",
                        "员工可以拿出工资单；生意人的收入可能每年都有波动，很多还放在公司或信托里。贷款机构依然要确认你还得起，所以会找证据判断收入是否真实、稳定。")),
                ("p", T("The most common surprise is that sensible tax planning reduces the income a lender can see. Lower taxable income can mean a lower borrowing figure, even when the business is doing well.",
                        "最常见的意外是：合理节税之后，贷款机构能看到的收入也变少了。即使生意不错，应税收入低，也可能意味着能借的钱变少。")),
            ]},
            {"h2": T("Full doc: the usual starting point", "Full Doc：通常的第一选择"), "blocks": [
                ("p", T("If your tax is up to date, a full doc loan is usually the place to start, because it tends to offer the widest choice of lenders. Requirements vary, but lenders commonly ask for:",
                        "如果报税都是最新的，通常先看 Full Doc 贷款，因为可选的贷款机构一般最多。各家要求不同，常见的材料包括：")),
                ("ul", [T("Personal and business tax returns, often for the last two years.", "个人和公司报税单，通常是最近两年。"),
                        T("ATO Notices of Assessment.", "ATO 的 Notice of Assessment。"),
                        T("Company or trust financial statements, where relevant.", "公司或信托的财务报表（如适用）。"),
                        T("Business Activity Statements and recent bank statements.", "BAS 和近期银行流水。")]),
                ("callout", T("Some lenders may accept one year of financials or add back certain expenses, such as depreciation. These policies differ widely, which is why two lenders can give you very different borrowing figures from the same paperwork.",
                              "部分贷款机构可能接受一年的财务报表，或者把折旧等部分开支加回收入。这些政策差异很大，所以同一份材料，两家给出的可贷金额可能相差很多。")),
            ]},
            {"h2": T("Low doc: when your tax returns are not ready", "Low Doc：报税单还没准备好时"), "blocks": [
                ("p", T("A low doc loan lets you show income with alternative evidence when your latest tax returns are not available. It does not mean no checks: the lender must still be satisfied that you can afford the loan.",
                        "Low Doc 贷款让你在最新报税单还没有时，用其他材料证明收入。这不代表不用审核：贷款机构仍然必须确认你还得起。")),
                ("p", T("Depending on the lender, alternative evidence can include:", "根据贷款机构不同，其他材料可以包括：")),
                ("ul", [T("Business Activity Statements, commonly covering 6 to 12 months.", "BAS，通常涵盖 6 到 12 个月。"),
                        T("Business bank statements.", "公司银行流水。"),
                        T("A letter or declaration from your accountant, where the lender accepts one.", "会计师信或声明（如贷款机构接受）。"),
                        T("Your own signed income declaration.", "你本人签署的收入声明。")]),
                ("p", T("Many lenders look for an ABN that has been active for about 12 to 24 months, and some specialist lenders will consider less. Criteria change, so treat these as a guide and not a rule.",
                        "很多贷款机构要求 ABN 已经有效约 12 到 24 个月，部分专门机构可接受更短。条件会变化，这些数字只能作为参考，不是定论。")),
                ("warn", T("Only declare income you can genuinely support. Overstating income on a loan application is serious, and it can leave you with repayments you cannot afford. Be wary of anyone who suggests inflating the figures.",
                           "只申报你真实能支持的收入。在贷款申请中夸大收入是严重的问题，也可能让你背上还不起的月供。如果有人建议你把数字做高，一定要警惕。")),
            ]},
            {"h2": T("The trade-offs of low doc", "Low Doc 的代价"), "blocks": [
                ("ul", [T("Rates and fees are often higher than a comparable full doc loan.", "利率和费用通常高于条件相近的 Full Doc 贷款。"),
                        T("You may need a bigger deposit. Maximum loan-to-value ratios are commonly around 80%, and can be lower for investment loans.", "可能要更多首付。最高贷款成数常见在 80% 左右，投资贷款可能更低。"),
                        T("Fewer lenders offer it, and many of them are non-bank lenders.", "提供的机构较少，很多是非银行贷款机构。"),
                        T("It can be a stepping stone. Once your tax returns are lodged, you may be able to refinance to a full doc loan.", "它可以是过渡方案。报税完成后，你也许可以转回 Full Doc 贷款。")]),
                ("p", link("article-refinancing-guide.html", T("Read how to work out whether refinancing is worth it", "看看怎么判断转贷是否划算"))),
            ]},
            {"h2": T("How to prepare before you apply", "申请前怎么准备"), "blocks": [
                ("ul", [T("Talk to your accountant and your broker before lodging your next return, especially if you plan to buy within a year or two.", "在下一次报税前，先和会计师、贷款顾问谈一谈，尤其是打算一两年内买房的话。"),
                        T("Bring your tax and BAS lodgements up to date. Outstanding ATO debt needs to be explained.", "把报税和 BAS 都补齐。如果有未结清的 ATO 欠款，需要说明清楚。"),
                        T("Keep business and personal spending in separate accounts.", "公司和个人开支分开账户。"),
                        T("Pay down credit cards and reduce limits you do not need. Limits count against you even when the balance is zero.", "还清信用卡，降低用不到的额度。即使余额为零，额度也会影响评估。"),
                        T("Avoid several credit applications close together.", "避免短时间内多次申请信贷。")]),
                ("p", link("borrowing-power-calculator.html", T("Estimate your borrowing power", "估算你的借款能力"))),
            ]},
            {"h2": T("Example: two loans from the same paperwork", "示例：同一份材料，两种走法"), "blocks": [
                ("p", T("Imagine a tradesperson who has held an ABN for three years, with strong BAS but tax returns that are a year behind. On the current paperwork, full doc lenders may only see older, lower income. They could choose a low doc loan now and accept the trade-offs, or lodge their returns first and apply for full doc later. Neither is right for everyone: it depends on timing, deposit and the cost difference. This is a general example, not a real client.",
                        "假设一位做工程的自雇人士，ABN 已有三年，BAS 很好，但报税晚了一年。按现有材料，Full Doc 贷款机构可能只能看到较早、较低的收入。这时可以现在选 Low Doc 并接受它的代价，也可以先报完税，之后再申请 Full Doc。两种走法都不是人人适用，要看时间、首付和成本差异。这只是一般示例，并非真实客户。")),
            ]},
        ],
        "cta": {"h": T("Not sure which path fits your paperwork?", "不确定哪种方式适合你的材料？"),
                "p": T("Tell us your situation. A broker will call you back within 12 hours to go through it with you.", "告诉我们你的情况，顾问会在 12 小时内回电，和你一起看一看。"),
                "tag": "Self-employed guide lead", "btn": T("Request a free assessment", "申请免费评估"),
                "options": [T("Sole trader or contractor", "个体户或合同工"), T("Company or trust owner", "公司或信托持有人"),
                            T("My tax returns are behind", "报税还没做完"), T("A bank has declined me", "被银行拒过"), T("Not sure yet", "还不确定")]},
        "faqs": [
            faq(T, "Can I get a home loan with less than two years of self-employment?", "自雇不满两年可以贷款吗？",
                "Possibly. Some lenders consider a shorter history, particularly if you have worked in the same industry before, although options are narrower and the terms may be less favourable.",
                "有可能。部分贷款机构可以接受较短的记录，特别是你之前在同一行业工作过，不过选择较少，条件也可能没那么好。"),
            faq(T, "What is the difference between low doc and no doc?", "Low Doc 和 No Doc 有什么区别？",
                "Low doc means you provide alternative evidence of income. Lenders still need to be satisfied that you can repay, so you should not expect to get a home loan with no evidence at all.",
                "Low Doc 是用其他材料证明收入。贷款机构仍然要确认你还得起，所以不要指望完全不提供证明就能拿到房贷。"),
            faq(T, "Will a low doc loan always cost more?", "Low Doc 贷款一定更贵吗？",
                "It often does, through a higher rate or fees, but it depends on the lender and your position. Compare the total cost, and consider whether you could refinance once your tax returns are lodged.",
                "通常会更贵，体现在利率或费用上，但具体取决于贷款机构和你的情况。要比较总成本，也可以考虑报税后是否能转贷。"),
            faq(T, "Should I reduce my tax deductions before applying?", "申请前要减少税务抵扣吗？",
                "That is a question for your accountant. Tax planning and borrowing can pull in opposite directions, so it is worth having your accountant and broker look at it together before you lodge.",
                "这个问题要问你的会计师。节税和贷款有时方向相反，建议报税前让会计师和贷款顾问一起看看。"),
        ],
        "related": [
            ("borrowing-power-calculator.html", T("Borrowing power calculator", "借款能力计算器"), T("Estimate how much you may be able to borrow.", "估算你可能借到多少。")),
            ("article-construction-finance.html", T("Construction and land finance", "自建与土地贷款"), T("How progress payments and subdivision finance work.", "分期放款和分割贷款怎么运作。")),
            ("article-refinancing-guide.html", T("Refinancing guide", "转贷指南"), T("When switching really saves money.", "什么情况下转贷才真正省钱。")),
            ("article-self-employed-home-loans-zh.html", T("Chinese guide for self-employed borrowers", "自雇房贷中文指南"), T("The same topic, written in Chinese.", "同一主题的中文版本。")),
        ],
        "disclaimer": T("This article is general information only and does not take into account your objectives, financial situation or needs. It is not tax advice. Lender criteria, documentation requirements and loan-to-value limits vary between lenders and change over time. All loans are subject to lender approval.",
                        "本文仅为一般信息，未考虑你的目标、财务状况或需求，也不构成税务建议。贷款条件、文件要求和贷款成数上限因贷款机构而异，并会随时间变化。所有贷款均须经贷款机构批准。"),
        "i18n": d,
    }
    return spec


if __name__ == "__main__":
    for s in (refinance(), low_doc()):
        p, miss = build(s)
        print(p.name, "untranslated:", miss or "none")
