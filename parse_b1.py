import json
import re
import os
import sys

text = """🇩🇪 B1: 1-Dars: Maqsad bog'lovchilari - "damit" va "um... zu" (Mustahkamlash)
B1 darazhasida ushbu ikki muhim maqsad kurilmasining farqini va murakkab haplarda qo'llanishini chukur o'rganamiz. Agar haplarda egalar bir hil bwlsa um... zu , har hil bwlsa damit qurilmalar.

Ich lerne Deutsch, um in Deutschland zu Studieren.

Aytilishi: [Ix lerne doych, um in Doychland tsu shtudiren.]

Tarjimasi: Germanyda o'qish uchun nemis tilini o'rganyapman. (Ega bitta - Erkaklar)

Ich helfe kerak, men Team gewinnt.

Aytilishi: [Ix xelfe dem proyekt, damit mayn tim gevinnt.]

Tarjimasi: Zhamoam galaba kozonishi uchun men loyigaga yordam beryapman. (Egalar har khil - Men va Zhamoam)

🇩🇪 B1: 2-Dars: Sabab-natija bog'lovchilar — "darum", "deshalb", "deswegen"
Uch uchta bog'lovchi ham uzbek tiliga "shu tufayli", "shunning uchun" deb tarjima orqali. Oltin qoida: bu bog'lovchilardan keyin darhol tuslangan fe'l (Tezkor tartib).

Ich war krank, deshalb konnte ich nicht kommen.

Aytilishi: [Ix var krank, deshalb konnte ix nixt kommen.]

Tarjimasi: Men kasal edim, shuning uchun kela olmadim. (konnte fe'li bog'lovchidan keyin turibdi)

Er lernt viel, darum spricht er gut Deutsch.

Aytilishi: [Er lernt fil, darum shprixt er gut doych.]

Tarjimasi: U kwp oqiidi, shu sababl nemischada yakhshi gapiradi.

🇩🇪 B1: 3-Dars: Sifatlarning maqolalari tuslanishi (Nullartikel)
Agar otning oldida hech kanday article (der, die, das, ein) bolmasa, sifat o'sha otning asl articles ohiridagi hos harflarni o'ziga oladi.

kalter Kaffee [kalter kafee] - sovuk kofe (Kaffee - der, maqola yoshligi uchun sifatga "-er" qo'shildi)

frisches Brot [frishes brot] - yangi non (Brot - das, sifatga "-es" qo'shildi)

Ich trinke gern kalten Kaffee.  (Oqkusativda)

Aytilishi: [Ix trinke gern kalten kafee.]

Tarjimasi: Men sovuk kofe ichishni yaxshi kuraman.

🇩🇪 B1: 4-Dars: Passive zamon format - O'tgan zamon Passiv (Präteritum Passiv)
Ish-harakatning o'tmishda kim tomonidan bajarilganligini ifodalash. Bunda wurden fe'li tuslanadi va asosiy fe'l gap ohirida Partizip II b'ladi.

Das Haus wurde im Jahre 2020 gebaut.

Aytilishi: [Das xaus vurde im yare svaytauzendtsvansix gebaut.]

Tarjimasi: Uy 2020 yilda qurilgan edi.

Ich wurde gestern angerufen.

Aytilishi: [Ix vurde gestern angerufen.]

Tarjimasi: Kecha menga qoʻngʻiroq qilishdi (men qoʻngʻiro qoʻyishm).

🇩🇪 B1: 5-Dars: Toʻsiqsiz bogʻlovchi - “obwohl” (Karamay / Soʻziga karamay)
Ozbek tilidagi "...ga karamay", "...sa ham" mazmunini beradi. Fel har doim gapning eng ohiriga suriladi.

Obwohl es regnet, gehe ich spazieren.

Aytilishi: [Obvoyl es regnet, ge-e ix shpatsiren.]

Tarjimasi: Yomgir yogayotgan bulsa ham (yogishiga karamai), men yuklayotgan ketyapman.

Ich habe das Auto gekauft, obwohl es teuer war.

Aytilishi: [Ix xabe das auto gekauft, obvoyl es toyer var.]

Tarjimasi: Qimmat bo'lishiga karamai, men u mashinasini sotib oldim.

🇩🇪 B1: 6-Dars: Noaniklik bog'lovchisi - “ob” (Mi / Yo'kmi)
Swrok gaplarni tasdik gapga boglashda "mi yoki ywkmi" mazmunini ifodalaidi. Fel gap ohiriga boradi.

Ich weiß nicht, ob er morgen kommt.

Aytilishi: [Ix vays nixt, ob er morgen kommt.]

Tarjimasi: uni ertaga kelish-kelishni Men bilmayman (keladimi-yo'kmi).

Können Sie mir sagen, ob der Bus schon da ist?

Aytilishi: [Kynnen Zi mir zagen, ob der bus shon da ist?]

Tarjimasi: Bus keldimi-yukmi, menga aytasizmi?

🇩🇪 B1: 7-Dars: Vaqt boglovchisi - “seit / seitdem” (...dan take)
Ish-at o'tmishda boshlanib, gozirgacha davom etaotgan bulsa haroratda. Fel gap ohirida turadi.

Germaniyada Seitdem ich wohne, lerne ich viel.

Aytilishi: [Zaytdem ix in Doychland vone, lerne ix fil.]

Tarjimasi: Germanyda yashayotganimdan beri kwp o'kiyapman.

Seit ya v Berlin, habe ich einen Job.

Aytilishi: [Zayt ix in Berlin bin, xabe ix aynen job.]

Tarjimasi: Berlinda bulganimdan olib mening ishim bor.

🇩🇪 B1: 8-Dars: Gerund va Sifatdosh kurilmalari - Infinitiv mit "zu"
Nemis tilida ikkita fe'l yonma-yon kelganda, qaerda fe'l oldidan zu qo'yilishi shart. Ammo modal fe'llar wa sehen, hören, gehen kabi fe'llardan keyin zu islatilmaydi .

Es ist wichtig, jeden Tag Deutsch zu lernen.

Aytilishi: [Es ist vixtix, yeden tag doych tsu lernen.]

Tarjimasi: Har kuni nemis tilini o'rganish muximdir.

Ich habe vergessen, dich anzurufen.

Aytilishi: [Ix xabe fergessen, dix antsurufen.]

Tarjimasi: Senga qo'ng'iroq qilishni unutibman. (Ajraladigan fe'llarda 'zu' o'rtaga tushadi)

🇩🇪 B1: 9-Dars: Istatk va orzu maili — "Konjunktiv II" (Hätte / Wäre)
"Agar mening... bulganida edi" yoki "Agar men... bulganimda edi" kabi reallikka tugri kelmaydigan orzularni ifodalash.

Wenn ich reich wäre, würde ich reisen.

Aytilishi: [Ven ix rayx vere, vyrde ix rayzen.]

Tarjimasi: Agar boy bulganimda edi, sayohat kilgan bulardim.

Ich hätte gern ein großes Haus.

Aytilishi: [Ix xatte gern ayn groses xaus.]

Tarjimasi: Katta uyim bo'lishini istardim.

🇩🇪 B1: 10-Dars: Birinchi modul takrori (Wiederholung)
B1 darazhasining ishlab chiqarishich murakkab boglovchilarini suhbatda qullash.

A: Weißt du, ob Anvar den Test bestanden hat? [Vaysst du, ob Anvar den test bestanden xat?] — Anvar testdan o'tdimi-yuqmi bilasanmi?

B: Ja, obwohl der Test schwer war, hat er es geschafft. [Ya, obvoyl der test shver var, xat er es geshafft.] - Ha, test qiyin bulishiga karamai, u uddaladi.

Javob: Deshalb ist er so glücklich! [Deshalb ist er zo glyuklix!] - Buning uchun u zhuda baxtli!

🇩🇪 B1: 11-Dars: Shahsiy munosabat - Fikr bildirish iboralari (Meinung)
Muchokamalarda uz fikrini professional darajada ifodalash.

Meiner Meinung nach... [Mayner moynung nax] - Mening fikrimcha... (Keyin darhol fe'l keladi)

Ich bin der Ansicht, dass... [Ix bin der anzix, dass] - Men shunday fikrdamanki...

Meiner Meinung nach ist Deutsch emas kiyin.

Aytilishi: [Mayner moynung nax ist doych nixt shver.]

Tarjimasi: Mening fikrimcha, nemis tili qiyin emas.

🇩🇪 B1: 12-Dars: Glad etish boglovchisi - "ohne dass" va "ohne... zu"
Biror haraqatni bazharmasdan, boshka ishni qilish. Agar egalar har khil bulsa ohne dass qurilmalar.

Er geht keng, ohne dass ich es merke.

Aytilishi: [Er geyt veg, ohne dass ix es merke.]

Tarjimasi: U men sezmasdan (bilib qolmasidan) chiqib ketyapti.

Er uchib ketdi, ohne "Tschüss" zu sagen.

Aytilishi: [Er geyt veg, ohne chyus tsu zagen.]

Tarjimasi: U "khair" demasdan chiqib ketdi.

🇩🇪 B1: 13-Dars: Natijaviy vaqt bogʻlovchisi - “bevor” (...Aldin tomonidan berilgan)
Biror ishdan oldin sodir buladigan haraqat. Fel gap ohirida turadi.

Bevor ich schlafen gehe, lese ich ein Buch.

Aytilishi: [Bevor ix shlafen ge-e, leze ix ayn bux.]

Tarjimasi: Uxlashga ketishimdan oldin, men kitob o'qiyman.

Trink ein Wasser, bevor du gehst. [Trink ayn vasser, bevor du geyst.] — Ketmasingdan oldingi suv ichib ol.

🇩🇪 B1: 14-Dars: Ikki kismli boglovchilar - "entweder ... oder"
"Yoki...yoki" tanlov mazmunini beruvchi zhuft bog'lovchi.

Entweder wir gehen ins Kino, oder wir bleiben zu Hause.

Aytilishi: [Entveder vir geen ins kino, oder vir blayben tsu xauze.]

Tarjimasi: Yoki biz kinoga boramiz, youki uida qolamiz.

Ich trinke entweder Tee oder Kaffee. [Ix trinke entveder tee oder kafee.] — My yo choy yoki koy ichaman.

🇩🇪 B1: 15-Dars: Ikki kismli boglovchilar - "sowohl... als auch"
"Nafakat... beams ham" yoki "ham... ham" mazmunini beruvchi kuchli bog'lovchi.

Ich spreche sowohl Usbekisch als auch Deutsch.

Aytilishi: [Ix shpreexe zovohl usbekish als aux doych.]

Tarjimasi: Men ham uzbekcha, ham nemischa gapiraman.

Er hat sowohl ein Avto als auch ein Fahrrad. [Er xat zovohl ayn auto als aux ayn farrad.] — Uning ham mashinsi, ham magnitibor.

🇩🇪 B1: 16-Dars: Murakkab Nisbiy olmoshlar - Dativ va Akkusativ (Relativsätze)
Gap oʻzaro bogʻliq holda nisbiy aniklovchilarning Dativ va Akkusativ kelishiklarida u muzlatiladi.

Der Mann, den ich gestern gesehen habe, ist Arzt.  (Aqkusativ - den)

Aytilishi: [Der man, den ix gestern gezeyen xabe, ist artst.]

Tarjimasi: Men kecha ko'rgan odamdir.

Die Frau, der ich geholfen habe, ist nett.  (Dativ - der, chunki helfen Dativ talab qiladi)

Aytilishi: [Di frau, der ix gexolfen xabe, ist nett.]

Tarjimasi: Men yordam bergan ayol juda mehribon.

🇩🇪 B1: 17-Dars: Bank xizmatlari va kreditlar (Auf der Bank)
Germanyda bank hisobi ochish va atamalar.

das Girokonto [jirokonto] - zhoriy bank hisobi

die Kreditkarte [kreditkarte] - kredit karta

Geld abheben [geld abheben] — pu echib olmoq (bankomatdan)

Ich möchte ein Girokonto eröffnen.

Aytilishi: [Ix myoxte ayn jirokonto eröffnen.]

Tarjimasi: Men bank hisob raqami ochmoqchi edim.

🇩🇪 B1: 18-Dars: Atrof-muhit va ekologiya muammolari (Umwelt)
muammolar:  die Umweltverschmutzung [umvelt-fershmutsung] - atrof-muhitning ifloslanishi, der Müll [myull] - chikindi, recyceln [resaykeln] - qayta ishlash.

Wir mussen den Myul trennen.

Aytilishi: [Vir myssen den myull trennen.]

Tarjimasi: Biz chikindilarni saralashimiz (turlarga bwlishimiz) kerak.

🇩🇪 B1: 19-Dars: Shartley voz kechish - "anstatt dass" wa "anstatt... zu"
Biror ishni qilish urniga, boshka ishni bazharish.

Er bleibt zu Hause, anstatt zur Arbeit zu gehen.

Aytilishi: [Er bleybt tsu xauze, anstatt tsur arbayt tsu geen.]

Tarjimasi: Ishga borish o'rniga, ket ketyapti.

Anstatt dass du lernst, spielst du Computer.

Aytilishi: [Anstatt dass du lernst, shpilst du kompyuter.]

Tarjimasi: Ŏqishing o'rniga, kompyuter o'ng'in qilmoqda.

🇩🇪 B1: 20-Dars: Ikkinci modul takrori (Wiederholung)
Javob: Meiner Meinung nach sollten wir mehr für die Umwelt tun. [Mayner moynung nax sollten vir mer fyr di umvelt tun.] — Mening firmamcha, biz atro-muxitushunchni ko'p ish qilishimiz kerak.

B: Da hast du recht. Anstatt Plastik zu kaufen, sollten wir Stofftaschen benutzen. [Da xast du rext. Anstatt plastik tsu kaufen, sollten vir shtofftashen benutsen.] — To'g'ri aytsan. Filtr sotib olish urniga, matoli sumlardan foydalanamiz liz.
"""

B1_LESSONS = {}
parts = re.split(r'(🇩🇪 B1: \d+-Dars:|🇩🇪 B1: \d+-dars:)', text)
for i in range(1, len(parts), 2):
    header = parts[i]
    content = parts[i+1].strip()
    match = re.search(r'🇩🇪 B1: (\d+)-(D|d)ars:', header)
    if match:
        lesson_num = int(match.group(1))
        B1_LESSONS[str(lesson_num)] = "📖 **" + header.replace("🇩🇪 B1: ", "") + "**\n\n" + content

# Since we only have lessons 1-20 so far, we append to or create the file
lessons_file = os.path.join(os.path.dirname(__file__), 'website', 'b1_lessons.py')

existing_lessons = {}
if os.path.exists(lessons_file):
    try:
        sys.path.append(os.path.dirname(lessons_file))
        from b1_lessons import B1_LESSONS as existing
        existing_lessons = existing
    except Exception as e:
        print("Error loading existing:", e)

existing_lessons.update(B1_LESSONS)

with open(lessons_file, 'w', encoding='utf-8') as f:
    f.write('B1_LESSONS = ' + json.dumps(existing_lessons, ensure_ascii=False, indent=4))
