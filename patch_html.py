import re

with open('website/templates/assistant.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Admin Dashboard elements
admin_html = '''
    <!-- Admin Stats View -->
    <div class="chat-container hidden" id="admin-stats-view">
        <header class="chat-header" style="background: linear-gradient(180deg, #1e1b4b 0%, #0f172a 100%); border-bottom: 2px solid #8b5cf6;">
            <div class="header-left">
                <button class="action-btn back-btn" id="admin-back-btn" title="Back to Menu" style="margin-right: 10px; font-size: 1.3rem;">
                    <i class="fa-solid fa-chevron-left"></i>
                </button>
                <div class="header-info">
                    <h1 class="header-title" id="admin-title-text" style="color: #a78bfa;">ADMIN DASHBOARD</h1>
                    <div class="header-status">
                        <span class="status-dot" style="background-color: #a78bfa; box-shadow: 0 0 8px #a78bfa;"></span>
                        <span class="status-text" id="admin-status-text" style="color: #c4b5fd;">STATISTICS & USERS</span>
                    </div>
                </div>
            </div>
        </header>

        <main class="dashboard-content" style="flex: 1; overflow-y: auto; padding: 20px;">
            <div id="admin-stats-content">
                <!-- Dynamically populated -->
            </div>
        </main>
    </div>
'''

if 'id="admin-stats-view"' not in html:
    html = html.replace('<!-- Custom Script -->', admin_html + '\n    <!-- Custom Script -->')

# Add Admin menu buttons to the Dashboard view
admin_menu_html = '''
            <!-- Admin Actions Grid -->
            <div class="menu-grid hidden" id="admin-menu-grid" style="margin-top: 20px;">
                <h3 style="color: #8b5cf6; margin-bottom: 10px; font-family: var(--font-display); border-bottom: 1px solid #334155; padding-bottom: 5px;">ADMIN PANEL</h3>
                <button class="menu-card" id="btn-admin-courses" style="border-left: 4px solid #3b82f6;">
                    <div class="card-icon" style="background-color: rgba(59, 130, 246, 0.15); color: #3b82f6;"><i class="fa-solid fa-book"></i></div>
                    <div class="card-details"><h3>Курсы (Darslar)</h3><p>View standard courses</p></div>
                    <div class="card-arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </button>
                <button class="menu-card" id="btn-admin-users" style="border-left: 4px solid #10b981;">
                    <div class="card-icon" style="background-color: rgba(16, 185, 129, 0.15); color: #10b981;"><i class="fa-solid fa-users"></i></div>
                    <div class="card-details"><h3>Список пользователей</h3><p>All registered users</p></div>
                    <div class="card-arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </button>
                <button class="menu-card" id="btn-admin-paid" style="border-left: 4px solid #f59e0b;">
                    <div class="card-icon" style="background-color: rgba(245, 158, 11, 0.15); color: #f59e0b;"><i class="fa-solid fa-credit-card"></i></div>
                    <div class="card-details"><h3>Оплатившие</h3><p>Paid subscribers</p></div>
                    <div class="card-arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </button>
                <button class="menu-card" id="btn-admin-progress" style="border-left: 4px solid #8b5cf6;">
                    <div class="card-icon" style="background-color: rgba(139, 92, 246, 0.15); color: #8b5cf6;"><i class="fa-solid fa-chart-line"></i></div>
                    <div class="card-details"><h3>Прогресс студентов</h3><p>Students levels & lessons</p></div>
                    <div class="card-arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </button>
                <button class="menu-card" id="btn-admin-skipped" style="border-left: 4px solid #ef4444;">
                    <div class="card-icon" style="background-color: rgba(239, 68, 68, 0.15); color: #ef4444;"><i class="fa-solid fa-user-clock"></i></div>
                    <div class="card-details"><h3>Пропустившие урок</h3><p>Inactive users (>24h)</p></div>
                    <div class="card-arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </button>
            </div>
'''
if 'id="admin-menu-grid"' not in html:
    html = html.replace('<!-- Action 3: Take Level Exam -->', admin_menu_html + '\n                <!-- Action 3: Take Level Exam -->')

# Add Voice Record button and audio player
voice_input_html = '''
            <div class="input-wrapper">
                <button class="send-btn" id="voice-btn" style="background-color: #3b82f6; width: 36px; height: 36px; color: #fff; margin-right: 5px;" title="Hold to record">
                    <i class="fa-solid fa-microphone"></i>
                </button>
                <textarea id="message-input" placeholder="Schreibe eine Nachricht..." rows="1"></textarea>
                <button class="send-btn" id="send-btn">
                    <i class="fa-solid fa-paper-plane"></i>
                </button>
            </div>
            <audio id="tts-audio-player" style="display:none;"></audio>
'''

html = re.sub(r'<div class="input-wrapper">\s*<textarea id="message-input"[\s\S]*?</button>\s*</div>', voice_input_html, html)


with open('website/templates/assistant.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('assistant.html patched')
