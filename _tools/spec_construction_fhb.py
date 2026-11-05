#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""construction loan 1,600/mo KD 0; buying property nsw 1,900/mo KD 4 (rank 62 in Nov 2026 on a 358-word page).
NSW facts checked Nov 2026: nsw.gov.au contracts and deposits, exchanging contracts and settlement, contracts for
residential building work; SIRA home building compensation; Revenue NSW transfer duty."""
from build_article import build
from spec_refi_lowdoc import maker, link, faq


def construction():
    d, T = maker()
    return {
        "slug": "article-construction-finance", "date": "2026-11-05",
        "title": "Construction Loans in Australia Explained | Mortgage Bridge",
        "desc": "How construction loans work in NSW: progress payments, what you pay during the build, what lenders need, and the mistakes that delay a project.",
        "badge": T("Construction · Land", "自建 · 土地"),
        "h1": T("Construction loans: how building finance actually works", "自建贷款：建房融资到底怎么运作"),
        "read_time": T("8 min read", "阅读约 8 分钟"),
        "intro": T("A construction loan does not hand you the money in one lump sum. It is released in stages as the work is done, and you generally pay interest only on what has been drawn so far. Understanding that timing is what keeps a build from running short of money halfway through.",
                   "自建贷款不是一次把钱给你，而是随着工程进度分阶段放款，通常只按已经放出的金额付利息。搞清楚这个节奏，才不会建到一半资金接不上。"),
        "lead_after": 1,
        "sections": [
            {"h2": T("How progress payments work", "分期放款怎么运作"), "blocks": [
                ("p", T("Your building contract sets out a schedule of payments tied to stages of the work. When a stage is finished, the builder sends an invoice, you approve it, and the lender checks the progress before releasing the money. In NSW, contracts over $20,000 must include a progress payment schedule, and payments should reflect the work actually done.",
                        "建筑合同会写明与工程阶段挂钩的付款安排。一个阶段完成后，建筑商开发票，你确认，贷款机构核实进度后放款。在 NSW，超过 $20,000 的合同必须列明进度付款安排，而且付款应与实际完成的工程相符。")),
                ("p", T("Common stages include:", "常见阶段包括：")),
                ("ul", [T("Deposit", "定金"), T("Base or slab", "地基或楼板"), T("Frame", "框架"), T("Lock-up", "封顶门窗（Lock-up）"), T("Fixing", "内部安装（Fixing）"), T("Practical completion", "实际完工（Practical completion）")]),
                ("callout", T("The stages and percentages vary by contract and lender. Check them against each other before you sign, because a lender may not release funds for a stage it does not recognise.",
                              "各阶段和比例因合同和贷款机构而异。签约前要核对两边是否一致，否则贷款机构可能不会为它不认可的阶段放款。")),
            ]},
            {"h2": T("What you pay during the build", "建房期间要付什么"), "blocks": [
                ("p", T("Repayments are often interest only during construction and are calculated on the amount drawn, so they rise after each stage. Once the build finishes, the loan usually moves to principal and interest. Ask your lender how long the interest-only period lasts, and what happens if the build runs late.",
                        "建房期间通常只还利息，并按已放款金额计算，所以每过一个阶段月供都会增加。完工后，贷款一般转为本息同还。要问清楚只还利息的期限多长，工期延误时怎么处理。")),
                ("p", T("If you are renting or paying another mortgage at the same time, budget for both for the whole build, plus some room for delays.",
                        "如果同时在租房或还另一笔房贷，要按整个工期预留两边的开支，并多留一些余地应对延误。")),
                ("p", link("construction-loan-calculator.html", T("Estimate it stage by stage with our construction loan calculator", "用自建贷款计算器按阶段估算"))),
            ]},
            {"h2": T("What lenders usually ask for", "贷款机构通常要什么"), "blocks": [
                ("ul", [T("A signed building contract with a licensed builder. Many lenders prefer a fixed-price contract.", "与持牌建筑商签订的建筑合同。很多贷款机构更偏好固定总价合同。"),
                        T("Council-approved plans and specifications, or a complying development certificate.", "经市政批准的图纸和规格，或 Complying Development Certificate。"),
                        T("A valuation based on the finished home.", "按完工后价值做的估价。"),
                        T("Evidence of home building compensation cover, where it applies.", "相关情况下的房屋建筑赔偿保险（HBC）证明。"),
                        T("The usual proof of income and deposit.", "常规的收入和首付证明。")]),
                ("warn", T("In NSW, residential building work over $20,000 must be insured under the home building compensation scheme. The builder must arrange cover before asking for or accepting any money, so see the certificate before you pay. A deposit above 10% of the contract price may not be recoverable under the cover.",
                           "在 NSW，超过 $20,000 的住宅建筑工程必须投保房屋建筑赔偿保险。建筑商在收取任何款项前就要办好，所以付款前先看证书。超过合同价 10% 的定金，可能无法从保险中追回。")),
            ]},
            {"h2": T("Where building finance goes wrong", "自建贷款常见的问题"), "blocks": [
                ("ul", [T("Variations. Changes after you sign can increase the price beyond what the lender approved, and you may need to fund the difference yourself.", "工程变更。签约后的改动可能让造价超过贷款批准额，差额可能要自己补。"),
                        T("A low valuation. If the finished-home valuation comes in under the build cost, you may need more cash.", "估价偏低。如果完工估价低于造价，可能要多拿现金。"),
                        T("Items outside the contract, such as landscaping, driveways, fences and window coverings.", "合同外项目，例如园林、车道、围栏和窗饰。"),
                        T("Delays. Each extra month can mean more interest and more rent.", "工期延误。每多一个月，都可能多付利息和房租。"),
                        T("Paying invoices too early. Check the stage is really finished before you approve it.", "太早付款。确认阶段真正完成后再批准发票。")]),
            ]},
            {"h2": T("Land first, subdivisions and owner-builders", "先买地、土地分割和自建业主"), "blocks": [
                ("p", T("If you buy land before building, you may settle the land loan first and start the construction stage later. Some lenders treat vacant land differently from a home, so the deposit they ask for can differ.",
                        "如果先买地再建房，可能要先完成土地贷款的交割，之后才开始建筑阶段。部分贷款机构对空地的要求和房屋不同，首付要求也可能不一样。")),
                ("p", T("Subdivisions and small developments are usually assessed differently, and often on the project as well as on you. Owner-builder projects can also be harder to finance. These are the cases where it pays to check lender policy before you commit. If you are self-employed or buying through a company, your income will be assessed under that lender's own rules too.",
                        "土地分割和小型开发的评估方式通常不同，往往既看项目也看你本人。自建业主项目也可能更难融资。这些情况最好在做决定前先确认贷款机构的政策。如果你是自雇或用公司购买，收入也会按该机构自己的规则评估。")),
                ("p", link("article-self-employed-home-loans.html", T("Read our guide to self-employed and low doc loans", "阅读自雇与 Low Doc 贷款指南"))),
            ]},
            {"h2": T("First home buyers who are building", "首次置业者自建"), "blocks": [
                ("p", T("In NSW, the $10,000 First Home Owner Grant can apply to a new build, but the land and building contract together must not exceed $750,000. Other schemes have different limits, so check each one for your situation.",
                        "在 NSW，$10,000 首次置业补助可用于新建房屋，但土地加建筑合同总价不能超过 $750,000。其他计划的上限不同，要逐项按你的情况确认。")),
                ("p", link("first-home-buyer-grants-nsw.html", T("See the NSW first home buyer schemes", "查看 NSW 首次置业计划"))),
            ]},
        ],
        "cta": {"h": T("Planning a build or subdivision?", "正在计划建房或土地分割？"),
                "p": T("Tell us about the project. A broker will call you back within 12 hours to talk through the finance.", "告诉我们项目情况，顾问会在 12 小时内回电，和你讨论融资方案。"),
                "tag": "Construction guide lead", "btn": T("Talk about my project", "聊聊我的项目"),
                "options": [T("Building a new home", "新建住宅"), T("Knockdown rebuild", "推倒重建"), T("Buying land first", "先买地"), T("Subdivision or small development", "土地分割或小型开发"), T("Not sure yet", "还不确定")]},
        "faqs": [
            faq(T, "Do you pay interest on the whole construction loan?", "自建贷款要按全额付利息吗？",
                "Generally no. During the build you usually pay interest only on the amount drawn so far, so repayments rise as each stage is paid. Check how your lender handles this.",
                "一般不用。建房期间通常只按已放款金额付利息，所以月供会随每个阶段增加。具体要向贷款机构确认。"),
            faq(T, "How much deposit do I need for a construction loan?", "自建贷款要多少首付？",
                "It depends on the lender, the loan-to-value ratio and whether you already own the land. A deposit under 20% may mean paying Lenders Mortgage Insurance.",
                "取决于贷款机构、贷款成数，以及你是否已经拥有土地。首付低于 20% 可能要付贷款保险（LMI）。"),
            faq(T, "What happens if the build costs more than the loan?", "造价超过贷款怎么办？",
                "You may need to pay the difference from your own funds or ask the lender to review the loan, which is not guaranteed. That is why variations should be costed before you agree to them.",
                "可能要自己补差额，或者请贷款机构重新审批，但不保证通过。所以工程变更在同意之前就要算好费用。"),
            faq(T, "Can I get a construction loan if I am self-employed?", "自雇可以申请自建贷款吗？",
                "Yes, subject to lender criteria. You will need to show your income, and options can be narrower, so compare lender policy before you sign a building contract.",
                "可以，但要符合贷款机构的条件。你需要证明收入，选择可能较少，所以签建筑合同前要比较各家政策。"),
        ],
        "related": [
            ("construction-loan-calculator.html", T("Construction loan calculator", "自建贷款计算器"), T("Interest and repayments, stage by stage.", "按阶段估算利息和月供。")),
            ("bridging-loan-australia.html", T("Bridging loans explained", "过桥贷款解析"), T("If you need to build or buy before you sell.", "如果需要先建或先买，再卖旧房。")),
            ("article-self-employed-home-loans.html", T("Self-employed and low doc loans", "自雇与 Low Doc 贷款"), T("What lenders ask for when income is harder to prove.", "收入较难证明时，贷款机构会要什么。")),
            ("first-home-buyer-grants-nsw.html", T("NSW first home buyer schemes", "NSW 首次置业计划"), T("Grants, stamp duty and the 5% deposit scheme.", "补助、印花税和 5% 首付计划。")),
        ],
        "disclaimer": T("This article is general information only and does not take into account your objectives, financial situation or needs. It is not legal or building advice. Lender criteria and government rules change, so check them for your situation. All loans are subject to lender approval. Sources: NSW Government, SIRA, accessed November 2026.",
                        "本文仅为一般信息，未考虑你的目标、财务状况或需求，也不构成法律或建筑建议。贷款条件和政府规定会变化，请按你的情况确认。所有贷款均须经贷款机构批准。资料来源：NSW 政府、SIRA，2026 年 11 月查阅。"),
        "i18n": d,
    }


def first_home():
    d, T = maker()
    return {
        "slug": "article-first-home-buyer-nsw", "date": "2026-11-05",
        "title": "Buying Property in NSW: Step-by-Step Guide | Mortgage Bridge",
        "desc": "The steps to buying property in NSW, from pre-approval and exchange to settlement, with the costs, cooling-off rules and first home buyer schemes.",
        "badge": T("Buying in NSW", "在 NSW 买房"),
        "h1": T("Buying property in NSW: the steps, the costs and the rules", "在 NSW 买房：步骤、费用和规则"),
        "read_time": T("9 min read", "阅读约 9 分钟"),
        "intro": T("Buying a home in NSW follows a fairly standard path, but a few moments carry real risk: exchanging contracts before your finance is ready, assuming you have a cooling-off period at auction, and forgetting the costs on top of the deposit. Here is the process in order.",
                   "在 NSW 买房的流程大致固定，但有几个时刻风险很大：贷款没准备好就交换合同、以为拍卖也有冷静期，以及忘了首付之外的费用。下面按顺序说明。"),
        "lead_after": 2,
        "sections": [
            {"h2": T("Step 1: Work out your budget and upfront costs", "第一步：算预算和前期费用"), "blocks": [
                ("p", T("The deposit is only part of the cash you need. Allow for:", "首付只是所需现金的一部分，还要预留：")),
                ("ul", [T("Stamp duty, unless you qualify for an exemption or concession.", "印花税，除非符合免税或减免条件。"),
                        T("Lenders Mortgage Insurance, usually if your deposit is under 20%.", "贷款保险（LMI），通常在首付低于 20% 时需要。"),
                        T("Conveyancing or legal fees.", "过户或律师费。"),
                        T("Building and pest inspections, plus a strata report for apartments.", "房屋和虫害检查；公寓还要看 strata 报告。"),
                        T("Mortgage and title registration fees, and moving costs.", "抵押和产权登记费，以及搬家费用。")]),
                ("p", link("stamp-duty-calculator-nsw.html", T("Calculate your NSW stamp duty", "计算你的 NSW 印花税"))),
                ("p", link("borrowing-power-calculator.html", T("Estimate your borrowing power", "估算你的借款能力"))),
            ]},
            {"h2": T("Step 2: Check the first home buyer schemes", "第二步：查首次置业计划"), "blocks": [
                ("p", T("If this is your first home, three schemes may apply, and they can sometimes be combined. Each has its own rules and limits.", "如果是第一次买房，可能适用三个计划，有时还可以叠加。每个计划都有自己的规则和上限。")),
                ("ul", [T("First Home Buyers Assistance Scheme: no transfer duty on eligible homes up to $800,000, and a concession up to $1,000,000.", "首次置业者援助计划：符合条件的房屋 $800,000 以下免印花税，$1,000,000 以下可减免。"),
                        T("First Home Owner Grant: $10,000 for eligible new homes up to $600,000, or land and building up to $750,000.", "首次置业补助：符合条件的新房 $600,000 以下，或土地加建筑 $750,000 以下，可获 $10,000。"),
                        T("Australian Government 5% Deposit Scheme: buy with as little as 5% deposit and no LMI, within the price caps.", "澳洲政府 5% 首付计划：在房价上限内，最低 5% 首付且免 LMI。")]),
                ("p", link("first-home-buyer-grants-nsw.html", T("See the details and who qualifies", "查看详情和申请条件"))),
            ]},
            {"h2": T("Step 3: Get pre-approval", "第三步：办理贷款预批"), "blocks": [
                ("p", T("Pre-approval shows sellers you are serious and tells you your likely limit, but it is not a promise to lend. The lender still has to assess the specific property, so your finance is not final just because you are pre-approved.",
                        "预批能让卖家看到你的诚意，也让你了解大概额度，但它不是放款承诺。贷款机构还要评估具体的房产，所以有预批不代表贷款已经落实。")),
                ("p", link("home-loan-pre-approval.html", T("What pre-approval does and does not cover", "预批能保证什么，不能保证什么"))),
            ]},
            {"h2": T("Step 4: Find the property and do your checks", "第四步：找房并做好检查"), "blocks": [
                ("ul", [T("Have a conveyancer or solicitor review the contract before you commit.", "决定前，请过户律师审阅合同。"),
                        T("Get building and pest inspections, and read the strata report for an apartment.", "做房屋和虫害检查；公寓要看 strata 报告。"),
                        T("Ask your broker whether the lender has limits on that property type, such as small apartments.", "问顾问贷款机构对该类房产有没有限制，例如小面积公寓。")]),
            ]},
            {"h2": T("Step 5: Exchange contracts and the cooling-off period", "第五步：交换合同和冷静期"), "blocks": [
                ("p", T("The sale becomes binding when contracts are exchanged. You usually pay a deposit, commonly 10% unless a lower amount is agreed.", "交换合同后，买卖就具有约束力。通常要支付定金，一般是 10%，除非协商了更低的金额。")),
                ("p", T("Residential buyers in NSW generally have a cooling-off period until 5pm on the fifth business day after exchange. If you withdraw during that time, you pay the seller 0.25% of the purchase price.", "NSW 住宅买家通常有冷静期，到交换合同后第五个工作日下午 5 点结束。在此期间退出，要向卖家支付房价的 0.25%。")),
                ("warn", T("There is no cooling-off period if you buy at auction, or exchange on auction day after the property is passed in. A 66W certificate from your solicitor or conveyancer also waives it. Make sure your finance and checks are done before you bid or sign.", "拍卖买房没有冷静期；拍卖流拍后当天交换合同也没有。律师开具的 66W 证书也会放弃冷静期。出价或签字前，贷款和检查都要准备好。")),
            ]},
            {"h2": T("Step 6: Finish your loan and settle", "第六步：完成贷款并交割"), "blocks": [
                ("ul", [T("Send the contract to your broker straight away so the lender can value the property and move to formal approval.", "马上把合同交给顾问，让贷款机构估价并进入正式审批。"),
                        T("Sign your loan documents and arrange building insurance if your lender or contract requires it.", "签署贷款文件；如贷款机构或合同要求，安排房屋保险。"),
                        T("Pay transfer duty if it applies. It is generally due within 3 months of signing the contract, or at settlement if earlier.", "如需缴纳印花税，一般在签约后 3 个月内缴纳；如交割更早，则在交割时缴纳。"),
                        T("Do a final inspection shortly before settlement. Your conveyancer and lender then complete the transfer, and you receive the keys.", "交割前不久做最后验房。之后由过户律师和贷款机构完成过户，你就可以拿钥匙了。")]),
                ("callout", T("Settlement timing is set in your contract, so check the date and how long your lender needs before you agree to it.", "交割时间写在合同里。同意之前要确认日期，以及贷款机构需要多长时间。")),
            ]},
            {"h2": T("Buying to invest?", "买房投资？"), "blocks": [
                ("p", T("The steps are similar, but loan structure and tenants come into play, and first home buyer schemes generally do not apply. If you arrange your investment loan through us, new clients can receive up to 12 months of free property management. Conditions apply.", "步骤类似，但还要考虑贷款结构和租客，首次置业计划一般也不适用。如果通过我们办理投资房贷款，新客户最多可免 12 个月物业管理费，须符合相关条件。")),
                ("p", link("property-management.html", T("See how property management works", "了解物业管理服务"))),
            ]},
        ],
        "cta": {"h": T("Want someone to check your numbers?", "想请人帮你算一算？"),
                "p": T("Tell us where you are up to. A broker will call you back within 12 hours.", "告诉我们你进行到哪一步，顾问会在 12 小时内回电。"),
                "tag": "Buying in NSW guide lead", "btn": T("Talk to a broker", "联系顾问"),
                "options": [T("Just starting to research", "刚开始了解"), T("I need pre-approval", "我需要预批"), T("I found a property", "已经看中房子"), T("I am buying an investment property", "我要买投资房")]},
        "faqs": [
            faq(T, "How much deposit do I need to buy in NSW?", "在 NSW 买房要多少首付？",
                "Lenders commonly look for 20% to avoid LMI. Some buyers can purchase with less, including eligible first home buyers using the 5% Deposit Scheme. You also need money for the upfront costs.",
                "贷款机构通常希望有 20%，这样可以免 LMI。部分买家可以用更少首付，包括使用 5% 首付计划的合格首次置业者。此外还要准备前期费用。"),
            faq(T, "Can I back out after exchanging contracts in NSW?", "在 NSW 交换合同后可以退出吗？",
                "Usually during the cooling-off period, by paying 0.25% of the purchase price. There is no cooling-off at auction or where it has been waived. After it ends, withdrawing can have serious consequences, so get legal advice.",
                "通常可以在冷静期内退出，要支付房价的 0.25%。拍卖或已放弃冷静期的情况下没有冷静期。冷静期结束后退出可能后果严重，请咨询律师。"),
            faq(T, "When do I pay stamp duty in NSW?", "在 NSW 什么时候交印花税？",
                "Transfer duty is generally due within 3 months of signing the contract, or earlier if settlement comes first. Some buyers qualify for exemptions, concessions or a deferral on off-the-plan homes.",
                "印花税一般在签约后 3 个月内缴纳；如果交割更早，则要更早缴纳。部分买家可享受免税、减免或楼花延期缴纳。"),
            faq(T, "Do I need a conveyancer or a solicitor?", "我需要过户律师还是普通律师？",
                "Either can handle a standard purchase in NSW. Use someone experienced with your property type, and have them review the contract before you exchange.",
                "在 NSW，一般的买房两者都可以办理。选择熟悉该类房产的人，并在交换合同前请对方审阅合同。"),
        ],
        "related": [
            ("stamp-duty-calculator-nsw.html", T("NSW stamp duty calculator", "NSW 印花税计算器"), T("Includes first home buyer exemptions.", "含首次置业免税和减免。")),
            ("first-home-buyer-grants-nsw.html", T("NSW first home buyer schemes", "NSW 首次置业计划"), T("Grants, stamp duty and the 5% deposit scheme.", "补助、印花税和 5% 首付计划。")),
            ("guarantor-home-loan.html", T("Guarantor home loans", "担保贷款"), T("How a family guarantee works, and the risks.", "家庭担保怎么运作，有什么风险。")),
            ("lmi-calculator.html", T("LMI calculator", "LMI 计算器"), T("Estimate your insurance and the deposit that removes it.", "估算保险费，以及多少首付可以免掉。")),
        ],
        "disclaimer": T("This article is general information only and does not take into account your objectives, financial situation or needs. It is not legal advice. Government schemes and lender criteria change and have eligibility rules. All loans are subject to lender approval. Sources: NSW Government and Revenue NSW, accessed November 2026.",
                        "本文仅为一般信息，未考虑你的目标、财务状况或需求，也不构成法律建议。政府计划和贷款条件会变化，并有申请资格要求。所有贷款均须经贷款机构批准。资料来源：NSW 政府和 Revenue NSW，2026 年 11 月查阅。"),
        "i18n": d,
    }


if __name__ == "__main__":
    for s in (construction(), first_home()):
        p, miss = build(s)
        print(p.name, "untranslated:", miss or "none")
