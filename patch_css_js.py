import os
import re

# 1. Fix CSS for light theme inputs
css_path = "website/assistant.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix input background and color
css = css.replace("background-color: rgba(0, 0, 0, 0.3);", "background-color: #ffffff;")
css = css.replace("background-color: rgba(15, 23, 42, 0.8);", "background-color: #f8fafc;")

# Ensure text color in inputs is dark
css = re.sub(r'\.input-group input\s*\{[^}]*color:\s*var\(--text-bright\)[^}]*\}', 
    lambda m: m.group(0).replace('var(--text-bright)', 'var(--text-bright)'), css)

# Make sure we change the chat input bar background too
css = css.replace("background: linear-gradient(0deg, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);", "background: #ffffff;")
css = css.replace("background-color: rgba(15, 23, 42, 0.8);", "background-color: #f1f5f9;")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("CSS fixed.")

# 2. Fix JS logic for admin bypass in ALL PLACES (registration success, login success, loadUserData)
js_path = "website/assistant.js"
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# Make sure after registration we force sub=vip if admin
target_reg = """        if(response.ok) {
            userDetails.name = name;
            userDetails.webapp_registered = true;
            document.getElementById('registration-view').style.display = 'none';
            switchView('dashboard');
            renderDashboard();
            if (userDetails.sub === 'none') {
                document.getElementById('payment-modal').style.display = 'flex';
            }
        }"""
replacement_reg = """        if(response.ok) {
            userDetails.name = name;
            userDetails.webapp_registered = true;
            
            if (String(userId) === '5543183063') {
                userDetails.is_admin = true;
                userDetails.sub = 'vip';
            }
            
            document.getElementById('registration-view').style.display = 'none';
            
            if (userDetails.is_admin) {
                document.getElementById('admin-menu-grid').classList.remove('hidden');
            }
            
            switchView('dashboard');
            renderDashboard();
            if (userDetails.sub === 'none') {
                document.getElementById('payment-modal').style.display = 'flex';
            }
        }"""
if "if (String(userId) === '5543183063')" not in js.split("function register(e)")[1]:
    js = js.replace(target_reg, replacement_reg)

# Force it directly below userId definition
target_user = "const userUsername = tgUser.username || '';"
replacement_user = "const userUsername = tgUser.username || '';\n// GLOBAL OVERRIDE\nif (String(userId) === '5543183063') { window.FORCE_ADMIN = true; }"
if "window.FORCE_ADMIN" not in js:
    js = js.replace(target_user, replacement_user)

# In btn-agree-warning:
target_agree = """    if (userDetails.is_admin) {"""
replacement_agree = """    if (window.FORCE_ADMIN) {
        userDetails.is_admin = true;
        userDetails.sub = 'vip';
    }
    if (userDetails.is_admin) {"""
if "if (window.FORCE_ADMIN) {" not in js:
    js = js.replace(target_agree, replacement_agree)


with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)
print("JS fixed.")

# Cache bust
import time
html_path = "website/templates/assistant.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()
ts = int(time.time())
html = re.sub(r'assistant\.css\?v=\d+', f'assistant.css?v={ts}', html)
html = re.sub(r'assistant\.js\?v=\d+', f'assistant.js?v={ts}', html)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Cache busted.")
