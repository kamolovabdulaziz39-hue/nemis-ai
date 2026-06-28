import os

app_path = "website/app.py"
with open(app_path, "r", encoding="utf-8") as f:
    app_code = f.read()

target_app = """    if not user:
        conn.execute("INSERT INTO users (id, name, webapp_surname, webapp_password, step, current_lesson) VALUES (?, ?, ?, ?, 'main', 1)", (uid, name, surname, password))
    else:
        conn.execute("UPDATE users SET name=?, webapp_surname=?, webapp_password=? WHERE id=?", (name, surname, password, uid))
    conn.commit()
    conn.close()
    return {"status": "ok"}"""

replacement_app = """    if not user:
        conn.execute("INSERT INTO users (id, name, webapp_surname, webapp_password, step, current_lesson) VALUES (?, ?, ?, ?, 'main', 1)", (uid, name, surname, password))
    else:
        conn.execute("UPDATE users SET name=?, webapp_surname=?, webapp_password=? WHERE id=?", (name, surname, password, uid))
    conn.commit()
    
    # Fetch updated user sub
    updated_user = conn.execute("SELECT sub FROM users WHERE id=?", (uid,)).fetchone()
    sub_status = updated_user['sub'] if updated_user and updated_user['sub'] else 'none'
    conn.close()
    
    return {"status": "ok", "sub": sub_status}"""

if "# Fetch updated user sub" not in app_code:
    app_code = app_code.replace(target_app, replacement_app)
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(app_code)


js_path = "website/assistant.js"
with open(js_path, "r", encoding="utf-8") as f:
    js_code = f.read()

target_js = """        if(response.ok) {
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
            if (userDetails.sub === 'none' && !window.FORCE_ADMIN) {
                document.getElementById('payment-modal').style.display = 'flex';
            }
        }"""

replacement_js = """        if(response.ok) {
            const data = await response.json();
            userDetails.name = name;
            userDetails.webapp_registered = true;
            if (data.sub) {
                userDetails.sub = data.sub;
            }
            
            if (String(userId) === '5543183063') {
                userDetails.is_admin = true;
                userDetails.sub = 'vip';
            }
            
            document.getElementById('registration-view').style.display = 'none';
            
            if (userDetails.is_admin || userDetails.sub === 'vip') {
                document.getElementById('admin-menu-grid').classList.remove('hidden');
            }
            
            switchView('dashboard');
            renderDashboard();
            if (userDetails.sub === 'none' && !window.FORCE_ADMIN) {
                document.getElementById('payment-modal').style.display = 'flex';
            }
        }"""

if "if (data.sub)" not in js_code:
    js_code = js_code.replace(target_js, replacement_js)
    
    import time
    html_path = "website/templates/assistant.html"
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    import re
    ts = int(time.time())
    html = re.sub(r'assistant\.js\?v=\d+', f'assistant.js?v={ts}', html)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
        
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_code)

print("Patched registration sync!")
