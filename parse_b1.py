import json
import re
import os
import sys

text = """🇩🇪 B1: 41-Dars: Mazhul nisbatning uzoq o'tmish zamoni (Plusquamperfekt Passiv)
otmishda sodir bulgan bir haraqatdan ham oldinroq bazharilib bulingan ishni Mazhul (Passiv) shaklda ifodalash. Bunda waren fe'li tuslanadi va gap ohirida Partizip II + worden o'zgarmay turadi.

Das Auto war repariert worden, bevor ich es abholte.

Aytilishi: [Das auto var repariert vorden, bevor ix es abxolte. ]

Tarjimasi: Men machinani olib ketishga borishimdan oldin, u tamirlab bulingan edi.

Die Briefe waren schon geschrieben worden.

Aytilishi: [Di brife varen shon geshriben vorden. ]

Tarjimasi: Xatlar allakachon yozib bulingan edi.

🇩🇪 B1: 42-Dars: Quchirma haplar va OAV tili - "Konjunktiv I"
Germaniyada gazeta va rasmiy baenotlarda boshka birovning gapini ("uning aitishicha", "deb takidladi") u o'zgartirmasdan, betaraf tiklanish uchun xavfsizlik.

Vazir sagten, er helfe der Wirtschaft.

Aytilishi: [Der vazir zagte, er xelfe der virtshaft. ]

Tarjimasi: Vazir iqtisodiyotga yordam berishini (uning o'z gapiga ko'ra). (er uchun 'helfe' b'ladi, 'hilft' emas) 

Sie sagten, sie seien bereit.

Aytilishi: [Zi zagten, zi zayen berayt. ]

Tarjimasi: Ular tayer ekanliklarini aytishdi.

🇩🇪 B1: 43-Dars: Sabab preloglari - "aufgrund" va "dank" (Genitiv / Dativ)
aufgrund (tufayli / asosan) - Genitiv faculty of talab qiladi:

aufgrund des wetters [aufgrund des vetters] - tufayli haqida.

dank (sharofati bilan / tufaili - izhobiy manoda) - asosan Dativ talab qiladi:

dank o'z yordam [dank dayner xilfe] - sening yordaming sharofati bilan.

Aufgrund des Staus bin ich zu spät gekommen.

Aytilishi: [Aufgrund des shtaus bin ix tsu shpet gekommen. ]

Tarjimasi: Cork tufayli men kechikib keldim.

🇩🇪 B1: 44-Dars: karama-qarshilik bogʻlovchisi - “während” (Gaplar aro)
23-darsda o'rganilgan "davomida" prelogidan tashkari, während ikkita gapni bir-biriga solistirib, "vaholanki", "... gan bir vaqtda" degan zidlik ma'nosini ham beradi. Fel gap ohiriga boradi. 

Anvar lernt viel, während Max nur spielt.

Aytilishi: [Anvar lernt fil, verd Maks nur shpilt. ]

Tarjimasi: Anvar kwp o'qiidi, vaholanki Max faqat o'yin o'ynaydi.

🇩🇪 B1: 45-Dars: Sifatdoshlarning tulik takrori va mustakamlash
Partizip I (hozirgi zamon) va Partizip II (o'tgan zamon) formatni matnlarda tugri qo'llash masklari.

der fliegende Vogel [der fliegende vogel] - uchayotgan qush (HHozir bölayotgan ish)

das reparierte Auto [das reparierte auto] — ta'mirlangan mashina (Bajaib bo'lgan ish)

Ich mag das kochende Wasser nicht.

Aytilishi: [Ix mag das koxende vasser nixt. ]

Tarjimasi: Men qayinayotgan suvni yo'qtirmayman.

🇩🇪 B1: 46-Dars: Rasmiy muzokara odobi va rad etish iboralari
Ish beruvchi yoki sheriklarning fikriga hushmuomalalik bilan qarshi chikish.

Ich verstehe stand, aber... [Ix fershte-e daynen shtandpunkt, aber] - Sening nuktai nazaringni tushunaman, lekin...

Da muss ich Ihnen leider widersprechen.

Aytilishi: [Da muss ix Inen layder vidershprexen. ]

Tarjimasi: Bu masalada sizga (afsuski) qarshi chikishga mazhburman.

🇩🇪 B1: 47-Dars: Germanyda suhurta tizimi (Versicherung)
Germaniyada yashash uchun eng muxim bulgan tibbiyoty va izhtimoiy suhurta turlari.

die Krankenversicherung [kranken-fershixerung] - Tibbiy suhurta.

die Haftpflichtversicherung [xaft-pflix-fershixerung] —uchichchi shaxsga etkailgan zararni koplash joyi.

Ich bin bei dieser Krankenkasse versichert.

Aytilishi: [Ix bin bay dizer kranken-kasse fershixert. ]

Tarjimasi: Men ushbu tibbiyoty suhurta company sida suhurtalanganman.

🇩🇪 B1: 48-Dars: Oliy talim va Universitetga huzhat topshirish (Studium)
Germaniya oligogulariga kirish zharayoni va atamalari.

die Zulassung [tsulassung] - o'qishga qabul qilinganlik xakida huzhzhat (qabul).

die Bewerbungsfrist [beverbungs-frist]

Ich habe mich um einen Studienplatz beworben.

Aytilishi: [Ix xabe mix um aynen shtudien-plats bevorben. ]

Tarjimasi: Men universitetidan o'quv zhoyi olish uchun huzhat topshirdim.

🇩🇪 B1: 49-Dars: Rasmiy yarim-shikoyat xati (Halboffizielle Beschwerde)
Izhara beruvchi yoki qo'shnilarga qanday qilib yozma shaklda.

Sehr geehrter Herr Myuller, ich schreibe Ihnen, weil ... — Hurmatli janob Myuler, sizga yozayotganimning birinchi...

Ich bitte Sie, das Problem so passend zu lösen.

Aytilishi: [Ix bitte Zi, das problem zo shnell vi myoglix tsu lyozen. ]

Tarjimasi: Sizdan ushbu muammoni ilozhi qanday tezrok hal qilishni iltimos qiling.

🇩🇪 B1: 50-Dars: Oltinci modul takrori (Wiederholung)
Javob: Trotz des Problems habe ich die Zulassung bekommen! [Trots des Problems xabe ix di tsulassung bekommen!] - Muammoga karamai, men o'kishga kabul huzhzhatini oldim! 

B: Das ist wunderbar! Navbatdagi qadam nima? [Das ist vunderbar! Was ist der nächste Schritt?] - Bu zhuda ajoyib! Navbatdagi qadam nima? 

🇩🇪 B1: 51-Dars: B1 Xalqaro Imtigoni umumiy tuzilish (Goethe / Telc)
Imtihon 4 ta asosiy blokdan (Module) iborat va har biridan alohida 60 balldan yukori to'plash kerak.

Lesen (okish) - 65 dak.

Hören (Tinglash) - 40 dak.

Shrayben (Yozish) - 60 dollar.

Sprechen (Gapirish) - 15 kun.

🇩🇪 B1: 52-Dars: B1 Imtixon sirlari – Lesen (Oʻqish) 1 va 2-qismlar
Blog va gazeta makolalari bilan ishlash.

Siri: Birinchi bo'lib matnni emas, savollarni o'qing. Savoldagi kalit so'zlarni (raqam, nomlar) matn ichidan qidiring. Matnda huddi shu so'z sinonimlari (boshqacha turi) sotib olish mumkin.

🇩🇪 B1: 53-Dars: B1 Īmtihon sirlagi — Lesen (Oʻqish) 3, 4 va 5-qismlar
Elonlar va rasmiy koidalarni bir-biriga moslash.

Siri: 3-qismda odamlarning istaklariga karab elonlarni moslash kerak. Agar hech kaisi elon tugri kelmasa, zhavob varakasiga X belgisini qo'yishni yo'qotish (kamida bitta yoki ikkita zhavob doim X b'ladi).

🇩🇪 B1: 54-Dars: B1 Imtihon sirlari — Hören (Tinglash) 1 va 2-qismlar
Radio xabarlar va elonlarni tinglab, Tggri/Noto'g'ri (Richtig/Falsch) testlarini echish.

Siri: 1-qismdagi audiolar ikki marta qo'yib beriladi. Birinchi jamoadayoq umumiy manoni ulang va martada anik kalit so'zga etibor bering.

🇩🇪 B1: 55-Dars: B1 Imtihon sirlari – Hören (Tinglash) 3 va 4-qismlar
Muhokama (intervyu) eshitib, kim qayisi fikrni o'z ichiga olganligini topish.

Siri: 4-qismda boshlovchi va ikkita mehon gaplashadi. Ularning ovozini (erkak/ael) darhol azhratib oling varakka ismlarini yozib qying, chalkashib ketmas uchun.

🇩🇪 B1: 56-Dars: B1 Imtixon sirlari – Shrayben (Yozish) 1-Aufgabe
Do'stga shakhsiy khat mahsulot (kamida 80 ta s'z).

Siri: Twrtta berylgan puntning (Hukt) hammasiga albatta 2-3 tadan gap shart. Agar bitta nuqta qolib ketsa, nuqta juda paste tushadi. Xatni suti Liebe/Liber bilan boslab, Viele Grüßebilan tortish.

🇩🇪 B1: 57-Dars: B1 Imtixon sirlari – Schreiben (Yozish) 2 va 3-Aufgabe
Forumda o'z fikrini bildirish (80 swz) va rasmiy qiska khat (40 swz).

Siri:3-vazifada (rasmiy hat) albatta albattaSehr geehrte Damen und Herren,va ohiriniMit freundlichen Grüßendeb yozing.Bu structuring uzig alohida nuqta beriladi.

🇩🇪 B1: 58-Dars: B1 Imtixon sirlari – Sprechen (Gapirish) 1-Teil
Sherik bilan birgalikda biror tadbirni (sayohat,Bayram) qayta tiklash.

Siri:Faqat o'zingiz gapiravermang,sherigingizni ham eshiting.Uning fikriga munosabat building: "Das ist ein guter Vorschlag, aber..."(Bu yahshi taklif,Lekin...) yokiki"Was meinst du dazu?"(Bunga nima deisan?).

🇩🇪 B1: 59-Dars: B1 Imtixon sirlari – Sprechen (Gapirish) 2 va 3-Teil
Berilgan mavzu bo'yicha Presentation (Takdimot) qilish va sherikning takdimotiga savol berish.

Tuzilishi:Takdimotni doim kirish suzi bilan qarab: Ich möchte heute über das Thema... sprechen.Keyin uz tazhribangis,O'zbekistondagi holat,mavzuning izhobiy/salbiy tomonlarini itib,Yakunda Rahamat Aiting.

🇩🇪 B1: 60-Dars: B1 Yakuniy Katta Imtixon (B1 Sertifikat Testi)
Ush darsimizda foydalanuvchi haqiqiy Gyote instituti va B1 model testini (Modellsatz) twlik ish va o'z darazhasini aniklaydi.

Tabrik:Kursni muvaffakiyatli tugatdingiz!Siz andi nemis tilini mustakil va erkin bilasiz.Oldinda life Germaniyada katta katta kutmoqda!
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
