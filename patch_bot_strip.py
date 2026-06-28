import os

bot_path = "bot.py"
with open(bot_path, "r", encoding="utf-8") as f:
    code = f.read()

# Fix web_app_url = os.getenv("WEB_APP_URL").strip()
# to web_app_url = (os.getenv("WEB_APP_URL") or "https://nemis-ai.onrender.com/assistant").strip()
code = code.replace('web_app_url = os.getenv("WEB_APP_URL").strip()', 'web_app_url = (os.getenv("WEB_APP_URL") or "https://nemis-ai.onrender.com/assistant").strip()')

with open(bot_path, "w", encoding="utf-8") as f:
    f.write(code)
print("Fixed bot.py strip.")
