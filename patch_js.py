import re

with open('website/assistant.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update acceptChallengeBtn logic to bypass auth if is_admin
auth_logic_target = '''
    // Instead of dashboard, show auth views
    if (userDetails.webapp_registered) {
        document.getElementById('login-view').style.display = 'flex';
    } else {
        document.getElementById('registration-view').style.display = 'flex';
    }
'''

auth_logic_replacement = '''
    // Instead of dashboard, show auth views
    if (userDetails.is_admin) {
        document.getElementById('admin-menu-grid').classList.remove('hidden');
        switchView('dashboard');
    } else if (userDetails.webapp_registered) {
        document.getElementById('login-view').style.display = 'flex';
    } else {
        document.getElementById('registration-view').style.display = 'flex';
    }
'''

if 'userDetails.is_admin' not in js:
    js = js.replace(auth_logic_target, auth_logic_replacement)

# 2. Add is_admin parsing in loadUserData
user_data_target = "userDetails.webapp_registered = data.webapp_registered || false;"
user_data_replacement = "userDetails.webapp_registered = data.webapp_registered || false;\n            userDetails.is_admin = data.is_admin || false;"
if 'userDetails.is_admin = data.is_admin' not in js:
    js = js.replace(user_data_target, user_data_replacement)

# 3. Add Voice Recording logic
voice_logic = '''
// Voice Recording Logic
let mediaRecorder;
let audioChunks = [];
const voiceBtn = document.getElementById('voice-btn');
const ttsAudioPlayer = document.getElementById('tts-audio-player');
let isRecording = false;

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    voiceBtn.addEventListener('mousedown', startRecording);
    voiceBtn.addEventListener('touchstart', startRecording);
    voiceBtn.addEventListener('mouseup', stopRecording);
    voiceBtn.addEventListener('touchend', stopRecording);
} else {
    voiceBtn.style.display = 'none';
}

async function startRecording(e) {
    e.preventDefault();
    if (isRecording) return;
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];
        
        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };
        
        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
            sendVoiceMessage(audioBlob);
            stream.getTracks().forEach(track => track.stop());
        };
        
        mediaRecorder.start();
        isRecording = true;
        voiceBtn.style.backgroundColor = '#ef4444'; // Red while recording
        voiceBtn.classList.add('pulse-anim');
        
        if (tg.HapticFeedback) tg.HapticFeedback.impactOccurred('heavy');
    } catch (err) {
        console.error("Mic error:", err);
        alert("Mikrofon ruxsat etilmagan / Microphone access denied.");
    }
}

function stopRecording(e) {
    e.preventDefault();
    if (!isRecording) return;
    mediaRecorder.stop();
    isRecording = false;
    voiceBtn.style.backgroundColor = '#3b82f6';
    voiceBtn.classList.remove('pulse-anim');
}

async function sendVoiceMessage(audioBlob) {
    // Show user message (Voice Note)
    addMessage("🎤 <i>Ovozli xabar (Voice message)</i>", 'user');
    showTyping();
    
    // Convert blob to base64
    const reader = new FileReader();
    reader.readAsDataURL(audioBlob);
    reader.onloadend = async function() {
        const base64AudioMessage = reader.result;
        
        try {
            const response = await fetch('/assistant/query_voice', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ audio: base64AudioMessage, lang: userLang })
            });
            
            hideTyping();
            if (response.ok) {
                const data = await response.json();
                addMessage(data.answer, 'bot');
                
                // Play TTS audio
                if (data.audio_base64) {
                    ttsAudioPlayer.src = data.audio_base64;
                    ttsAudioPlayer.play();
                }
            } else {
                addMessage('Fehler bei der Verbindung mit dem Server.', 'bot');
            }
        } catch (err) {
            hideTyping();
            addMessage('Netzwerkfehler.', 'bot');
        }
    };
}
'''
if 'let mediaRecorder;' not in js:
    js += '\n' + voice_logic

# 4. Add Admin Dashboard Logic
admin_logic = '''
// Admin Dashboard Logic
const adminStatsView = document.getElementById('admin-stats-view');
const adminBackBtn = document.getElementById('admin-back-btn');
const adminStatsContent = document.getElementById('admin-stats-content');
views['adminStats'] = adminStatsView;

if (adminBackBtn) {
    adminBackBtn.addEventListener('click', () => {
        switchView('dashboard');
    });
}

async function fetchAdminStats(type) {
    switchView('adminStats');
    adminStatsContent.innerHTML = '<div style="text-align:center; padding: 40px; color: var(--accent-gold);"><i class="fa-solid fa-spinner fa-spin fa-2x"></i><br>Yuklanmoqda...</div>';
    document.getElementById('admin-title-text').textContent = "ADMIN DASHBOARD";
    
    try {
        const response = await fetch(API_BASE + '/api/admin_stats', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId })
        });
        
        if (!response.ok) {
            adminStatsContent.innerHTML = 'Error loading stats';
            return;
        }
        
        const data = await response.json();
        let html = '';
        
        if (type === 'users') {
            document.getElementById('admin-status-text').textContent = `Total: ${data.total_users} users`;
            html += `<h2 style="color:#10b981; margin-bottom: 15px;">Foydalanuvchilar ro'yxati (${data.total_users})</h2>`;
            html += '<table style="width:100%; border-collapse:collapse; color:#cbd5e1; font-size:0.9rem;"><tr><th style="border-bottom:1px solid #334155; padding:8px; text-align:left;">ID</th><th style="border-bottom:1px solid #334155; padding:8px; text-align:left;">Name</th></tr>';
            data.users.forEach(u => {
                html += `<tr><td style="border-bottom:1px solid #1e293b; padding:8px;">${u.id}</td><td style="border-bottom:1px solid #1e293b; padding:8px;">${u.name || '-'}</td></tr>`;
            });
            html += '</table>';
        } 
        else if (type === 'paid') {
            document.getElementById('admin-status-text').textContent = `Total Paid: ${data.total_paid}`;
            html += `<h2 style="color:#f59e0b; margin-bottom: 15px;">To'lov qilganlar (${data.total_paid})</h2>`;
            html += '<table style="width:100%; border-collapse:collapse; color:#cbd5e1; font-size:0.9rem;"><tr><th style="border-bottom:1px solid #334155; padding:8px; text-align:left;">ID</th><th style="border-bottom:1px solid #334155; padding:8px; text-align:left;">Name</th><th style="border-bottom:1px solid #334155; padding:8px; text-align:left;">Sub</th></tr>';
            data.paid.forEach(u => {
                html += `<tr><td style="border-bottom:1px solid #1e293b; padding:8px;">${u.id}</td><td style="border-bottom:1px solid #1e293b; padding:8px;">${u.name || '-'}</td><td style="border-bottom:1px solid #1e293b; padding:8px; color:#10b981;">${u.sub}</td></tr>`;
            });
            html += '</table>';
        }
        else if (type === 'progress') {
            document.getElementById('admin-status-text').textContent = `Progress Distribution`;
            html += `<h2 style="color:#8b5cf6; margin-bottom: 15px;">Talabalar progressi</h2>`;
            html += '<div style="display:flex; flex-direction:column; gap:10px;">';
            for (const [levelLesson, count] of Object.entries(data.progress)) {
                html += `<div style="background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.3); padding: 10px; border-radius: 8px; display:flex; justify-content:space-between;"><span>${levelLesson}</span><span style="font-weight:bold; color:#a78bfa;">${count} o'quvchi</span></div>`;
            }
            html += '</div>';
        }
        else if (type === 'skipped') {
            document.getElementById('admin-status-text').textContent = `Skipped: ${data.skipped.length}`;
            html += `<h2 style="color:#ef4444; margin-bottom: 15px;">Dars qoldirganlar (>24h)</h2>`;
            html += '<table style="width:100%; border-collapse:collapse; color:#cbd5e1; font-size:0.9rem;"><tr><th style="border-bottom:1px solid #334155; padding:8px; text-align:left;">ID</th><th style="border-bottom:1px solid #334155; padding:8px; text-align:left;">Name</th><th style="border-bottom:1px solid #334155; padding:8px; text-align:left;">Last Activity</th></tr>';
            data.skipped.forEach(u => {
                html += `<tr><td style="border-bottom:1px solid #1e293b; padding:8px;">${u.id}</td><td style="border-bottom:1px solid #1e293b; padding:8px;">${u.name || '-'}</td><td style="border-bottom:1px solid #1e293b; padding:8px; color:#f87171;">${u.last_activity}</td></tr>`;
            });
            html += '</table>';
        }
        
        adminStatsContent.innerHTML = html;
        
    } catch (err) {
        adminStatsContent.innerHTML = 'Network error loading stats';
    }
}

// Bind Admin buttons
const btnAdminCourses = document.getElementById('btn-admin-courses');
if (btnAdminCourses) btnAdminCourses.addEventListener('click', () => switchView('lessonsList'));

const btnAdminUsers = document.getElementById('btn-admin-users');
if (btnAdminUsers) btnAdminUsers.addEventListener('click', () => fetchAdminStats('users'));

const btnAdminPaid = document.getElementById('btn-admin-paid');
if (btnAdminPaid) btnAdminPaid.addEventListener('click', () => fetchAdminStats('paid'));

const btnAdminProgress = document.getElementById('btn-admin-progress');
if (btnAdminProgress) btnAdminProgress.addEventListener('click', () => fetchAdminStats('progress'));

const btnAdminSkipped = document.getElementById('btn-admin-skipped');
if (btnAdminSkipped) btnAdminSkipped.addEventListener('click', () => fetchAdminStats('skipped'));
'''
if 'const adminStatsView =' not in js:
    js += '\n' + admin_logic

with open('website/assistant.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('assistant.js patched')
