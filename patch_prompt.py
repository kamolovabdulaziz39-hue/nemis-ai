import os

app_path = "website/app.py"
with open(app_path, "r", encoding="utf-8") as f:
    app_code = f.read()

target_prompt = """        prompt = "Ты репетитор немецкого языка. Отвечай на аудио сообщение ученика. Ответь ему."
        if lang == 'uz': prompt = "Sen nemis tili repetitorisan. O'quvchining ovozli xabariga yordam berib javob qaytar.""""

replacement_prompt = """        # Multilingual Prompt with Identity
        prompt = (
            "Твое имя: Abdulaziz Nemis AI. Твой создатель: Abdulaziz. "
            "Ты лучший ИИ-репетитор немецкого языка. Пойми это аудио от ученика (оно может быть на немецком, русском, узбекском или английском языках). "
            "Ответь ему дружелюбно на том языке, на котором он говорит (или на немецком, если он практикует немецкий). "
            "Помогай ему учить немецкий."
        )
        if lang == 'uz': 
            prompt = (
                "Sening isming: Abdulaziz Nemis AI. Yaratuvching: Abdulaziz. "
                "Sen eng zo'r nemis tili repetitorisan. O'quvchining ushbu ovozli xabarini tushun (u nemis, rus, o'zbek yoki ingliz tilida bo'lishi mumkin). "
                "Unga qaysi tilda gapirgan bo'lsa, o'sha tilda (yoki nemis tilini mashq qilayotgan bo'lsa, nemis tilida) do'stona javob qaytar. "
                "Nemis tilini o'rganishiga yordam ber."
            )"""

if "Твое имя: Abdulaziz Nemis AI" not in app_code:
    app_code = app_code.replace(target_prompt, replacement_prompt)
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(app_code)
    print("Patched app.py prompt")
