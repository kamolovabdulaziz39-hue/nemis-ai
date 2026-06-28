import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'website'))
from a1_lessons import A1_LESSONS

text = """60-Dars: Yakuniy Katta Imtihon (A1 Final Test)
Tabriklaymiz! Kursimiz o‘z yakuniga yetdi. Ushbu darsda bot foydalanuvchisi o‘tilgan barcha 59 ta dars bo‘yicha yakuniy katta test topshiradi.

Imtihondan oldin eslatma:
Nemis tilini o‘rganish bu — muntazamlik. Hamma darslarni qaytadan takrorlab, lug‘atlarni har kuni yodlab turishni unutmang.
"""

A1_LESSONS["60"] = "📖 **" + text

with open(os.path.join(os.path.dirname(__file__), 'website', 'a1_lessons.py'), 'w', encoding='utf-8') as f:
    f.write('A1_LESSONS = ' + json.dumps(A1_LESSONS, ensure_ascii=False, indent=4))
