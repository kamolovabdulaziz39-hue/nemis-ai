import json
import re
import os
import sys

text = """🇩🇪 B2: 21-Dars: Sifatdosh iboralarining rangi - "Partizipialkonstruktionen"
B2 darazhasida uzun nisbiy haplarni kiskartirish sifatdosh iboralari uchun. Bunda haraqat asosiy gapdagi ega bilan bir vaktda sodir bulayotgan buladi.

Laut singend kam er ins Zimmer.

Aytilishi: [Laut zingend kam er ins tsimmer.]

Tarjimasi: U baland ovozda qoʻshiq kuylagancha (kuylab) xonaga kirdi.

Den Fehler bemerkend, korrigierte er la rejalashtirilgan.

Aytilishi: [Den feler bemerkend, korrigierte er das proyekt.]

Tarjimasi: Khatoni sezgan zagoti, u tartibga solishni tug'iladi.

🇩🇪 B2: 22-Dars: Passiv muqobillari - "sein + zu + Infinitiv"
Nemis tilida Passiv + modal fe'l (müssen / können) o'rnini bosuvchi zhuda mashur rasmiy kurilma. Gap faol (faol) ko'rinishda b'lsa-da, mazhul (passiv) mano beradi.

Die Aufgabe ist bis morgen zu erledigen.  (muss erledigt werden manosida)

Aytilishi: [Di aufgabe ist bis morgen tsu erledigen.]

Tarjimasi: Vozifa ertagacha bazharilishi shart.

Das Buch ist überall zu finden.  (kann gefunden werden manosida)

Aytilishi: [Das bux ist uberall tsu finden.]

Tarjimasi: Bu kitobni hamma erdan topish mumkin.

🇩🇪 B2: 23-Dars: Passiv muqobillari - "-bar" va "-lich" qo'shimchalari
Swz ohiriga -bar yoki -lich qo'shimchalarini qo'yish orkali "qila olsa bo'ladigan" (kann... werden) degan Passive manosidagi sifatlar yasaladi.

trinken (ichmoq) -> trinkbar [trinkbar] — ichsa bo'lgan / ichishga yaroqli.

Das Wasser ist trinkbar.

Aytilishi: [Das vasser ist trinkbar.]

Tarjimasi: Bu suvni ichsa bo'ladi (ichish mumkin).

lesen (o'qkћmoq) -> leserlich [lezerlix] - o'qisa bo'ladigan (khat hakida).

Deine Schrift ist ne leserlich. [Dayne shrift ist nixt lezerlix.] — Sening xatingni o'qish bo'lmaydi.

🇩🇪 B2: 24-Dars: Rasmiy til usuli - Fel-ot birikmalari (Nomen-Ferb-Verbindungen I)
B2 darazhasining eng muxim belgisi. Bunda oddiy bir fe'l urniga From + Fe'l birikmasi keladi va u rasmiy/business tili keladi.

Fragen stellen (= fragen) - savol bermok / savol chikarmok.

Sie können jederzeit Fragen stellen.

Aytilishi: [Zi kynnen yedertsayt fragen shtellen.]

Tarjimasi: Siz xolagan vaktda savollar berishingiz mumkin.

eine Rolle spielen (= wichtig sein) - o'ynamok / muhim bwlmok roli.

Das keine Rolle. [Das shpilt kayne rolle.] — Buning yoki yo'q (rol o'ynamaydi).

🇩🇪 B2: 25-Dars: Fe'l-ot birikmalari (Nomen-Ferb-Verbindungen II)
in Erfüllung gehen (= sich erfüllen) - amalga oshmoq / ushalmoq (orzular xakida).

Mein Traum Erfullung gegangen shahrida.

Aytilishi: [Mayn travma ist in erfyullung gegangen.]

Tarjimasi: Mening orzum amalga oshdi (ushaldi).

Unterstützung finden (= unterstützt werden) - qullab-quvvatlanish / erdam topmoq.

Das Projekt shapka Unterstützung gefunden. [Das proyekt xat untershpropsyutsung gefunden.] - Loyiha qullab-quvvatlandi.

🇩🇪 B2: 26-Dars: Germany so'g' saklash tizimi va Tibbiyot (Medizin)
Shifohonalarda, suhurta ishlarida va tibbiyoty kirikda kerak buladigan B2 darazhasidagi murakkab atamalar.

die Diagnoz [diagnoz] - tashhis, davolashno retsept:  das Reze davolash [  retsept] die Behandlung [bexandlung].

Der Arzt shapka o'lib tashxis gestellt.

Aytilishi: [Der artst xat di diagnoze gheshtelt.]

Tarjimasi: Shifokor tashkhis qo'ydi.

Behandlung urush erfolgreich Die. [Di bexandlung var erfolgrayx.] - Davolanish muwaffakiyatli o'tdi.

🇩🇪 B2: 27-Dars: Sabab-natija bog'lovchilar — "insofern" va "insoweit"
“Shu manodaki”, “shu darazhadaki” mazmunini va boshqa fikrni tekshirish yoki tushuntirib keluvchi B2 bog'lovchilari.

Ich stimme dir insofern zu, als o'z firk yo'q.

Aytilishi: [Ix shtimme dir inzofern tsu, als dayne argumente rixtix zind.]

Tarjimasi: Men senga shu manoda qushilamanki, senning dallylaring tugri.

Insoweit hato yök, beraylik. [Inzovayt qayn feler ist, maxen vir vayter.] - Shu darazada hato ywk ekan, davom etadi.

🇩🇪 B2: 28-Dars: Ortda kolgan shart boglovchisi - "ansonsten" (Aks holda)
"Aks Holda", "Bulmasa" Mazmunidagi Bog'lovchi. Koida: ansonsten soʻzidan keyin darhol tuslangan feʼl keladi (Tezkor tartib).

Du musst fleißig lernen, ansonsten bestehst du die Prüfung nicht.

Aytilishi: [Du musst flayssix lernen, anzonsten beshteyst du di pryufung nixt.]

Tarjimasi: Sen tirishib o'qishing kerak, aks holda imtihondan o'ta olmaisan.

Beeil dich, ansonsten kommen wir zu spät. [Be-ayl dix, anzonsten kommen vir tsu shpet.] - Tezrok bwl, aks holda kechikib qolamiz.

🇩🇪 B2: 29-Dars: Murakkab Genitiv predlogi - "mithilfe" va "zwecks"
Faqat Genitiv kelishigi bilan oliy uslubdagi preloglar.

mithilfe (erdamida / k'magida) - mithilfe des Computers [mit-xilfe des kompyuters] - kompyuter erdamida.

zwecks (maqsadida) - zwecks der Weiterbildung [tsveks der vayterbildung] - malaka qobiliyati.

Er hat mithilfe seines Freundes la loyichani tugatdi.

Aytilishi: [Er xat mit-xilfe zaynes froyndes das proyekt bedet.]

Tarjimasi: U o'stining yordamini yakunladi.

🇩🇪 B2: 30-Dars: Uchinchi modul takrori (Wiederholung)
Rasmiy fe'l-ot birikmalari va murakkab Passiv muqobillarini mustaxkamlash.

Javob: Diagnose schon zu topildimi? [Ist di diagnoze shon tsu finden?] - Tashkhisni topsa b'ladimi (tayermi)?

B: Ja, doktor savollar berdi va tashkhisni qo'ydi. [Ya, der Arzt hat Fragen gestellt und die Diagnose mitgeteilt.] - HA, savollar berdi va tashkhisni ma'lum qildi .

🇩🇪 B2: 31-Dars: Sifatdosh kurilmalari - Gerundy va haraqat nomi (Substantivierte Adjektive)
Sifatlarning otga ailanishi va sud tugri tuslanishi (masalan: kattalar, bemorlar, ishchilar).

krank (kasal) -> der Kranke / die Kranke [der kranke / di kranke] - bemor odam.

Der Kranke muss im Bett bleiben.

Aytilishi: [Der kranke muss im bett blayben.]

Tarjimasi: Bemor twshakda qolishi shart.

die Erwachsenen [di ervaxsenen] - kattalar (yoshi kattalar).

🇩🇪 B2: 32-Dars: Twldiruvchi nisbiy haplar - "was baroi" va "wovon"
Butun bir gap mazmuniga nisbatan nisbiy bog'lovchi yasash (masalan: “bu menga zhuda yokdi” deb butun gapni ulash).

Er hat die Prüfung bestanden, mich sehr freut edi.

Aytilishi: [Er xat di pryufung bestanden, vas mix zer froyt.]

Tarjimasi: U imtihondan o'tdi, bu esa meni zhuda xursand kiladi. (was butun oldin haraqatga tegishli)

🇩🇪 B2: 33-Dars: Joy va makon nisbiy boglovchisi — "wohin" va "woher"
Nisbiy haplarda o'shnini anik ko'rsatib kelish.

Das Land, wohin ich reise, ist Deutschland.

Aytilishi: [Das land, voxin ix rayse, ist Doychland.]

Tarjimasi: Men sayohat qilish (kayergaki uchyapman) davlat Germaniyadir.

Die Stadt, woher ya kelaman, juda chiroli.

Aytilishi: [Di shtadt, voxer ix komme, ist shyon.]

Tarjimasi: Menga (kelib chikishim bulgan) shahar chiroilidir.

🇩🇪 B2: 34-Dars: Ishtiyok va maksad preloglar orqali - “aus” va “vor” (hissiyyotlar uchun)
Biror isni kaisi hissiyot tufayli bajarilganligini atish.

aus (katyy/ongli ravish) - aus Liebe [aus libe] - sevgidan / muhabbat tufayli.

vor (zhismoniy/beikhtiyor ravish) - vor Angst [vor angst] - qo'rquvdan.

Er hat vor Angst gezittert.

Aytilishi: [Er xat vor angst getsittert.]

Tarjimasi: U quurkuvdan titrab ketdi.

Ich tue das aus reinem Interesse. [Ix tue das aus raynem interesse.] - Men buni sof kiziqish tufayli kilyapman.

🇩🇪 B2: 35-Dars: Ikki kismli boglovchilar - "nicht destotrotz" (Shunga karamai)
Trotzdem suzining oliy, rasmiy va kuchlirok varianti. Orkasidan darhol fe'l keladi.

Es gab viele Probleme, nichtsdestotrotz haben wir gewonnen.

Aytilishi: [Es gab file probleme, nixts-desto-trots xaben vir gevonnen.]

Tarjimasi: Kwp muammolar bwldi, shunga karamai biz galaba kozondik.

🇩🇪 B2: 36-Dars: Turtinchi model takrori (Wiederholung)
Javob: Warum hat der Kranke vor Angst gezittert? [Varum xat der kranke vor angst getsittert?] — Nima uchun bemor qo'rquvdan titrab ketdi?

B: Angst vor der Operation, nichtsdestotrotz ist alles gut gelaufen. [Er xatte angst vor der operatsyon, nixts-desto-trots ist alles gut gelaufen.] - U operatsiyadan qo'rqqan edi, shunga karamai hammasi yaxshi o'tdi.

🇩🇪 B2: 37-Dars: Ilmiy tadqiqotlar va Technology (Wissenschaft)
Ilmiy makolalarda va subatlarda yuzaga kelgan yukori sokhaviy suzlar.

die Forschung [forhung] - tadqiqot, kashfiyot:  die Entdeckung [entdekkung] - ichtiro / kashfiyot, rivozhlantirmok:  entwickeln [entvikkeln].

Wissenschaftler haben eine neue Entdeckung gemacht.

Aytilishi: [Vissenshaftler xaben ayne noye entdekkung gemaxt.]

Tarjimasi: Olimlar yangi kashfiyot aniqlandi.

🇩🇪 B2: 38-Dars: Murakab sifatli yasalishi — Qushma sifatlar (Zusammengesetzte Adjektive)
Ikkita so'zni qo'shib, ko'tarilgan manodagi sifatlar yasash.

weltweit [velt-vayt] - dunyo mikoshidagi / butun dunyo bo'ylab.

umweltfreundlich [umvelt-froyndlix] - atrof-muhit uchun hafsiz (ekologik toza).

Wir mussen umweltfreundliche Autos kaufen.

Aytilishi: [Vir myssen umvelt-froyndlixe autos kaufen.]

Tarjimasi: Biz ecologists toza machinelar sotib olishimiz kerak.

🇩🇪 B2: 39-Dars: Gumon va Shart maili - "Konjunktiv II" murakkab zamonlarda.
O'tmishdagi bir voqea mumkinga nisbatan "beams u o'shanda kilgan bulishi edi" deb takhmin bildirish kurilmasi.

Er hätte das wissen müssen.

Aytilishi: [Er xatte das vissen myssen.]

Tarjimasi: U buni bilishi kerak edi (lekin bilmagan).

To'lovni amalga oshirish uchun. [Das vere toll gevezen.] - Bu zhuda z'r b'lgan b''lardi (lekin b'lmadi).

🇩🇪 B2: 40-Dars: Beshinchi modul takrori (Wiederholung)
Javob: Die weltweite Forschung entwickelt sich schnell. [Di velt-vayte forshung entvikselt zix shnell.] - Butun dunyo bo'ylab tadqiqot tez rivozhlanmokda.

B: Das stimmt, atrof-muhit uchun yangi ichtirolar qilinmoqda. [Das stimmt, es werden neue umweltfreundliche Entdeckungen gemacht.] - Tugri, atroph-muhit uchun yangi ekolog ichtirolar yaratilyapti.
"""

B2_LESSONS = {}
parts = re.split(r'(🇩🇪 B2: \d+-Dars:|🇩🇪 B2: \d+-dars:)', text)
for i in range(1, len(parts), 2):
    header = parts[i]
    content = parts[i+1].strip()
    match = re.search(r'🇩🇪 B2: (\d+)-(D|d)ars:', header)
    if match:
        lesson_num = int(match.group(1))
        B2_LESSONS[str(lesson_num)] = "📖 **" + header.replace("🇩🇪 B2: ", "") + "**\n\n" + content

lessons_file = os.path.join(os.path.dirname(__file__), 'website', 'b2_lessons.py')

existing_lessons = {}
if os.path.exists(lessons_file):
    try:
        sys.path.append(os.path.dirname(lessons_file))
        from b2_lessons import B2_LESSONS as existing
        existing_lessons = existing
    except Exception as e:
        print("Error loading existing:", e)

existing_lessons.update(B2_LESSONS)

with open(lessons_file, 'w', encoding='utf-8') as f:
    f.write('B2_LESSONS = ' + json.dumps(existing_lessons, ensure_ascii=False, indent=4))
