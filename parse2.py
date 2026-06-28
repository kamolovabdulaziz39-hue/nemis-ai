import json
import re
import sys
import os

# Import the current lessons
sys.path.append(os.path.join(os.path.dirname(__file__), 'website'))
from a1_lessons import A1_LESSONS

text = """🇩🇪 36-Dars: Uchinchi modul takrorlovi va lug‘at testi (Wiederholung)

Ushbu modulda o‘rganilgan Dativ, Akkusativ va modal fe'llarni muloqot orqali mustahkamlaymiz.
Amaliy muloqot:
A: Entschuldigung, ich suche ein Hotel. Kannst du mir helfen? [Entshuldigung, ix zuxe ayn xotel. Kannst du mir xelfen?] — Kechirasiz, men mehmonxona qidiryapman. Menga yordam bera olasanmi?
B: Ja, gerne. Das Hotel ist dort, neben dem Bahnhof. [Ya, gerne. Das xotel ist dort, neben dem banxof.] — Ha, jon deb. Mehmonxona anavi yerda, vokzalning yonida.
A: Vielen Dank! Ich muss auch einen Kaffee trinken. Gibt es hier ein Café? [Filen dank! Ix muss aux aynen kafee trinken. Gibt es xir ayn kafe?] — Katta rahmat! Men kofe ham ichishim kerak. Bu yerda kafe bormi?
B: Ja, geh geradeaus. Dort ist ein schönes Café. [Ya, ge geradeaus. Dort ist ayn shyones kafe.] — Ha, to‘g‘riga yur. Anavi yerda chiroyli kafe bor.   

🇩🇪 37-Dars: Xobbi va bo'sh vaqt (Hobbys und Freizeit)
Ushbu darsda biz bo'sh vaqtimizda nimalar bilan shug'ullanishimiz, mashg'ulotlarimiz va sevimli mashg'ulotlarimiz haqida gapirishni o'rganamiz.

Qiziqishlar va xobbilar:
Fußball spielen - [fusbal shpilen] - futbol o'ynamoq

Bücher lesen - [byuxer lezen] - kitoblar o'qimoq

Musik hören - [muzik xoren] - musiqa tinglamoq

Schwimmen - [shvimmen] - suzmoq

Reisen - [rayzen] - sayohat qilmoq

Gaplarda qo'llanilishi (Misollar):
Was ist dein Hobby?

Aytilishi: [Vas ist dayn xobbi?]

Tarjimasi: Sening xobbing nima?

Mein Hobby ist Reisen.

Aytilishi: [Mayn xobbi ist rayzen.]

Tarjimasi: Mening xobbiym sayohat qilish.

In Meiner Freizeit spiele ich Fußball.

Aytilishi: [In mayner fraytsayt shpile ix fusbal.]

Tarjimasi: Bo'sh vaqtimda men futbol o'ynayman.

🇩🇪 38-Dars: Do'stlar bilan uchrashuv (Verabredung)
Do'stlarni biror joyga taklif qilish, uchrashuv vaqti va joyini kelishib olish uchun kerak bo'ladigan jonli iboralar.

Taklif qilish va kelishish iboralari:
Hast du am Samstag Zeit? - [Xast du am zamstag tsayt?] - Shanba kuni vaqting bormi?

Wollen wir ins Kino gehen? - [Vollen vir ins kino geen?] - Kinoga boramizmi?

Ja, das ist eine gute Idee. - [Ya, das ist ayne gute idee.] - Ha, bu yaxshi g'oya.

Wann treffen wir uns? - [Van treffen vir uns?] - Qachon uchrashamiz?

Um wie viel Uhr? - [Um vi fil ur?] - Soat nechchida?

Treffen wir uns um 18 Uhr vor dem Kino. - [Treffen vir uns um axtsen ur vor dem kino.] - Soat 18:00 da kino teatri oldida uchrashamiz.

🇩🇪 39-Dars: Ob-havo va iqlim (Das Wetter)
Tabiat tasviri, ob-havoni va harorat haqida gapirish. Nemis tilida ob-havo har doim shaxssiz "es" olmoshi bilan aytiladi.

Ob-havo iboralari:
Wie ist das Wetter heute? - [Vi ist das vetter xoyte?] - Bugun ob-havo qanday?

Es ist kalt. - [Es ist kalt.] - Havo sovuq.

Es ist warm / heiß. - [Es ist varm / xays.] - Havo iliq / issiq.

Die Sonne scheint. - [Di zonne shaynt.] - Quyosh charoqlayapti.

Es regnet. - [Es regnet.] - Yovg'ir yog'yapti.

Es schneit. - [Es shnayt.] - Qor yog'yapti.

Wie viel Grad ist es? - [Vi fil grad ist es?] - Havo necha daraja?

Es sind 25 Grad. - [Es zind finf und svansix grad.] - Havo 25 daraja issiq.

🇩🇪 40-Dars: Kiyim-kechaklar va xaridlar (Kleidung und Einkaufen)
Do'konda kiyim sotib olish, o'lcham va kiyimni so'rash, kiyimlarning nemischa nomlanishi.

Kiyimlar ro'yxati:
der Mantel [mantel] — palto

die Hose [xoze] — shim

das Hemd [xemd] - ko'ylak (erkaklar)

das T-Shirt [t-shirt] — futbolka

die Schuhe [shue] - poyabzal (har doim ko'plikda)

Do'kondagi muloqot:
Ich suche eine Hose. (Hose ayol jinsida, Akkusativda "eine" bo'lib qoladi)

Aytilishi: [Ix zuxe ayne xoze.]

Tarjimasi: Men shim qidiryapman.

Welche Größe brauchst du?

Aytilishi: [Velxe grose brauxst du?]

Tarjimasi: Senga qaysi o'lcham kerak?

Größe M, bitte. - [Grose em, bitte.] - M o'lcham, iltimos.

🇩🇪 41-Dars: Tana a'zolari (Der menschliche Körper)
Inson tanasining qismlari. Bu mavzu keyingi darsda shifokor qabulida qayerimiz og'riyotganini aytish uchun juda kerak bo'ladi.

Tana a'zolari:
der Kopf [kopf] — bosh

das Auge / die Augen [auge / augen] - ko'z / ko'zlar

das Ohr / die Ohren [or / oren] – quloq / quloqlar

der Mund [mund] — og'iz

die Hand / die Hände [xand / xende] - qo'l (kaft qismi)

das Bein / die Beine [bayn / bayne] - oyoq

🇩🇪 42-Dars: Shifokor qabulida: Salomatlik (Beim Arzt)
Kasallik holati, kasallikni aytish va tibbiy iboralar. Nemis tilida "Mening... og'riyapti" deyish uchun ...schmerzen (og'riqlar) so'zi bilan qurilmalar yasaladi.

Muhim iboralar:
Ich bin krank. - [Ix bin krank.] - Men kasalman.

Ich habe Kopfschmerzen.

Aytilishi: [Ix xabe kopfshmertsen.]

Tarjimasi: Mening boshim og'riyapti.

Ich habe Halsschmerzen.

Aytilishi: [Ix xabe xalsshmertsen.]

Tarjimasi: Mening tomog'im og'riyapti.

Ich habe Fieber. - [Ix xabe fiber.] - Mening isitmam bor.

Was fehlt Ihnen? - [Vas felt Inen?] - Sizni nima bezovta qilyapti? (Shifokor so'raydi)

Sie müssen im Bett bleiben. - [Zi myssen im bett blayben.] - Siz to'shakda qolishingiz (yotishingiz) shart.

🇩🇪 43-Dars: O'tgan zamon bilan tanishuv: Perfekt
Nemis tilida so'zlashuvda (og'zaki nutqda) o'tgan zamon haqida gapirish uchun asosan Perfekt zamon shaklidan foydalaniladi. Perfekt murakkab zamon, ya'ni u ikkita fe'ldan tashkil topadi:

Yordamchi fe'l: Gapda 2-o'rinda haben yoki sein fe'li shaxsga qarab tuslanadi (o'zi tarjima qilinmaydi).

Asosiy fe'l: Gapning eng oxiriga Partizip II (o'tgan zamon sifatdoshi) shaklida o'zgarishsiz o'tadi. Asosiy fe'llarning oldiga ko'pincha ge- qo'shimchasi qo'shiladi (Masalan: machen -> gemacht).

Oltin qoida: Agar harakat bir joydan boshqa joyga ko'chish (harakatlanish) bo'lsa sein yordamchi fe'li olinadi. Qolgan barcha holatlarda (tinch turgan harakatlar) haben ishlatiladi.

🇩🇪 44-Dars: Perfekt: "haben" yordamchi fe'li bilan (Perfekt mit haben)
Harakatlanish bo'lmagan, bir joyda bajariladigan fe'llarning o'tgan zamon shakli.

To‘g‘ri fe’llarning Partizip II shakli: ge + fe’l o‘zagi + t
machen (qilmoq) -> gemacht [gemaxt]

lernen (o'rganmoq) -> gelernt [gelernt]

kaufen (sotib olmoq) -> gekauft [gekauft]

Gaplarda qo'llanilishi (Misollar):
Ich habe heute Deutsch gelernt. (Habe 2-o'rinda, gelernt esa gap oxirida)

Aytilishi: [Ix xabe xoyte doych gelernt.]

Tarjimasi: Men bugun nemis tilini o'rgandim.

Was hast du gemacht?

Aytilishi: [Vas xast du gemaxt?]

Tarjimasi: Sen nima qilding?

Wir haben ein Auto gekauft.

Aytilishi: [Vir xaben ayn auto gekauft.]

Tarjimasi: Biz mashina sotib oldik.

🇩🇪 45-Dars: Perfekt: "sein" yordamchi fe'li bilan (Perfekt mit sein)
A nuqtadan B nuqtaga siljish, harakatlanish yoki holatning o'zgarishi shaklini anglatuvchi fe'llarning o'tgan zamon shakli. Bunda 2-o'rinda sein fe'li tuslanib keladi.

Harakat fe'llarining Partizip II shakli (ko'pchiligi noto'g'ri fe'l bo'lgani uchun yodlanadi):
gehen (piyoda ketmoq) -> gegangen [gegangen]

fahren (transportda ketmoq) -> gefahren [gefaren]

kommen (kelmoq) -> gekommen [gekommen]

Gaplarda qo'llanilishi (Misollar):
Ich bin nach Hause gegangen. (Bin 2-o'rinda, gegangen gap oxirida)

Aytilishi: [Ix bin nax xauze gegangen.]

Tarjimasi: Men uyga ketdim.

Er ist nach Deutschland gefahren.

Aytilishi: [Er ist nax doychland gefaren.]

Tarjimasi: U Germaniyaga ketdi.

Wann bist du gekommen?

Aytilishi: [Van bist du gekommen?]

Tarjimasi: Sen qachon kelding?

🇩🇪 46-Dars: Transport: Avtobus, poyezd va samolyot (Verkehrsmittel)
Sayohat va kundalik hayotda transportdan foydalanib harakatlanish. Nemis tilida biror transportda ketayotganlikni aytish uchun mit predlogi va Dativ kelishigi ishlatiladi (mit dan keyin doim Dativ keladi).

Transportlar ro'yxati:
der Bus -> mit dem Bus [mit dem bus] — avtobusda

der Zug -> mit dem Zug [mit dem tsug] - poyezdda

die Bahn -> mit der Bahn [mit der ban] — tramvayda/metroda

das Auto -> mit dem Auto [mit dem auto] — mashinada

Gaplarda qo'llanilishi:
Ich fahre mit dem Bus zur Arbeit.

Aytilishi: [Ix fare mit dem bus tsur arbayt.]

Tarjimasi: Men ishga avtobusda boraman.

Fliegst du mit dem Flugzeug?

Aytilishi: [Fligst du mit dem flugtsoyg?]

Tarjimasi: Sen samolyotda uchasanmi?

🇩🇪 47-Dars: Yo'nalish ko'rsatish: Predloglar (Lokale Präpositionen)
O'rin-joy ko'rsatish, binoning qayerdaligini aniqlash predloglari. Bu predloglardan keyin "Qayerda?" (Wo?) so'rog'iga javob bo'lsa, Dativ kelishigi ishlatiladi.

Predloglar ro'yxati:
auf [auf] - ustida (yuzasiga tegib turgan)

unter [unter] — tagida

vor [vor] — oldida

hinter [xinter] — orqasida

neben [neben] — yonida

in [in] — ichida

Amaliy misollar:
Das Buch liegt auf dem Tisch. (Tisch erkak jinsida, Dativda "dem" bo'ldi)

Aytilishi: [Das bux ligt auf dem tish.]

Tarjimasi: Kitob stolning ustida yotibdi.

Der Hund ist hinter dem Haus.

Aytilishi: [Der xund ist xinter dem xaus.]

Tarjimasi: It uyning orqasida.

🇩🇪 48-Dars: To'rtinchi modul takrorlovi va audio-mashq (Wiederholung)
O'tilgan Perfekt o'tgan zamoni, ob-havo kiyim-kechaklar mavzusini jonli suhbat orqali mustahkamlaymiz.

Amaliy muloqot:
A: Salom Anvar! Was hast du am Wochenende gemacht? [Salom Anvar! Vas xast du am voxenende gemaxt?] - Salom Anvar! Dam olish kunlari nima qilding?

B: Salom! Ich bin mit dem Zug nach Samarqand gefahren. Das Wetter war sehr schön. [Salom! Ix bin mit dem tsug nax Samarqand gefaren. Das vetter var zer shyon.] - Salom! Men poyezdda Samarqandga ketgandim. Ob-havo juda chiroyli bo'ldi.

A: Toll! Hast du dort auch etwas gekauft? [Toll! Xast du dort aux etvas gekauft?] - Zo'r-ku! U yerda biror narsa sotib oldingmi?

B: Ja, ich habe einen neuen Mantel gekauft. Und es hat gestern geregnet, deshalb habe ich den Mantel getragen. [Ya, ix xabe aynen noyen mantel gekauft. Und es xat gestern geregnet, deshalb xabe ix den mantel getragen.] - Ha, men yangi palto sotib oldim. Va kecha yomg'ir yog'di, shuning uchun paltoni kiydim.
"""

# Extract lessons
parts = re.split(r'(🇩🇪 \d+-Dars:)', text)
for i in range(1, len(parts), 2):
    header = parts[i]
    content = parts[i+1].strip()
    match = re.search(r'🇩🇪 (\d+)-Dars:', header)
    if match:
        lesson_num = int(match.group(1))
        # Remove anything after the end text if present
        if "To'rtinchi blok ham yakunlandi" in content:
            content = content.split("To'rtinchi blok ham yakunlandi")[0].strip()
        
        A1_LESSONS[str(lesson_num)] = "📖 **" + header.replace("🇩🇪 ", "") + "**\n\n" + content

# Write back to file
with open(os.path.join(os.path.dirname(__file__), 'website', 'a1_lessons.py'), 'w', encoding='utf-8') as f:
    f.write('A1_LESSONS = ' + json.dumps(A1_LESSONS, ensure_ascii=False, indent=4))
