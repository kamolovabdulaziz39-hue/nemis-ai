import json
import re
import os
import sys

text = """🇩🇪 B2: 1-Dars: Ikki qismli murakkab boglovchilar - “je ... desto” (Mustahkamlash)
B2 darazhasida ushbu bogʻlovchining sifat va ravishlar bilan bogʻliq murakkab va uzun haplar ichida qʼ tarbiyasini taʼminlaymiz.

Bu B2 ni yanada kuchaytiradi, buning uchun siz o'z ichiga oladi.

Aytilishi: [Ye intensiver du dix auf be-tsvay vorberaytest, desto felerfrayer virst du shprexen.]

Tarjimasi: Sep B2 darazhasig kanchalik zhiddiy tayorgarlik kursang, shunchalik hatosiz gapiradigan belasan.

Je mehr Fachwörter du kennst, desto besser verstehst du die Nachrichten.

Aytilishi: [Ye mer faxvorter du kennst, desto besser fershteyst du di naxrixten.]

Tarjimasi: Kanchalik kwp professional (sohaviy) swzlarni bilsang, yangiliklarni shunchalik yakhshi tushunasan.

🇩🇪 B2: 2-Dars: Sifatdosh kurilmalari sifatida aniklovchilar (Erweiterte Partizipialattribute)
B2 darazhasida sifatdoshlar oddiygina from oldid kelmaydi, beams uzi bilan butun bir haraqatni ergashtirib keladi. Bu nemis tilining eng qiyin va oliy darajasidan biridir.

die gestern vom Lehrer korrigierten Hausaufgaben

Aytilishi: [di gestern fom lerer korrigierten xausaufgaben.]

Tarjimasi Kecha o'kituvchi tomonidan tekshirilgan (tugrilangan) uy mashinasi. (Hausaufgaben s'zini sifat darajasi uchun butun bir gap b''lib kelyapti)

Noutbuklar uchun dasturchi

Aytilishi: [der am laptop arbaytende programmer.]

Tarjimasi: Laptopda ishlayotgan dasturchi.

🇩🇪 B2: 3-Dars: So'z yasalishi — Nomdosh mahsulotlar (Nominalisierung von Verben)
B2 darazhasida nutkni kiskartiris va rasmiylashtirish uchun fe'lardan yasash zhuda mukhim o'rin tutada. Kwp hollarda fellar das articles bilan otga ailanadi.

lernen (o'rganmoq) -> das Lernen [das lernen] - o'rganish (qovurilgan)

Das Lernen einer Fremdsprache erfordert viel Geduld.

Aytilishi: [Das lernen ayner fremdshpraxe erfordert fil geduld.]

Tarjimasi: Chet tilini o'rganish zhuda kwp sabr-toqat talab qiladi.

leben (yashamok) -> das Leben [das leben] - deydi.

🇩🇪 B2: 4-Dars: Pasi zamonaviy shakllari — Moal mahsulotlar bilan Pasif (Passiv mit Modalverben)
Ish-harakatning mazhburiiligi yoki uni Mazhul (Passiv) shaklda ifodalash. Koida: Modal fe'l (2-o'rinda tuslanadi) + Partizip II + werden (o'zgarmay gap ohirida turadi) .

Die Dokumente müssen sofort unterschrieben werden.

Aytilishi: [Di dokumente myssen zofort untershriben vorden.]

Tarjimasi: Huzhatlar zudlik bilan imzolanishi shart (kerak).

Das Problem kann schnell gelöst werden.

Aytilishi: [Das problem kann shnell gellyost vorden.]

Tarjimasi: muammoni tezda hal qilish mumkin.

🇩🇪 B2: 5-Dars: Chegaralovchi boglovchilar - “solange” va “sofern” (Mustahkamlash)
sofern (agar mabodo / basharti) - shartli bog'lovchi bo'lib, falls so'zining rasmiyrok turidir.

Sofern Sie keine Fragen haben, wir das Gespräch edi.

Aytilishi: [Zofern Zi kayne fragen xaben, be-enden vir das geshprax.]

Tarjimasi: Basharti sizda savollar bulmasa, subatni yakunlaymiz.

Solange du hier bist, bist du sicher.

Aytilishi: [Zolange du xir bist, bist du zixer.]

Tarjimasi: Modomiki shu erda ekansan, hafsizlikdasan.

🇩🇪 B2: 6-Dars: Kelajakda tugallangan zamon – Futur II
Kelazhak bir vaktga borib bazharilib bulinadigan harakatni yoki o'tmishdagi bir ish khaqida gumon/tahmin qilishni ifodalaidi. Koida: werden (tuslanadi) + Partizip II + haben/sein (bo'shliq ohirida) .

Biz B2-Zertifikat bekommen haben bor.

Aytilishi: [Bis nexstes yar verde ix das be-tsvay sertifikat bekommen xaben.]

Tarjimasi: Kelasi ishlab men B2 sertifikatini olib bulgan bulaman.

Er wird wohl schon nach Hause gegangen sein.

Aytilishi: [Er virt vohl shon nax xauze gegangen zayn.]

Tarjimasi: U allakaxon uyga ketib bulgan bulsa kerak (taxmin).

🇩🇪 B2: 7-Dars: Swz o'rni va inkor - "nicht"ning gapdagi pozitsiyasi (Inkor qilish)
B2 darazhasida haplar uzunlashgani tufayli, nicht swzini tugri zhoiga quyish zhuda muhim. nicht nimaning oldiga qo'yilsa, ainan o'sha swzni inkor qiladi.

Ich habe not bu kitobni sotib oldim, beams unikini.

Aytilishi: [Ix xabe nixt dizes bux gekauft, sondern yenes.]

Tarjimasi: Men ainan bu kitobni sotib olmadim, beams ana unikini oldim.

Ich kann heute kelaman emas. [Ix kann xoyte nixt kommen.] - Men bugun kela olmayman. (Butun gapni inkor kilsa, gap ohirida yoki fe'l oldida keladi)

🇩🇪 B2: 8-Dars: Rasmiy suhbat va fikrni himoya qilish — Argumentation
Munozaralarda uz fikrini isbot bilan isbotlash va boshqa fikrini inkor qilish.

Ich bin der festen Überzeugung, dass... [Ix bin der festen uberzeugung, dass] - Men katyy ishonamanki...

Ein schlagendes Argument dafür ist... [Ayn shlagendes argument dafyr ist] — Buning uchun eng kuchli dail shundaki...

Ich kann etu firga qushilmaman.

Aytilishi: [Ix kann dizer moynung nixt zustimmen.]

Tarjimasi: Men bu fikrga qo'shila olmayman.

🇩🇪 B2: 9-Dars: Sifatdosh kurillmalari - Gerundy ornida "zu" + Partizip I (Gerundivum)
Mazhburiyat yoki imkoniyatlarni ifodalaydi va faqat Passiv ma'nosini beradigan sifatdosh shakli.

das zu lösende Problem

Aytilishi: [das tsu lyozende muammosi.]

Tarjimasi: Halol kerak bulgan muammo. (Problem das gelöst werden muss manosida)

die zu erledigenden Aufgaben

Aytilishi: [di tsu erledigenden aufgaben.]

Tarjimasi: Bajarilishi lozim bulgan.

🇩🇪 B2: 10-Dars: Birinchi modul takrori (Wiederholung)
B2 darazhasining birinchi murakkab Passive va sifatdosh kurilmalarini amaliy subatda mustakamlash.

A: Sind die zu erledigenden Aufgaben schon fertig? [Zind di tsu erledigenden aufgaben shon fertig?] - Bazharilishi kerak bulgan mashina tajormi?

B: Ja, hama huzhatlar imzolanib bulindi. [Ya, alle Dokumente sind schon unterschrieben worden.] - Ha, hhamma hujjatlar allakachon imzolab belindi.

🇩🇪 B2: 11-Dars: Fellarning barkaror predloglar bilan kelishilgan (Verben mit Präpositionen)
B2 darazhasida fellarning preloglarini va ular Akkusativ yoki Dativ talab qilishini yodlash shart.

abhängen von + Dativ [apxengen fon] - ...ga bo'g'lik bwlmok.

Das hängt vom Wetter ab.

Aytilishi: [Das xengt fom vetter ap.]

Tarjimasi: Bu ob-havoga boglik.

sich beschweren über + Akkusativ [zix beshveren uber] - ...ustidan shikoyat qilmoq.

Er beschwert sich über den Lärm. [Er beshvert zix uber den lerm.] — U shovqin ustidan shkoyyat qilyapti.

🇩🇪 B2: 12-Dars: Sifatlarning barkaror predloglar bilan kelishilgan (Adjektive mit Präpositionen)
stolz sein auf + Akkusativ [shtolts zayn auf] - ...bilan fahrlanmok.

Ich bin stolz auf dich.

Aytilishi: [Ix bin shtolts auf dix.]

Tarjimasi: Men sen bilan fahrlanaman.

zufrieden sein mit + Dativ [tsufrieden zayn mit] - ...dan konikmok / mamnun bolmok.

Bist du mit deiner Arbeit zufrieden? [Bist du mit dayner arbayt tsufriden?] - Ishingdan mamnunmisan?

🇩🇪 B2: 13-Dars: Predloglar o'rnini bosuvchi olmoshlar — "woran", "daran", "wovon", "davon"
Agar was suggest savol zhonsiz buyumga nisbatan berils, wo(r)- qo'shimchasi, zhavobda esa da(r)- qo'shimchasied ilova.

Woran denkst du?  (denken an + Akkusativ fe'lidan)

Aytilishi: [Voran denkst du?]

Tarjimasi: Nima xakida o'ylayapsan?

Ich denke daran.

Aytilishi: [Ix denke daran.]

Tarjimasi: Men o'sha xakida o'ylayapman.

Wovon sprecht ihr? [Vofon shprext ir?] - Nima hkida haplashyapsizlar?

🇩🇪 B2: 14-Dars: Ikki qismli murakkab boglovchilar - "zwar...aber"
“Tugri... lekin”, “Garchi... bulsa-da, ammo” mazmunidagi zhuft bog‘lovchi.

Deutsch ist zwar schwer, aber es ist sehr interessant.

Aytilishi: [Doych ist tsvar shver, aber es ist zer interessant.]

Tarjimasi: Nemis tili tugri qiyin, lekin u zhuda kizikarli.

Er hat zwar Geld, aber er kauft kein Auto. [Er xat tsvar geld, aber er kauft qayn auto.] — Uning puli bo-u, lekin mashina sotib olmayapti.

🇩🇪 B2: 15-Dars: Ikki qismli murakkab boglovchilar - "solange... bis"
"...guncha", "...guniga qadar" vakt chegarasini ifodalovchi bogʻlovchi. Fel gap ohiriga boradi.

Ich werde Deutsch lernen, bis ich perfect spreche.

Aytilishi: [Ix verde doych lernen, bis ix perfect shprexe.]

Tarjimasi: Men mukammal gapirgunimga qadar nemis tilini o'rganaman.

Warte hier, bis ich zurückkomme. [Varte xir, bis ix tsyuryukkomme.] - Men qayitgunimcha shu erda kutib tur.

🇩🇪 B2: 16-Dars: Nisbiy haplarning murakkab turlari - Predloglar bilan (Relativsätze)
Nisbiy olmoshlar o'zidan oldin kelgan preposition ta'sirida Akkusativ yoki Dativ shaklga qiradi.

Der Freund, mit dem ich reise, ist Arzt.  (mit sutli Dativ - dem)

Aytilishi: [Der froynd, mit dem ix rayse, ist artst.]

Tarjimasi: birga sayohat kilayotgan dostim Men foydalanishdir.

Das Thema, über das wir sprechen, ist wichtig.  (über shu erda Akkusativ - das)

Aytilishi: [Das tema, uber das vir shprexen, ist vixtix.]

Tarjimasi: Biz gaplashayotgan mavzu zhuda mukhim.

🇩🇪 B2: 17-Dars: Germany mehnat bozori va "Anerkennung" (Diplom qilish)
Germaniyada xorizhiy diplomlarni tan oldirish zharajoni va rasmiy atamalar.

die Anerkennung [anerkennung] - diplom yoki hujjatning tan olinishi (tasdiqlanishi).

die Urkunde [urkunde] - Rasmiy guvonoma / diplom.

einen Antrag stellen [aynen antrag shtellen] - ariza topshirmoq.

Ich muss einen Antrag auf Anerkennung meines Diploms stellen.

Aytilishi: [Ix muss aynen antrag auf anerkennung maynes diploms shtellen.]

Tarjimasi: Men diplomamni tasdiqlash uchun ariza topshirishim kerak.

🇩🇪 B2: 18-Dars: Ishxonadagi nizolar va ularni hal qilish (Konflikte am Arbeitsplatz)
Ish zhoyidagi kelishmovchiliklarni bartaraf etish va professional muloqot.

der Konflikt [konflikt] - past / kelishmovchilik, murosa:  der Kompromiss [kompromiss], hal kilmok:  lösen [lyozen].

Wir mussen einen Kompromiss topildi.

Aytilishi: [Vir myssen aynen kompromiss finden.]

Tarjimasi: Biz o'zaro paydo (compromise) topishimiz kerak.

Lassen uns das Problem ruhig besprechen. [Lassen uns das problem ruix beshprexen.] — Keling, muammoni tinggina muxokama qilaylik.

🇩🇪 B2: 19-Dars: Shartley istisno boglovchisi - “es sei denn, dass” (... masalan / faqat ... gina bulsa)
Agar bolishi qiyin bulgan yagona bir istisno shart koldirilsa sodir bo'lgan. Fel gap ohiriga boradi.

Ich gehe heute spazieren, es sei denn, dass es stark regnet.

Aytilishi: [Ix ge-e xoyte shpatsiren, es zay denn, dass es shtark regnet.]

Tarjimasi: Men bugunga boraman, faqat qattiq yomg'ir yog'ib qolmasagina (agar yog'sa bormaiman).

🇩🇪 B2: 20-Dars: Ikkinci modul takrori (Wiederholung)
Javob: Bist du mit der Anerkennung deines Diploms zufrieden? [Bist du mit der anerkennung daynes diploms tsufriden?] - Diploming maktabidan mamnunmisan?

B: Ja, das hat zwar lange gedauert, aber jetzt ist alles erledigt. [Ya, das xat tsvar lange gedauert, aber yetst ist alles erledigt.] - HA, bu garchi uzok vakt olgan bulsa-da, lekin hozir hammasi tayer .
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
