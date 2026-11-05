/* Construction loan calculator. calcConstruction is pure so it can be tested on its own. */
(function (root) {
  "use strict";
  // Own funds are spent first. Stages are spread evenly across the build, with the first at the
  // start and the last at completion. Interest accrues monthly on the balance drawn so far.
  function calcConstruction(o) {
    var r = o.rate / 100 / 12, n = Math.max(1, Math.round(o.months));
    var left = o.own, bal = o.land, stages = [], drawMonth = {};
    var count = o.pcts.length;
    o.pcts.forEach(function (p, i) {
      var amount = o.build * p / 100, fromOwn = Math.min(left, amount);
      left -= fromOwn;
      var month = count > 1 ? Math.round(i * n / (count - 1)) : 0;
      stages.push({ i: i, month: month, amount: amount, fromOwn: fromOwn, draw: amount - fromOwn });
      drawMonth[month] = (drawMonth[month] || 0) + amount - fromOwn;
    });
    var totalInterest = 0, peak = 0;
    bal = o.land + (drawMonth[0] || 0);
    var balAtStart = [bal];
    for (var m = 1; m <= n; m++) {
      var interest = bal * r;
      totalInterest += interest;
      if (interest > peak) peak = interest;
      bal += drawMonth[m] || 0;
      balAtStart.push(bal);
    }
    var running = o.land;
    stages.forEach(function (s) { running += s.draw; s.owing = running; s.monthly = running * r; });
    var nTerm = Math.round(o.term * 12), repay = nTerm <= 0 ? 0 : r <= 0 ? bal / nTerm : bal * r / (1 - Math.pow(1 + r, -nTerm));
    var rentTotal = o.rent * 52 / 12 * n;
    return { stages: stages, totalInterest: totalInterest, peak: peak, finalLoan: bal, repayment: repay, rentTotal: rentTotal,
             holding: totalInterest + rentTotal, ownUnused: left, months: n };
  }
  root.calcConstruction = calcConstruction;
  if (typeof document === "undefined") return;

  var NAMES = { en: ["Deposit", "Base or slab", "Frame", "Lock-up", "Fixing", "Completion"], zh: ["定金", "地基或楼板", "框架", "封顶门窗", "内部安装", "实际完工"] };
  var $ = function (id) { return document.getElementById(id); };
  var num = function (id) { var n = parseFloat(String($(id).value).replace(/[^0-9.]/g, "")); return isFinite(n) ? n : 0; };
  var money = function (n) { return "$" + Math.round(n).toLocaleString("en-AU"); };
  var ids = ["land", "build", "own", "rate", "months", "term", "rent"];

  function card(label, value, sub) {
    return '<div><div class="text-sm text-on-surface-variant">' + label + '</div><div class="font-display text-2xl font-bold text-primary mt-1">' + value + '</div>' +
      (sub ? '<div class="text-xs text-on-surface-variant mt-1">' + sub + "</div>" : "") + "</div>";
  }
  function render() {
    var zh = document.documentElement.lang === "zh-CN";
    var pcts = NAMES.en.map(function (_, i) { return num("s" + i); });
    var sum = pcts.reduce(function (a, b) { return a + b; }, 0);
    var msg = $("pctMsg"), ok = Math.abs(sum - 100) < 0.01;
    msg.textContent = (zh ? "合计 " : "Total ") + (Math.round(sum * 100) / 100) + "%" + (ok ? "" : (zh ? "，应为 100%" : ", should be 100%"));
    msg.style.color = ok ? "#40484b" : "#93000a";
    var c = calcConstruction({ land: num("land"), build: num("build"), own: num("own"), rate: num("rate"), months: num("months"), term: num("term"), rent: num("rent"), pcts: pcts });
    $("summary").innerHTML =
      card(zh ? "建房期间总利息" : "Interest during the build", money(c.totalInterest), (zh ? "约 " + c.months + " 个月" : "Over about " + c.months + " months") + (c.rentTotal ? (zh ? "；连房租共 " : "; with rent, ") + money(c.holding) : "")) +
      card(zh ? "建房期间最高月利息" : "Highest monthly interest", money(c.peak), zh ? "完工前最后一段时间" : "Late in the build") +
      card(zh ? "完工后预计月供" : "Estimated repayment after", money(c.repayment), (zh ? "贷款 " : "On a loan of ") + money(c.finalLoan) + (zh ? "，本息同还" : ", principal and interest"));
    var L = zh ? ["阶段", "约第几个月", "应付", "贷款放款", "贷款余额", "之后每月利息"] : ["Stage", "About month", "Payable", "Loan drawn", "Loan balance", "Monthly interest after"];
    $("thead").innerHTML = "<tr>" + L.map(function (h, i) { return '<th class="py-2 pr-3 font-semibold text-on-surface-variant ' + (i ? "text-right" : "text-left") + '">' + h + "</th>"; }).join("") + "</tr>";
    var names = zh ? NAMES.zh : NAMES.en;
    $("tbody").innerHTML = c.stages.map(function (s) {
      return '<tr class="border-t border-outline-variant/40"><td class="py-2 pr-3">' + names[s.i] + '</td><td class="py-2 pr-3 text-right">' + s.month + '</td><td class="py-2 pr-3 text-right">' + money(s.amount) +
        '</td><td class="py-2 pr-3 text-right">' + money(s.draw) + '</td><td class="py-2 pr-3 text-right">' + money(s.owing) + '</td><td class="py-2 pr-3 text-right font-semibold">' + (s.i === c.stages.length - 1 ? (zh ? "转本息同还" : "Moves to P&amp;I") : money(s.monthly)) + "</td></tr>";
    }).join("");
    $("note").textContent = zh ? "估算：假设各阶段在工期内平均分布，每月按已放款余额计息，并先用自有资金。不含贷款费用、LMI 和工程变更。"
      : "Estimate: assumes stages are spread evenly across the build, interest is charged monthly on the balance drawn, and your own money is used first. Excludes lender fees, LMI and variations.";
  }
  ids.concat(NAMES.en.map(function (_, i) { return "s" + i; })).forEach(function (id) { $(id).addEventListener("input", render); });
  ["land", "build", "own", "rent"].forEach(function (id) {
    $(id).addEventListener("blur", function () { var n = num(id); $(id).value = n ? Math.round(n).toLocaleString("en-AU") : "0"; });
  });
  window.onLangChange = render;
  render();
})(typeof window !== "undefined" ? window : globalThis);
