import os

html_path = 'website/templates/assistant.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

modal_code = """
    <!-- Lesson 1 Test Modal -->
    <div class="modal hidden" id="lesson1-test-modal" style="z-index: 2000;">
        <div class="modal-content" style="background: var(--bg-color); border: 2px solid var(--accent-gold); max-width: 90%; height: auto; max-height: 80vh; overflow-y: auto;">
            <div class="modal-header" style="border-bottom: 1px solid var(--border-color); padding-bottom: 15px; margin-bottom: 15px;">
                <h2 style="font-size: 1.5rem; color: var(--accent-gold); font-family: var(--font-display);">1-Dars Testi</h2>
                <p style="font-size: 0.9rem; color: var(--text-color); margin-top: 5px;">Keyingi darsga o'tish uchun ushbu testdan o'tishingiz shart!</p>
            </div>
            
            <div id="lesson1-test-questions" style="margin-bottom: 20px;">
                <!-- Test questions will be injected here dynamically -->
            </div>
            
            <button class="action-btn primary-btn w-100" id="submit-lesson1-test-btn" style="margin-bottom: 10px;">Tekshirish</button>
            <button class="action-btn w-100" id="close-lesson1-test-btn" style="background: var(--card-color); color: var(--text-color);">Bekor qilish</button>
        </div>
    </div>
"""

if 'id="lesson1-test-modal"' not in html:
    html = html.replace('<!-- Payment Required Modal -->', modal_code + '\n    <!-- Payment Required Modal -->')
    import time
    import re
    ts = int(time.time())
    html = re.sub(r'assistant\.js\?v=\d+', f'assistant.js?v={ts}', html)
    html = re.sub(r'assistant\.css\?v=\d+', f'assistant.css?v={ts}', html)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Injected modal HTML')
else:
    print('Modal already exists')
