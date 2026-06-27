import json
import re
import os
import sys

text = """🇩🇪 A2: 1-Dars: O'tgan khayot xakida gapirish (Präteritum: war und hatte)
A2 darazhasini ytgan zamonni mustaxkamlashdan boshlaymiz. Ohzaki nutkda sein va haben larining fel o'tgan zamon mos zhuda kwp uskunalar.

war - edim / bolgan edim ( sein fe'lidan)

hatte - menda bor edi / ega edim ( haben fe'lidan)

Shakllari:
Ich war / Ich hatte

Du warst / Du hattest

Er, sie, es war / Er, sie, es hatte

Wir waren / Wir hatten

Misollar:
Deutschlanddagi Letztes Jahr urushi. [Letstes yar var ix in Doychland.] - O'tgan yili men Germaniada edim.

Früher hatte ich kein Auto. [Fryuer xatte ix kayn auto.] — Ilgari mening mashinam yo'q edi.

🇩🇪 A2: 2-Dars: Sabab inkor haplar - "weil" boglovchisi (Weil-Sätze)
"Chunki" suzi nemis tilida weil deyiladi. Oltin koida: weil kelgan gapda fe'l har doim gapning eng ohiriga boradi va sha erda tuslanadi.

Ich lerne Deutsch, weil ich Germaniyada fahren bo'ladi.

Aytilishi: [Ix lerne doych, vayl ix nax Doychland fahren vill.]

Tarjimasi: Men nemis tilini o'rganyapman, chunki men Germanyga bormoqchiman. ( ohirida o'z ichiga oladi ).

Ich bleibe im Bett, weil ich krank bin. [Ix blaybe im bett, vayl ix krank bin.] — Me kavatda qolaman, chunki men kataman.

🇩🇪 A2: 3-Dars: Maksad haplar - "um... zu" kurilmasi (Finalsätze)
Biror ishni "qilish uchun", "maqsadida" deyish uchun um... zu islatiladi. Gap ohirida zu + felning tikich shakli (infinitiv) turadi.

Ich fliege nach Berlin, um dort zu arbeiten.

Aytilishi: [Ix flige nax Berlin, um dort tsu arbayten.]

Tarjimasi: Men Berlinga u erda ishlash uchun uchapman.

Ich brauche Geld, um ein Auto zu kaufen. [Ix brauxe geld, um ayn auto tsu kaufen.] - Machine sotib olish uchun menga pool kerak.

🇩🇪 A2: 4-Dars: Murakkab o'tgan zamon - “Perfekt” takrorovi va kuchli fellar
A2 darazhasida kwp urgangan va o'zagi o'zgarib ketadigan kuchli (noto'g'ri) fellarning o'tgan zamonni yodlaymiz.

schreiben (yezish) -> hat geschrieben [xat geshriben]

trinken (ichish) -> shapka getrunken [xat getrunken]

essen (eyash) -> hat gegessen [xat gegessen]

Misol:  Ich habe einen Brief geschrieben. [Ix xabe aynen brif geshriben.] - Erkaklar shapkasi boramiz.

🇩🇪 A2: 5-Dars: Oldid Kelishidan Sifatlarning - Akkusativ (Adjektivdeklination)
Agar sifat otning oldida kelsa, u albatta quimcha oladi. Akkusativda erkak zhinsi uchun -en , ayol va o'rta zhins uchun noanik artikldan keyin -e qo'shiladi.

der Kaffee (erkak) -> Ich trinke einen heißer Kaffe.  [Ich trinke einen heißen Kaffee.] - Men issiq kofe ichäpman.

das Auto (o'rta) -> Ich kaufe ein neu es Auto. [Ix kaufe ayn noyes auto.] — Me yangi mashina sotib olyapman.

die Tasche (ayol) -> Ich habe eine schwarz e Tasche. [Ix xabe ayne shvartse tashe.] — Mening qo'ra sumam bor.

🇩🇪 A2: 6-Dars: Sifatlarning Dativ kelishigida tuslanishi.
Bu koida zhuda oson. Dativ kelishigida sifat otning oldida kelsa, maqolalar bor barcha zhinslarga (erkak, ayol, o'ta, kwplik) faqat bir hil — -en qo'shimchasi qo'shiladi.

mit (milk Dativ) + der Freund -> mit dem alt en Freund [mit dem alten froynd] - eski dwst bilan.

Ich spreche mit dem alten Freund. — Men eski dust bilan haplashapman.

in (Dativ) + das Haus -> in dem groß en Haus [in dem grosen xaus] - catta uyda.

🇩🇪 A2: 7-Dars: Ozlik fellari - "sich" bilan ishlash (Reflexive Verben)
Ozbek tilidagi "yuvinmok", "taranmok", "hursand bulmok" kabi harakat uziga kaytadigan fellar nemis tilida sich sherigi bilan keladi.

sich freuen [zix froyen] - hursand bolmoq

sich waschen [zix vashen] - yuvinmok

Ich froye mich. [Ix froye mix.] — M xursandman.

Du freust dich. [Du froyst dix.] - Sen Xursandsan.

Er freut sich. [Er froyt zix.] - U Xursand.

🇩🇪 A2: 8-Dars: Modallarning o'tgan vaqti (Präteritum der Modalverben)
Modal fe'llar o'tgan zamonda qo'llaniganda qonun ustidagi umlaut (nuktalar) tushib koladi va -te qo'shimchasi qo'shiladi.

können (qila olmoq) -> konnte [konnte] (qila olgan edim)

mussen (mazhbur bolmoq) -> musste [musste] (mazhbur edim)

wollen (xohlamok) -> wollte [vollte] (xohlagan edim)

Misol:  Ich konnte gestern nicht kommen. [Ix konnte gestern nixt kommen.] - Men kecha kela olmadim.

🇩🇪 A2: 9-Dars: Takkoslash darajalari - Sifat darajalari (taqqoslash)
Narsalarni bir-biriga solistirish. Kichikroq, kattaroq yoki eng katta kun.

schön (chiroyli) -> schöner (chiroyliroq) -> am schönsten (eng chiroyli)

groß (katta) -> größer (kattarok) -> am größten (eng katta)

Solishtirganda "da kura" suzi uchun als audio :

Anvar ist größer als Max. [Anvar ist groser als Maks.] - Anvar Maksdan kattarok.

🇩🇪 A2: 10-Dars: Istisno sokoslashlar (Gut, Viel, Gern)
Bu suzlar qoidaga buysunmasdan, butunlay uzgarib ketadi:

gut (yaxshi) -> besser (yaxshiroq) -> am besten (eng yaxshi)

viel (kwp) -> mehr (kwprok) -> am meisten (eng kwp)

gern (yakhshi kwrish bazharish) -> lieber (yahshiroq kwrish) -> am liebsten (eng yakhshi kwrish)

Misol:  Ich trinke lieber Tee. [Ix trinke liber tee.] - Men choy ichishni afzal kuraman (yahshiroq kuraman).

🇩🇪 A2: 11-Dars: Shartley haplar - "wenn" boglovchisi (Wenn-Sätze)
"Agar", "...sa/...si" shart mazmunini beruvchi bogʻlovchi. Khuddi weil kabi, wenn kelgan gapda ham fe'l eng ohiriga suriladi.

Wenn ich Zeit habe, komme ich.

Aytilishi: [Ven ix tsayt xabe, komme ix.]

Tarjimasi: Agar vaktim bulsa, kelaman.

Wenn es regnet, bleiben wir zu Hause. [Ven es regnet, blayben vir tsu xauze.] - Agar yomg'ir yogsa, biz uyda qolamiz.

🇩🇪 A2: 12-Dars: Birinchi modul takrori (Wiederholung)
A2 darajasining birinchi mavzularini mustaxkamlash uchun amaliy dialog:

Javob: Deutschni yaxshi bilasizmi? [Varum lernst du doych?] - Nima uchun nemis tilini o'rganyapsan?

B: Ich lerne Deutsch, weil ich v Germany studieren will . [Ix lerne doych, vayl ix nax Doychland shtudiren vill.] — Me nemishcha o'rganyapman, chunki Germaniyada o'qishmoqchiman.

Javob: Konntest du früher Deutsch sprechen? [Konntest du fryuer doych shprexen?] — Ilgari nemicha gapara ularmiding?

B: Nein, oldingi konnte ich ne. [Nayn, fryuer konnte ix das nixt.] — Yo‘q, ilgari buni qila olmasdim.

🇩🇪 A2: 13-Dars: Uy ishlari va ishlab chiqarishlar (Haushalt)
Uy ichidagi kundalik yumushlar nomlanishi:

aufräumen [aufroymen] - uini yig'ishtirmoq

kochen [koxen] - ovkat pishirmok

die Wäsche waschen [di veshe vashen] - kir yuvmok

Ich muss mein Zimmer aufräumen. [Ix muss mayn tsimmer aufroymen.] — Me xonamni yig'ishtirim kerak.

🇩🇪 A2: 14-Dars: Mehmonga chaqirish va taklifnoma (Einladung)
Dustlarni rasmiy yoki norasmiy yordamga taklif qilish iboralari.

Ich lade dich zu meiner Party ein.  (Fe'l: einladen)

Aytilishi: [Ix lade dix tsu mayner parti ayn.]

Tarjimasi: Men seni o'z bazm (partiya) imga taklif qilaman.

Du am Sonntag Zeit bormi? - [Xast du am zontag tsayt?] - Yakshanba kuni vakting bormi?

Men yotishga ketyapman. — [Men yotishga ketyapman.] — John deb boraman.

🇩🇪 A2: 15-Dars: Pochta va jonatmalar (Auf der Post)
Mail orkali hat yoki posilka yuborish zharayoni.

der Brief [brif] — kulba

das Paket [paket] - posilka (zho'natma)

die Briefmarke [brifmarke] — pochta markasi

Ich möchte ein Paket nach Usbekistan schicken.

Aytilishi: [Ix myoxte ayn paket nax Usbekistan shikken.]

Tarjimasi: Men Uzbekistonga posilka yubormoqchi edim.

🇩🇪 A2: 16-Dars: Kuchada va o'yinlarda harakat (Orientierung)
Shaharda machine yoki piyoda yo'l topishning murakkabrok iboralari.

geradeaus [geradeaus] - tugriga

nach links / nach rechts [nax links / nax rexts] - chapga / o'ngga

Biegen Sie nach rechts ab.  (Fe'l:abbiegen)

Aytilishi: [Bigen Zi nax rexts ayn.]

Tarjimasi: Yong burg'ulash.

An der Kreuzung - [An der kroytsung] - Chorrahad.

🇩🇪 A2: 17-Dars: Sport va Fitness
Sport machen [sport maxen] - sport bilan shugullanmoq

joggen [joggen] - yugurish (jismonium tarbiya uchun)

sich fit halten [zix fit xalten] — o‘zini sog‘lom/formada ushlab turmoq

Ich jogge jeden Morgen, um mich fit zu halten.

Aytilishi: [Ix jogge yeden morgen, um mix fit tsu xalten.]

Tarjimasi: Ozimni soglom yugurish uchun men har tongdaaman.

🇩🇪 A2: 18-Dars: Sayohat va transport chiptalari (Reise buchen)
Train yoki airplane chipta sotib olish va malumot surash.

die Fahrkarte [farkarte] - o'l chiptasi

einfach ] - bir davr (chipta)

hin und zurück [xin und tsyuryuk] - borish va kelishga

Ich brauche eine Fahrkarte nach Myunchen hin und zurück.

Aytilishi: [Ix brauxe ayne farkarte nax Myunxen xin und tsyuryuk.]

Tarjimasi: Menga Munchenga boris wa kaitish uchun chipta kerak.

🇩🇪 A2: 19-Dars: Bog'lovchining qarshisida - “trotzdem” (Shunga karamai)
"Shunga karamai", "lekin baribir" mazmunidagi bog'lovchi. Koida: trotzdem soʻzidan keyin darhol tuslangan feʼl keladi (Tezkor tartib).

Es regnet. Trotzdem gehe ich spazieren.

Aytilishi: [Es regnet. Trotsdem ge-e ix shpatsiren.]

Tarjimasi: Yomgir yogyapti. Shunga karamai, men bunga ketyapman.

Ich bin mude. Trotzdem lerne ich. [Ix bin myude. Trotsdem lerne ix.] - Men charchaganman. Shunga karamai, o'kiyapman.

🇩🇪 A2: 20-Dars: Ikkinchi modul takrori (Wiederholung)
Javob: Gehst du heute zum Sport? [Geyst du xoyte tsum sport?] - Bugun sportga borasanmi?

B: Ich bin sehr mude. Trotzdem gehe ich zum Fitnessstudio. [Ix bin zer myude. Trotsdem ge-e ix tsum fitnesstudio.] - Juda Charchaganman. Shunga Karamay, Fitnes klubi Boraman.

Javob: Super! Viel Spaß! [Super! Fil shpas!] - Zur! Wakting chug otsin!    🇩🇪 A2: 21-Dars: Kasallik va hamdardlik bildirish (Krankheit)
Kabulida yoki kasal bulgan do'stimizga hamdardlik shifokor bildirish iboralari.

Alomat:  der Husten [xusten] - o'tal, der Schnupfen [shnupfen] - tumov, die Grippe [grippe] - gripp.

Gute Besserung! - [Gute besserung!] - Tezrok sogayib keting!

Ich fühle mich nicht gut. - [Ix fyule mix nixt gut.] - Ozimni yakhshi his kilmayapman.

🇩🇪 A2: 22-Dars: Mazhburiyatsiz tawsia - "sollten" (Konjunktiv II)
Biror kimga "Kilsangiz yaxshi bwlardi" deb maslahat yoki tavsia berganda.

sollten - kerak edi (maslahat mazmunida).

Ich sollte , du solltest , er/sie/es sollte , wir sollten .

Arzt gehen uchun solltest zum. [Dulltest tsum geen.] - Sen so'zga borsang yaxshi bwlardi.

🇩🇪 A2: 23-Dars: Davomli haraqat boglovchisi - "während" (Genitiv)
"...yotgan vaktda", "...davomida" mazmunidagi bogʻlovchi boulib, u uzidan keyin Genitiv (karatkich kelishigi) talab qiladi.

während des Urlaubs [verend des urlaubs] - ta'til yordam.

Während des Unterrichts darf man nicht sprechen.

Aytilishi: [Verend des unterrixts darf man nixt shprexen.]

Tarjimasi: Dars gapirish mumkin emas.

🇩🇪 A2: 24-Dars: Maksad bog'lovchisi — "damit" (Damit-Sätze)
Agar ikkita gapning egasi (shakhsi) hhar hil bwlsa va "maqsadida" demokchi bwlsak, damit tadqiqot (fel gap ohiriga ketadi).

Ich gebe dir Geld, damit du ein Buch kaufst.

Aytilishi: [Ix gebe dir geld, damit du ayn bux kaufst.]

Tarjimasi: Sen kitob sotib olish uchun (maqsadida) men senga pul beryapman.

🇩🇪 A2: 25-Dars: Tasdiqlovchi nisbiy olmoshlar - “dass” (Dass-Sätze)
Ozbek tilidagi "...ligini", "...ishini" mazmunini beradi (masalan: bilishini, holashini). Fel gap ohiriga boradi.

Ich weiß, dass du Deutsch lernst.

Aytilishi: [Ix vays, dass du doych lernst.]

Tarjimasi: Sen nemis tilini o'rganayotgangni bilaman.

Er sagt, dass er morgen kommt. [Er zagt, dass er morgen kommt.] - U ertag kelishini aytyapti.

🇩🇪 A2: 26-Dars: Qizi-ovkat dukonida va haridlar (Lebensmittel)
das Kilo [kilo] — kilogramm, die Flasche [flashe] — shisha (shisha), die Dose [doze] — mumkin.

Ich hätte gern ein Kilo Pomidor.

Aytilishi: [Ix xette gern ayn kilo tomaten.]

Tarjimasi: Menga bir kilo pomidor bersangiz (istradim).

🇩🇪 A2: 27-Dars: Surov va iltimos — "Könnten / Würden" (Höfliche Bitte)
Juda muloyim shaklda biror narsa iltimos kilish.

Könnten Sie mir helfen? — [Kynnten Zi mir xelfen?] — Menga yordam bera ularmidingiz?

Würden Sie bitte das Fenster schließen?

Aytilishi: [Vyrden Zi bitte das fenster shlissen?]

Tarjimasi: Iltimos, kiyimni yopib bera olasizmi?

🇩🇪 A2: 28-Dars: Uy tartib va izhara (Wohnungssuche)
die Miete [mite] - izhara xaki, die Kaltmiete [kaltmite] - kommunal twlovlarsiz toza izhara xaki, der Umzug [umtsug] - quchish.

Ich suche eine Dreizimmerwohnung. [Ix zuxe ayne draytsimmervonung.] — Men ch xonali uy qidiryapman.

🇩🇪 A2: 29-Dars: Voz kechish va rad etish - “ohne... zu”
Biror ishni "kilmasdan", "bazharmasdan" tarzida ifodalash.

Er geht keng, ohne "Tschüss" zu sagen.

Aytilishi: [Er geyt veg, ohne chyus tsu zagen.]

Tarjimasi: U "khair" demasdan chiqib ketdi.

Ich trinke Kaffee ohne Zucker zu nehmen. [Ix trinke kafee ohne tsukker tsu nemen.] - Men shakar solmasdan kofe ichaman.

🇩🇪 A2: 30-Dars: Mexnat bozori va ish vaqti (Jobsuche)
die Stellenanzeige [shtellen-antsayge] - ish e'loni, die Bewerbung [beverbung] - ishga huzhat topshirish, der Lebenslauf [lebenslauf] - xulosa (CV).

Ich muss einen Lebenslauf schreiben. [Ix mus aynen lebenslauf shrayben.] - Men resume mahsulotim kerak.

🇩🇪 A2: 31-Dars: Mehnat foydalanish va ish sharoitlari (Aritsvertrag)
der Arbeitsvertrag [arbaytsfertrag] - mehnat ishlab, das Gehalt [gexalt] - oilik maosh, die Arbeitszeit [arbayts-tsayt] - ish vakti.

Ich habe den Arbeitsvertrag unterschrieben. [Ix xabe den arbaytsfertrag untershriben.] - Men mehnat quvvatni imzoladim.

🇩🇪 A2: 32-Dars: Ortda kolgan vakt boglovchisi - “als” (Als-Sätze)
O'tmishda faqat bir marta sodir bo'lgan harakatlar uchun "qachonki...da" mazmunida (fel gap ohirida).

Als ich ein mehribon urush, wohnte ich Asakada.

Aytilishi: [Als ix ayn kind var, Asakada vonte ix.]

Tarjimasi: Men bola bulgan vaqtimda, Asakada yashaganman.

🇩🇪 A2: 33-Dars: Kaytashavanda vakt boglovchisi - “wenn” (Oʻtvan zamonda)
O'tmishda bir necha marta (doimiy) sodir bulgan harakatlar uchun "kachonki... yes" mazmunida.

Immer wenn ich Zeit hatte, las ich Bücher.

Aytilishi: [Immer ven ix tsayt xatte, las ix byuxer.]

Tarjimasi: Hhar gal vaktim bulganida, kitob o'qidim.

🇩🇪 A2: 34-Dars: Ko'plikdagi otlarning Dativ kelishigida u muzlatib
Dativ kelishigida ko'plikdagi otlarning maqolalari den b'ladi va otning ohiriga -n hharfi qo'shiladi.

die Kinder (bolalar) -> Ich helfe den Kinder n . [Ix xelfe den kindern.] — Me bolalarga yordam beraman .

die Freunde (do'stlar) -> Ich antworte den Freunde n . [Ix antvorte den froynden.] — Men do'stlarga javob beraman.

🇩🇪 A2: 35-Dars: Sabab ko'rsatuvchi predlog - “wegen” (Genitiv)
"...sababli", "...tufaili" ma'nosini beruvchi predlog bo'lib, Genitiv kelishigini talab qiladi.

wegen des Wetters [vegen des vetters] - tufayli haqida.

Wegen des Regens bleiben wir zu Hause.

Aytilishi: [Vegen des regens blayben vir tsu xauze.]

Tarjimasi: Yomgir tufayli biz uyda qolamiz.

🇩🇪 A2: 36-Dars: Uchinchi modul takrori (Wiederholung)
Javob: Umid qilamanki? [Varum bist du nixt gekommen?] - Nima uchun kelmading?

B: Wegen des Regens konnte ich emas. [Vegen des regens konnte ix nixt kommen.] — Yomg'ir tufay qalamadim.

Javob: Qani, muammo! [Ax zo, qayn muammo!] — E, tushunarli, muammo yo'q!

🇩🇪 A2: 37-Dars: Tabiat va atrof-muhit (Natur und Umwelt)
der Wald [vald] - o'rmon, der Fluss [fluss] - daryo, die Luft [luft] - xavo, schützen [shyutsen] - himoya kћlmoq.

Wir mussen die Natur schützen. [Vir myssen di natur shyutsen.] - Biz tabiatni himoya qilishimiz kerak.

🇩🇪 A2: 38-dars: OAV va Internet (Ommaviy axborot vositalari va Internet)
die Zeitung [tsaytung] — gazeta, die Nachricht [naxrixt] — yangilik, herunterladen [xerunterladen] — yuklab olmoq (skachat).

Ich lade ein Buch herunter. [Ix lade ayn bux xerunter.] — My kitob yuklab olyapman.

🇩🇪 A2: 39-Dars: Kelajak maksadlari - "werden" (Futur I)
A2 darazhasida kelajak zamon kurilmasini mustahkamlaymiz. werden 2-o'rinda tuslanadi, asosiy harakat esa o'zgarishsiz gap ohiriga boradi.

Ich werde nextes Jahr nach Berlin reisen.

Aytilishi: [Ix verde nexstes yar nax Berlin rayzen.]

Tarjimasi: Men kelasi yili Berlinga sayohat kilaman.

🇩🇪 A2: 40-Dars: Turtinchi model takrori (Wiederholung)
Javob: Wirst du morgen machen edi? [Vas virst du morgen maxen?] - Ertaga nima qilasan?

B: Ich werde Deutsch lernen, weil ich bald eine Prüfung habe. [Ix verde doych lernen, vayl ix bald ayne pryufung xabe.] — Nemis tivini o'rganaman, chunki yaqinda imtihonim bor.    🇩🇪 A2: 41-Dars: Passiv (Majhul nisbat)
Nemis tilida ish-harakatni kim bazhargani emas, beams o'sha ishning bazharilganligi mukhim bulsa, Passive (Mazhul nisbat) yuqori. Buning uchun werden fe'li tuslanadi va asosiy fe'l gaphiriga Partizip II o'tadi.

Das Auto wird repariert.

Aytish: [Avtomatik qayta tiklash.]

Tarjimasi: Tamirlanyapti mashinasi. (Kim berilganligi muhim emas)

Das Brot wird gebacken.

Aytilishi: [Das brot virt gebakken.]

Tarjimasi: Non epilyapti.

🇩🇪 A2: 42-Dars: Nisbiy olmoshlar (Relativsätze)
Ozbek tilidagi "...gan odam", "...gan buyum" yoki "kaisiki" mazmunini beradigan haplar. Bunda aniklovchi bo'lib o'tning maqolalar gap o'rtasida qo'llanma va asos haraqat (fe'l) gapning eng ohiriga boradi.

Der Mann, der dort steht, ist mein Vater.

Aytilishi: [Der man, der dort shteyt, ist mayn fater.]

Tarjimasi: Ana u erda turgan kishi mening otamdir.

Das Buch, das ich lese, ist interessant.

Aytilishi: [Das bux, das ix leze, ist interessant.]

Tarjimasi: Men o'qiyotgan kitob qizikarli.

🇩🇪 A2: 43-Dars: Muloyim taklif va istak - "Könnte" (Konjunktiv II)
Biror kimdan muloim shaklda s'rash yoki "qila olardim" deb istak bildirish uchun können modal fe'lining mahsus könnte shakli tashqi.

Ich könnte heute kommen.

Aytilishi: [Ix kynnte xoyte kommen.]

Tarjimasi: Men bugun kela olardim (beams kelarman).

Könntest du mir das Buch geben?

Aytilishi: [Kynntest du mir das bux geben?]

Tarjimasi: Menga shu kitobni bera olmaisanmi?

🇩🇪 A2: 44-Dars: Ikki qismli bog'lovchilar (Doppelkonjunktionen)
Gapda bir vaktning o'zida ikkita bog'lovchi zhuftlik bo'lib kelishuv. Bu nutkni zhuda chiroili kiladi.

nicht nur... sondern auch (nafaqat... beams ham):

Ich lerne nicht nur Deutsch, sondern auch Englisch.

Aytilishi: [Ix lerne nixt nur doych, sondern aux inglish.]

Tarjimasi: Men milliy nemis tilini, beams ingliz tilini ham o'rganyapman.

weder ... noch (on ... on):

Er hat weder Geld noch Zeit.

Aytilishi: [Er xat veder geld nox tsayt.]

Tarjimasi: O'q ustida uning, vakti bor.

🇩🇪 A2: 45-Dars: Sifat darajalari (Mustahkamlash)
A2 darazhasida sifatlarning takkoslash darazhalarini murakkabrok haplar misolida mustakamlaymiz.

schnell — schneller — am schnellsten [shnell — shneller — am shnellsten] (tez — tezroq — eng tez)

Mein Auto ist schneller als dein Auto.

Aytilishi: [Mayn auto ist schneller als dayn auto.]

Tarjimasi: Mening mashinalari sening machinesangdan kura tezrok.

Er läuft am schnellsten.

Aytilishi: [Er loyft am shnellsten.]

Tarjimasi: U hammadan tezyuradi.

🇩🇪 A2: 46-Dars: O'tgan zamon - "Plusquamperfekt"
otmishda sodir bulgan yangi harakatning biridan oldinroq bulib utganligini kursatish uchun ishlatilady. Bunda xatte yoki war + Partizip II qurilmasi islatiladi.

Nachdem ich gelernt hatte, schlief ich.

Aytilishi: [Naxdem ix gelernt xatte, shlif ix.]

Tarjimasi: Men o'qib bulganimdan keyin (birinchi harakat), biz sovutamiz (ikkinchi harakat).

🇩🇪 A2: 47-Dars: Buyruk va hizmatlardan foidalanish - "lassen" fe'li.
Biror ishni o'zimiz emas, beams usta yoki boshka odamga qildirishimizni anglatish uchun lassen (qo'yib bermok/qildirmok) feʼi tajriba.

Avtomatik qayta tiklash.

Aytilishi: [Avtomatik qayta tiklash mumkin.]

Tarjimasi: Men machinemni tamirlattiryapman (ustaga).

Ich lasse meine Haare schneiden.

Aytilishi: [Ix lasse mayne xare shnayden.]

Tarjimasi: Men sochimni oldirapman (sartaroshga).

🇩🇪 A2: 48-Dars: Ozlik fellari va Dativ kelishigi
Agar o'zlik harakatī biror anik ěazoga tagishli bwlsa, sich olmoshi Akkusativdan Dativ shakliga ( mir, dir ) o'tadi.

Men mich edim. [Ix vashe mix.] — My yuvinyopman. (Akkusativ)

Ich wasche mir die Hände.

Aytilishi: [Ix vashe mir di xende.]

Tarjimasi: Men qullarimni yuväpman. (Dative - chunki "qullarimni" so'zi bor)

🇩🇪 A2: 49-Dars: Telefon orqali shoshilinch xabarlar (Notfall)
Muammo yoki favqulodda qurilmada qo'ng'iroq qilib yordam chaqirish iboralari.

Es ist ein Notfall!

Aytilishi: [Es ist ayn notfall!]

Tarjimasi: Bu favqulodda vaziyat (baxtsiz hodisa)!

Rufen Sie bitte die Polizei!

Aytilishi: [Rufen Zi bitte di politsay!]

Tarjimasi: Iltimos, politsiyachilar chaqirishadi!

Ich brauche einen Krankenwagen.

Aytilishi: [Ix brauxe aynen krankenvagen.]

Tarjimasi: Menga tez yordam mashinasi kerak.

🇩🇪 A2: 50-Dars: Turtinchi model takrori (Wiederholung)
Ush blokdagi Passive va o'zlik fellarini amaliy mulokotda tekshiramiz.

Javob: Avtomatik nima? [Vo ist dayn auto?] - Mashinang qani?

B: Werkstatt reparantida es wird gerade. [Es virt gerade in der verkshatt repariert.] - U hozir ustahonada tamirlanyapti.

A: Ach so, yordaming kerakmi? [Ax zo, musst du lange warten?] - E ha, uzok tekshirish kerakmi?

B: Nein, morgen ist es fertig. [Nayn, morgen ist es fertig.] - Ywk, ertaga tayer b'ladi.

🇩🇪 A2: 51-Dars: Rasmiy hujjatlar bilan ishlash (Formulare)
Germanyda davlat idoralari yoki banklarda profil to'ldirishda murakkabrok atamalar.

die Steuernummer [shtoyernummer] - Soliq to'lovchining identifikatsiya raqami (TIN)

der Familienstand [familienstand] - oila aholisi

die Postleitzahl (PLZ) [postlayttsal] — pochta indekslari

Füllen Sie das Formular aus, bitte.

Aytilishi: [Fyllen Zi das formulalar aus, bitte.]

Tarjimasi: Iltimos, ushbu anketa twldiring.

🇩🇪 A2: 52-Dars: Rasmiy shikoyat xati (Beschwerdebrief)
Agar sotib olingan buyum yoki hizmat sifati emon bulsa, rasmiy norosilik xati buyurtma koidasi.

Sehr geehrte Damen und Herren, [Zer geerte damen und xerren] — Hurmatli xonimlar va janoblar.

Ich bin mit dem Service nicht zufrieden.

Aytilishi: [Ix bin mit dem servis nixt tsufriden.]

Tarjimasi: Men k o' tish hizmatdan ko'nikmadim (noroziman).

Mit freundlichen Grüßen [Mit froyndlixen gryusen] - Samimiy xurmat ila.

🇩🇪 A2: 53-Dars: Do'stga xat yuborish (E-Mail va einen Freund)
Do'stlarni kunga taklif qilish yoki hol-avol so'rab hatilgan.

Liber Anvar, [Liber Anvar] - Azizim Anvar,

Qanday bo'lmasin? Ich lade dich zu mir ein.

Aytilishi: [Vi geyt es dir? Ix lade dix tsu mir ayn.]

Tarjimasi: Ishlaring qayla? Men seni ozimnikiga (mehmonga) taklif qilaman.

Schreib mir kal! Viele Grüße.

Aytilishi: [Shrayb mir kal! Fayl dahshatli.]

Tarjimasi: Tez orada menga yozib yubor! Ko'plab salomlar bilan.

🇩🇪 A2: 54-Dars: Jamoat transportida o'nalish so'rash (Verkehr)
Bat bekatlarida va stationlarda adashib kolganda kerak buladigan zhonli iboralar.

Welcher Bus Zentrum zummi?

Aytilishi: [Velxer bus fert tsum tsentrum?]

Tarjimasi: Avtobus markazga boradi-chi?

Wo muss ich umsteigen?

Aytilishi: [Vo muss ix umshtaygen?]

Tarjimasi: Men kaerda boshka transporta o'tirishim (transfer qilishim) kerak?

Der Zug shlyapa 10 Minuten Verspätung.

Aytilishi: [Der tsug xat tsen minuten fershpetung.]

Tarjimasi: Poyezd 10 daqiqaga ketyapti.

🇩🇪 A2: 55-Dars: Sog'lik va sog'lom turmush tarzi (Gesundheit)
Soglom yashash koidalari, sport va tugri ovkatlanish mavzusi.

Ich ernähre mich gesund.

Aytilishi: [Ix er-nere mix gezund.]

Tarjimasi: Men soglom ovkatlanyapman.

Man muss täglich Wasser trinken.

Aytilishi: [Man muss teglix vasser trinken.]

Tarjimasi: Inson har kuni suv ichishi kerak.

Obst und Gemüse [obst und gemyuze] - mevalar va yordam.

🇩🇪 A2: 56-Dars: Kelasi zamon - Futur I (Mustahkamlash)
Kelazhakdagi qatii rezhalarni ifodalash qurilmasini tulik takrorlash.

Ich werde morgen die Prüfung machen.

Aytilishi: [Ix verde morgen di pryufung maxen.]

Tarjimasi: Men ertaga imtikxon topshiraman.

Wirst du am Wochenende tun edi?

Aytilishi: [Vas virst du am voxenende tun?]

Tarjimasi: Dam olish kunlari nima ish qilasan?

🇩🇪 A2: 57-Dars: A2 darazhasining eng mukhim 50 ta fe'li (Top Verben)
A2 darazhasida eng kwp islatiladigan kuchli fe'llar ruyhati.

anbieten [anbiten] - taklif qilmoq

entscheiden [entshayden] - karor kabul qilmoq

verstehen [fershteen] - tushunmoq

empfehlen [empfelen] - tavsia kilmoq

Ich empfehle dir dieses Buch. [Ix empfele dir dizes bux.] - Men senga ushbu kitobni tavsia kilaman.

🇩🇪 A2: 58-Dars: A2 imtihon sirlari – Xören (Tinglash)
Imtihonning audio eshitib, tugri zhavobni topish qismi uchun strategiya.

Maslahat: Eshitmasdan oldin savol raqamlari, wakt va zhoy nom tagiga chizib oling.

Tuzoqlar: Agar audioda birinchi marta bir fikr itilib, keyin "aber" (lekin) bilan inkor qilinsa, "aber"dan keyingi fikr tugri bo'ldi.

🇩🇪 A2: 59-Dars: A2 imtihon sirlari – Sprechen (Gapirish)
Ozaki imtihonda yukori ball olish usullari.

1-qism: Ozi xakida joydaroq gapirish (A1 ga qaraganda murakkabrok haplar bilan).

2-qism: Sherigi bilan bir xil rezha (Masalan: birlashgan kasal destni borib kurish rezhasi). Bunda "Wollen wir..." yoki "Ich schlage vor..." (Men taklif qilaman) iboralari islatiladi.

🇩🇪 A2: 60-Dars: A2 yakuniy imtihoni (Yakuniy test)
Butun A2 kursini (1-dan 59-gacha bo'lgan darslarni) mustahkamlovchi katta yakuniy test imtihoni.

Eslatma: Ush imtihondan o'tgan o'tuvchilarga keyingi - B1 (Orta) darazhasi eshiklari ochiladi!
"""

A2_LESSONS = {}
parts = re.split(r'(🇩🇪 A2: \d+-Dars:|🇩🇪 A2: \d+-dars:)', text)
for i in range(1, len(parts), 2):
    header = parts[i]
    content = parts[i+1].strip()
    match = re.search(r'🇩🇪 A2: (\d+)-(D|d)ars:', header)
    if match:
        lesson_num = int(match.group(1))
        A2_LESSONS[str(lesson_num)] = "📖 **" + header.replace("🇩🇪 A2: ", "") + "**\n\n" + content

with open(os.path.join(os.path.dirname(__file__), 'website', 'a2_lessons.py'), 'w', encoding='utf-8') as f:
    f.write('A2_LESSONS = ' + json.dumps(A2_LESSONS, ensure_ascii=False, indent=4))
