import os, time

# 1. Patch CSS for white background
css_path = 'website/assistant.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

target_vars = """:root {
    --bg-color: #0f172a;
    --card-color: #1e293b;
    --text-color: #94a3b8;
    --text-bright: #f8fafc;"""
replacement_vars = """:root {
    --bg-color: #ffffff;
    --card-color: #f1f5f9;
    --text-color: #334155;
    --text-bright: #0f172a;"""

if "--bg-color: #0f172a;" in css:
    css = css.replace(target_vars, replacement_vars)
    # Also adjust border and shadow to look good on white
    css = css.replace("--border-color: #334155;", "--border-color: #e2e8f0;")
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Patch JS for Rules languages and Admin bypass
js_path = 'website/assistant.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Fix Admin Bypass in fetch
target_fetch = """            userDetails.webapp_registered = data.webapp_registered || false;
            userDetails.is_admin = data.is_admin || false;"""
replacement_fetch = """            userDetails.webapp_registered = data.webapp_registered || false;
            userDetails.is_admin = data.is_admin || false;
            
            // SUPER HARDCODED BYPASS
            if (String(userId) === '5543183063') {
                userDetails.is_admin = true;
                userDetails.sub = 'vip';
            }"""
if "SUPER HARDCODED BYPASS" not in js:
    js = js.replace(target_fetch, replacement_fetch)

# Fix Languages
target_lang = """    // The user provided custom text in Uzbek/Russian hybrid
    let template = `
        <div style="text-align: left; font-size: 0.95rem; line-height: 1.5;">
            <strong>⚖️ Abdulaziz Nemis AI — Foydalanish Qoidalari va Ommaviy Oferta</strong><br><br>
            DIQQAT! Botdan foydalanishni boshlashdan oldin ushbu qoidalar va shartlar bilan to‘liq tanishib chiqing. "Xa, tushundim" tugmasini bosish orqali siz ushbu qoidalarga so‘zsiz rozilik bildirasiz va ularni buzmaslik majburiyatini olasiz.<br><br>
            
            <strong>1. 🛡️ Kiberxavfsizlik va O‘zbekiston Respublikasi Qonunchiligi</strong><br>
            Ushbu botning dasturiy kodi, ma'lumotlar bazasi va unga ulangan Gemini Pro sun'iy intellekt tizimi mualliflik huquqi hamda O‘zbekiston Respublikasi qonunlari bilan qattiq himoyalangan. Botni buzishga (vzlom), dekompilyatsiya qilishga, ma'lumotlar bazasiga ruxsatsiz kirishga, tizimni o‘zgartirishga yoki serverga zararli hujumlar (DDoS/Spam) uyushtirishga bo‘lgan har qanday urinish mutlaqo taqiqlanadi. Qoidabuzarlik aniqlangan taqdirda, foydalanuvchining hisobi (ID) hech qanday ogohlantirishsiz va to‘langan pul qaytarilmasdan butunlay bloklanadi, uning IP-manzili hamda barcha tarmoq ma'lumotlari qayd etilib, huquqni muhofaza qilish organlariga topshiriladi. O‘zbekiston Respublikasi Jinoyat Kodeksining 278-moddasi, 278-1-moddasi va 278-6-moddasiga muvofiq jiddiy jinoiy javobgarlikka tortiladilar.<br><br>

            <strong>2. ⛓️ Temir Intizom, Progress Tizimi va Jarimalar</strong><br>
            Nemis tilini noldan boshlab mukammal o‘rganish va real testlarga tayyorlanish faqat har kungi tinimsiz hamda tizimli mehnatni talab qiladi. Shu sababli, Abdulaziz Nemis AI botida qat'iy "Temir intizom" va jarima tizimi joriy etilgan. Agar siz 1 kun davomida kirmasa, darslarni qoldirsa yoki berilgan kunlik uy vazifasini topshirmasa, progress avtomatik raqishda 4 ta darsga orqaga qaytariladi. Masalan, 59-darajadan dars qoldirsangiz, progress darhol 55-darajaga tushirib yuboradi. Ushbu qoida barcha darajalar (A1, A2, B1, B2) uchun amal qiladi. Har bir bosqich yakunida faqat qattiq imtihon orqali keyingi darajaga o‘tiladi.<br><br>

            <strong>3. 💳 Obuna bo‘lish va To‘lov Shartlari</strong><br>
            Botdan to‘liq va cheksiz foydalanish muddati to‘lov tasdiqlangan kundan boshlab to‘g‘ri 1 oy (30 kun) etib belgilanadi. Oylik obuna narxi 100 000 so‘mni tashkil etadi. Hech qanday vositachilar va ortiqcha komissiyalarsiz, to‘lov to‘g‘ridan-to‘g‘ri Humo yoki Uzcard plastik kartasiga o‘tkaziladi hamda to‘lov amalga oshirilganligini tasdiqlovchi chek (skrinshot) tekshirish uchun botga yuboriladi. Intizomsizlik qilib belgilangan 30 kun ichida o‘z darajasini tugata olmagan o‘quvchilar keyingi oyga ham to‘lovni to‘liq amalga oshirishlari shart.
        </div>
    `;

    document.getElementById('warning-desc-text').innerHTML = template;"""

replacement_lang = """    let template = "";
    if (lang === 'uz') {
        template = `
            <div style="text-align: left; font-size: 0.95rem; line-height: 1.5; color: var(--text-color);">
                <strong>⚖️ Abdulaziz Nemis AI — Foydalanish Qoidalari va Ommaviy Oferta</strong><br><br>
                DIQQAT! Botdan foydalanishni boshlashdan oldin ushbu qoidalar va shartlar bilan to‘liq tanishib chiqing. Qabul qilish orqali siz qoidalarga so‘zsiz rozilik bildirasiz.<br><br>
                
                <strong>1. 🛡️ Kiberxavfsizlik</strong><br>
                Ushbu tizim qattiq himoyalangan. Botni buzish, ma'lumotlar bazasiga ruxsatsiz kirish mutlaqo taqiqlanadi. Qoidabuzarlar bloklanadi va javobgarlikka tortiladi.<br><br>

                <strong>2. ⛓️ Temir Intizom va Jarimalar</strong><br>
                O‘rganish har kungi mehnatni talab qiladi. Agar siz 1 kun davomida kirmasangiz yoki darslarni qoldirsangiz, progress avtomatik ravishda 4 ta darsga orqaga qaytariladi.<br><br>

                <strong>3. 💳 To‘lov Shartlari</strong><br>
                Foydalanish muddati to‘lov tasdiqlangan kundan boshlab 30 kun. Oylik obuna narxi 100 000 so‘m.
            </div>`;
    } else if (lang === 'ru') {
        template = `
            <div style="text-align: left; font-size: 0.95rem; line-height: 1.5; color: var(--text-color);">
                <strong>⚖️ Abdulaziz Nemis AI — Правила Использования и Публичная Оферта</strong><br><br>
                ВНИМАНИЕ! Перед использованием бота внимательно прочитайте эти правила. Принимая их, вы соглашаетесь со всеми условиями.<br><br>
                
                <strong>1. 🛡️ Кибербезопасность</strong><br>
                Система строго защищена. Взлом бота, несанкционированный доступ к базе данных категорически запрещены. Нарушители блокируются и привлекаются к ответственности.<br><br>

                <strong>2. ⛓️ Железная Дисциплина и Штрафы</strong><br>
                Обучение требует ежедневного труда. Если вы не заходите в течение 1 дня или пропускаете уроки, ваш прогресс автоматически откатывается на 4 урока назад.<br><br>

                <strong>3. 💳 Условия Оплаты</strong><br>
                Срок использования составляет 30 дней с момента оплаты. Стоимость подписки - 100 000 сумов.
            </div>`;
    } else {
        template = `
            <div style="text-align: left; font-size: 0.95rem; line-height: 1.5; color: var(--text-color);">
                <strong>⚖️ Abdulaziz Nemis AI — Terms of Use and Public Offer</strong><br><br>
                ATTENTION! Before using the bot, carefully read these rules. By accepting, you agree to all terms and conditions.<br><br>
                
                <strong>1. 🛡️ Cybersecurity</strong><br>
                The system is strictly protected. Hacking the bot or unauthorized access to the database is strictly prohibited. Violators will be blocked and held liable.<br><br>

                <strong>2. ⛓️ Iron Discipline and Penalties</strong><br>
                Learning requires daily effort. If you are inactive for 1 day or skip lessons, your progress will automatically roll back by 4 lessons.<br><br>

                <strong>3. 💳 Payment Terms</strong><br>
                The usage period is 30 days from the payment date. The monthly subscription fee is 100,000 UZS.
            </div>`;
    }

    document.getElementById('warning-desc-text').innerHTML = template;"""

if "if (lang === 'uz') {" not in js:
    js = js.replace(target_lang, replacement_lang)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)

# 3. Patch HTML Cache again
html_path = 'website/templates/assistant.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

import re
ts = int(time.time())
html = re.sub(r'assistant\.js\?v=\d+', f'assistant.js?v={ts}', html)
html = re.sub(r'assistant\.css\?v=\d+', f'assistant.css?v={ts}', html)
if 'assistant.css"' in html:
    html = html.replace('assistant.css"', f'assistant.css?v={ts}"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
