#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mortgage broker vs bank: 480/mo, KD 0, CPC $34 (DataForSEO, Nov 2026). SERP is small brokers and
comparison sites, not the banks. Duty and commission facts: Moneysmart, using a mortgage broker."""
from build_article import build
from spec_refi_lowdoc import maker, link, faq


def spec():
    d, T = maker()
    return {
        "slug": "mortgage-broker-vs-bank",
        "title": "Mortgage Broker vs Bank: Which Is Better? | Mortgage Bridge",
        "desc": "Mortgage broker or bank? An honest comparison of how each one works, how brokers get paid, when going direct makes sense, and what to ask.",
        "date": "2026-11-05",
        "badge": T("Broker or bank", "经纪人还是银行"),
        "h1": T("Mortgage broker vs bank: which is right for you?", "贷款经纪人还是银行：哪个更适合你？"),
        "read_time": T("7 min read", "阅读约 7 分钟"),
        "intro": T("Neither is better for everyone. A bank can only offer its own loans. A broker can compare several lenders, but is usually paid by the lender you end up with. The right choice depends on how simple your situation is and how much comparing you want to do yourself.",
                   "没有哪一个对所有人都更好。银行只能提供自家的贷款；经纪人可以比较多家贷款机构，但佣金通常由你最终选择的贷款机构支付。怎么选，要看你的情况有多简单，以及你愿意自己花多少精力比较。"),
        "lead_after": 2,
        "sections": [
            {"h2": T("The key differences", "主要区别"), "blocks": [
                ("ul", [T("Choice: a bank offers its own products, while a broker can compare the lenders on its panel. A panel is not the whole market, so ask which lenders it includes.",
                          "选择范围：银行只提供自家产品；经纪人可以比较其合作名单上的贷款机构。名单不等于整个市场，要问清楚包括哪些机构。"),
                        T("Duty: mortgage brokers must act in your best interests when suggesting a loan. Lenders must meet responsible lending obligations, which is a different test.",
                          "义务：贷款经纪人在推荐贷款时必须以你的最佳利益行事。贷款机构要遵守负责任放贷义务，这是不同的标准。"),
                        T("Payment: bank staff are paid by the bank. Brokers are usually paid commission by the lender, so you typically do not pay them directly.",
                          "收费：银行员工由银行支付薪酬。经纪人通常从贷款机构获得佣金，所以你一般不用直接付费。"),
                        T("Paperwork: with a bank, you deal with one lender's process. With a broker, one person can run the comparison and manage the application, including when you change lender.",
                          "手续：找银行，你面对的是一家机构的流程；找经纪人，由同一个人负责比较和跟进申请，换贷款机构时也一样。")]),
            ]},
            {"h2": T("How brokers get paid, and why you should ask", "经纪人怎么赚钱，为什么要问清楚"), "blocks": [
                ("p", T("Commission is usually a percentage of the loan, with an upfront part and an ongoing part. Brokers must tell you about the commissions they may receive. If a broker charges you a fee, it should be set out in a written quote that you sign before any service starts.",
                        "佣金通常是贷款金额的一定比例，分为前期佣金和持续佣金。经纪人必须告诉你可能收到的佣金。如果经纪人向你收费，应该在服务开始前，以书面报价写明并由你签字。")),
                ("p", T("This does create a possible conflict. Commission can be larger on bigger loans and can differ between lenders. The best interests duty exists to manage that, but it is still fair to ask a broker why they recommend a particular loan over the alternatives.",
                        "这确实可能带来利益冲突。贷款越大，佣金往往越多，不同机构的佣金也可能不同。最佳利益义务正是为此而设，但你仍然可以问经纪人：为什么推荐这笔贷款，而不是其他方案？")),
            ]},
            {"h2": T("When going direct to a bank can make sense", "什么时候直接找银行更合适"), "blocks": [
                ("ul", [T("Your situation is simple, and you already know which loan you want.", "情况简单，而且已经知道自己想要哪款贷款。"),
                        T("You have a strong relationship with your bank, and it has offered you a rate you are happy with.", "和银行关系很好，对方给的利率你也满意。"),
                        T("You prefer dealing with a branch, or the loan you want is only sold directly.", "你更喜欢到分行办理，或者想要的贷款只能直接申请。")]),
                ("p", T("Even then, it can be worth checking one or two other quotes. Moneysmart's comparison tools and our calculators can help you test the numbers yourself.",
                        "即使这样，也值得多看一两家报价。Moneysmart 的比较工具和我们的计算器，都可以帮你自己验证一下数字。")),
            ]},
            {"h2": T("When a broker tends to help most", "什么时候经纪人最能帮上忙"), "blocks": [
                ("ul", [T("You are self-employed, or your income runs through a company or trust.", "你是自雇，或者收入经公司、信托走账。"),
                        T("A bank has already said no, or your borrowing figure came back lower than expected.", "银行已经拒绝过，或者可贷金额比预期低。"),
                        T("You are building, subdividing or buying before you sell.", "你在自建、做土地分割，或者想先买后卖。"),
                        T("You are building a property portfolio and need the loans structured with the next purchase in mind.", "你在建立房产组合，需要为下一次购买提前规划贷款结构。"),
                        T("You would rather work in Mandarin, Cantonese or Vietnamese.", "你更习惯用普通话、粤语或越南语沟通。")]),
                ("p", T("Lenders can assess the same income in very different ways, which is where comparing policies matters more than comparing advertised rates.",
                        "不同贷款机构对同样的收入，评估结果可能相差很大。这时比较政策，比比较广告利率更重要。")),
                ("p", link("article-self-employed-home-loans.html", T("Read our guide to self-employed and low doc loans", "阅读自雇与 Low Doc 贷款指南"))),
            ]},
            {"h2": T("Five questions to ask any broker, including us", "问任何经纪人都该问的五个问题（也包括我们）"), "blocks": [
                ("ul", [T("Which lenders are on your panel, and which do you use most often?", "你的合作名单上有哪些贷款机构？最常用的是哪几家？"),
                        T("How much commission would you receive on this loan, and on the alternatives?", "这笔贷款和其他方案，你分别能拿到多少佣金？"),
                        T("Why are you recommending this loan over the others you compared?", "为什么推荐这笔贷款，而不是你比较过的其他方案？"),
                        T("Do you charge me any fees? Can I see your credit guide?", "你会向我收费吗？能给我看你的 credit guide 吗？"),
                        T("Have you worked on situations like mine before?", "你处理过和我类似的情况吗？")]),
                ("callout", T("A good broker will answer all five without hesitation. If the answers are vague, it is reasonable to keep looking.",
                              "好的经纪人会毫不犹豫地回答这五个问题。如果答得含糊，继续找别家也很合理。")),
            ]},
        ],
        "cta": {"h": T("Want a second opinion on your loan?", "想听听第二意见？"),
                "p": T("Tell us what you are trying to do. A broker will call you back within 12 hours, with no obligation to proceed.", "告诉我们你的计划，顾问会在 12 小时内回电，没有任何继续办理的义务。"),
                "tag": "Broker vs bank lead", "btn": T("Talk to a broker", "联系顾问"),
                "options": [T("I am buying a home", "我要买自住房"), T("I am buying an investment property", "我要买投资房"),
                            T("I want to refinance", "我想转贷"), T("A bank has declined me", "被银行拒过"), T("Not sure yet", "还不确定")]},
        "faqs": [
            faq(T, "Is a mortgage broker free?", "贷款经纪人是免费的吗？",
                "Often, because lenders usually pay brokers a commission. Some brokers do charge fees, which should be set out in a written quote that you sign before any services start.",
                "通常是，因为佣金一般由贷款机构支付。也有经纪人收费，费用应在服务开始前写入书面报价，并由你签字确认。"),
            faq(T, "Can a broker get a better rate than the bank?", "经纪人能拿到比银行更低的利率吗？",
                "Sometimes, but it is not guaranteed. A broker can compare lenders and may be able to request pricing, while going direct gives you one lender's offer. Compare the rate, fees and features together.",
                "有时可以，但不保证。经纪人可以比较多家，也可能帮你申请价格；直接找银行，你只能看到一家的报价。要把利率、费用和功能放在一起比较。"),
            faq(T, "Does using a broker hurt my credit score?", "找经纪人会影响信用分吗？",
                "Talking to a broker does not by itself affect your file. A formal application normally appears on it, whether it is lodged by you or a broker.",
                "和经纪人聊本身不会影响信用档案。正式申请通常会留下记录，无论是你自己还是经纪人递交。"),
            faq(T, "Can I use a broker and still choose my own bank?", "用经纪人，还能选自己的银行吗？",
                "Yes, if your bank is on the broker's panel and suits your situation. The final decision is always yours, and every loan is subject to lender approval.",
                "可以，只要你的银行在经纪人的合作名单上，且适合你的情况。最终决定权始终在你，所有贷款都须经贷款机构批准。"),
        ],
        "related": [
            ("article-self-employed-home-loans.html", T("Self-employed and low doc loans", "自雇与 Low Doc 贷款"), T("What lenders ask for when income is harder to prove.", "收入较难证明时，贷款机构会要什么。")),
            ("article-refinancing-guide.html", T("Refinancing guide", "转贷指南"), T("When switching really saves money.", "什么情况下转贷才真正省钱。")),
            ("borrowing-power-calculator.html", T("Borrowing power calculator", "借款能力计算器"), T("Estimate how much you may be able to borrow.", "估算你可能借到多少。")),
            ("home-loan-pre-approval.html", T("Home loan pre-approval", "贷款预批"), T("What pre-approval does and does not guarantee.", "预批能保证什么，不能保证什么。")),
        ],
        "disclaimer": T("This article is general information only and does not take into account your objectives, financial situation or needs. All loans are subject to lender approval. Sources: Moneysmart (ASIC), using a mortgage broker, accessed November 2026.",
                        "本文仅为一般信息，未考虑你的目标、财务状况或需求。所有贷款均须经贷款机构批准。资料来源：ASIC Moneysmart“使用贷款经纪人”页面，2026 年 11 月查阅。"),
        "i18n": d,
    }


if __name__ == "__main__":
    p, miss = build(spec())
    print(p.name, "untranslated:", miss or "none")
