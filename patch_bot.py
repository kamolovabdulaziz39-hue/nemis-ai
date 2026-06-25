import re

with open('bot.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, l in enumerate(lines):
    if l.startswith('    if is_owner:'):
        start_idx = i
    if l.strip().startswith('if u[\'step\'] == "agreement":') or l.strip().startswith('if u.get(\'step\') == "agreement":'):
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_admin_block = """    if is_owner:
        admin_kb = [
            [{"text": "📢 E'lon (Rassilka)"}, {"text": "🔓 Blokdan chiqarish"}],
            [{"text": "🚨 Ataka"}, {"text": "🔍 Ataka batafsil"}],
            [{"text": "🎁 VIP Sovg'a qilish"}, {"text": "⬅️ Menyu"}]
        ]

        # Broadcast Step
        if u['step'] == "admin_broadcast":
            if txt and (txt == "⬅️ Menyu" or txt == "/admin"):
                db.update_user(uid, step="admin_main")
                send_msg(cid, "🛠️ *Admin Panel*", kb={"keyboard": admin_kb, "resize_keyboard": True}); return
            else:
                all_u = db.get_all_users(); count = 0
                for user_id in all_u:
                    # if it has text, video, photo...
                    try:
                        url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage"
                        import json
                        data = {"chat_id": user_id, "from_chat_id": cid, "message_id": m['message_id']}
                        req = urllib.request.Request(url, data=json.dumps(data).encode(), headers={'Content-Type': 'application/json'})
                        res = urllib.request.urlopen(req)
                        if res.getcode() == 200: count += 1
                    except Exception as e: pass
                    import time
                    time.sleep(0.05)
                db.update_user(uid, step="admin_main")
                send_msg(cid, f"✅ E'lon {count} ta foydalanuvchiga yuborildi!", kb={"keyboard": admin_kb, "resize_keyboard": True})
                return

        # Unban Step
        if u['step'] == "admin_unban":
            if txt and (txt == "⬅️ Menyu" or txt == "/admin"):
                db.update_user(uid, step="admin_main")
                send_msg(cid, "🛠️ *Admin Panel*", kb={"keyboard": admin_kb, "resize_keyboard": True}); return
            else:
                target_id = str(txt).strip()
                target_user = db.get_user(target_id)
                if target_user:
                    db.update_user(target_id, banned=0, violations=0, step="main")
                    send_msg(cid, f"✅ Foydalanuvchi (ID: {target_id}) blokdan chiqarildi!", kb={"keyboard": admin_kb, "resize_keyboard": True})
                    send_msg(target_id, "🔓 Sizning akkauntingiz admin tomonidan blokdan chiqarildi. Xush kelibsiz!")
                else:
                    send_msg(cid, "❌ Bunday ID bilan foydalanuvchi topilmadi.")
                return

        # Gift VIP Step
        if u['step'] == "admin_gift_vip" and txt:
            if txt == "⬅️ Menyu" or txt == "/admin":
                db.update_user(uid, step="admin_main")
                send_msg(cid, "🛠️ *Admin Panel*", kb={"keyboard": admin_kb, "resize_keyboard": True}); return
            else:
                target_id = str(txt).strip()
                target_user = db.get_user(target_id)
                if target_user:
                    db.update_user(target_id, sub="vip", sub_expire="2099-12-31 23:59:59", ai_count=0, banned=0, violations=0)
                    send_msg(cid, f"✅ Foydalanuvchi (ID: {target_id}) ga VIP taqdim etildi!", kb={"keyboard": admin_kb, "resize_keyboard": True})
                    send_msg(target_id, "🎁 Tabriklaymiz! Admin sizga bir umrlik *VIP* ta'lim kurslarini taqdim etdi. Endi barcha xizmatlardan bepul foydalanishingiz mumkin!")
                else:
                    send_msg(cid, "❌ Bunday ID bilan foydalanuvchi topilmadi.")
                return

        # Main Admin Menu Buttons
        if u['step'] == "admin_main" and txt:
            if txt == "📢 E'lon (Rassilka)":
                db.update_user(uid, step="admin_broadcast")
                send_msg(cid, "📢 Barcha foydalanuvchilarga yuboriladigan xabar, rasm yoki videoni yuboring (forward qilsangiz ham bo'ladi):\\n\\n(Bekor qilish uchun ⬅️ Menyu bosing)", kb={"keyboard": [[{"text": "⬅️ Menyu"}]], "resize_keyboard": True})
                return
            elif txt == "🔓 Blokdan chiqarish":
                db.update_user(uid, step="admin_unban")
                send_msg(cid, "🔓 *Blokdan chiqarish:*\\n\\nFoydalanuvchining Telegram ID raqamini yuboring:", kb={"keyboard": [[{"text": "⬅️ Menyu"}]], "resize_keyboard": True})
                return
            elif txt == "🚨 Ataka":
                # Fetch recent hackers from hacker_logs
                logs = db.conn.execute("SELECT user_id, action, timestamp FROM hacker_logs ORDER BY id DESC LIMIT 10").fetchall()
                if not logs:
                    send_msg(cid, "Hech qanday hujum (ataka) qayd etilmagan.")
                else:
                    res = "🚨 *So'nggi 10 ta Hujum (Ataka):*\\n\\n"
                    for l in logs:
                        res += f"👤 ID: `{l[0]}`\\n🕒 {l[2]}\\n⚠️ Harakat: {l[1]}\\n\\n"
                    send_msg(cid, res)
                return
            elif txt == "🔍 Ataka batafsil":
                # Fetch detailed logs (what exactly they wrote)
                logs = db.conn.execute("SELECT user_id, action, timestamp FROM hacker_logs ORDER BY id DESC LIMIT 5").fetchall()
                if not logs:
                    send_msg(cid, "Hech qanday hujum (ataka) qayd etilmagan.")
                else:
                    res = "🔍 *Batafsil Hujumlar:*\\n\\n"
                    for l in logs:
                        # Sometimes they upload a fake receipt or write something
                        res += f"👤 Hacker ID: `{l[0]}`\\n🕒 Vaqt: {l[2]}\\n💬 Tafsilot:\\n_{l[1]}_\\n\\n"
                    send_msg(cid, res)
                return
            elif txt == "🎁 VIP Sovg'a qilish":
                db.update_user(uid, step="admin_gift_vip")
                send_msg(cid, "🎁 *VIP Sovg'a qilish:*\\n\\nFoydalanuvchining Telegram ID raqamini yuboring:", kb={"keyboard": [[{"text": "⬅️ Menyu"}]], "resize_keyboard": True})
                return
            elif txt == "⬅️ Menyu":
                db.update_user(uid, step="main")
                send_msg(cid, "🏠 Asosiy menyu:", kb=get_main_kb(uid, u.get('lang', 'uz')))
                return
\n"""
    new_lines = lines[:start_idx] + [new_admin_block] + lines[end_idx:]
    with open('bot.py', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Bot.py patched successfully")
else:
    print("Failed to find indices in bot.py")

