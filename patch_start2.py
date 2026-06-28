import os

bot_path = "bot.py"
with open(bot_path, "r", encoding="utf-8") as f:
    bot_code = f.read()

target = """        # First send a dummy message to completely remove any old reply keyboard if present
        del_kb = {"remove_keyboard": True}
        dummy_id = send_msg(cid, "⏳ Yuklanmoqda... / Загрузка...", kb=del_kb)
        if dummy_id and dummy_id is not True:
            delete_msg(cid, dummy_id)
            
        # Send the beautiful greeting with the NEW main keyboard (which only has the Web App button)
        send_msg(cid, welcome_text, kb=get_main_kb(uid, lang))
        return"""

replacement = """        # Send the beautiful greeting with the NEW main keyboard (which only has the Web App button)
        send_msg(cid, welcome_text, kb=get_main_kb(uid, lang))
        return"""

if target in bot_code:
    bot_code = bot_code.replace(target, replacement)
    with open(bot_path, "w", encoding="utf-8") as f:
        f.write(bot_code)
    print("Patched bot.py")
else:
    print("Target not found in bot.py")
