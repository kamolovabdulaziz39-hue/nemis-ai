import os

app_path = "website/app.py"
with open(app_path, "r", encoding="utf-8") as f:
    app_code = f.read()

target1 = """    try:
        import google.generativeai as genai
    except ImportError:"""

replace1 = """    try:
        from google import genai
    except ImportError:"""

app_code = app_code.replace(target1, replace1)

target2 = """    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        sample_file = genai.upload_file(path=temp_audio_path)
        
        # Multilingual Prompt with Identity
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
            )
        
        model = genai.GenerativeModel(model_name="models/gemini-flash-latest")
        response = model.generate_content([prompt, sample_file])
        answer_text = response.text
        
        try:
            genai.delete_file(sample_file.name)
        except:
            pass"""

replace2 = """    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        sample_file = client.files.upload(file=temp_audio_path)
        
        # Multilingual Prompt with Identity
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
            )
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[prompt, sample_file]
        )
        answer_text = response.text
        
        try:
            client.files.delete(name=sample_file.name)
        except:
            pass"""

app_code = app_code.replace(target2, replace2)

with open(app_path, "w", encoding="utf-8") as f:
    f.write(app_code)

print("Patched SDK in app.py!")
