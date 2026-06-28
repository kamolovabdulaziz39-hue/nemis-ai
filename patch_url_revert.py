import os

bot_path = "bot.py"
with open(bot_path, "r", encoding="utf-8") as f:
    code = f.read()

# Revert hardcoded URL back to os.getenv
code = code.replace('"https://nemis-ai.onrender.com/assistant"', 'os.getenv("WEB_APP_URL")')

with open(bot_path, "w", encoding="utf-8") as f:
    f.write(code)
print("Reverted URL in bot.py")
