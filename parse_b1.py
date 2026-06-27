import json
import re
import os
import sys

text = """🇩🇪 B1: 21-Dars: O'tmishdagi armon va ushalmagan orzular - "Konjunktiv II" (O'tgan zamon)
Agar o'tmishda b'lib o'tgan ishga nisbatan "Agar unday b''lganida, bunday b''lardi (lekin b''lmadi)" deb afsuslanish ifodalansa, hätte / wäre + Partizip II kurylmasi islatiladi.

Wenn ich mehr gelernt hätte, hätte ich die Prüfung bestanden.

Aytilishi: [Ven ix mer gelernt xatte, xatte ix di pryufung bestanden.]

Tarjimasi: Agar kwprok o'qiganimda edi, imtihondan o'tgan bwlardim. (Afsus, o'ta olmadim)

Wenn ich pünktlich gewesen wäre, wäre ich nicht zu spät gekommen.

Aytilishi: [Ven ix pyunktlix gevezen vere, vere ix nixt tsu shpet gekommen.]

Tarjimasi: Agar vaktida bulganimda edi, kechikmagan bulardim.

🇩🇪 B1: 22-Dars: Mazhul nisbatning o'tgan tugallangan zamoni (Perfekt Passiv)
Ish-harakatning yaqin o'tmishda bazharilib keyinligini Mazhul (Pasive) shaklda aitish. Koida: sein (tuslanadi) + Partizip II + worden (gap ohirida uzgarmaydi).

Avtomatik so'zni qayta tiklash.

Aytilishi: [Das auto ist reparent vorden.]

Tarjimasi: Machine tamirlab bwlindi.

Ich bin angerufen worden.

Aytilishi: [Ix bin angerufen vorden.]

Tarjimasi: Menga qo'ng'iroq qilib o'lindi.

🇩🇪 B1: 23-Dars: Shartli qarshilik bogʻlovchisi - “tushadi” (Agar mabodo)
Wenn boglovchi uhshaidi, lekinsiga zhuda kam bulgan, "mabodo, twsatdan sodir bulib kolsa" degan shartlar uchun javob. Fel gap ohiriga boradi.

Falls es regnet, kutamiz tark.

Aytilishi: [Falls es regnet, blayben vir tsu xauze.]

Tarjimasi: Mabodo yomgir yogib kolsa, qolamiz.

Falls du Hilfe Brauchst, Ruf Mich an.

Aytilishi: [Falls du xilfe brauxst, ruf mix an.]

Tarjimasi: Mabodo yerdam kerak bo'lib kolsa, menga qo'ng'irok kil.

🇩🇪 B1: 24-Dars: Sifatdosh I - Hozirgi zamon sifatdoshi (Partizip I)
Ayni vaqtda bazhar qilinayotgan haraqatni sifat sifatida otning oldida kullash. Buni yasash uchun fe'l boslangich shakli (infinitiv) ohiriga -d harfi va kelishik qo'shimchasi qo'shiladi.

weinen (yiglamok) -> das weinende Kind [das vaynende kind] - yiglayotgan bola.

Ich sehe das weinende Kind.

Aytilishi: [Ix ze-e das vaynende kind.]

Tarjimasi: Men yiglayotgan bolani kuryapman.

das lachende Mädchen [das laxende medxen] - kulayotgan kiz.

🇩🇪 B1: 25-Dars: Sifatdosh II - O'tgan zamon sifatdoshi (Partizip II)
Bazharilib bulingan haraqatni sifat sifatida otning oldida qullash. Bunda felning Partizip II shakli otning oldiga qo'yilib, sifatdek tuslanadi.

kaufen (sobit olmoq) -> das gekaufte Auto [das gekaufte auto] — sobit oblingan mashina.

Das gekaufte Auto ist sehr neu.

Aytilishi: [Das gekaufte auto ist zer noy.]

Tarjimasi: Sotib olingan mashina juda yangi.

die geschriebene E-Mail [di geshribene i-meyl] - ezilgan elektron hut.

🇩🇪 B1: 26-Dars: Ish joyida suhbat va muzokaralar (Berufsleben)
Germanyda hamkasblar yoki boshlik bilan loyixalarni muhokama qilish iboralari.

die Besprechung [beshprexung] - Majlis / yigilish, u xizmat:  verschieben [fershiben] - koldirmok (boshqa vaqtga).

Wir mussen termdan kutisch Verschieben.

Aytilishi: [Vir myssen den termin verschiben.]

Tarjimasi: Biz uchrashuv vaktini boshka kunga koldirishimiz kerak.

Ich bin für diesen Vorschlag. [Ix bin fyr dizen forshlag.] - Men bu taklifni yo'qlayman.

🇩🇪 B1: 27-Dars: Ketma-ketlik vaqt bogʻlovchisi - “nachdem” (...dan keyin)
Agar bir ish tugagandan sungi boshlansa va gap gozirgi/kelasi zamonda bulsa, nachdem kelgan gapda Perfekt zamoni islatiladi. asosiy gap oddiy hozirgi zamonda koladi.

Nachdem ich gegessen habe, gehe ich arbeiten.

Aytilishi: [Naxdem ix gegessen xabe, ge-e ix arbayten.]

Tarjimasi: Ovqatlanib bulganimdan keyin, ishga ketaman.

Nachdem ya doich o'rganim, flge ya v Germaniya.

Aytilishi: [Naxdem ix doych gelernt xabe, flige ix nax Doychland.]

Tarjimasi: Nemis tilini o'rganib bulganimdan keyin, Germaniyaga uchib ketaman.

🇩🇪 B1: 28-Dars: Davriylik vakt boglovchisi - “solange” (...gan muddatda / vaqt)
Ikkita harakat bir vaktda, bir hil vakt natijasida sodir bo'layotganligini kw. Fel gap ohirida turadi.

Solange ich hier wohne, lerne ich Deutsch.

Aytilishi: [Zolange ix xir vone, lerne ix doych.]

Tarjimasi: Shu erda yashayotgan muddatim nemis tilini o'rganaman.

Bleib hier, solange es regnet. [Blayb xir, zolange es regnet.] - Yomgir yogayotgan vaktda shu erda tour.

🇩🇪 B1: 29-Dars: Cheklovchi boglovchilar - "soft" va "sobald"
sobald (hamonok / zakhotiok) - Sobald ich anrufen, kelaman. [Sobald ix anrufe, komme ix.] - Men qo'ng'irok qilgan zatem kelaman.

sooft (har gal / necha marta bulsa ham) - Soft ich dikh sehen, xursand belaman. [Sooft ix dix ze-e, froye ix mix.] - Seni kar gal ko'rganimda, xursand bo'laman.

🇩🇪 B1: 30-Dars: Uchinchi modul takrori (Wiederholung)
Partizip I, Partizip II va murakkab vakt boglovchilarini suxbatda mustakamlash.

Javob: Machst du, sobald du nach Hause kommst edimi? [Vas maxst du, sobald du nax xauze kommst?] - Uyga kelgan zahoting nima qilasan?

B: Nachdem ich gegessen habe, lese ich das gekaufte Buch. [Naxdem ix gegessen xabe, leze ix das gekaufte bux.] - Ovqatlanib bulganimdan keyin, sotib olingan kitobni o'qiyman.

🇩🇪 B1: 31-Dars: Junatma olish va Bozhxona (Zoll)
Germaniada halkaro posilka olish va bozhona ishlari.

der Zoll [soll] — bojxona, boj:  die Zollgebühr [tsoll-gebyur] — bojxona to‘lovi, partin nazorati:  die Passkontrolle [pass-kontrolle].

Ich muss mein Paket beim Zoll abholen.

Aytilishi: [Ix muss mayn paket baym tsoll abxolen.]

Tarjimasi: Men posilkamni bozhonadan olib ketishim kerak.

🇩🇪 B1: 32-Dars: Voz kechish predloglari — "statt" (Genitiv)
"...ning o'rniga" manosini beruvchi va faqat Genitiv kelishuvini talab qiluvchi muhim pretext.

statt des Autos [shtatt des autos] — mashining urniga.

Statt des Kaffees trinke ich heute Tee.

Aytilishi: [Shtatt des kafees trinke ix xoyte tee.]

Tarjimasi: Bugun kofe urniga choy ichapman.

Statt meiner Schwester kommt mein Bruder. [Shtatt mayner shvester kommt mayn bruder.] - Opamning o'rniga ukam kelapti.

🇩🇪 B1: 33-Dars: Noanik nisbiy olmoshlar - "was" wa "wo"
Agar gapda biror aniq from emas, beams butun bir fikr yoki alles, etwas, nichts so'zlari aniqlab kelinsa, nisbiy gap was yoki wo orkali boshlanadi.

Das ist alles, was ich weiß.

Aytilishi: [Das ist alles, vas ix vays.]

Tarjimasi: Bu men bilgan hamma narsa.

Dort, vo men yashayman, juda chiroili.

Aytilishi: [Dort, vo ix vone, ist es zer shyon.]

Tarjimasi: Men yashayotgan joy juda chiroili.

🇩🇪 B1: 34-Dars: Taxmin va gumon manolari - “scheinen” (Gyoki / Tuyulmoq)
Biror narsa huddi shundayidek tuyishini ifodalash uchun scheinen ... zu + infinitiv kurylmasi islatiladi.

Er scheint krank zu sein.

Aytilishi: [Er shaynt krank tsu zayn.]

Tarjimasi: U g'o'yoki kasaldek tushyapti (kasal b'lsa kerak).

Du scheinst viel zu arbeiten. [Du shaynt fil tsu arbayten.] - Sen kwp islayotganga okhshaisan.

🇩🇪 B1: 35-Dars: Ikki kismli boglovchilar - “je...desto” (kanchalik...shunchalik)
Zhuftlikda islatiladigan eng chiroili boglovchilardan biri. Koida: je sifatli sifat darazhasi kelib, fe'l gap ohiriga ketadi. desto asosiy sifat darazhasidan keyin darhol fe'l keladi.

Je mehr du lernst, desto besser sprichst du.

Aytilishi: [Ye mer du lernst, desto besser shprixst du.]

Tarjimasi: Kanchalik kwp oqisang, shunchalik yakhshi gapirasan.

Je schneller, desto besser. [Ye shneller, desto besser.] — Qanchalik tez bo'lsa, shunchalik yaxshi.

🇩🇪 B1: 36-Dars: To'rtinchi modul takrori (Wiederholung)
Javob: Je länger ich Deutsch lerne, desto einfacher finde ich es . [Ye lenger ix doych lerne, desto aynfaxer finde ix es.] — Nemis tivini qanchalik uzoq o'rgansam, shunchalik oson tuyulyapti.

B: Das stimmt. Dunyoda hech bir til qiyin emas. [Das shtimmt. Keine Sprache ist zu schwer.] - Tugri. Chech kaisi til o'ta qiyin emas.

🇩🇪 B1: 37-Dars: Silent huquqlari va xavfsizligini saqlang (Garie)
Technique va buyumlar sotib olish uchun hal qilish.

die Garantie [garanti] - kafolat, yurish:  umtauschen [umtauschen] - ayirboshlash (boshkasiga), qaytarish:  zurückgeben [tsyuryukgeben].

Ich möchte dieses Handy umtauschen, ich habe noch Garantie.

Aytilishi: [Ix myoxte dizes xendi umtauschen, ix xabe nox garanti.]

Tarjimasi: Men bu telefon yordamkchiman, hali kafolati bor.

🇩🇪 B1: 38-Dars: Murakkab predloglar — "innerhalb" va "außerhalb" (Genitiv)
Makon va vaqt chegaralarini kushish uchun faqat va faqat Genitiv kelishuv bilan keladi.

innerhalb (ichida / inner) - innerhalb einer Woche - bir hafta ichida.

außerhalb (tashkarisida) - außerhalb der Arbeitszeit [auzerxalb der arbayts-tsayt] - ish vaktidan tashkarida.

Sie mussen innerhalb von 3 Tagen bezahlen.

Aytilishi: [Zi myssen innerxalb fon dray tagen bessalen.]

Tarjimasi: Siz 3 kun ichida to'xtash shart.

🇩🇪 B1: 39-Dars: To'ldiruvchi predlog - “ohne” va “mit” (Mustahkamlash)
A2 dagi mavzuni murakkab shaklda predlog va kelishiklar koidasi bilan B1 darazhasiga moslab chukur o'rganish.

Ohne sizning yordam men kila olmasdim.

Aytilishi: [Ohne dayne Xilfe xatte ix das nixt geschafft.]

Tarjimasi: Sening yordamingsiz men buni uddalai olmasdim. (ohne milk Akkusativ)

Mit moy dest men sayohat kilaman. [Mit maynem Freund reise ich.] - Men dustim bilan sayohat kilaman. (mit sut dativ)

🇩🇪 B1: 40-Dars: Beshinchi modul takrori (Wiederholung)
Javob: Kann ich das Produkt innerhalb einer Woche zurückgeben? [Kann ix das produkt innerxalb ayner voxe tsyuryukgeben?] - Mahsulotni bir hfta ichida qaytarib bersam bwladimi?

B: Ja, agar kafolat qo'g'ozi bo'lsa, muammo o'q. [Ya, wenn Sie die Garantie haben, kein Problem.] - Ha, agar kafolatingiz bo'lsa, muammo o'q.
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
