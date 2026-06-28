import os
import re

bot_path = "bot.py"
with open(bot_path, "r", encoding="utf-8") as f:
    code = f.read()

# Replace any os.getenv("WEB_APP_URL", ...) with hardcoded string
code = re.sub(r'os\.getenv\("WEB_APP_URL"[^)]*\)', '"https://nemis-ai.onrender.com/assistant"', code)

with open(bot_path, "w", encoding="utf-8") as f:
    f.write(code)

env_path = ".env"
with open(env_path, "r", encoding="utf-8") as f:
    env = f.read()

# Remove WEB_APP_URL line
env = "\n".join([line for line in env.split('\n') if not line.startswith("WEB_APP_URL=")])

with open(env_path, "w", encoding="utf-8") as f:
    f.write(env)
print("Hardcoded WEB_APP_URL in bot.py and removed from .env.")
