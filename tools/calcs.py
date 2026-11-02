"""Free HR calculators (leave balance, overtime pay, final settlement), built from the end-of-service
calculator page so they share its header, footer, styles and analytics. Run by gen.py after it has
refreshed the end-of-service page."""
import os, re

SITE = "https://www.syncstead.com.sa"
DEMO = "/{lang}/demo/"

# Shared helpers for the page scripts: dates, service years (calendar years + days/365), number format.
JS_LIB = r"""var L=document.documentElement.lang==='ar';
function fmt(n){return n.toLocaleString(L?'ar-SA':'en-US',{maximumFractionDigits:2});}
function years(s,e){var fy=e.getFullYear()-s.getFullYear(),an=new Date(s);an.setFullYear(s.getFullYear()+fy);if(an>e){fy--;an=new Date(s);an.setFullYear(s.getFullYear()+fy);}return fy+(e-an)/86400000/365;}
function num(v){var n=parseFloat(v);return isNaN(n)?0:n;}
function eos(w,y,reason){var base=y<=5?w*0.5*y:w*(2.5+(y-5)),f=1;if(reason==='resign'){f=y<2?0:y<5?1/3:y<10?2/3:1;}return {amt:base*f,f:f};}
function accrued(y){return 21*Math.min(y,5)+30*Math.max(y-5,0);}
"""

PAGES = {
 "leave-balance-calculator": {
  "en": dict(
   title="Annual leave balance calculator (Saudi Labour Law) | Syncstead",
   desc="Free calculator for an employee's annual leave balance and its value under the Saudi Labour Law, Articles 109 and 111.",
   h1="Annual leave balance calculator",
   intro="Work out how many annual leave days an employee has earned, how many are left and what they are worth (Saudi Labour Law, Articles 109 and 111).",
   form="""<label>Start date<input name="start" type="date" required></label>
<label>Calculate up to<input name="end" type="date" required></label>
<div class="two"><label>Leave days already taken<input name="taken" type="number" min="0" step="0.5" inputmode="decimal" value="0"></label><label>Monthly wage (SAR), basic plus regular allowances<input name="wage" type="number" min="0" step="1" inputmode="numeric"></label></div>""",
   how="""<li>21 days of paid annual leave a year, rising to 30 days a year once the employee has five years of service with the employer (Article 109). Leave builds up day by day.</li>
<li>The value of a day of leave is the monthly wage divided by 30.</li>
<li>Leave not taken by the end of service is paid out at the wage for those days (Article 111).</li>""",
   note="This is an estimate for guidance only and is not legal advice. Your contract or company policy may give more leave than the law.",
   js=r"""var s=new Date(f.start.value),e=new Date(f.end.value),t=num(f.taken.value),w=num(f.wage.value);
if(!(e>s)){return bad();}
var y=years(s,e),acc=accrued(y),bal=acc-t;
show((L?'مدة الخدمة: ':'Service: ')+fmt(y)+(L?' سنة':' years')+'<br>'+(L?'الأيام المكتسبة: ':'Days earned: ')+fmt(acc)+(L?' · المأخوذة: ':' · taken: ')+fmt(t)+
'<div class="big">'+fmt(bal)+(L?' يوم':' days')+'</div>'+(w>0?(L?'قيمة الرصيد: ':'Value of the balance: ')+fmt(bal*w/30)+(L?' ريال':' SAR'):''));""",
  ),
  "ar": dict(
   title="حاسبة رصيد الإجازة السنوية (نظام العمل السعودي) | سينكستيد",
   desc="حاسبة مجانية لرصيد الإجازة السنوية للموظف وقيمته وفق نظام العمل السعودي، المادتان 109 و111.",
   h1="حاسبة رصيد الإجازة السنوية",
   intro="احسب عدد أيام الإجازة السنوية التي استحقها الموظف، والمتبقي منها، وقيمتها (نظام العمل السعودي، المادتان 109 و111).",
   form="""<label>تاريخ بداية الخدمة<input name="start" type="date" required></label>
<label>الاحتساب حتى تاريخ<input name="end" type="date" required></label>
<div class="two"><label>أيام الإجازة المأخوذة<input name="taken" type="number" min="0" step="0.5" inputmode="decimal" value="0"></label><label>الأجر الشهري (ريال)، الأساسي مع البدلات الثابتة<input name="wage" type="number" min="0" step="1" inputmode="numeric"></label></div>""",
   how="""<li>يستحق الموظف إجازة سنوية مدفوعة الأجر مدتها 21 يومًا، تزيد إلى 30 يومًا إذا أمضى خمس سنوات متصلة لدى صاحب العمل (المادة 109). وتُكتسب الإجازة يومًا بيوم.</li>
<li>قيمة يوم الإجازة تساوي الأجر الشهري مقسومًا على 30.</li>
<li>يُدفع للموظف أجر أيام الإجازة التي لم يحصل عليها عند انتهاء خدمته (المادة 111).</li>""",
   note="هذه نتيجة تقديرية للاسترشاد وليست استشارة قانونية. قد يمنح العقد أو لائحة الشركة إجازة أطول مما ينص عليه النظام.",
  ),
 },
 "overtime-calculator": {
  "en": dict(
   title="Overtime pay calculator (Saudi Labour Law) | Syncstead",
   desc="Free calculator for overtime pay under the Saudi Labour Law, Article 107: the hourly wage plus 50% of the basic hourly wage.",
   h1="Overtime pay calculator",
   intro="Work out overtime pay under the Saudi Labour Law (Article 107): each extra hour is paid at the hourly wage plus 50% of the basic hourly wage.",
   form="""<div class="two"><label>Basic monthly salary (SAR)<input name="basic" type="number" min="1" step="1" inputmode="numeric" required></label><label>Total monthly wage (SAR), basic plus allowances<input name="wage" type="number" min="1" step="1" inputmode="numeric" required></label></div>
<div class="two"><label>Overtime hours<input name="hours" type="number" min="0.5" step="0.5" inputmode="decimal" required></label><label>Normal working hours a day<select name="day"><option value="8">8 hours</option><option value="6">6 hours (Ramadan, Muslim employees)</option></select></label></div>""",
   how="""<li>Overtime is paid at the hourly wage plus 50% of the basic hourly wage (Article 107).</li>
<li>The hourly wage here is the monthly wage divided by 30 days and by the normal hours a day (8, or 6 for Muslim employees in Ramadan, Article 98).</li>
<li>Some companies divide by a different number of days or hours. Check your policy and contract.</li>""",
   note="This is an estimate for guidance only and is not legal advice.",
   js=r"""var b=num(f.basic.value),w=num(f.wage.value),h=num(f.hours.value),d=num(f.day.value);
if(!(b>0&&w>=b&&h>0)){return bad();}
var hw=w/30/d,hb=b/30/d,rate=hw+0.5*hb;
show((L?'أجر الساعة: ':'Hourly wage: ')+fmt(hw)+(L?' ريال · أجر الساعة الإضافية: ':' SAR · overtime hour: ')+fmt(rate)+(L?' ريال':' SAR')+
'<div class="big">'+fmt(rate*h)+(L?' ريال':' SAR')+'</div>'+(L?'عن ':'for ')+fmt(h)+(L?' ساعة إضافية':' overtime hours'));""",
  ),
  "ar": dict(
   title="حاسبة أجر العمل الإضافي (نظام العمل السعودي) | سينكستيد",
   desc="حاسبة مجانية لأجر العمل الإضافي وفق نظام العمل السعودي، المادة 107: أجر الساعة مضافًا إليه 50% من الأجر الأساسي للساعة.",
   h1="حاسبة أجر العمل الإضافي",
   intro="احسب أجر العمل الإضافي وفق نظام العمل السعودي (المادة 107): تُدفع كل ساعة إضافية بأجر الساعة مضافًا إليه 50% من الأجر الأساسي للساعة.",
   form="""<div class="two"><label>الراتب الأساسي الشهري (ريال)<input name="basic" type="number" min="1" step="1" inputmode="numeric" required></label><label>إجمالي الأجر الشهري (ريال)، الأساسي مع البدلات<input name="wage" type="number" min="1" step="1" inputmode="numeric" required></label></div>
<div class="two"><label>عدد الساعات الإضافية<input name="hours" type="number" min="0.5" step="0.5" inputmode="decimal" required></label><label>ساعات العمل العادية يوميًا<select name="day"><option value="8">8 ساعات</option><option value="6">6 ساعات (رمضان، للموظفين المسلمين)</option></select></label></div>""",
   how="""<li>يُدفع عن ساعات العمل الإضافية أجر الساعة مضافًا إليه 50% من الأجر الأساسي للساعة (المادة 107).</li>
<li>أجر الساعة هنا هو الأجر الشهري مقسومًا على 30 يومًا ثم على ساعات العمل اليومية (8، أو 6 للموظفين المسلمين في رمضان، المادة 98).</li>
<li>بعض الشركات تقسم على عدد أيام أو ساعات مختلف. راجع لائحة الشركة والعقد.</li>""",
   note="هذه نتيجة تقديرية للاسترشاد وليست استشارة قانونية.",
  ),
 },
 "final-settlement-calculator": {
  "en": dict(
   title="Final settlement calculator (Saudi Labour Law) | Syncstead",
   desc="Free calculator for an employee's final settlement in Saudi Arabia: end-of-service award, unused leave, last month's salary and deductions.",
   h1="Final settlement calculator",
   intro="Estimate everything due to an employee when they leave: the end-of-service award, pay for unused annual leave and the salary for days worked in the last month, less any deductions.",
   form="""<label>Last monthly wage (SAR), basic plus regular allowances<input name="wage" type="number" min="1" step="1" inputmode="numeric" required></label>
<div class="two"><label>Start date<input name="start" type="date" required></label><label>Last working day<input name="end" type="date" required></label></div>
<label>Reason for leaving<select name="reason"><option value="end">Contract ended or terminated by the employer</option><option value="resign">Resignation by the employee</option></select></label>
<div class="two"><label>Annual leave days already taken (whole service)<input name="taken" type="number" min="0" step="0.5" inputmode="decimal" value="0"></label><label>Days worked in the last month and not yet paid<input name="days" type="number" min="0" max="31" step="1" inputmode="numeric" value="0"></label></div>
<div class="two"><label>Other amounts due (SAR), e.g. unpaid overtime<input name="add" type="number" min="0" step="1" inputmode="numeric" value="0"></label><label>Deductions (SAR), e.g. loans or advances<input name="ded" type="number" min="0" step="1" inputmode="numeric" value="0"></label></div>""",
   how="""<li>End-of-service award: half a month's wage for each of the first five years and a full month's wage for each year after (Article 84), reduced on resignation (Article 85).</li>
<li>Unused annual leave: 21 days a year, 30 after five years (Article 109), paid at the monthly wage divided by 30 (Article 111).</li>
<li>Last month's salary: the monthly wage divided by 30, times the days worked and not yet paid.</li>""",
   note="This is an estimate for guidance only and is not legal advice. Notice-period pay, compensation for unlawful termination and special cases are not included.",
   js=r"""var w=num(f.wage.value),s=new Date(f.start.value),e=new Date(f.end.value),r=f.reason.value,t=num(f.taken.value),dd=num(f.days.value),ad=num(f.add.value),de=num(f.ded.value);
if(!(e>s&&w>0)){return bad();}
var y=years(s,e),eo=eos(w,y,r),bal=Math.max(0,accrued(y)-t),lv=bal*w/30,sal=dd*w/30,tot=eo.amt+lv+sal+ad-de;
var row=function(a,b){return '<tr><td>'+a+'</td><td style="text-align:end">'+fmt(b)+'</td></tr>';};
show((L?'مدة الخدمة: ':'Service: ')+fmt(y)+(L?' سنة':' years')+'<table style="width:100%;margin-top:8px">'+
row((L?'مكافأة نهاية الخدمة':'End-of-service award')+(r==='resign'?' ('+Math.round(eo.f*100)+'%)':''),eo.amt)+
row((L?'بدل الإجازة غير المستخدمة (':'Unused leave (')+fmt(bal)+(L?' يوم)':' days)'),lv)+
row(L?'راتب أيام الشهر الأخير':'Last month\'s salary',sal)+(ad?row(L?'مبالغ أخرى مستحقة':'Other amounts due',ad):'')+(de?row(L?'الاستقطاعات':'Deductions',-de):'')+
'</table><div class="big">'+fmt(tot)+(L?' ريال':' SAR')+'</div>');""",
  ),
  "ar": dict(
   title="حاسبة المخالصة النهائية (نظام العمل السعودي) | سينكستيد",
   desc="حاسبة مجانية للمخالصة النهائية للموظف في السعودية: مكافأة نهاية الخدمة، بدل الإجازة غير المستخدمة، راتب الشهر الأخير والاستقطاعات.",
   h1="حاسبة المخالصة النهائية",
   intro="احسب تقديريًا كل ما يستحقه الموظف عند انتهاء خدمته: مكافأة نهاية الخدمة، وبدل الإجازة السنوية غير المستخدمة، وراتب أيام الشهر الأخير، مخصومًا منها أي استقطاعات.",
   form="""<label>آخر أجر شهري (ريال)، الأساسي مع البدلات الثابتة<input name="wage" type="number" min="1" step="1" inputmode="numeric" required></label>
<div class="two"><label>تاريخ بداية الخدمة<input name="start" type="date" required></label><label>آخر يوم عمل<input name="end" type="date" required></label></div>
<label>سبب انتهاء الخدمة<select name="reason"><option value="end">انتهاء العقد أو إنهاؤه من صاحب العمل</option><option value="resign">استقالة الموظف</option></select></label>
<div class="two"><label>أيام الإجازة السنوية المأخوذة (طوال الخدمة)<input name="taken" type="number" min="0" step="0.5" inputmode="decimal" value="0"></label><label>أيام العمل في الشهر الأخير غير المدفوعة<input name="days" type="number" min="0" max="31" step="1" inputmode="numeric" value="0"></label></div>
<div class="two"><label>مبالغ أخرى مستحقة (ريال)، مثل عمل إضافي<input name="add" type="number" min="0" step="1" inputmode="numeric" value="0"></label><label>الاستقطاعات (ريال)، مثل السلف والقروض<input name="ded" type="number" min="0" step="1" inputmode="numeric" value="0"></label></div>""",
   how="""<li>مكافأة نهاية الخدمة: أجر نصف شهر عن كل سنة من السنوات الخمس الأولى، وأجر شهر كامل عن كل سنة بعدها (المادة 84)، وتُخفض عند الاستقالة (المادة 85).</li>
<li>الإجازة السنوية غير المستخدمة: 21 يومًا في السنة، و30 يومًا بعد خمس سنوات (المادة 109)، ويُدفع اليوم بالأجر الشهري مقسومًا على 30 (المادة 111).</li>
<li>راتب الشهر الأخير: الأجر الشهري مقسومًا على 30، مضروبًا في أيام العمل غير المدفوعة.</li>""",
   note="هذه نتيجة تقديرية للاسترشاد وليست استشارة قانونية. لا تشمل أجر فترة الإشعار ولا التعويض عن الإنهاء غير المشروع ولا الحالات الخاصة.",
  ),
 },
}

NAMES = {
 "end-of-service-calculator": ("End-of-service calculator", "حاسبة مكافأة نهاية الخدمة"),
 "leave-balance-calculator": ("Annual leave balance", "رصيد الإجازة السنوية"),
 "overtime-calculator": ("Overtime pay", "أجر العمل الإضافي"),
 "final-settlement-calculator": ("Final settlement", "المخالصة النهائية"),
}


def build():
    written = []
    for lang in ("en", "ar"):
        en = lang == "en"
        tpl = open(os.path.join(lang, "end-of-service-calculator", "index.html"), encoding="utf-8").read()
        for slug, spec in PAGES.items():
            c = spec[lang]
            js = spec["en"]["js"]  # one script, bilingual by page language
            others = " · ".join(f'<a href="/{lang}/{s}/">{NAMES[s][0 if en else 1]}</a>' for s in NAMES if s != slug)
            demo = "See how Syncstead does it automatically" if en else "شاهد كيف يحسبها سينكستيد تلقائيًا"
            main = f'''<main id="main" class="w"><div class="page">
<h1>{c["h1"]}</h1>
<p>{c["intro"]}</p>
<form id="calc" style="margin-top:20px" novalidate>
{c["form"]}
<button class="btn" type="submit">{"Calculate" if en else "احسب"}</button>
<div class="result" id="out" hidden aria-live="polite"></div>
</form>
<h2>{"How it is calculated" if en else "طريقة الاحتساب"}</h2>
<ul>{c["how"]}</ul>
<p>{c["note"]} {"Syncstead calculates this automatically for every employee." if en else "يحسب سينكستيد ذلك تلقائيًا لكل موظف."}</p>
<p><a class="btn" href="{DEMO.format(lang=lang)}" style="margin-top:12px">{demo}</a></p>
<p style="margin-top:24px">{"More free calculators:" if en else "حاسبات مجانية أخرى:"} {others}</p>
<script>
(function(){{
{JS_LIB}var f=document.getElementById('calc'),out=document.getElementById('out');
function show(h){{out.hidden=false;out.innerHTML=h;}}
function bad(){{show(L?'تحقق من القيم والتواريخ.':'Please check the numbers and dates.');}}
f.addEventListener('submit',function(ev){{ev.preventDefault();if(!f.checkValidity()){{f.reportValidity();return;}}
{js}
}});
}})();
</script>
</div></main>'''
            s = re.sub(r'<main id="main" class="w">.*?</main>', lambda _: main, tpl, flags=re.S)
            s = re.sub(r"<title>.*?</title>", f"<title>{c['title']}</title>", s, flags=re.S)
            s = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda m: m.group(1) + c["desc"], s)
            s = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + c["title"], s)
            head, body = s.split("</head>", 1)
            head = head.replace("/end-of-service-calculator/\"", f"/{slug}/\"")  # canonical + hreflang
            other = "ar" if en else "en"
            body = body.replace(f'href="/{other}/end-of-service-calculator/"', f'href="/{other}/{slug}/"')  # language switch
            s = head + "</head>" + body
            path = os.path.join(lang, slug, "index.html")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").write(s)
            written.append(path)
    return written
