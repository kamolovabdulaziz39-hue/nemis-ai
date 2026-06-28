import json
import re
import sys
import os

# Import the current lessons
sys.path.append(os.path.join(os.path.dirname(__file__), 'website'))
from a1_lessons import A1_LESSONS

text = """🇩🇪 50-Dars: O‘tgan zamon: "war" va "hatte" shakllari
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

Herr Schmidt ist heute nicht da. — [Xerr Shmit ist xoyte nixt da.] — Janob Shmit bugun bu yerda yo‘q.

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

Bitte und Form (Iltimos yoki buyruq asosida muloqot): Kartochkada rasm bo‘ladi (Masalan, olma rasmi). Siz sherigingizdan iltimos qilasiz: "Gib mir bitte den Apfel!" Sherigingiz esa: "Bitte, hier ist es" deb javob beradi."""

# Extract lessons
parts = re.split(r'(🇩🇪 \d+-Dars:)', text)
for i in range(1, len(parts), 2):
    header = parts[i]
    content = parts[i+1].strip()
    match = re.search(r'🇩🇪 (\d+)-Dars:', header)
    if match:
        lesson_num = int(match.group(1))
        
        # Add to A1_LESSONS
        A1_LESSONS[str(lesson_num)] = "📖 **" + header.replace("🇩🇪 ", "") + "**\n\n" + content

# Handle 60th course which might be exam? 
# For now just write 50-59.
with open(os.path.join(os.path.dirname(__file__), 'website', 'a1_lessons.py'), 'w', encoding='utf-8') as f:
    f.write('A1_LESSONS = ' + json.dumps(A1_LESSONS, ensure_ascii=False, indent=4))
