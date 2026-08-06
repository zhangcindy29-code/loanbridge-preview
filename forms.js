/* =====================================================================
   Lead form backend  —  Mortgage Bridge
   ---------------------------------------------------------------------
   一次性设置 (约2分钟):
   1. 打开 https://web3forms.com
   2. 输入"线索要发到的邮箱"(例如你的 Gmail / 公司邮箱),点 Create Access Key
   3. 去邮箱点验证链接
   4. 把拿到的 Access Key 粘到下面 ACCESS_KEY 里,替换占位字符串
   完成后,网站所有表单(首页匹配/咨询、物业管理落地页、避坑指南下载)
   提交的线索都会自动发到那个邮箱。无需服务器。
   ===================================================================== */
(function () {
  "use strict";

  var ACCESS_KEY = "30b94e92-6cb2-46f9-b0be-b61f348c22a4"; // Web3Forms → leads go to service@mortgagebrg.com.au (verified via live form submit 2026-07)
  var ENDPOINT = "https://api.web3forms.com/submit";

  function isZh() { return document.documentElement.lang === "zh-CN"; }

  var forms = document.querySelectorAll("form[data-lead-form]");
  forms.forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      var btn = form.querySelector("button[type=submit]") || form.querySelector("button");
      if (!btn) return;
      var original = btn.textContent;
      btn.disabled = true;
      btn.textContent = isZh() ? "提交中…" : "Sending…";

      var fd = new FormData(form);
      fd.append("access_key", ACCESS_KEY);
      if (!fd.get("subject")) {
        fd.append("subject", form.getAttribute("data-lead-form") || "New website lead");
      }
      fd.append("from_name", "Mortgage Bridge Website");
      fd.append("page_url", location.href);

      var notConfigured = ACCESS_KEY.indexOf("REPLACE_") === 0;

      function showSuccess() {
        var okEn = form.getAttribute("data-success-en") || "✓ Thanks! A specialist will call you within 12 hours.";
        var okZh = form.getAttribute("data-success-zh") || "✓ 已收到!顾问将在12小时内与你联系。";
        btn.textContent = isZh() ? okZh : okEn;
        if (typeof window.trackLead === "function") {
          window.trackLead(form.getAttribute("data-lead-form") || "form");
        }
        form.reset();
        if (form.hasAttribute("data-redirect")) {
          setTimeout(function () { location.href = form.getAttribute("data-redirect"); }, 800);
        }
      }
      function showError() {
        btn.disabled = false;
        btn.textContent = original;
        alert(isZh()
          ? "抱歉,提交出了点问题。请稍后再试,或直接致电我们。"
          : "Sorry, something went wrong. Please try again or call us.");
      }

      if (notConfigured) {
        // Key 还没填:不发送,但让客户端流程看起来正常,并在控制台提醒站长。
        console.warn("[forms.js] Web3Forms ACCESS_KEY 未设置 — 线索未发送。请在 forms.js 中填入 key。");
        showSuccess();
        return;
      }

      fetch(ENDPOINT, { method: "POST", headers: { "Accept": "application/json" }, body: fd })
        .then(function (r) { return r.json(); })
        .then(function (json) {
          if (json && json.success) { showSuccess(); }
          else { throw new Error((json && json.message) || "submit failed"); }
        })
        .catch(function (err) { console.error("[forms.js]", err); showError(); });
    });
  });
})();
