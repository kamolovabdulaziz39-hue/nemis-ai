import json
import re

text = """🇩🇪 3-Dars: 0 dan 20 gacha sanash (Zahlen von 0 bis 20)
Alifbo va o‘qish qoidalarini o‘rganib oldik. Endi esa nemis tilida sanashni o‘rganamiz. Sonlarni to‘g‘ri aytish kundalik hayotda, do‘konlarda va telefon raqamlarini aytishda juda muhim.
0 dan 12 gacha bo‘lgan sonlar
Bu sonlarni shunchaki yodlab qolish kerak, chunki ular asos hisoblanadi:
0 — null
Aytilishi: [null]
Tarjimasi: nol
1 — eins
Aytilishi: [ayns]
Tarjimasi: bir
2 — zwei
Aytilishi: [svay]
Tarjimasi: ikki
3 — drei
Aytilishi: [dray]
Tarjimasi: uch
4 — vier
Aytilishi: [fir]
Tarjimasi: to‘rt
5 — fünf
Aytilishi: [fynf]
Tarjimasi: besh
6 — sechs
Aytilishi: [zeks]
Tarjimasi: olti
7 — sieben
Aytilishi: [ziben]
Tarjimasi: yetti
8 — acht
Aytilishi: [axt]
Tarjimasi: sakkiz
9 — neun
Aytilishi: [noyn]
Tarjimasi: to‘qqiz
10 — zehn
Aytilishi: [tsen]
Tarjimasi: o‘n
11 — elf
Aytilishi: [elf]
Tarjimasi: o‘n bir
12 — zwölf
Aytilishi: [svolf]
Tarjimasi: o‘n ikki
13 dan 19 gacha bo‘lgan sonlar
Bu sonlarni yasash juda oson! Buning uchun kerakli songa o‘nlik, ya’ni zehn so‘zini qo‘shamiz (masalan: 3 + 10 = 13):
13 — dreizehn
Aytilishi: [draytsen]
Tarjimasi: o‘n uch
14 — vierzehn
Aytilishi: [firtsen]
Tarjimasi: o‘n to‘rt
15 — fünfzehn
Aytilishi: [fynftsen]
Tarjimasi: o‘n besh
16 — sechzehn (Diqqat: "sechs" dagi "s" harfi tushib qoladi!)
Aytilishi: [zextsen]
Tarjimasi: o‘n olti
17 — siebzehn (Diqqat: "sieben" dagi "en" qo‘shimchasi tushib qoladi!)
Aytilishi: [zibtsen]
Tarjimasi: o‘n yetti
18 — achtzehn
Aytilishi: [axttsen]
Tarjimasi: o‘n sakkiz
19 — neunzehn
Aytilishi: [noyntsen]
Tarjimasi: o‘n to‘qqiz
Yigirmalik soni
20 — zwanzig
Aytilishi: [svansix]
Tarjimasi: yigirma
O‘zini tekshirish uchun mashq
Quyidagi misollarni nemis tilida ovoz chiqarib yechib ko‘ring:
zwei + drei = fünf (2 + 3 = 5)
vier + sechs = zehn (4 + 6 = 10)
elf + zwei = dreizehn (11 + 2 = 13)
3-Dars yakunlandi! Keyingi darsga o‘tish tugmasini bosing.
🇩🇪 4-Dars: Shaxsiy olmoshlar (Personalpronomen)
Har qanday tilda gap tuzish uchun "Men", "Sen", "U" kabi so‘zlarni bilish kerak. Nemis tilida bular shaxsiy olmoshlar deyiladi. Ularni yodlab olish keyingi darslarda fe'llarni to‘g‘ri ishlatish uchun poydevor bo‘ladi.
Birlik shakli (Faqat bitta shaxs uchun)
ich
Aytilishi: [ix]
Tarjimasi: men
du
Aytilishi: [du]
Tarjimasi: sen (do‘stona va tengdoshlarga)
er
Aytilishi: [er]
Tarjimasi: u (erkak kishiga nisbatan)
sie
Aytilishi: [zi]
Tarjimasi: u (ayol kishiga nisbatan)
es
Aytilishi: [es]
Tarjimasi: u (o‘rta jinsdagi so‘zlar yoki jonsiz buyumlar uchun)
Ko‘plik shakli (Ko‘p shaxslar uchun)
wir
Aytilishi: [vir]
Tarjimasi: biz
ihr
Aytilishi: [ir]
Tarjimasi: sizlar (ikki yoki undan ko‘p yaqin insonlarga qarata)
sie
Aytilishi: [zi]
Tarjimasi: ular
Rasmiy murojaat shakli (Kattalarga yoki notanishlarga)
Sie (Har doim katta harf bilan yoziladi)
Aytilishi: [Zi]
Tarjimasi: Siz (Hurmat ma'nosida, bir kishiga ham, ko‘p kishiga ham)
Muhim eslatma (Bot foydalanuvchisi uchun):
Nemis tilida sie (u - ayol), sie (ular) va Sie (Siz - hurmat) so‘zlari bir xil aytiladi va yoziladi. Ularni gapning mazmunidan va fe'lning o‘zgarishidan ajratib olishni keyingi darsda o‘rganamiz.
4-Dars yakunlandi! Keyingi darsga o‘tish tugmasini bosing.     🇩🇪 5-Dars: Eng muhim fe'l — "sein" (bo‘lmoq) fe’li
Nemis tilida deyarli har bir gapda fe'l (harakat) qatnashishi shart. O‘zbek tilidagi "Men talabaman", "U chiroyli" kabi gaplarda harakat yo‘qdek tuyuladi. Ammo nemis tilida bunday vaziyatlarda sein (bo‘lmoq) fe'li ishlatiladi. Bu fe'l shaxslarga qarab butunlay o‘zgaradi (tuslanadi).
"Sein" fe'lining hozirgi zamonda tuslanishi:
ich bin
Aytilishi: [ix bin]
Tarjimasi: men ...-man
du bist
Aytilishi: [du bist]
Tarjimasi: sen ...-san
er / sie / es ist
Aytilishi: [er / zi / es ist]
Tarjimasi: u ...-dir
wir sind
Aytilishi: [vir zind]
Tarjimasi: biz ...-miz
ihr seid
Aytilishi: [ir zayd]
Tarjimasi: sizlar ...-sizlar
sie / Sie sind
Aytilishi: [zi / Zi zind]
Tarjimasi: ular ...-lar / Siz ...-siz
Gaplarda qo‘llanilishi (Misollar):
Ich bin Anvar.
Aytilishi: [Ix bin Anvar.]
Tarjimasi: Men Anvarman.
Du bist klug.
Aytilishi: [Du bist klug.]
Tarjimasi: Sen aqllisan.
Wir sind hier.
Aytilishi: [Vir zind xir.]
Tarjimasi: Biz shu yerdamiz.
🇩🇪 6-Dars: Davlatlar va tillar (Länder und Sprachen)
Ushbu darsda qaysi davlatdan ekanligimizni mukammal aytishni va qaysi tillarda gapirishimizni tushuntirishni o‘rganamiz. Buning uchun yangi fe'l: sprechen (gapirmoq) fe'lini o‘rganamiz.
Davlatlar va Tillar ro‘yxati:
Usbekistan -> Usbekisch
Aytilishi: [Usbekistan -> Usbekish]
Tarjimasi: O‘zbekiston -> O‘zbek tili
Deutschland -> Deutsch
Aytilishi: [Doychland -> Doych]
Tarjimasi: Germaniya -> Nemis tili
Kasachstan -> Kasachisch
Aytilishi: [Kasaxstan -> Kasaxish]
Tarjimasi: Qozog‘iston -> Qozoq tili
Russland -> Russisch
Aytilishi: [Russland -> Russish]
Tarjimasi: Rossiya -> Rus tili
England -> Englisch
Aytilishi: [England -> Inglish]
Tarjimasi: Angliya -> Ingliz tili
"Sprechen" fe'li bilan gaplar tuzish:
Ich spreche Usbekisch.
Aytilishi: [Ix shprexe usbekish.]
Tarjimasi: Men o‘zbekcha gapiraman.
Sprichst du Deutsch?
Aytilishi: [Shprixst du doych?]
Tarjimasi: Sen nemischa gapirasanmi?
Ich spreche ein bisschen Deutsch.
Aytilishi: [Ix shprexe ayn bissen doych.]
Tarjimasi: Men ozgina nemischa gapiraman.
🇩🇪 7-Dars: Ikkinchi muhim fe'l — "haben" (bormoq/ega bo‘lmoq)
Nemis tilidagi yana bir poydevor fe'llardan biri bu — haben (ega bo‘lmoq). Biz o‘zbek tilida "Mening mashinam bor", "Uning kitobi bor" degan gaplarni nemis tilida "Men mashinaga egaman", "U kitobga ega" shaklida, ya’ni haben fe'li orqali aytamiz.
"Haben" fe'lining hozirgi zamonda tuslanishi:
ich habe
Aytilishi: [ix xabe]
Tarjimasi: menda bor (men egaman)
du hast
Aytilishi: [du xast]
Tarjimasi: senda bor
er / sie / es hat
Aytilishi: [er / zi / es xat]
Tarjimasi: unda bor
wir haben
Aytilishi: [vir xaben]
Tarjimasi: bizda bor
ihr habt
Aytilishi: [ir xabt]
Tarjimasi: sizlarda bor
sie / Sie haben
Aytilishi: [zi / Zi xaben]
Tarjimasi: ularda bor / Sizda bor
Amaliy misollar:
Ich habe Zeit.
Aytilishi: [Ix xabe tsayt.]
Tarjimasi: Mening vaqtim bor.
Hast du Geld?
Aytilishi: [Xast du geld?]
Tarjimasi: Senda pul bormi?
Wir haben ein Auto.
Aytilishi: [Vir xaben ayn auto.]
Tarjimasi: Bizning mashinamiz bor.
🇩🇪 8-Dars: Oddiy fe'llarning hozirgi zamonda tuslanishi (Präsens: regelmäßige Verben)
Nemis tilida oddiy (to‘g‘ri) fe'llar qat'iy qoida asosida shaxslarga qarab o‘zgaradi. Barcha fe'llarning oxiri -en bilan tugaydi (Masalan: machen - qilmoq, lernen - o‘rganmoq, wohnen - yashamoq). Tuslashda shu -en olib tashlanadi va o‘rniga quyidagi qo‘shimchalar qo‘shiladi:
Shaxs qo‘shimchalari qoidasi:
ich -> -e qo‘shiladi
du -> -st qo‘shiladi
er/sie/es -> -t qo‘shiladi
wir -> -en qo‘shiladi
ihr -> -t qo‘shiladi
sie/Sie -> -en qo‘shiladi
"Lernen" (O‘rganmoq) fe'li misolida:
ich lerne — [ix lerne] — men o‘rganyapman
du lernst — [du lernst] — sen o‘rganyapsan
er/sie/es lernt — [er/zi/es lernt] — u o‘rganyapti
wir lernen — [vir lernen] — biz o‘rganyapmiz
ihr lernt — [ir lernt] — sizlar o‘rganyapsizlar    sie/Sie lernen — [zi/Zi lernen] — ular o‘rganyaptilar / Siz o‘rganyapsiz
Boshqa fe'llar bilan misol:
Ich wohne in Taschkent.
Aytilishi: [Ix vone in Tashkent.]
Tarjimasi: Men Toshkentda yashayman.
Was machst du?
Aytilishi: [Vas maxst du?]
Tarjimasi: Sen nima qilyapsan?
🇩🇪 9-Dars: Inkor formasi — "nicht" va "kein" (Negation)
Nemis tilida inkor shakli, ya’ni "yo‘q", "...emas" iboralarini yasash uchun ikkita so‘z ishlatiladi: nicht va kein. Ularning o‘z qoidasi bor.
1. "Kein" inkor so‘zi:
Faqat va faqat oldida noaniq artikli (ein/eine) bor otlarni yoki artiklsiz keladigan otlarni inkor qilish uchun ishlatiladi (ot so‘z turkumidan oldin keladi).
Ich habe ein Auto. (Mening mashinam bor) -> Ich habe kein Auto. (Mening mashinam yo‘q).
Ich habe Zeit. (Vaqtim bor) -> Ich habe keine Zeit. (Vaqtim yo‘q).
2. "Nicht" inkor so‘zi:
Fe'llarni, sifatlarni, ismlarni, joy nomlarini yoki aniq artiklli otlarni inkor qilish uchun ishlatiladi (asosan gap oxirida yoki sifatdan oldin keladi).
Ich rauche. (Men chekaman) -> Ich rauche nicht. (Men chekmayman).
Das ist gut. (Bu yaxshi) -> Das ist nicht gut. (Bu yaxshi emas).
Ich bin nicht Anvar. (Men Anvar emasman).
🇩🇪 10-Dars: Nemis tilida gap tuzish tartibi (Satzbau: Aussagesatz)
Nemis tilida gap tuzish qat'iy tartibga ega. Agar o‘zbek tilida fe'l (harakat) gap oxirida kelsa, nemis tilida oddiy gaplarda fe'l har doim 2-o‘rinda turishi shart! Bu oltin qoida.
To‘g‘ri tartibli gap (Ega + Fe'l + Ikkinchi darajali bo‘lak):
1-o‘rin (Ega): Ich
2-o‘rin (Fe'l): lerne
3-o‘rin (To‘ldiruvchi): Deutsch.
Ich lerne Deutsch. [Ix lerne doych.] — Men nemis tilini o‘rganyapman.
Teskari tartibli gap (Ikkinchi darajali bo‘lak + Fe'l + Ega):
Agar gapni vaqt yoki joy bilan boshlasak ham, fe'l baribir 2-o‘rinni tark etmaydi, ega esa 3-o‘ringa o‘tadi.
1-o‘rin (Vaqt): Heute (Bugun)
2-o‘rin (Fe'l): lerne (o‘rganyapman)
3-o‘rin (Ega): ich (men)
4-o‘rin: Deutsch.
Heute lerne ich Deutsch. [Xoyte lerne ix doych.] — Bugun men nemis tilini o‘rganyapman.
🇩🇪 11-Dars: So‘roq gaplar tuzish (W-Fragen va Ja/Nein Fragen)
Nemis tilida ikki xil so‘roq gap turi mavjud: so‘roq so‘zlar yordamida va so‘roq so‘zsiz (Ha/Yo‘q javobini talab qiluvchi).
1. W-Fragen (Maxsus so‘roq gaplar):
Bunday gaplar W harfi bilan boshlanadigan so‘roq so‘zlar bilan boshlanadi. Fe'l baribir 2-o‘rinda qoladi.
Was? [Vas?] — Nima?
Wie? [Vi?] — Qanday? / Kim?
Wo? [Vo?] — Qayerda?
Woher? [Voxer?] — Qayerdan?
Misol: Wo wohnst du? [Vo vonst du?] — Sen qayerda yashaysan?
2. Ja/Nein Fragen (Umumiy so‘roq gaplar):
Agar gapda so‘roq so‘zi bo‘lmasa, fe'l 1-o‘ringa chiqadi. Javob esa "Ha" (Ja) yoki "Yo‘q" (Nein) bilan boshlanadi.
Wohnst du in Taschkent? [Vonst du in Tashkent?] — Sen Toshkentda yashaysanmi?
Javob: Ja, ich wohne in Taschkent. (Ha, men Toshkentda yashayman) yoki Nein, ich wohne nicht in Taschkent. (Yo‘q, men Toshkentda yashamayman).
🇩🇪 12-Dars: Modulni takrorlash va test (Wiederholung)
Birinchi modul tugadi! Keling, o‘tilgan 11 ta darsdagi eng muhim iboralarni muloqot shaklida takrorlaymiz.
Takrorlash muloqoti:
A: Guten Tag! Wie heißen Sie? [Guten Tag! Vi xaysen Zi?] — Assalomu alaykum! Ismingiz nima?
B: Guten Tag! Ich heiße Anvar. Und Sie? [Guten Tag! Ix xayse Anvar. Und Zi?] — Assalomu alaykum! Mening ismim Anvar. Sizniki-chi?
A: Ich bin Max. Woher kommen Sie, Anvar? [Ix bin Maks. Voxer kommen Zi, Anvar?] — Men Maksman. Qayerdansiz, Anvar?
B: Ich komme aus Usbekistan, aber ich wohne jetzt in Berlin. [Ix komme aus Usbekistan, aber ix vone yetst in Berlin.] — Men O‘zbekistondanman, lekin hozir Berlinda yashayman.
A: Sprechen Sie Deutsch? [Shprexen Zi doych?] — Nemischa gapirasizmi?
B: Ja, ich lerne Deutsch. Ich spreche ein bisschen. [Ya, ix lerne doych. Ix shprexe ayn bissen.] — Ha, men nemis tilini o‘rganyapman. Men ozgina gapiraman.
A: Schön! Auf Wiedersehen! [Shyon! Auf viderzeen!] — Ajoyib! Xayr, salomat bo‘ling!
B: Tschüss! [Chyus!] — Xayr!    🇩🇪 13-Dars: Oila va qarindoshlar (Meine Familie)
Ushbu darsda biz oilamiz va qarindoshlarimiz haqida gapirishni o‘rganamiz. Nemis tilida oila a'zolarini aytganda ham har bir so‘zning o‘z artikli (jinsi) borligiga e'tibor berish kerak.
Oila a'zolari (Die Familienmitglieder):
die Familie — [di familie] — oila
die Eltern — [di eltern] — ota-ona
der Vater — [der fater] — ota
die Mutter — [di mutter] — ona
der Sohn — [der zon] — o‘g‘il farzand
die Tochter — [di toxten] — qiz farzand
der Bruder — [der bruder] — aka / uka
die Schwester — [di shvester] — opa / singil
die Geschwister — [di geshvister] — aka-uka / opa-singillar (umumiy)
der Großvater — [der grosfater] — boba
die Großmutter — [di grosmutter] — buvi
Gaplarda qo‘llanilishi (Misollar):
Das ist mein Vater.
Aytilishi: [Das ist mayn fater.]
Tarjimasi: Bu mening otam.
Hast du Geschwister?
Aytilishi: [Xast du geshvister?]
Tarjimasi: Aka-uka yoki opa-singling bormi?
Ja, ich habe einen Bruder.
Aytilishi: [Ya, ix xabe aynen bruder.]
Tarjimasi: Ha, mening akam (ukam) bor.
🇩🇪 14-Dars: Egalik olmoshlari (Possessivpronomen)
O‘zbek tilidagi "mening", "sening", "uning" kabi so‘zlar nemis tilida egalik olmoshlari deyiladi. Ular o‘zidan keyin kelayotgan so‘zning artikliga qarab o‘zgaradi. Agar orqadagi so‘z ayol jinsida (die) yoki ko‘plikda bo‘lsa, olmosh oxiriga -e harfi qo‘shiladi.
Asosiy egalik olmoshlari (Erkak va o‘rta jins / Ayol jinsi va ko‘plik):
mein / meine — [mayn / mayne] — mening
dein / deine — [dayn / dayne] — sening
sein / seine — [zayn / zayne] — uning (erkak va o‘rta jins uchun)
ihr / ihre — [ir / ire] — uning (ayol kishi uchun)
unser / unsere — [unzer / unzere] — bizning
euer / eure — [oyer / oyre] — sizlarning
ihr / ihre — [ir / ire] — ularning
Ihr / Ihre — [Ir / Ire] — Sizning (hurmat ma'nosida, har doim katta harfda)
Amaliy misollar:
Das ist mein Buch. (Buch — o‘rta jinsda)
Aytilishi: [Das ist mayn bux.]
Tarjimasi: Bu mening kitobim.
Das ist meine Mutter. (Mutter — ayol jinsida)
Aytilishi: [Das ist mayne mutter.]
Tarjimasi: Bu mening onam.
Wie ist Ihr Name? (Name — erkak jinsida, rasmiy murojaat)
Aytilishi: [Vi ist Ir name?]
Tarjimasi: Sizning ismingiz nima?
🇩🇪 15-Dars: Kasblar va ish joyi (Berufe und Arbeitsplatz)
Kim bo‘lib ishlashimiz yoki o‘qishimiz haqida gapirishni o‘rganamiz. Nemis tilida ayol kishining kasbini aytganda, erkaklar kasbining oxiriga -in qo‘shimchasi qo‘shiladi.
Kasblar ro‘yxati (Erkak kishi / Ayol kishi):
der Lehrer / die Lehrerin — [der lerer / di lererin] — o‘qituvchi
der Ingenieur / die Ingenieurin — [der injenyor / di injenyorin] — injener (muhandis)
der Arzt / die Ärztin — [der artst / di ertstin] — shifokor
der Student / die Studentin — [der student / di studentin] — talaba
der Programmierer / die Programmiererin — [der programmirer / di programmirerin] — dasturchi
Kasbni so‘rash va aytish iboralari:
Was bist du von Beruf?
Aytilishi: [Vas bist du fon beruf?]
Tarjimasi: Kasbing nima? / Kim bo‘lib clarifies ishleysan?
Ich bin Ingenieur. (Diqqat: Kasb aytilganda "men" so‘zidan keyin artikl qo‘yilmaydi)
Aytilishi: [Ix bin injenyor.]
Tarjimasi: Men injenerman.
Ich arbeite als Programmierer.
Aytilishi: [Ix arbayte als programmirer.]
Tarjimasi: Men dasturchi bo‘lib ishlayman.
🇩🇪 16-Dars: Artikllar bilan tanishuv (der, die, das)
Nemis tilida har bir ot (ot so‘z turkumi) u jonsiz buyum bo‘ladimi yoki tirik mavjudot, albatta 3 ta jinsdan biriga tegishli bo‘ladi va o‘z artikliga ega bo‘ladi. Buni shunchaki so‘z bilan birga yodlash shart.
Uchta asosiy jins:
der — Erkak jinsi (Maskulin)
die — Ayol jinsi (Feminin)
das — O‘rta jins (Neutral)
die — Ko‘plik shakli (Plural - barcha so‘zlarning ko‘pligi uchun umumiy)
Misollar:
der Tisch [der tish] — stol (erkak jinsida)
die Lampe [di lampe] — lamba (ayol jinsida)
das Auto [das auto] — mashina (o‘rta jinsda)   die Bücher [di byuxer] — kitoblar (ko‘plikda)
Oltin qoida: So‘zlarni tarjimasiga qarab jinsini topib bo‘lmaydi. Masalan, o‘zbek tilida qiz bola jonsiz emas, lekin nemis tilida "qiz bola" so‘zi (das Mädchen) o‘rta jinsga tegishli. Shuning uchun lug‘at yodlaganda doim artikli bilan yodlang.
🇩🇪 17-Dars: Noaniq artikl va uning ishlatilishi (ein, eine)
Artikllar ikki turga bo‘linadi: Aniq (der, die, das) va Noaniq (ein, eine). Agar biror buyum yoki shaxs haqida birinchi marta gapirayotgan bo‘lsak, noaniq artikl ishlatiladi.
Noaniq artikllarning jinslar bo‘yicha taqsimlanishi:
der (erkak) -> ein bo‘ladi
das (o‘rta) -> ein bo‘ladi
die (ayol) -> eine bo‘ladi
Ko‘plikda -> noaniq artikl ishlatilmaydi (chunki "ein" so‘zi "bitta" degan ma'noni beradi).
Misollar:
Das ist ein Tisch. [Das ist ayn tish.] — Bu stol (bitta qandaydir stol).
Das ist ein Auto. [Das ist ayn auto.] — Bu mashina.
Das ist eine Lampe. [Das ist ayne lampe.] — Bu lamba.
🇩🇪 18-Dars: 20 dan boshlab katta sonlar (Zahlen ab 20)
Nemis tilida 21 dan 99 gacha bo‘lgan sonlarni aytish qiziq: birinchi bo‘lib birlik aytiladi, keyin "va" (und) so‘zi qo‘yiladi, undan keyin o‘nlik aytiladi. Ya’ni "yigirma bir" emas, "bir va yigirma" deyiladi.
Sonlarning yasalishi:
21 — einundzwanzig — [ayn-und-svansix] (bir va yigirma)
22 — zweiundzwanzig — [svay-und-svansix] (ikki va yigirma)
25 — fünfundzwanzig — [fynf-und-svansix] (besh va yigirma)
O‘nliklar ro‘yxati (ularning oxiri "-zig" bilan tugaydi):
30 — dreißig — [draysix] (istisno: bu "zig" emas, "ßig" bilan tugaydi)
40 — vierzig — [firtsix]
50 — fünfzig — [fynftsix]
60 — sechzig — [zextsix]
70 — siebzig — [zibtsix]
80 — achtzig — [axtsix]
90 — neunzig — [noyntsix]
100 — hundert — [hundert]
Misol: 54 — vierundfünfzig [fir-und-fynftsix] — ellik to‘rt.
🇩🇪 19-Dars: Mening kun tartibim (Mein Tagesablauf)
Ushbu darsda ertalabdan kechgacha nimalar qilishimizni aytish uchun kerak bo‘ladigan iboralarni o‘rganamiz.
Kundalik harakatlar:
aufstehen — [aufsteen] — o‘rindan turmoq
frühstücken — [fryushtyuken] — nonushta qilmoq
arbeiten — [arbayten] — ishlamoq
nach Hause gehen — [nax xauze geen] — uyga ketmoq
schlafen — [shlafen] — uxlamoq
Kun tartibini tasvirlash:
Ich stehe um 7 Uhr auf.
Aytilishi: [Ix shte-e um ziben ur auf.]
Tarjimasi: Men soat 7 da turaman.
Um 8 Uhr frühstücke ich.
Aytilishi: [Um axt ur fryushtyuke ix.]
Tarjimasi: Soat 8 da men nonushta qilaman.
Ich arbeite den ganzen Tag.
Aytilishi: [Ix arbayte den gansen tag.]
Tarjimasi: Men butun kun ishlayman.
🇩🇪 20-Dars: Ajraladigan old qo‘shimchali fe’llar (Trennbare Verben)
Nemis tilida shunday fe'llar borki, ularning oldida kichik qo‘shimchasi bo‘ladi. Gapda fe'lni tuslaganimizda, shu old qo‘shimcha ajralib, gapning eng oxiriga ketadi.
Eng ko‘p uchraydigan ajraladigan fe'llar:
aufstehen (o‘rindan turmoq) -> old qo‘shimchasi: auf
einkaufen (bozorlik qilmoq) -> old qo‘shimchasi: ein
anrufen (telefon qilmoq) -> old qo‘shimchasi: an
fernsehen (televizor ko‘rmoq) -> old qo‘shimchasi: fern
Gap tuzish qoidasi:
Fe'lning o‘zi odatgidek 2-o‘rinda tuslanadi, old qo‘shimcha esa gap oxiriga tashlanadi.
Ich kaufe heute ein.
Aytilishi: [Ix kaufe xoyte ayn.]
Tarjimasi: Men bugun bozorlik qilyapman. (Fe'l: einkaufen)
Er ruft seine Mutter an.
Aytilishi: [Er ruft zayne mutter an.]
Tarjimasi: U onasiga telefon qilyapti. (Fe'l: anrufen)
🇩🇪 21-Dars: Haftalar, oylar va fasllar (Wochentage, Monate, Jahreszeiten)
Vaqt birliklarini nemis tilida to‘g‘ri qo‘llash. Hafta kunlari oldidan har doim am, oylar va fasllar oldidan esa im predlogi ishlatiladi.
Hafta kunlari (Die Wochentage — barchasi "der" jinsida):
Montag [montag] — Dushanba
Dienstag [dinstag] — Seshanba
Mittwoch [mitvox] — Chorshanba
Donnerstag [donnerstag] — Payshanba
Freitag [fraytag] — Juma
Samstag [zamstag] — Shanba
Sonntag [zontag] — Yakshanba
Misol: Am Montag arbeite ich. [Am montag arbayte ix.] — Dushanba kuni men ishlayman.     Fasllar (Die Jahreszeiten):
der Frühling [fryuling] — bahor
der Sommer [zommer] — yoz
der Herbst [xerbst] — kuz
der Winter [vinter] — qish
Misol: Im Sommer ist es heiß. [Im zommer ist es xays.] — Yozda havo issiq bo‘ladi.
🇩🇪 22-Dars: Vaqtni so‘rash va aytish (Uhrzeit)
Soat necha bo‘lganini so‘rash va unga javob berishning kundalik (norasmiy) usulini o‘rganamiz. Bunda daqiqa birinchi aytiladi. O‘tganini aytish uchun nach (keyin), qolganini aytish uchun vor (oldin) so‘zlari ishlatiladi. Yarim soatni aytganda esa halb (yarim) deyiladi va kelayotgan soat qo‘shib aytiladi.
Soatni so‘rash:
Wie spät ist es? yoki Wie viel Uhr ist es?
Aytilishi: [Vi shpet ist es? / Vi fil ur ist es?]
Tarjimasi: Soat necha bo‘ldi?
Soatni aytish (Misollar):
Es ist 14:00 -> Es ist zwei Uhr. [Es ist svay ur.] — Soat ikki.
Es ist 14:05 -> Es ist fünf nach zwei. [Es ist fynf nax svay.] — Ikkidan 5 daqiqa o‘tdi.
Es ist 14:50 -> Es ist zehn vor drei. [Es ist tsen vor dray.] — Soat uchga 10 ta bor.
Es ist 14:30 -> Es ist halb drei. [Es ist xalb dray.] — Soat ikki yarim (Uchga yarim soat qoldi ma'nosida).
🇩🇪 23-Dars: O‘zgaruvchan o‘zakli fe’llar (Unregelmäßige Verben)
Nemis tilida ba'zi fe'llar borki, ular du (sen) va er/sie/es (u) shaxslarida tuslanganda o‘zagi ichidagi unli harf o‘zgarib ketadi. Qolgan shaxslarda esa oddiy fe'llardek qolaveradi.
1. "e" harfi "i" yoki "ie" ga o‘zgaradigan fe'llar:
geben (bermoq) -> Ich gebe, lekin du gibst, er gibt.
sehen (ko‘rmoq) -> Ich sehe, lekin du siehst, er sieht.
2. "a" harfiga umlaut "ä" qo‘shiladigan fe'llar:
fahren (mashinada/transportda yurmoq) -> Ich fahren, lekin du fährst, er fährt.
schlafen (uxlamoq) -> Ich schlafe, lekin du schläfst, er schläft.
Misol: Fährst du nach Hause? [Ferst du nax xauze?] — Sen uyga ketyapsanmi?
🇩🇪 24-Dars: Ikkinchi modul takrorlovi (Wiederholung)
Ushbu modulda o‘rgangan bilimlarimizni to‘plab, oila, kasb va vaqt haqida muloqot qilamiz.
Amaliy muloqot:
A: Hallo! Wie geht es dir? [Xallo! Vi get es dir?] — Salom! Ishlaring qalay?
B: Hallo! Mir geht es gut, danke. Und dir? [Xallo! Mir get es gut, danke. Und dir?] — Salom! Yaxshi, rahmat. Senda-chi?
A: Auch gut. Was bist du von Beruf? [Aux gut. Vas bist du fon beruf?] — Hammasi yaxshi. Kasbing nima?
B: Ich bin Programmierer. Ich arbeite am Montag und Dienstag. [Ix bin programmirer. Ix arbayte am montag und dinstag.] — Men dasturchiman. Dushanba va seshanba kunlari ishlayman.
A: Wie spät ist es jetzt? [Vi shpet ist es yetst?] — Hozir soat necha bo‘ldi?
B: Es ist genau halb drei. Ich muss nach Hause gehen. [Es ist genau xalb dray. Ix muss nax xauze geen.] — Rostdan ham soat ikki yarim bo‘libdi. Men uyga ketishim kerak.
A: Ok, tschüss! [Ok, chyus!] — Mayli, xayr!
B: Bis bald! [Bis bald!] — Ko‘rishguncha!      🇩🇪 25-Dars: Kelishiklar bilan tanishuv: Tushum kelishigi (Akkusativ)
Nemis tilida kelishiklar juda muhim o‘rin tutadi, chunki ular gapdagi so‘zlarni bir-biriga bog‘laydi. O‘zbek tilidagi tushum kelishigi (kimni?, nimani?, qayerga?) nemis tilida Akkusativ deyiladi.
Akkusativ kelishigida faqat va faqat erkak jinsidagi (der) artikllar o‘zgaradi. Ayol, o‘rta jins va ko‘plik shakllari umuman o‘zgarmaydi.
Artikllarning Akkusativda o‘zgarishi:
der (aniq) -> den bo‘ladi | ein (noaniq) -> einen bo‘ladi | kein (inkor) -> keinen bo‘ladi
das (o‘rta) -> das (o‘zgarmaydi) | ein -> ein | kein -> kein
die (ayol) -> die (o‘zgarmaydi) | eine -> eine | keine -> keine
Amaliy misollar:
der Apfel (olma) -> Ich esse einen Apfel. [Ix esse aynen apfel.] — Men olma (nimani?) yeyapman.
das Buch (kitob) -> Ich lese ein Buch. [Ix leze ayn bux.] — Men kitob o‘qiyapman.
die Tasche (sumka) -> Ich habe eine Tasche. [Ix xabe ayne tashe.] — Mening sumkam bor.
🇩🇪 26-Dars: Oziq-ovqatlar va ichimliklar (Essen und Trinken)
Ushbu darsda kundalik hayotda eng ko‘p ishlatiladigan oziq-ovqat mahsulotlari nomlarini va ular bilan Akkusativ kelishigini qo‘llashni o‘rganamiz.
Mahsulotlar ro‘yxati:
das Brot [brot] — non
der Fleisch [flaysh] — go‘sht
der Käse [keze] — pishloq
die Milch [milx] — sut
der Kaffee [kafee] — kofe
der Tee [tee] — choy
das Wasser [vasser] — suv
Gaplarda qo‘llanilishi:
Ich trinke einen Tee. (Tee — erkak jinsida, shuning uchun "einen")
Aytilishi: [Ix trinke aynen tee.]
Tarjimasi: Men choy ichyapman.
Wir kaufen Brot und Käse.
Aytilishi: [Vir kaufenh brot und keze.]
Tarjimasi: Biz non va pishloq xarid qilyapmiz.
🇩🇪 27-Dars: Restoran va kafeda buyurtma berish (Im Restaurant)
Restoranga borganda taomlar ro‘yxatini so‘rash, buyurtma berish va hisobni to‘lash uchun kerak bo‘ladigan jonli iboralar.
Muhim iboralar:
Die Speisekarte, bitte! — [Di shpayzekarte, bitte!] — Menyuni bersangiz, iltimos!
Ich möchte... — [Ix myoxte...] — Men ... istardim (buyurtma berganda aytiladi).
Herr Ober! — [Xerr ober!] — Ofitsiant! (chaqirish).
Die Rechnung, bitte! — [Di rexnung, bitte!] — Hisobni keltirsangiz, iltimos!
Zusammen oder getrennt? — [Zuzammen oder getrennt?] — Birgami yoki alohida-alohida? (Ofitsiant so‘raydi)
Bar oder mit Karte? — [Bar oder mit karte?] — Naqdmi yoki karta bilan?
Kichik muloqot:
Ofitsiant: Was möchten Sie trinken? [Vas myoxten Zi trinken?] — Nima ichishni istaysiz?
Mijoz: Ich möchte ein Wasser, bitte. [Ix myoxte ayn vasser, bitte.] — Men suv istardim, iltimos.
🇩🇪 28-Dars: Modal fe’llar: "können" va "müssen"
Modal fe'llar asosiy harakatga qo‘shimcha ma'no (imkoniyat, majburiyat, xohish) yuklaydi. Oltin qoida: Modal fe'l gapda 2-o‘rinda tuslanadi, asosiy fe'l esa gapning eng oxiriga o‘zgarishsiz (infinitiv) holatda ketadi.
1. können (bila olmoq, imkoniyati bo‘lmoq) — tuslanishi:
Ich kann, du kannst, er/sie/es kann, wir können, ihr könnt, sie/Sie können.
Misol: Ich kann Deutsch sprechen. [Ix kann doych shprexen.] — Men nemischa gapira olaman. (Sprechen gap oxirida)
2. müssen (majbur bo‘lmoq, shart bo‘lmoq) — tuslanishi:
Ich muss, du musst, er/sie/es muss, wir müssen, ihr müsst, sie/Sie müssen.
Misol: Ich muss heute arbeiten. [Ix muss xoyte arbayten.] — Men bugun ishlashim kerak.
🇩🇪 29-Dars: Modal fe’llar: "wollen" va "möchten"
Istak va xohishlarni ifodalovchi navbatdagi ikkita muhim modal fe'l.
1. wollen (qat'iy xohlamoq, reja qilmoq) — tuslanishi:
Ich will, du willst, er/sie/es will, wir wollen, ihr wollt, sie/Sie wollen.
Misol: Ich will nach Deutschland fahren. [Ix vill nax doychland fahren.] — Men Germaniyaga bormoqchiman (qat'iy xohlayman).
2. möchten (istamoq — muloyim shakli) — tuslanishi:
Ich möchte, du möchtest, er/sie/es möchte, wir möchten, ihr möchtet, sie/Sie möchten.
Misol: Möchten Sie Kaffee trinken? [Myoxten Zi kafee trinken?] — Kofe ichishni istaysizmi?    🇩🇪 30-Dars: Mening uyim/xonadonim (Meine Wohnung)
Uy-joy, xonalar va yashash joyini tasvirlash uchun ishlatiladigan lug‘at boyligi.
Xonalar nomlanishi:
das Haus [xaus] — uy
die Wohnung [vonung] — xonadon (kvartira)
das Zimmer [tsimmer] — xona
die Küche [kyuxe] — oshxona
das Bad [bad] — yuvinish xonasi
das Wohnzimmer [vontsimmer] — mehmonxona
das Schlafzimmer [shlaftsimmer] — yotoqxona
Gaplarda qo‘llanilishi:
Meine Wohnung ist groß und hell.
Aytilishi: [Mayne vonung ist gros und xell.]
Tarjimasi: Mening xonadonim katta va yorug‘.
Das Haus hat vier Zimmer.
Aytilishi: [Das xaus xat fir tsimmer.]
Tarjimasi: Uyning to‘rtta xonasi bor.
🇩🇪 31-Dars: Mebel va uy jihozlari (Möbel)
Uy ichidagi mebellar va kundalik jihozlarning nemischa nomlanishi.
Mebellar:
der Tisch [tish] — stol
der Stuhl [shtul] — stul
das Bett [bett] — krovat (o‘rin)
der Schrank [shrank] — shkaf
das Sofa [sofa] — divan
die Lampe [lampe] — chiroq (lampa)
Gaplarda qo‘llanilishi:
Der Schrank ist neu. [Der shrank ist noy.] — Shkaf yangi.
Ich kaufe ein Sofa. (Sofa o‘rta jinsda, Akkusativda o‘zgarmaydi)
Aytilishi: [Ix kaufe ayn sofa.]
Tarjimasi: Men divan sotib bilyapman.
🇩🇪 32-Dars: Ranglar va sifatlar (Farben und Adjektive)
Predmetlarning belgilarini va ranglarini ifodalash. Nemis tilida sifatlar otning oldida kelganda o‘zgaradi, lekin fe'ldan keyin kelganda hech qanday qo‘shimcha olmaydi (A1 darajasida asosan fe'ldan keyin ishlatamiz).
Ranglar (Farben):
weiß [vays] — oq
schwarz [shvarts] — qora
rot [rot] — qizil
blau [blau] — ko‘k
grün [gryn] — yashil
Sifatlar (Adjektive):
groß / klein [gros / klayn] — katta / kichik
alt / neu [alt / noy] — eski / yangi
schön / hässlich [shyon / xesslix] — go‘zal / xunuk
Misol: Das Auto is rot va neu. [Das auto ist rot und noy.] — Mashina qizil va yangi.
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
"""

lessons = {}
parts = re.split(r'(🇩🇪 \d+-Dars:)', text)
for i in range(1, len(parts), 2):
    header = parts[i]
    content = parts[i+1].strip()
    match = re.search(r'🇩🇪 (\d+)-Dars:', header)
    if match:
        lesson_num = int(match.group(1))
        # Find if there is "vse" at the end and remove it
        if content.lower().endswith("всё"):
            content = content[:-3].strip()
        lessons[str(lesson_num)] = "📖 **" + header.replace("🇩🇪 ", "") + "**\n\n" + content

with open('c:\\Users\\Admin\\Music\\образование\\Abdulaziz Nemis AI\\website\\a1_lessons.py', 'w', encoding='utf-8') as f:
    f.write('A1_LESSONS = ' + json.dumps(lessons, ensure_ascii=False, indent=4))
