import os, re

# 1. Fix bot.py UnboundLocalError
bot_path = "bot.py"
with open(bot_path, "r", encoding="utf-8") as f:
    bot_code = f.read()

target_time = """                    import time
                    time.sleep(0.05)"""
replacement_time = """                    time.sleep(0.05)"""

if target_time in bot_code:
    bot_code = bot_code.replace(target_time, replacement_time)
    with open(bot_path, "w", encoding="utf-8") as f:
        f.write(bot_code)
    print("Fixed bot.py UnboundLocalError.")
else:
    print("Target time not found in bot.py.")

# 2. Fix assistant.js SUPER BYPASS in catch block
js_path = "website/assistant.js"
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

target_catch = """        console.error("Failed to load user data", e);
        welcomeModal.classList.remove('hidden');
        showWarningScreen();"""
replacement_catch = """        console.error("Failed to load user data", e);
        
        // SUPER HARDCODED BYPASS EVEN IF FETCH FAILS
        if (String(userId) === '5543183063') {
            userDetails.is_admin = true;
            userDetails.sub = 'vip';
            userDetails.webapp_registered = true;
            document.getElementById('admin-menu-grid').classList.remove('hidden');
        }
        
        welcomeModal.classList.remove('hidden');
        showWarningScreen();"""

if "SUPER HARDCODED BYPASS EVEN IF FETCH FAILS" not in js:
    js = js.replace(target_catch, replacement_catch)
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("Fixed assistant.js catch block.")

# 3. Cache-bust HTML again
html_path = "website/templates/assistant.html"
import time
ts = int(time.time())
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()
html = re.sub(r'assistant\.js\?v=\d+', f'assistant.js?v={ts}', html)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Busted cache.")
