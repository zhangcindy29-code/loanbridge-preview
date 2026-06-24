/* =====================================================================
   Analytics & conversion tracking  —  Broker Gateway
   ---------------------------------------------------------------------
   一处填 ID,全站生效。上线追踪只需做这三步:

   1) GA4 (网站流量分析,免费,必做)
      - 打开 https://analytics.google.com → 管理 → 创建"媒体资源"
      - 选"网站",数据流地址填: zhangcindy29-code.github.io
      - 拿到的"衡量 ID"长这样 G-XXXXXXXXXX,粘到下面 GA4_ID

   2) Google Ads 转化 (跑 SEM 时才需要,可先留空)
      - Google Ads → 工具 → 转化 → 新建"网站"转化 → 操作类型选"潜在客户/提交表单"
      - 拿到 转化 ID (AW-XXXXXXXXX) 和 转化标签 (一串字符)
      - 分别粘到 ADS_ID 和 ADS_LEAD_LABEL

   3) Search Console 验证: 见 index.html 里的注释(用"HTML 标记"方式)

   填好后无需改其他文件。未填时脚本自动静默,不会报错。
   线索提交成功会自动触发 generate_lead(GA4) + conversion(Ads) 事件。
   ===================================================================== */
(function () {
  "use strict";

  // ====== 在这里填你的 ID ======
  var GA4_ID         = "G-XXXXXXXXXX";   // GA4 衡量 ID
  var ADS_ID         = "AW-XXXXXXXXX";   // Google Ads 转化 ID(没投广告可先不填)
  var ADS_LEAD_LABEL = "XXXXXXXXXXXX";   // Google Ads 潜在客户转化"标签"
  // =============================

  function notSet(v) { return !v || v.indexOf("XXXX") > -1; }

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { dataLayer.push(arguments); };

  if (!notSet(GA4_ID)) {
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA4_ID;
    document.head.appendChild(s);
    gtag("js", new Date());
    gtag("config", GA4_ID);
    if (!notSet(ADS_ID)) { gtag("config", ADS_ID); }
  }

  // 表单提交成功时由 forms.js 调用,记录一条"线索"转化
  window.trackLead = function (source) {
    if (notSet(GA4_ID)) return;
    gtag("event", "generate_lead", { source: source || "form" });
    if (!notSet(ADS_ID) && !notSet(ADS_LEAD_LABEL)) {
      gtag("event", "conversion", { send_to: ADS_ID + "/" + ADS_LEAD_LABEL });
    }
  };
})();
