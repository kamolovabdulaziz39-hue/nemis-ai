import json
import re
import os
import sys

text = """🇩🇪 B2: 41-Dars: Rasmiy uslub – Nominalstil (Otlar orqali ifodalash)
B2 darajasida va nemis matbuotida gaplarni fe'llar bilan emas, o'tlar va predloglar orqali ifodalash juda keng tarqalgan. Bu uslub gapni qisqa va rasmiy qiladi.

Fe'l uslubi:  Weil es regnet, bleiben wir zu Hause. (Yom'ir yog'ayotgani tufayli...)

Nominal uslub:  Wegen des Regens bleiben wir zu Hause.

Aytilishi: [Vegen des regens blayben vir tsu xauze.]

Tarjimasi: Yomg'ir tufayli biz uyda qolamiz.

Bei der Ankunft in Berlin (= Als ich in Berlin ankam) [Bay der ankundt in Berlin] - Berlinga yetib kelganda.

🇩🇪 B2: 42-Dars: Murakab Nismbiylik - "wer" va "was" bilan gap boshlovchi
A1-B1 darajalarida nisbiy gaplar otning orqasidan kelgan bo'lsa, B2 da umumiy qoidani gapga shaxsiysiz ifodalashni o'rganamiz.

Wer fleißig lernt, besteht die Prüfung.

Aytilishi: [Ver flayssix lernt, beshteyt di pryufung.]

Tarjimasi: Kimki tirishib o'qisa, imtihondan o'tadi.

Was du sagst, ist absolut richtig.

Aytilishi: [Vas du zagst, ist absolut rixtix.]

Tarjimasi: Sen aytayotgan narsa mutloq to'g'ridir.

🇩🇪 B2: 43-Dars: Shartli cheklov - "es sei denn,..." (Istisno holat)
40-darsgacha bo'lgan qismda buni dass bilan o'rgangan edik. Agar dass ishlatilmasa, es sei denn iborasidan keyin to'g'ri gap tartibi (Ega + Fe'l 2-o'rinda) keladi.

Ich komme morgen, es sei denn, ich muss arbeiten.

Aytilishi: [Ix komme morgen, es zay denn, ix muss arbayten.]

Tarjimasi: Men ertaga kelaman, faqat yordamm kerak bo'lib qolmasa bo'ldi (agar ishlasam kelolmayman).

🇩🇪 B2: 44-Dars: Sifatdosh qurilishlarini yoyish (Dekodieren)
2-darsda o‘rganilgan murakkab va uzun sifatdosh iboralarini oddiy, tushunarli nisbiy gaplarga (Relativsatz) tuzatishli mashqi. Bu imtihonda matnni oshirish uchun hal qiluvchi rol o'ynaydi.

Konstruktsiya:  die vom Chef unterschriebene Urkunde

Yoyilmasi:  die Urkunde, die vom Chef unterschrieben wurde

Aytilishi: [di urkunde, di fom shef untershriben vurde.]

Tarjimasi: imzolangan guvohnoma.

🇩🇪 B2: 45-Dars: Sub'ektiv modal fe'llar - "sollen" va "wollen" (Mish-mishlar)
B2 darajasida bu fe'llar o'zining asosiy ma'nosidan tashqari, birovning gapi yoki mish-mishlarni ifodalash uchun keladi.

sollen - ularning soni (mish-mishlarga ko'ra).

Er soll sehr reich sein.

Aytilishi: [Er zoll zer rayx zayn.]

Tarjimasi: Eshitishlariga qaraganda, u juda boy emish.

wollen - o'zining da'vo qilishi bo'yicha (lekin odamlar ishonmaydi).

Er will la ixtiyorini yolg'iz o'zi qilgan. [Er vill das proyekt alayn gemaxt xaben.] - U rejasini yolg'iz o'zi qilganini da'vo qilyapti.

🇩🇪 B2: 46-Dars: O'rin-joy ko'rsatuvchi murakkab predloglar (Genitiv)
außerhalb [auzerxalb] - tashqarisida, ichida:  innerhalb [innerxalb], bo'ylab:  entlang [entlang].

Außerhalb der Stadt gibt es einen großen Wald.

Aytilishi: [Auzerxalb der shtadt gibt es aynen grosen vald.]

Tarjimasi: Shahar ustida katta o'rmon bor.

entlang so'zi otdan keyin kelsa, Akkusativ talab qiladi:

den Fluss entlang [den fluss entlang] - daryo bo'ylab.

🇩🇪 B2: 47-Dars: Kelishuv va Kontraktlar (Vertragswesen)
Germaniyada rasmiy huquqlar, ijaraga olish (Mietvertrag) shaxsiy yuridik yuridik iboralar.

einen Vertrag kündigen [aynen vertrag kyundigen] - shartnomani bekor qilmoq (rastorgnut).

die Kündigungsfrist [ kyundigung-frist] - shartnomani bekor qilish haqida rasman saqlash muddati.

Ich muss den Mietvertrag fristgerecht kündigen.

Aytilishi: [Ix muss den mit-vertrag frist-gerext kyundigen.]

Tarjimasi: Men ijaraga bekor qilish muddatiga amal qilgan holdaim kerak.

🇩🇪 B2: 48-Dars: Nemis korporativ madaniyati va Muloqot (Berufliche Communikation)
Ishxonada hamkasblar bilan professional muloqot va taqdimotlar qilish.

das Meeting leiten [das meet layten] - majlisni boshqarmoq.

Ich danke Ihnen für Ihre Aufmerksamkeit.

Aytilishi: [Ix danke Inen fyr Ire aufmerkzamkayt.]

Tarjimasi: E'tiboringiz uchun rahmat. (Taqdimotga aytiladi)

🇩🇪 B2: 49-Dars: Ishga ariza va Kuzatuv xati (Bewerbungsschreiben)
B2 darajasi eng yuqori yozma amaliyoti - Germaniyada ishga kirish uchun "Anschreiben" (Kuzatuv xati) formati.

Boshlanishi:  Sehr geehrte Damen und Herren, mit großem Interesse habe ich Ihre Stellenanzeige gelesen...

Ilova:  Men Anhang Sie meinen Lebenslaufni topdim.

Aytilishi: [Im anxang finden Zi maynen lebenslauf.]

Tarjimasi Ilovada mening rezumni (CV) oson.

🇩🇪 B2: 50-Dars: Oltinchi bo'lim takrori (Wiederholung)
Javob: Anschreiben shon fristgerecht verschickt bormi? [Xast du das anshrayben shon frist-gerext fershikt?] - Kuzatuv xatini belgilangan muddat ichida jo'natdingmi?

B: Ja, im Anhang habe ich alle Dokumente beigefügt. [Ya, im anxang xabe ix alle dokumente bay-gefuygt.] - Ha, ilovada hamma hujjatlarni biriktirdim.

🇩🇪 B2: 51-Dars: Xalqaro B2 Imtihoni Umumiy formati (Goethe-Zertifikat B2)
B2 imtihoni to'rtta moduldan iborat bo'lib, o'tish balli har bir modul uchun kamida 60 ball etarli etib.

Lesen: 5 ta qism (Teil), 65 daqiqa.

Hören: 4 ta qism, 40 daqiqa.

Schreiben: 2 ta topshiriq (Aufgabe), 75 daqiqa.

Sprechen: 2 ta topshiriq, 15 daqiqa.

🇩🇪 B2: 52-Dars: B2 Imtihon sirlari — Lesen (1 va 2-qismlar)
1-qism: To'rtta odamning fikriga ko'ra 5 ta sarlavhani to'g'ri moslashtirish.

Sir: Paragraflardagi gaplarni so'zma-so'z tarjima. asosiy maqsad - muallifning yaratish (pozitiv) yoki zarar (negativ) pozitsiyasini baholash.

🇩🇪 B2: 53-Dars: B2 Imtihon sirlari — Lesen (3, 4 va 5-qismlar)
3-qism: Matndan olib tashlangan gaplarni (AH) o'z joyiga qo'yish.

Sir: Bo'sh joydan oldin va keyingi gapdagi bog'lovchilarga ( deshalb, aber, tarafdorlar ) qarang. Agar keyingi gapda "Er" yoki "Das" kelsa, demak olib ketan gap ichida o'sha ot qatnashgan bo'ladi.

🇩🇪 B2: 54-Dars: B2 Imtihon sirlari — Hören (1 va 2-qismlar)
1-qism: Kundalik hayotiy va qisqa audio xabarlar (5 ta savol, faqat 1 marta qo'yiladi).

Sir: Audiodan keyin 30 soniya ichida faqat variantlarni tez ko'rib chiqing. Variantlar bir-biridan qaysi kalit so'z orqali farqni aniqlang.

🇩🇪 B2: 55-Dars: B2 Imtihon sirlari — Hören (3 va 4-qismlar)
4-qism: Radio-shou yoki diskussiya (2 marta qo'yiladi). Uchta odam gapiradi.

Sir: Kim rozilik bildiryapti ( zustimmen ), kim qarshi chiqyapti ( widersprechen ) - shuni boshqarish shart. Gap uchun "Da o'z fikringiz to'g'ri, lekin..." degan gaplarga juda ehtiyot bo'ling.

🇩🇪 B2: 56-Dars: B2 Imtihon sirlari — Schreiben (1-Aufgabe: Forumsbeitrag)
Onlayn forumda ijtimoiy mavzu bo'yicha o'z fikrini (150 ta so'z).

Sir: Berilgan 4 ta punktning hammasini ochib berish shart. Strukturada albatta B2 darajadagi murakkab bo'lgan Je... desto , Nicht nur... sondern auch va Obwohl kabi bog'lovchilarni qo'llang. Bu grammatika uchun yuqori ball beradi.

🇩🇪 B2: 57-Dars: B2 Imtihon sirlari — Schreiben (2-Aufgabe: Rasmiy xat)
Ish joyiga yoki biron bir tashkilotga rasmiy xat/so'rovnoma ilovasi (kamida 100 ta so'z).

Sir: Muloyimlik formasi ( Konjunktiv II - Könnten Sie bitte... ) juda ko'p foydalanish kerak. Xat strukturasini buzmang: Sehr geehrte Damen und Herren va ustoz Mit freundlichen Grüßen .

🇩🇪 B2: 58-Dars: B2 Imtihon sirlari — Sprechen (1-Teil: Vortrag)
Berilgan ikki mavzudan biridan tanlab, 3-4 daqiqada qisqa taqdimot qilish.

Tuzilishi:

Einleitung (Kirish):  Das Thema mog'or taqdimotlari...

Vorteile/Nachteile (Sodda va zaif tomonlari).

Eigene Meinung & Usbekistan (Shaxsiy fikr va O'zbekistondagi holat).

Schluss (Yakun).

🇩🇪 B2: 59-Dars: B2 Imtihon sirlari — Sprechen (2-Teil: Munozara)
Sherik bilan berilgan muammo diskussiya (munozara) qilish va umumiy qarorga kelish.

Sir: Sherigingizning fikrini eshitib turmang. Agar u gapini tugatsa, darhol munosabat bildiring: "Ich verstehe, was du meinst, aber ich sehe das etwas anders..." [Ix fershte-e, vas du maynst, aber ixze-e das etvas anders...] - Nima demoqchingni tushunaman, lekin men biroz boshqacha qarayman.

🇩🇪 B2: 60-Dars: B2 Yakuniy Katta Imtixon (B2 Sertifikat Yakuniy Test)
Muvaffaqiyatli yakun! Ush darsda foydalanuvchi jami 180 ta dars (A1-B2) olgan barcha bilimlarini xalqaro standartdagi B2 model testi orqali sinovdan o'tkazadi.

Tabrik xabari: SIZ buni uddaladingiz! Nemis tilining eng yuqori professional darajalaridan biri bo'lgan B2 to'liq tugatdingiz. Endi Germaniyada oliy ta'lim olish yoki yuqori daromad olish uchun eshiklar sizga to'liq ochiq!
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
