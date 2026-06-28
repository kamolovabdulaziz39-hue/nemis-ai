import json
import re
import os
import sys

text = """🇩🇪 1-Dars: Salomlashish va tanishuv (Begrüßung und Kennenlernen)
Nemis tilida vaziyatga qarab rasmiy va norasmiy salomlashish shakllari mavjud.

Hallo! — [Xallo!] — Salom! (Do‘stona)

Guten Tag! — [Guten Tag!] — Kun xayr! / Assalomu alaykum! (Rasmiy)

Guten Morgen! — [Guten Morgen!] — Hayrli tong!

Guten Abend! — [Guten Abend!] — Hayrli kech!

Ism so‘rash:
Wie heißt du? — [Vi xayst du?] — Sening isming nima?

Ich heiße Anvar. — [Ix xayse Anvar.] — Mening ismim Anvar.

Wie heißen Sie? — [Vi xaysen Zi?] — Sizning ismingis nima? (Rasmiy)

Xayrlashish:
Tschüss! — [Chyus!] — Xayr! (Do‘stona)

Auf Wiedersehen! — [Auf viderzeen!] — Xayr! / Salomat bo‘ling! (Rasmiy)

🇩🇪 2-Dars: Nemis tili alifbosi va o‘qish qoidalari (Das Alphabet)
Nemis tilida maxsus harflar va unli/undosh birikmalari mavjud.

Maxsus harflar (Umlaut va Eszett):
Ä ä — [E] kabi o‘qiladi. Mädchen [Medxen] — qiz bola.

Ö ö — [Yo] kabi yumshoq o‘qiladi. schön [shyon] — go‘zal.

Ü ü — [Yu] kabi yumshoq o‘qiladi. tschüss [chyus] — xayr.

ß — [ss] kabi o‘qiladi. heißen [xaysen] — nomlanmoq.

Unli va undosh birikmalari:
ei — [Ay] deb o‘qiladi: Nein [Nayn] — Yo‘q.

eu — [Oy] deb o‘qiladi: Euro [Oyro] — Yevro.

sch — [Sh] deb o‘qiladi: Schule [Shule] — Maktab.

st / sp — so‘z boshida [Sht / Shp] deb o‘qiladi: Straße [Shtrasse] — Ko‘cha.

🇩🇪 3-Dars: 0 dan 20 gacha sanash (Zahlen von 0 bis 20)
Asosiy sonlarni yodlash keyingi darslar uchun poydevor bo‘ladi.

0 - null [null], 1 - eins [ayns], 2 - zwei [svay], 3 - drei [dray], 4 - vier [fir], 5 - fünf [fynf]

6 - sechs [zeks], 7 - sieben [ziben], 8 - acht [axt], 9 - neun [noyn], 10 - zehn [tsen]

11 - elf [elf], 12 - zwölf [svolf]

13 dan 19 gacha sonlar (-zehn qo‘shimchasi bilan):
13 - dreizehn [draytsen], 14 - vierzehn [firtsen], 15 - fünfzehn [fynftsen]

16 - sechzehn [zextsen], 17 - siebzehn [zibtsen], 18 - achtzehn [axttsen], 19 - neunzehn [noyntsen]

20 - zwanzig [svansix]

🇩🇪 4-Dars: Shaxsiy olmoshlar (Personalpronomen)
Gap tuzishda kim haqida gapirilayotganini ifodalash uchun ishlatiladi.

ich — [ix] — men

du — [du] — sen

er — [er] — u (erkak)

sie — [zi] — u (ayol)

es — [es] — u (o‘rta jins)

wir — [vir] — biz

ihr — [ir] — sizlar

sie — [zi] — ular

Sie — [Zi] — Siz (hurmat ma'nosida, har doim katta harfda)

🇩🇪 5-Dars: Eng muhim fe'l — "sein" (bo‘lmoq) fe’li
Nemis tilida "Men talabaman" yoki "U chiroyli" deyish uchun sein fe'li shaxslarga qarab tuslanadi.

ich bin — [ix bin] — men ...-man

du bist — [du bist] — sen ...-san

er/sie/es ist — [er/zi/es ist] — u ...-dir

wir sind — [vir zind] — biz ...-miz

ihr seid — [ir zayd] — sizlar ...-sizlar

sie/Sie sind — [zi/Zi zind] — ular ...-lar / Siz ...-siz

Misol: Ich bin o‘quvchi. [Ix bin student.] — Men talabaman.

🇩🇪 6-Dars: Davlatlar va tillar (Länder und Sprachen)
Qayerdan ekanligimizni aytish va sprechen (gapirmoq) fe'lini o‘rganamiz.

Woher kommst du? — [Voxer komst du?] — Sen qayerdansan?

Ich komme aus Usbekistan. — [Ix komme aus Usbekistan.] — Men O‘zbekistondanman.

Ich spreche Usbekisch. — [Ix shprexe usbekish.] — Men o‘zbekcha gapiraman.

Sprechen Sie Deutsch? — [Shprexen Zi doych?] — Nemischa gapirasizmi?

🇩🇪 7-Dars: Ikkinchi muhim fe'l — "haben" (bormoq/ega bo‘lmoq)
"Mening ... bor" degan gaplar nemis tilida haben (ega bo‘lmoq) fe'li orqali aytiladi.

ich habe — [ix xabe] — menda bor

du hast — [du xast] — senda bor

er/sie/es hat — [er/zi/es xat] — unda bor

wir haben — [vir xaben] — bizda bor

ihr habt — [ir xabt] — sizlarda bor

sie/Sie haben — [zi/Zi xaben] — ularda bor / Sizda bor

Misol: Ich habe Zeit. [Ix xabe tsayt.] — Mening vaqtim bor.

🇩🇪 8-Dars: Oddiy fe'llarning hozirgi zamonda tuslanishi (Präsens)
Oddiy fe'llarni tuslash uchun ularning oxiridagi -en olib tashlanadi va quyidagi shaxs qo‘shimchalari qo‘shiladi:

ich -> -e (ich lerne)

du -> -st (du lernst)

er/sie/es -> -t (er lernt)

wir -> -en (wir lernen)

ihr -> -t (ihr lernt)

sie/Sie -> -en (sie lernen)

Fe'l: lernen [lernen] — o‘rganmoq.

🇩🇪 9-Dars: Inkor formasi — "nicht" va "kein" (Negation)
kein — faqat oldida artikli bor yoki artiklsiz keladigan otlarni inkor qiladi.

Ich habe kein Auto. [Ix xabe kayn auto.] — Mening mashinam yo‘q.

nicht — fe'l, sifat, ism yoki joy nomlarini inkor qiladi.

Ich rauche nicht. [Ix rauxe nixt.] — Men chekmayman.

🇩🇪 10-Dars: Nemis tilida gap tuzish tartibi (Satzbau)
Nemis tilida oddiy darak gaplarda fe'l har doim 2-o‘rinda turishi shart!

To‘g‘ri tartib: Ich (1) lerne (2) Deutsch (3). — Men nemis tilini o‘rganyapman.

Teskari tartib: Heute (1) lerne (2) ich (3) Deutsch (4). — Bugun men nemis tilini o‘rganyapman.

🇩🇪 11-Dars: So‘roq gaplar tuzish (W-Fragen va Ja/Nein Fragen)
1. W-Fragen (Maxsus so‘roq): So‘roq so‘z 1-o‘rinda, fe'l esa 2-o‘rinda turadi.

Was machst du? [Vas maxst du?] — Nima qilyapsan?

2. Ja/Nein Fragen (Umumiy so‘roq): So‘roq so‘zi bo‘lmasa, fe'l 1-o‘ringa chiqadi.

Wohnst du hier? [Vonst du xir?] — Shu yerda yashaysanmi?

🇩🇪 12-Dars: Modulni takrorlash va mini-test (Wiederholung)
O‘tilgan 11 ta darsdagi asosiy iboralarni muloqot orqali mustahkamlash:

A: Hallo! Wie bist du? — [Xallo! Vi bist du?] — Salom! Qalaysan?

B: Danke, gut. Ich lerne Deutsch. Und du? — [Danke, gut. Ix lerne doych. Und du?] — Rahmat, yaxshi. Men nemischa o‘rganyapman. Senda-chi?

A: Ich spreche schon Englisch. — [Ix shprexe shon inglish.] — Men allaqachon inglizcha gapiraman.

🇩🇪 13-Dars: Oila va qarindoshlar (Meine Familie)
Oila a'zolarining artikllar bilan nomlanishi:

die Familie [di familie] — oila

der Vater [der fater] — ota

die Mutter [di mutter] — ona

der Bruder [der bruder] — aka/uka

die Schwester [di shvester] — opa/singil

Das ist mein Vater. [Das ist mayn fater.] — Bu mening otam.

🇩🇪 14-Dars: Egalik olmoshlari (Possessivpronomen)
Mening, sening kabi egalik so‘zlari keyingi kelayotgan so‘z ayol jinsida yoki ko‘plikda bo‘lsa, oxiriga -e oladi.

mein / meine — mening

dein / deine — sening

sein / seine — uning (erkak)

ihr / ihre — uning (ayol)

Das ist mein Buch. [Das ist mayn bux.] — Bu mening kitobim.

Das ist meine Lampe. [Das ist mayne lampe.] — Bu mening chirog‘im.

🇩🇪 15-Dars: Kasblar va ish joyi (Berufe und Arbeitsplatz)
Ayol kishining kasbini aytganda erkaklar kasbi oxiriga -in qo‘shiladi. Kasb oldidan artikl ishlatilmaydi.

der Lehrer / die Lehrerin [lerer / lererin] — o‘qituvchi

der Programmierer [programmirer] — dasturchi

Was bist du von Beruf? [Vas bist du fon beruf?] — Kasbing nima?

Ich bin Programmierer. [Ix bin programmirer.] — Men dasturchiman.

🇩🇪 16-Dars: Artikllar bilan tanishuv (der, die, das)
Nemis tilida har bir ot o‘z jinsiga ega:

der — Erkak jinsi (der Tisch — stol)

die — Ayol jinsi (die Tasche — sumka)

das — O‘rta jins (das Auto — mashina)

die (Plural) — Barcha so‘zlarning ko‘plik shakli uchun umumiy artikl.

🇩🇪 17-Dars: Noaniq artikl va uning ishlatilishi (ein, eine)
Narsa haqida birinchi marta gapirganda noaniq artikl ishlatiladi.

der -> ein (Das ist ein Tisch)

das -> ein (Das ist ein Auto)

die -> eine (Das ist eine Tasche)

Ko‘plik shaklida noaniq artikl ishlatilmaydi.

🇩🇪 18-Dars: 20 dan boshlab katta sonlar (Zahlen ab 20)
Nemis tilida avval birlik, keyin "va" (und), so‘ng o‘nlik aytiladi.

21 — einundzwanzig [ayn-und-svansix] (bir va yigirma)

25 — fünfundzwanzig [fynf-und-svansix] (besh va yigirma)

30 — dreißig [draysix], 40 - vierzig [firtsix], 50 - fünfzig [fynftsix], 100 - hundert [hundert]

🇩🇪 19-Dars: Mening kun tartibim (Mein Tagesablauf)
Kun davomida bajariladigan asosiy harakatlar:

aufstehen [aufsteen] — o‘rindan turmoq

frühstücken [fryushtyuken] — nonushta qilmoq

arbeiten [arbayten] — ishlamoq

Ich stehe um 7 Uhr auf. [Ix shte-e um ziben ur auf.] — Men soat 7 da turaman.

🇩🇪 20-Dars: Ajraladigan old qo‘shimchali fe’llar (Trennbare Verben)
Bunday fe'llarning old qo‘shimchasi gap oxiriga boradi, fe'lning o‘zi esa 2-o‘rinda tuslanadi.

einkaufen (bozorlik qilmoq) -> Old qo‘shimcha: ein

anrufen (telefon qilmoq) -> Old qo‘shimcha: an

Gap: Ich kaufe bugun ein. [Ix kaufe xoyte ayn.] — Men bugun bozorlik qilyapman.

🇩🇪 21-Dars: Hafta kunlari, oylar va fasllar (Wochentage, Monate, Jahreszeiten)
Hafta kunlari oldidan har doim am, oylar va fasllar oldidan esa im predlogi ishlatiladi.

Montag [montag] — Dushanba, Samstag [zamstag] — Shanba, Sonntag [zontag] — Yakshanba.

Am Montag arbeite ich. [Am montag arbayte ix.] — Dushanba kuni men ishlayman.

der Sommer [zommer] — yoz, der Winter [vinter] — qish.

Im Sommer ist es heiß. [Im zommer ist es xays.] — Yozda havo issiq bo‘ladi.

🇩🇪 22-Dars: Vaqtni so‘rash va aytish (Uhrzeit)
Soatni so‘rash va daqiqalarni to‘g‘ri aytish.

Wie spät ist es? — [Vi shpet ist es?] — Soat necha bo‘ldi?

Es ist zwei Uhr. — [Es ist svay ur.] — Soat ikki.

nach (o‘tdi) / vor (gacha/bor):

Es ist fünf nach zwei. [Es ist fynf nax svay.] — Ikkidan 5 daqiqa o‘tdi.

Es ist halb drei. [Es ist xalb dray.] — Soat ikki yarim (uchga yarim soat qoldi).

🇩🇪 23-Dars: O‘zgaruvchan o‘zakli fe’llar (Unregelmäßige Verben)
Ba'zi fe'llar du va er/sie/es shaxslarida tuslanganda o‘zakdagi unli harf o‘zgaradi.

geben (bermoq) -> Ich gebe, lekin: du gibst, er gibt.

fahren (transportda yurmoq) -> Ich fahren, lekin: du fährst, er fährt.

Fährst du nach Hause? [Ferst du nax xauze?] — Sen uyga ketyapsanmi?

🇩🇪 24-Dars: Ikkinchi modul takrorlovi (Wiederholung)
O‘tilgan darslarni jonli muloqot orqali mustahkamlash:

A: Was bist du von Beruf? — [Vas bist du fon beruf?] — Kasbing nima?

B: Ich bin Programmierer. Ich arbeite am Montag. — [Ix bin programmirer. Ix arbayte am montag.] — Men dasturchiman. Dushanba kuni ishlayman.

A: Wie spät ist es? — [Vi shpet ist es?] — Soat necha bo‘ldi?

B: Es ist halb drei. — [Es ist xalb dray.] — Soat ikki yarim.

🇩🇪 25-Dars: Tushum kelishigi (Akkusativ)
O‘zbek tilidagi tushum kelishigi (kimni?, nimani?). Akkusativda faqat erkak jinsidagi (der) artikllar o‘zgaradi.

der -> den (noaniq: einen / inkor: keinen)

das -> das / die -> die (ayol va o‘rta jins o‘zgarmaydi).

Ich esse einen Apfel. [Ix esse aynen apfel.] — Men olma (nimani?) yeyapman. (der Apfel)

🇩🇪 26-Dars: Oziq-ovqatlar va ichimliklar (Essen und Trinken)
Kundalik yeguliklar va ular bilan Akkusativ kelishigini qo‘llash.

das Brot [brot] — non, der Käse [keze] — pishloq, der Tee [tee] — choy.

Ich trinke einen Tee. [Ix trinke aynen tee.] — Men choy ichyapman.

Wir kaufen Brot. [Vir kaufenh brot.] — Biz non sotib bilyapman.

🇩🇪 27-Dars: Restoran va kafeda buyurtma berish (Im Restaurant)
Die Speisekarte, bitte! — [Di shpayzekarte, bitte!] — Menyuni bersangiz, iltimos!

Ich möchte... — [Ix myoxte...] — Men ... istardim.

Die Rechnung, bitte! — [Di rexnung, bitte!] — Hisobni keltirsangiz, iltimos!

Zusammen oder getrennt? — [Zuzammen oder getrennt?] — Birgami yoki alohida?

🇩🇪 28-Dars: Modal fe’llar: "können" va "müssen"
Modal fe'l gapda 2-o‘rinda tuslanadi, asosiy fe'l esa gap oxiriga o‘zgarishsiz (infinitiv) o‘tadi.

können (bila olmoq): Ich kann Deutsch sprechen. [Ix kann doych shprexen.] — Men nemischa gapira olaman.

müssen (majbur bo‘lmoq): Ich muss heute arbeiten. [Ix muss xoyte arbayten.] — Men bugun ishlashim kerak.

🇩🇪 29-Dars: Modal fe’llar: "wollen" va "möchten"
wollen (qat'iy xohlamoq): Ich will nach Deutschland fahren. [Ix vill nax doychland fahren.] — Men Germaniyaga bormoqchiman.

möchten (istamoq - muloyim shakli): Möchten Sie Kaffee trinken? [Myoxten Zi kafee trinken?] — Kofe ichishni istaysizmi?

🇩🇪 30-Dars: Mening uyim va xonadonim (Meine Wohnung)
Uy va xonalar nomlanishi:

das Haus [xaus] — uy, die Wohnung [vonung] — xonadon (kvartira).

die Küche [kyuxe] — oshxona, das Bad [bad] — yuvinish xonasi, das Zimmer [tsimmer] — xona.

Meine Wohnung ist groß. [Mayne vonung ist gros.] — Mening xonadonim katta.

🇩🇪 31-Dars: Mebel va uy jihozlari (Möbel)
der Tisch [tish] — stol, der Stuhl [shtul] — stul, der Schrank [shrank] — shkaf, das Bett [bett] — krovat.

Der Schrank ist neu. [Der shrank ist noy.] — Shkaf yangi.

Ich kaufe ein Sofa. [Ix kaufe ayn sofa.] — Men divan sotib bilyapman.

🇩🇪 32-Dars: Ranglar va sifatlar (Farben und Adjektive)
weiß [vays] — oq, schwarz [shvarts] — qora, rot [rot] — qizil.

groß [gros] — katta, klein [klayn] — kichik, neu [noy] — yangi.

Das Auto ist rot und neu. [Das auto ist rot und noy.] — Mashina qizil va yangi.

🇩🇪 33-Dars: Joylashuvni so‘rash va shahar bo‘ylab sayohat (In der Stadt)
Shaharda adashib qolmaslik, kerakli binolarni topish va yo‘l so‘rash iboralari.

Shahardagi muhim joylar:
die Bank [bank] — bank

der Bahnhof [banxof] — vokzal

das Hotel [xotel] — mehmonxona

die Apotheke [apoteke] — dorixona

die Post [post] — pochta

Yo‘l so‘rash iboralari:
Entschuldigung, wo ist der Bahnhof?

Aytilishi: [Entshuldigung, vo ist der banxof?]

Tarjimasi: Kechirasiz, vokzal qayerda?

Das ist hier in der Nähe.

Aytilishi: [Das ist xir in der ne-e.]

Tarjimasi: Bu shu yaqin atrofda.

🇩🇪 34-Dars: Kelishiklar: Jo‘nalish va o‘rin-joy kelishigi (Dativ)
O‘zbek tilidagi jo‘nalish (kimga?, nimaga?) va o‘rin-joy (kimda?, qayerda?) kelishiklari nemis tilida Dativ deyiladi. Dativ kelishigida barcha artikllar butunlay o‘zgaradi.

Artikllarning Dativda o‘zgarishi:
der (erkak) -> dem bo‘ladi | ein -> einem bo‘ladi

das (o‘rta) -> dem bo‘ladi | ein -> einem bo‘ladi

die (ayol) -> der bo‘ladi | eine -> einer bo‘ladi

die (ko‘plik) -> den bo‘ladi va otning oxiriga -n harfi qo‘shiladi.

Amaliy misollar:
Ich helfe dem Vater. (Vater aslida "der", Dativda "dem" bo‘ldi, chunki helfen fe'li Dativ talab qiladi)

Aytilishi: [Ix xelfe dem fater.]

Tarjimasi: Men otamga yordam beryapman.

Ich bin in der Schule. (Schule aslida "die", Dativda "der" bo‘ldi)

Aytilishi: [Ix bin in der shule.]

Tarjimasi: Men maktabdaman (qayerdaman?).

🇩🇪 35-Dars: Buyruq mayli (Imperativ)
Suhbatdoshga buyruq berish, iltimos qilish yoki taklif kiritish shakli. A1 darajasida do‘stona (du) va rasmiy (Sie) shakllarini o‘rganamiz.

1. Rasmiy shakli (Siz uchun):
Fe'l birinchi o‘ringa chiqadi va yoniga "Sie" qo‘yiladi.

Kommen Sie bitte! [Kommen Zi bitte!] — Keling, iltimos!

Lesen Sie das! [Lezen Zi das!] — Shuni o‘qing!

2. Do‘stona shakli (Sen uchun):
Fe'lning oxiridagi -en olib tashlanadi va "du" olmoshi gapda ishlatilmaydi.

Komm! [Komm!] — Kel! (Kommen fe'lidan)

Lies! [Lis!] — O‘qi! (Lesen fe'lidan, o‘zgaruvchan fe'l qoidasiga ko‘ra)

🇩🇪 36-Dars: Uchinchi modul takrorlovi va lug‘at testi (Wiederholung)
Ushbu modulda o‘rganilgan Dativ, Akkusativ va modal fe'llarni muloqot orqali mustahkamlaymiz.

Amaliy muloqot:
A: Entschuldigung, ich suche ein Hotel. Kannst du mir helfen? [Entshuldigung, ix zuxe ayn xotel. Kannst du mir xelfen?] — Kechirasiz, men mehmonxona qidiryapman. Menga yordam bera olasanmi?

B: Ja, gerne. Das Hotel ist dort, neben dem Bahnhof. [Ya, gerne. Das xotel ist dort, neben dem banxof.] — Ha, jon deb. Mehmonxona anavi yerda, vokzalning yonida.

A: Vielen Dank! Ich muss auch einen Kaffee trinken. Gibt es hier ein Café? [Filen dank! Ix muss aux aynen kafee trinken. Gibt es xir ayn kafe?] — Katta rahmat! Men kofe ham ichishim kerak. Bu yerda kafe bormi?

B: Ja, geh geradeaus. Dort ist ein schönes Café. [Ya, ge geradeaus. Dort ist ayn shyones kafe.] — Ha, to‘g‘riga yur. Anavi yerda chiroyli kafe bor.

🇩🇪 37-Dars: Xobbi va bo‘sh vaqt (Hobbys und Freizeit)
Ushbu darsda biz bo‘sh vaqtimizda nimalar bilan shug‘ullanishimiz, qiziqishlarimiz va sevimli mashg‘ulotlarimiz haqida gapirishni o‘rganamiz.

Qiziqishlar va xobbilar (Hobbys):
Fußball spielen — [fusbal shpilen] — futbol o‘ynamoq

Bücher lesen — [byuxer lezen] — kitoblar o‘qimoq

Musik hören — [muzik xoren] — muzika tinglamoq

Schwimmen — [shvimmen] — suzmoq

Reisen — [rayzen] — sayohat qilmoq

Gaplarda qo‘llanilishi (Misollar):
Was ist dein Hobby?

Aytilishi: [Vas ist dayn xobbi?]

Tarjimasi: Sening xobbing nima?

Mein Hobby ist Reisen.

Aytilishi: [Mayn xobbi ist rayzen.]

Tarjimasi: Mening xobbiym sayohat qilish.

In meiner Freizeit spiele ich Fußball.

Aytilishi: [In mayner fraytsayt shpile ix fusbal.]

Tarjimasi: Bo‘sh vaqtimda men futbol o‘ynayman.

🇩🇪 38-Dars: Do‘stlar bilan uchrashuv belgilash (Verabredung)
Do‘stlarni biror joyga taklif qilish, uchrashuv vaqti va joyini kelishib olish uchun kerak bo‘ladigan jonli iboralar.

Taklif qilish va kelishish iboralari:
Hast du am Samstag Zeit? — [Xast du am zamstag tsayt?] — Shanba kuni vaqting bormi?

Wollen wir ins Kino gehen? — [Vollen vir ins kino geen?] — Kinoga boramizni?

Ja, das ist eine gute Idee. — [Ya, das ist ayne gute idee.] — Ha, bu yaxshi g‘oya.

Wann treffen wir uns? — [Van treffen vir uns?] — Qachon uchrashamiz?

Um wie viel Uhr? — [Um vi fil ur?] — Soat nechchida?

Treffen wir uns um 18 Uhr vor dem Kino. — [Treffen vir uns um axtsen ur vor dem kino.] — Soat 18:00 da kino teatri oldida uchrashamiz.

🇩🇪 39-Dars: Ob-havo va iqlim (Das Wetter)
Tabiat hodisalari, ob-havoni tasvirlash va harorat haqida gapirish. Nemis tilida ob-havo har doim shaxssiz es olmoshi bilan aytiladi.

Ob-havo iboralari:
Wie ist das Wetter heute? — [Vi ist das vetter xoyte?] — Bugun ob-havo qanday?

Es ist kalt. — [Es ist kalt.] — Havo sovuq.

Es ist warm / heiß. — [Es ist varm / xays.] — Havo iliq / issiq.

Die Sonne scheint. — [Di zonne shaynt.] — Quyosh charoqlayapti.

Es regnet. — [Es regnet.] — Yovg‘ir yog‘yapti.

Es schneit. — [Es shnayt.] — Qor yog‘yapti.

Wie viel Grad es es? — [Vi fil grad ist es?] — Havo necha daraja?

Es sind 25 Grad. — [Es zind finf und svansix grad.] — Havo 25 daraja issiq.

🇩🇪 40-Dars: Kiyim-kechaklar va xaridlar (Kleidung und Einkaufen)
Do‘konda kiyim sotib olish, o‘lcham va ranglarni so‘rash, kiyimlarning nemischa nomlanishi.

Kiyimlar ro‘yxati:
der Mantel [mantel] — palto

die Hose [xoze] — shim

das Hemd [xemd] — ko‘ylak (erkaklar)

die T-Shirt [ti-shirt] — futbolka

die Schuhe [shue] — poyabzal (har doim ko‘plikda)

Do‘kondagi muloqot:
Ich suche eine Hose. (Hose ayol jinsida, Akkusativda "eine" bo‘lib qoladi)

Aytilishi: [Ix zuxe ayne xoze.]

Tarjimasi: Men shim qidiryapman.

Welche Größe brauche du?

Aytilishi: [Velxe grose brauxen du?]

Tarjimasi: Senga qaysi o‘lcham kerak?

Größe M, bitte. — [Grose em, bitte.] — M o‘lcham, iltimos.

🇩🇪 41-Dars: Tana a’zolari (Der menschliche Körper)
Inson tanasining asosiy qismlari. Bu mavzu keyingi darsda shifokor qabulida qayerimiz og‘riyotganini tushuntirish uchun juda kerak bo‘ladi.

Tana a'zolari:
der Kopf [kopf] — bosh

das Auge / die Augen [auge / augen] — ko‘z / ko‘zlar

der Ohr / die Ohren [or / oren] — quloq / quloqlar

der Mund [mund] — og‘iz

die Hand / die Hände [xand / xende] — qo‘l (kaft qismi)

das Bein / die Beine [bayn / bayne] — oyoq

🇩🇪 42-Dars: Shifokor qabulida: Salomatlik (Beim Arzt)
Kasallik belgilari, shifokorga muammoni aytish va tibbiy iboralar. Nemis tilida "Mening ... og‘riyapti" deyish uchun ...schmerzen (og‘riqlar) so‘zi ishlatiladi.

Muhim iboralar:
Ich bin krank. — [Ix bin krank.] — Men kasalman.

Ich habe Kopfschmerzen.

Aytilishi: [Ix xabe kopfshmertsene.]

Tarjimasi: Mening boshim og‘riyapti.

Ich habe Halsschmerzen.

Aytilishi: [Ix xabe xalsshmertsene.]

Tarjimasi: Mening tomog‘im og‘riyapti.

Ich habe Fieber. — [Ix xabe fiber.] — Mening isitmam bor.

Was fehlt Ihnen? — [Vas felt Inen?] — Sizni nima bezovta qilyapti? (Shifokor so‘raydi)

Sie müssen im Bett bleiben. — [Zi myssen im bett blayben.] — Siz yotoqda qolishingiz (yotishingiz) shart.

🇩🇪 43-Dars: O‘tgan zamon bilan tanishuv: Perfekt
Nemis tilida so‘zlashuvda (og‘zaki nutqda) o‘tgan zamon haqida gapirish uchun asosan Perfekt zamon shakli ishlatiladi. Perfekt murakkab zamon hisoblanadi, ya’ni u ikkita fe'ldan tashkil topadi:

Yordamchi fe'l: Gapda 2-o‘rinda haben yoki sein fe'li shaxsga qarab tuslanadi (o‘zi tarjima qilinmaydi).

Asosiy fe'l: Gapning eng oxiriga Partizip II (o‘tgan zamon sifatdoshi) shaklida o‘zgarishsiz o‘tadi. Asosiy fe'llarning oldiga ko‘pincha ge- qo‘shimchasi qo‘shiladi (Masalan: machen -> gemacht).

Oltin qoida: Agar harakat bir joydan ikkinchi joyga ko‘chish (harakatlanish) bo‘lsa yordamchi fe'l sifatida sein ishlatiladi. Qolgan deyarli barcha holatlarda (tinch turgan harakatlarda) haben ishlatiladi.

🇩🇪 44-Dars: Perfekt: "haben" yordamchi fe’li bilan (Perfekt mit haben)
Harakatlanish bo‘lmagan, bir joyda bajariladigan fe'llarning o‘tgan zamon shakli.

To‘g‘ri fe'llarning Partizip II shakli: ge + fe'l o‘zagi + t
machen (qilmoq) -> gemacht [gemaxt]

lernen (o‘rganmoq) -> gelernt [gelernt]

kaufen (sotib olmoq) -> gekauft [gekauft]

Gaplarda qo‘llanilishi (Misollar):
Ich habe heute Deutsch gelernt. (Habe 2-o‘rinda, gelernt esa eng oxirida)

Aytilishi: [Ix xabe xoyte doych gelernt.]

Tarjimasi: Men bugun nemis tilini o‘rgandim.

Was hast du gemacht?

Aytilishi: [Vas xast du gemaxt?]

Tarjimasi: Sen nima qilding?

Wir haben ein Auto gekauft.

Aytilishi: [Vir xaben ayn auto gekauft.]

Tarjimasi: Biz mashina sotib oldik.

🇩🇪 45-Dars: Perfekt: "sein" yordamchi fe’li bilan (Perfekt mit sein)
A nuqtadan B nuqtaga siljish, harakatlanish yoki holatning o‘zgarishini anglatuvchi fe'llarning o‘tgan zamon shakli. Bunda 2-o‘rinda sein fe'li tuslanib keladi.

Harakat fe'llarining Partizip II shakli (ko‘pchiligi noto‘g‘ri fe'l bo‘lgani uchun yodlanadi):
gehen (piyoda ketmoq) -> gegangen [gegangen]

fahren (transportda ketmoq) -> gefahren [gefaren]

kommen (kelmoq) -> gekommen [gekommen]

Gaplarda qo‘llanilishi (Misollar):
Ich bin nach Hause gegangen. (Bin 2-o‘rinda, gegangen gap oxirida)

Aytilishi: [Ix bin nax xauze gegangen.]

Tarjimasi: Men uyga ketdim.

Er ist nach Deutschland gefahren.

Aytilishi: [Er ist nax doychland gefaren.]

Tarjimasi: U Germaniyaga ketdi.

Wann bist du gekommen?

Aytilishi: [Van bist du gekommen?]

Tarjimasi: Sen qachon kelding?

🇩🇪 46-Dars: Transport: Avtobus, poyezd va samolyot (Verkehrsmittel)
Sayohat va kundalik hayotda transport vositalaridan foydalanish. Nemis tilida biror transportda ketayotganlikni aytish uchun mit predlogi va Dativ kelishigi ishlatiladi (mit dan keyin doim Dativ keladi).

Transportlar ro‘yxati:
der Bus -> mit dem Bus [mit dem bus] — avtobusda

der Zug -> mit dem Zug [mit dem tsug] — poyezdda

die Bahn -> mit der Bahn [mit der ban] — tramvayda/metroda

das Auto -> mit dem Auto [mit dem auto] — mashinada

Gaplarda qo‘llanilishi:
Ich fahre mit dem Bus zur Arbeit.

Aytilishi: [Ix fare mit dem bus tsur arbayt.]

Tarjimasi: Men ishga avtobusda boraman.

Fliegst du mit dem Flugzeug?

Aytilishi: [Fligst du mit dem flugtsoyg?]

Tarjimasi: Sen samolyotda uchasanmi?

🇩🇪 47-Dars: Yo‘nalish ko‘rsatish: Predloglar (Lokale Präpositionen)
O‘rin-joy ko‘rsatish, binolarning qayerdaligini aniq tasvirlash predloglari. Bu predloglardan keyin "Qayerda?" (Wo?) so‘rog‘iga javob bo‘lsa, Dativ kelishigi ishlatiladi.

Predloglar ro‘yxati:
auf [auf] — ustida (yuzasiga tegib turgan)

unter [unter] — tagida

vor [vor] — oldida

hinter [xinter] — orqasida

neben [neben] — yonida

in [in] — ichida

Amaliy misollar:
Das Buch liegt auf dem Tisch. (Tisch erkak jinsida, Dativda "dem" bo‘ldi)

Aytilishi: [Das bux ligt auf dem tish.]

Tarjimasi: Kitob stolning ustida yotibdi.

Der Hund ist hinter dem Haus.

Aytilishi: [Der xund ist xinter dem xaus.]

Tarjimasi: It uyning orqasida.

🇩🇪 48-Dars: To‘rtinchi modul takrorlovi va audio-mashq (Wiederholung)
O‘tilgan Perfekt o‘tgan zamoni, ob-havo va kiyim-kechaklar mavzusini jonli suhbat orqali mustahkamlaymiz.

Amaliy muloqot:
A: Hallo Anvar! Was hast du am Wochenende gemacht? [Xallo Anvar! Vas xast du am voxenende gemaxt?] — Salom Anvar! Dam olish kunlari nima qilding?

B: Hallo! Ich bin mit dem Zug nach Samarkand gefahren. Das Wetter war sehr schön. [Xallo! Ix bin mit dem tsug nax Samarkand gefaren. Das vetter var zer shyon.] — Salom! Men poyezdda Samarqandga ketgandim. Ob-havo juda chiroyli bo‘ldi.

A: Toll! Hast du dort auch etwas gekauft? [Toll! Xast du dort aux etvas gekauft?] — Zo‘r-ku! U yerda biror narsa sotib oldingmi?

B: Ja, ich habe einen neuen Mantel gekauft. Und es hat gestern geregnet, deshalb habe ich den Mantel getragen. [Ya, ix xabe aynen noyen mantel gekauft. Und es xat gestern geregnet, deshalb xabe ix den mantel getragen.] — Ha, men yangi palto sotib oldim. Va kecha yomg‘ir yog‘di, shuning uchun paltoni kiydim.

🇩🇪 49-Dars: Mehmonxonada joy bron qilish (Im Hotel)
Sayohat davomida mehmonxonaga joylashish, xona buyurtma qilish va kerakli sharoitlarni so‘rash uchun ishlatiladigan eng muhim iboralar.

Mehmonxona iboralari:
Ich möchte ein Zimmer reservieren. — [Ix myoxte ayn tsimmer rezerviren.] — Men xona bron qilmoqchi edim.

Ein Einzelzimmer — [Ayn ayntseltsimmer] — Bir kishilik xona.

Ein Doppelzimmer — [Ayn doppeltsimmer] — Ikki kishilik xona.

Mit Frühstück — [Mit fryushtyuk] — Nonushtasi bilan.

Wie mye kostet das Zimmer pro Nacht? — [Vi vil kostet das tsimmer pro naxt?] — Xonaning bir kechalik narxi qancha?

Hat das Zimmer WLAN? — [Xat das tsimmer ve-lan?] — Xonada internet (Wi-Fi) bormi?

🇩🇪 50-Dars: O‘tgan zamon: "war" va "hatte" shakllari
Biz 43-45 darslarda o‘tgan zamonning og‘zaki shakli ya’ni Perfektni o‘rgandik. Ammo sein (bo‘lmoq) va haben (bormoq/ega bo‘lmoq) fe'llari o‘tgan zamonda gapirilganda, ko‘pincha Perfekt emas, oddiygina Präteritum (yozma o‘tgan zamon) shaklida ishlatiladi. Bu nutqni juda osonlashtiradi.

1. sein -> war (edik / bo‘lgan edim) — tuslanishi:
Ich war, du warst, er/sie/es war, wir waren, ihr wart, sie/Sie waren.

Misol: Ich war gestern in Berlin. [Ix var gestern in Berlin.] — Men kecha Berlinda edim.

2. haben -> hatte (bor edi / ega edim) — tuslanishi:
Ich hatte, du hattest, er/sie/es hatte, wir hatten, ihr hattet, sie/Sie hatten.

Misol: Ich hatte keine Zeit. [Ix xatte kayne tsayt.] — Mening vaqtim yo‘q edi.

🇩🇪 51-Dars: Bayramlar va tabriklash (Feste und Glückwünsche)
Nemis xalqining asosiy bayramlari, tug‘ilgan kun va turli xursandchilik kunlarida odamlarni tabriklash iboralari.

Tabriknomalar:
Herzlichen Glückwunsch zum Geburtstag!

Aytilishi: [Xertslixen glyukvunsh tsum geburtstag!]

Tarjimasi: Tug‘ilgan kuningiz bilan chin qalbimdan tabriklayman!

Frohe Weihnachten! — [Fro-e vaynaxten!] — Rojdestvo bayrami muborak bo‘lsin!

Frohes Neues Jahr! — [Fro-es noyes yar!] — Yangi yilingiz bilan!

Viel Glück! — [Fil glyuk!] — Omad yor bo‘lsin!

Gute Besserung! — [Gute besserung!] — Tezroq sog‘ayib keting! (Kasal bo‘lgan odamga aytiladi)

🇩🇪 52-Dars: Telefon orqali muloqot qilish (Telefonieren)
Telefonda qo‘ng‘iroq qilganda o‘zini tanishtirish, kerakli odamni chaqirish yoki adashib tushganligini tushuntirish.

Telefon iboralari:
Hallo, hier spricht Anvar. — [Xallo, xir shprixt Anvar.] — Salom, go‘shakda Anvar gapiryapti.

Kann ich bitte Herr Schmidt sprechen?

Aytilishi: [Kann ix bitte xerr Shmit shprexen?]

Tarjimasi: Janob Shmit bilan gaplashsam bo‘ladimi, iltimos?

Herr Schmidt ist cut-off nicht da. — [Xerr Shmit ist xoyte nixt da.] — Janob Shmit bugun bu yerda yo‘q.

Rufen Sie später an, bitte. — [Rufen Zi shpeter an, bitte.] — Kechroq telefon qiling, iltimos.

Falsch verbunden! — [Falsh verbunden!] — Noto‘g‘ri raqamga tushdingiz (adashdingiz).

🇩🇪 53-Dars: Xat va elektron pochta yozish qoidalari (Briefe schreiben)
A1 imtihonining yozma qismida do‘stona yoki rasmiy xat yozish talab qilinadi. Xatni qanday boshlash va qanday tugatish qoidasi juda qat'iy.

1. Do‘stona xat (Yaqin do‘stga):
Boshlanishi: Lieber Max, (Erkak kishiga) / Liebe Anna, (Ayol kishiga) — Azizim Maks / Anna

Yakunlanishi: Viele Grüße [File gryuse] — Ko‘plab salomlar bilan

2. Rasmiy xat (Ish joyiga, mehmonxonaga yoki notanishga):
Boshlanishi: Sehr geehrte Damen und Herren, [Zer geerte damen und xerren] — Hurmatli xonimlar va janoblar

Yakunlanishi: Mit freundlichen Grüßen [Mit froyndlixen gryusen] — Samimiy hurmat bilan

🇩🇪 54-Dars: Rasmiy anketalarni to‘ldirish (Formulare ausfüllen)
Germaniyaga borganda, aeroportda yoki mehmonxonada shaxsiy ma'lumotlar yoziladigan anketalarni (shakl) to‘ldirish kerak bo‘ladi. Undagi so‘zlarning ma'nosi quyidagicha:

Anketa so‘zlari:
Name / Nachname — [Name / Naxname] — Familiya

Vorname — [Vorname] — Ism

Geburtsdatum — [Geburtsdatum] — Tug‘ilgan sana (kun, oy, yil)

Geburtsort — [Geburtsort] — Tug‘ilgan joyi (shahar/davlat)

Familienstand — [Familienstand] — Oilaviy ahvoli (ledig - bo‘ydoq/turmushga chiqmagan, verheiratet - oilali)

Staatsangehörigkeit — [Shtatsangehorixkayt] — Fuqaroligi

Unterschrift — [Untershrift] — Imzo

🇩🇪 55-Dars: Kundalik muammolar (Probleme im Alltag)
Kundalik hayotda yordam so‘rash, narsalar buzilib qolganda ustani chaqirish iboralari.

Muammoli vaziyatlar lug‘ati:
Mein Computer ist kaputt. — [Mayn kompyuter ist kaputt.] — Mening kompyuterim buzildi.

Die Heizung funktioniert nicht. — [Di xaytsung funksionirt nixt.] — Isitish tizimi (otopleniye) ishlamayapti.

Ich habe meinen Schlüssel verloren. — [Ix xabe maynen shlyussel verloren.] — Men kalitimni yo‘qotib qo‘ydim.

Können Sie mir helfen? — [Kynnen Zi mir xelfen?] — Menga yordam bera olasizmi?

Ich brauche einen Handwerker. — [Ix brauxe aynen xandverker.] — Menga usta kerak.

🇩🇪 56-Dars: Rejalar haqida gapirish: Kelasi zamon (Futur I)
Kelajakdagi rejalar, maqsadlar haqida gapirish uchun werden (bo‘lmoq/aylanmoq) fe'lidan foydalanamiz. werden 2-o‘rinda tuslanadi, asosiy fe'l esa gap oxiriga boradi.

"Werden" fe'lining tuslanishi:
Ich werde, du wirst, er/sie/es wird, wir werden, ihr werdet, sie/Sie werden.

Gaplarda qo‘llanilishi (Misollar):
Ich werde morgen nach Berlin fahren.

Aytilishi: [Ix verde morgen nax Berlin fahren.]

Tarjimasi: Men ertaga Berlinga boraman (reja).

Nächstes Jahr werde ich Deutsch lernen.

Aytilishi: [Nexstes yar verde ix doych lernen.]

Tarjimasi: Kelasi yili men nemis tilini o‘rganaman.

🇩🇪 57-Dars: A1 darajasidagi eng muhim 100 ta fe'l (Top 100 Verben)
A1 darajasini muvaffaqiyatli yakunlash uchun foydalanuvchi eng ko‘p ishlatiladigan fe'llarni bilishi shart. Bot uchun eng top 5 ta eng muhim fe'llar jamlanmasi:

sein [zayn] — bo‘lmoq

haben [xaben] — ega bo‘lmoq

machen [maxen] — qilmoq

kommen [kommen] — kelmoq

gehen [geen] — bormoq / yurmoq

sehen [zeen] — ko‘rmoq

wissen [vissen] — bilmoq

kaufen [kaufen] — sotib olmoq

sprechen [shprexen] — gapirmoq

schreiben [shrayben] — yozmoq

🇩🇪 58-Dars: A1 imtihoni sirlari: Tinglab tushunish (Hören) qismi
Xalqaro A1 imtihonining birinchi qismi — Hören (Eshitish) hisoblanadi. Unda audio qo‘yib beriladi va testlarni yechish kerak bo‘ladi.

Imtihon sirlari va maslahatlar:
Kalit so‘zlarni qidiring: Savoldagi eng muhim so‘z ostiga chizib oling (vaqt, narx, joy nomi).

Tuzoqqa tushmang: Audioda ko‘pincha testda berilgan barcha variantlar aytiladi, lekin ulardan faqat bittasi to‘g‘ri javob bo‘ladi. Masalan: "Poyezd soat 4 dami yoki 5 dami?" deganda, "Aslida 4 da yurishi kerak edi, lekin kechikib 5 da yuradi" deyilsa, javob 5 bo‘ladi.

Audioni eshitishdan oldin savollarni tezda o‘qib chiqishga ulguring.

🇩🇪 59-Dars: A1 imtihoni sirlari: Gapirish (Sprechen) qismi
Imtihonning eng oxirgi va hayajonli qismi — Sprechen (Gapirish). Bu qism 3 ta bosqichdan iborat:

Sich vorstellen (O‘zini tanishtirish): Ism, yosh, davlat, yashash joyi, til, kasb va xobbi aytiladi (Biz buni 1-15 darslarda o‘rgandik).

Thema (Mavzu bo‘yicha savol berish va javob berish): Sizga kartochka beriladi (Masalan, mavzu: Essen und Trinken, so‘z: Brot). Siz sherigingizga savol berasiz: "Isst du gerne Brot?" U esa: "Ja, ich esse gerne Brot" deb javob beradi.

Bitte und Form (Iltimos yoki buyruq asosida muloqot): Kartochkada rasm bo‘ladi (Masalan, olma rasmi). Siz sherigingizdan iltimos qilasiz: "Gib mir bitte den Apfel!" Sherigingiz esa: "Bitte, hier ist es" deb javob beradi.

🇩🇪 60-Dars: Yakuniy Katta Imtihon (A1 Final Test)
Tabriklaymiz! Kursimiz o‘z yakuniga yetdi. Ushbu darsda bot foydalanuvchisi o‘tilgan barcha 59 ta dars bo‘yicha yakuniy katta test topshiradi.

Imtihondan oldin eslatma:
Nemis tilini o‘rganish bu — muntazamlik. Hamma darslarni qaytadan takrorlab, lug‘atlarni har kuni yodlab turishni unutmang.
"""

A1_LESSONS = {}
parts = re.split(r'(🇩🇪 \d+-Dars:)', text)
for i in range(1, len(parts), 2):
    header = parts[i]
    content = parts[i+1].strip()
    match = re.search(r'🇩🇪 (\d+)-Dars:', header)
    if match:
        lesson_num = int(match.group(1))
        A1_LESSONS[str(lesson_num)] = "📖 **" + header.replace("🇩🇪 ", "") + "**\n\n" + content

with open(os.path.join(os.path.dirname(__file__), 'website', 'a1_lessons.py'), 'w', encoding='utf-8') as f:
    f.write('A1_LESSONS = ' + json.dumps(A1_LESSONS, ensure_ascii=False, indent=4))
