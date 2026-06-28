import re

with open('website/templates/assistant.html', 'r', encoding='utf-8') as f:
    html = f.read()
import time
ts = int(time.time())
html = re.sub(r'assistant\.js\?v=\d+', f'assistant.js?v={ts}', html)

with open('website/templates/assistant.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('website/assistant.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = "const userId = tg.initDataUnsafe?.user?.id || 'demo_user';"
replacement = """const userId = tg.initDataUnsafe?.user?.id || 'demo_user';
// HARDCODED ADMIN FALLBACK TO PREVENT REGISTRATION
if (String(userId) === '5543183063') {
    userDetails.is_admin = true;
    userDetails.sub = 'vip';
    userDetails.webapp_registered = true;
}
"""
if "HARDCODED ADMIN FALLBACK" not in js:
    js = js.replace(target, replacement)

with open('website/assistant.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Patched successfully')
