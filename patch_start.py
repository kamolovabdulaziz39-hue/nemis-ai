import re, os

# 1. Patch app.py to return is_admin
app_path = "website/app.py"
if os.path.exists(app_path):
    with open(app_path, "r", encoding="utf-8") as f:
        app_js = f.read()
    
    target_app = "admin_telegram_id = os.getenv('ADMIN_TELEGRAM_ID', '5543183063')\n    if admin_telegram_id and uid == admin_telegram_id:\n        res['sub'] = 'vip'"
    replacement_app = "admin_telegram_id = os.getenv('ADMIN_TELEGRAM_ID', '5543183063')\n    res['is_admin'] = (uid == admin_telegram_id)\n    if admin_telegram_id and uid == admin_telegram_id:\n        res['sub'] = 'vip'"
    
    if "res['is_admin'] = (uid == admin_telegram_id)" not in app_js:
        app_js = app_js.replace(target_app, replacement_app)
        with open(app_path, "w", encoding="utf-8") as f:
            f.write(app_js)
        print("Patched app.py")


# 2. Patch bot.py main KB and /start
bot_path = "bot.py"
if os.path.exists(bot_path):
    with open(bot_path, "r", encoding="utf-8") as f:
        bot_code = f.read()
    
    # Patch get_main_kb
    target_kb = """def get_main_kb(uid, lang):
    t = TEXTS.get(lang, TEXTS['ru'])
    rows = [
        [{"text": t['ai_btn']}],
        [{"text": t['founder_btn']}]
    ]
    return {"keyboard": rows, "resize_keyboard": True}"""

    replacement_kb = """def get_main_kb(uid, lang):
    web_app_url = os.getenv("WEB_APP_URL", "https://nemis-ai.onrender.com/assistant").strip()
    rows = [
        [{"text": "🇩🇪 Nemis tilini o'rganish / Начать обучение", "web_app": {"url": web_app_url}}]
    ]
    return {"keyboard": rows, "resize_keyboard": True}"""

    if replacement_kb not in bot_code:
        bot_code = bot_code.replace(target_kb, replacement_kb)
    
    # Patch /start
    start_target = """    if txt == '/start':
        db.update_user(uid, step="main")
        
        # 2. Send the beautiful welcome text with the Inline Web App Button
        welcome_text = (
            "Assalomu alaykum! 👋 Abdulaziz NEMIS AI raqamli akademiyamizga xush kelibsiz! 🏛✨\\n\\n"
            "Bu yerda ortiqcha vaqt yo‘qotishlarsiz ⏳, uzoq yo‘l yurmasdan 🚷, uyingizda o‘tirib 24/7 rejimda mukammal bilim olasiz! 🧠💻 Bizning tizim dangasalikni butunlay yo‘q qiladi va yuqori natija beradi. 🎯🔥\\n\\n"
            "Qoidalarimiz qattiq, lekin adolatli. 🛡⚖️ O‘z darajangizni tanlang va maqsad sari ilk qadamni bosing! 🚀🏁"
        )
        web_app_url = os.getenv("WEB_APP_URL", "https://nemis-ai.onrender.com/assistant").strip()
        inline_kb = {
            "inline_keyboard": [
                [{"text": "🇩🇪 Nemis tilini o'rganish / Начать обучение", "web_app": {"url": web_app_url}}]
            ]
        }
        send_msg(cid, welcome_text, kb=inline_kb)
        return"""

    start_replacement = """    if txt == '/start':
        db.update_user(uid, step="main")
        
        welcome_text = (
            "Assalomu alaykum! 👋 Abdulaziz NEMIS AI raqamli akademiyamizga xush kelibsiz! 🏛✨\\n\\n"
            "Bu yerda ortiqcha vaqt yo‘qotishlarsiz ⏳, uzoq yo‘l yurmasdan 🚷, uyingizda o‘tirib 24/7 rejimda mukammal bilim olasiz! 🧠💻 Bizning tizim dangasalikni butunlay yo‘q qiladi va yuqori natija beradi. 🎯🔥\\n\\n"
            "Pastdagi tugmani bosib, akademiyaga kiring! 🚀🏁"
        )
        
        # First send a dummy message to completely remove any old reply keyboard if present
        del_kb = {"remove_keyboard": True}
        dummy_id = send_msg(cid, "⏳ Yuklanmoqda... / Загрузка...", kb=del_kb)
        if dummy_id and dummy_id is not True:
            delete_msg(cid, dummy_id)
            
        # Send the beautiful greeting with the NEW main keyboard (which only has the Web App button)
        send_msg(cid, welcome_text, kb=get_main_kb(uid, lang))
        return"""

    if "del_kb = {\"remove_keyboard\": True}" not in bot_code:
        bot_code = bot_code.replace(start_target, start_replacement)

    with open(bot_path, "w", encoding="utf-8") as f:
        f.write(bot_code)
    print("Patched bot.py")
