// Initialize Telegram Web App SDK
window.onerror = function(msg, url, line, col, error) {
    document.body.innerHTML += '<div style="position:fixed;top:0;left:0;z-index:99999;background:red;color:white;padding:20px;font-size:16px;">ERROR: ' + msg + '<br>Line: ' + line + '</div>';
};
const tg = window.Telegram.WebApp;
tg.expand();

// Base URL for all API calls - works with tunnels like Cloudflare
const API_BASE = window.location.origin;

// DOM elements
const chatHistory = document.getElementById('chat-history');
const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');
const clearBtn = document.getElementById('clear-btn');
const titleText = document.getElementById('chat-title-text');
const statusText = document.getElementById('chat-status-text');

// User settings & Localization
let userLang = localStorage.getItem('userLang') || 'de';
if (!localStorage.getItem('userLang') && tg.initDataUnsafe && tg.initDataUnsafe.user && tg.initDataUnsafe.user.language_code) {
    const code = tg.initDataUnsafe.user.language_code.toLowerCase();
    if (code === 'uz') userLang = 'uz';
    else if (code === 'ru') userLang = 'ru';
}

const LOCALIZATION = {
    de: {
        title: "ABDULAZIZ GERMAN AI",
        status: "DEUTSCH TUTOR // ONLINE",
        welcome: "Hallo! Ich bin dein Deutsch-Assistent. Wie kann ich dir heute beim Deutschlernen oder bei der Vorbereitung auf die B1-Prüfung helfen?",
        placeholder: "Schreibe eine Nachricht...",
        clearConfirm: "Möchtest du den Chat-Verlauf wirklich löschen?",
        dashboardTitle: "ABDULAZIZ GERMAN AI",
        dashboardStatus: "DEUTSCH TUTOR // ONLINE",
        welcomeUser: "Hallo, ",
        welcomeSub: "Lass uns gemeinsam das B1-Niveau in Deutsch erreichen!",
        progressLabel: "Niveau Fortschritt",
        lektionLabel: "Lektion",
        btnReadLessonTitle: "Heutige Lektion lesen",
        btnReadLessonDesc: "Grammatikregeln, Vokabeln und Übungen",
        btnChatTutorTitle: "Gespräch mit dem KI-Tutor",
        btnChatTutorDesc: "Fragen stellen und Konversation üben",
        btnTakeExamTitle: "Niveauprüfung ablegen",
        btnTakeExamDesc: "Verfügbar nach Abschluss von 60 Lektionen",
        backToMenu: "Zurück",
        completeLesson: "Lektion beenden",
        loadingLesson: "Lektion wird geladen...",
        lessonCompletedMsg: "Lektion abgeschlossen! Tolle Arbeit.",
        completeLessonConfirm: "Möchtest du diese Lektion wirklich als abgeschlossen markieren?",
        btnChangeLevel: "Niveaus // Stufen",
        ratingLabel: "Studienbewertung:"
    },
    uz: {
        title: "ABDULAZIZ NEMIS AI",
        status: "NEMIS TILI TUTORI // ONLINE",
        welcome: "Hallo! Men nemis tili bo'yicha AI-yordamchingizman. Nemis tilini o'rganishda va B1 imtihoniga (Ausbildung/ish) tayyorlanishda qanday yordam bera olaman?",
        placeholder: "Xabar yozing...",
        clearConfirm: "Chat tarixini o'chirishni xohlaysizmi?",
        dashboardTitle: "ABDULAZIZ NEMIS AI",
        dashboardStatus: "NEMIS TILI TUTORI // ONLINE",
        welcomeUser: "Salom, ",
        welcomeSub: "Nemis tili B1 darajasiga birgalikda erishamiz!",
        progressLabel: "Daraja progressi",
        lektionLabel: "Dars",
        btnReadLessonTitle: "Bugungi darsni o'qish",
        btnReadLessonDesc: "Barcha 60 ta darslar va mashqlar",
        btnChatTutorTitle: "AI Repetitor bilan suhbat",
        btnChatTutorDesc: "Savol-javob va mashq qilish",
        btnTakeExamTitle: "Daraja Imtihonini topshirish",
        btnTakeExamDesc: "60 ta dars tugagandan so'ng faollashadi",
        backToMenu: "Orqaga",
        completeLesson: "Darsni yakunlash",
        loadingLesson: "Dars yuklanmoqda...",
        lessonCompletedMsg: "Dars muvaffaqiyatli yakunlandi! Keyingi darsga o'tildi.",
        completeLessonConfirm: "Darsni yakunlashni xohlaysizmi?",
        btnChangeLevel: "Darajalar / Уровни",
        ratingLabel: "O'qish reytingi:"
    },
    ru: {
        title: "ABDULAZIZ NEMIS AI",
        status: "РЕПЕТИТОР НЕМЕЦКОГО // ОНЛАЙН",
        welcome: "Hallo! Я твой ИИ-помощник по немецкому языку. Чем я могу помочь тебе сегодня в изучении немецкого языка и подготовке к экзамену B1?",
        placeholder: "Напишите сообщение...",
        clearConfirm: "Вы уверены, что хотите очистить историю чата?",
        dashboardTitle: "ABDULAZIZ NEMIS AI",
        dashboardStatus: "РЕПЕТИТОР НЕМЕЦКОГО // ОНЛАЙН",
        welcomeUser: "Привет, ",
        welcomeSub: "Давайте вместе достигнем уровня B1 в немецком языке!",
        progressLabel: "Прогресс уровня",
        lektionLabel: "Урок",
        btnReadLessonTitle: "Читать сегодняшний урок",
        btnReadLessonDesc: "Все 60 уроков и упражнения",
        btnChatTutorTitle: "Чат с ИИ-репетитором",
        btnChatTutorDesc: "Вопросы, ответы и разговорная практика",
        btnTakeExamTitle: "Сдать экзамен уровня",
        btnTakeExamDesc: "Активируется после прохождения 60 уроков",
        backToMenu: "Назад",
        completeLesson: "Завершить урок",
        loadingLesson: "Загрузка урока...",
        lessonCompletedMsg: "Урок успешно завершен! Переходим к следующему уроку.",
        completeLessonConfirm: "Вы уверены, что хотите завершить текущий урок?",
        btnChangeLevel: "Уровни / Darajalar",
        ratingLabel: "Рейтинг обучения:"
    }
};

let texts = LOCALIZATION[userLang] || LOCALIZATION['de'];

function applyLanguage(lang) {
    userLang = lang;
    texts = LOCALIZATION[userLang] || LOCALIZATION['de'];
    
    // Update global UI Elements if they exist
    if (titleText) titleText.textContent = texts.title;
    if (statusText) statusText.textContent = texts.status;
    if (messageInput) messageInput.placeholder = texts.placeholder;
    
    // If dashboard is visible, re-render to update text
    if (views && views.dashboard && !views.dashboard.classList.contains('hidden')) {
        renderDashboard();
    }
}

// Initial application will be called at the bottom after initialization


// Apply Telegram theme colors dynamically
document.documentElement.style.setProperty('--tg-theme-bg-color', tg.backgroundColor || '#111215');
document.documentElement.style.setProperty('--tg-theme-text-color', tg.textColor || '#ffffff');
document.documentElement.style.setProperty('--tg-theme-hint-color', tg.hintColor || '#8e9297');
document.documentElement.style.setProperty('--tg-theme-button-color', tg.buttonColor || '#e63946');
document.documentElement.style.setProperty('--tg-theme-button-text-color', tg.buttonTextColor || '#ffffff');

// Local storage session key
const STORAGE_KEY = 'nemis_chat_history';

// Modal Elements
const welcomeModal = document.getElementById('welcome-modal');
const screenLevel = document.getElementById('screen-level');
const screenWarning = document.getElementById('screen-warning');
const warningTextContent = document.getElementById('warning-text-content');
const acceptChallengeBtn = document.getElementById('accept-challenge-btn');
const declineChallengeBtn = document.getElementById('decline-challenge-btn');

let selectedLevel = localStorage.getItem('nemis_selected_level') || '';
let challengeAccepted = localStorage.getItem('nemis_challenge_accepted') === 'true';

// Load history or initialize
let history = [];
try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
        history = JSON.parse(saved);
    }
} catch (e) {
    console.error("Error reading from localStorage", e);
}

// Render history
function renderChat() {
    chatHistory.innerHTML = '';
    
    // If empty history, add default welcome message
    if (history.length === 0) {
        let msg = texts.welcome;
        if (selectedLevel) {
            msg += ` (Niveau: ${selectedLevel})`;
        }
        addMessage(msg, 'bot', false);
    } else {
        history.forEach(msg => {
            addMessage(msg.text, msg.sender, false);
        });
    }
    scrollToBottom();
}

// Add message element to chat screen
function addMessage(text, sender, save = true) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', sender === 'user' ? 'message-user' : 'message-bot');
    
    const bubble = document.createElement('div');
    bubble.classList.add('message-bubble');
    
    // Render text with markdown format linebreaks
    bubble.innerHTML = formatMarkdown(text);
    
    msgDiv.appendChild(bubble);
    chatHistory.appendChild(msgDiv);
    
    if (save) {
        history.push({ text, sender });
        saveHistory();
    }
    scrollToBottom();
}

// Simple markdown formatter
function formatMarkdown(text) {
    if (!text) return '';
    let escaped = text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
    
    // Code blocks
    escaped = escaped.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
    // Inline code
    escaped = escaped.replace(/`([^`]+)`/g, '<code>$1</code>');
    // Bold
    escaped = escaped.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    escaped = escaped.replace(/\*([^*]+)\*/g, '<strong>$1</strong>');
    // Linebreaks
    return escaped.replace(/\n/g, '<br>');
}

function saveHistory() {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
    } catch (e) {
        console.error("Error saving to localStorage", e);
    }
}

function scrollToBottom() {
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

// Show/Hide typing indicator
let typingIndicator = null;
function showTyping() {
    if (typingIndicator) return;
    
    typingIndicator = document.createElement('div');
    typingIndicator.classList.add('message', 'message-bot');
    
    const bubble = document.createElement('div');
    bubble.classList.add('message-bubble', 'typing-bubble');
    bubble.innerHTML = '<div class="typing-dots"><span></span><span></span><span></span></div>';
    
    typingIndicator.appendChild(bubble);
    chatHistory.appendChild(typingIndicator);
    scrollToBottom();
}

function hideTyping() {
    if (typingIndicator) {
        typingIndicator.remove();
        typingIndicator = null;
    }
}

async function loadChatHistoryFromServer() {
    try {
        const response = await fetch(API_BASE + '/api/get_chat_history', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId })
        });
        if (response.ok) {
            const data = await response.json();
            history = (data.history || []).map(item => ({
                text: item.text,
                sender: item.role === 'user' ? 'user' : 'bot'
            }));
            saveHistory();
        }
    } catch (e) {
        console.error("Error loading chat history from server", e);
    }
}

// Handle message submission
async function handleSubmit() {
    const question = messageInput.value.trim();
    if (!question) return;
    
    // Send feedback vibration
    if (tg.HapticFeedback && typeof tg.HapticFeedback.impactOccurred === 'function') {
        try { tg.HapticFeedback.impactOccurred('light'); } catch(e){}
    }
    
    messageInput.value = '';
    messageInput.style.height = 'auto';
    
    addMessage(question, 'user');
    showTyping();
    
    try {
        const response = await fetch('/assistant/query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId, question, lang: userLang })
        });
        
        let data = null;
        try {
            data = await response.json();
        } catch (e) {}
        
        hideTyping();
        
        if (response.ok && data && !data.error) {
            addMessage(data.answer || 'Fehler beim Laden der Antwort.', 'bot');
        } else {
            const msg = (data && data.message) || 'Fehler bei der Verbindung mit dem Server.';
            alert(msg);
            if (data && data.status === 'banned') {
                tg.close();
            } else if (data && data.status === 'warning') {
                addMessage(msg, 'bot');
            }
        }
    } catch (e) {
        hideTyping();
        addMessage('Netzwerkfehler.', 'bot');
    }
}

// Event listeners
sendBtn.addEventListener('click', handleSubmit);

messageInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleSubmit();
    }
});

// Auto-expand textarea height
messageInput.addEventListener('input', () => {
    messageInput.style.height = 'auto';
    messageInput.style.height = (messageInput.scrollHeight) + 'px';
});

clearBtn.addEventListener('click', async () => {
    if (confirm(texts.clearConfirm)) {
        if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
            try { tg.HapticFeedback.notificationOccurred('warning'); } catch(e){}
        }
        history = [];
        saveHistory();
        renderChat();
        
        try {
            await fetch(API_BASE + '/api/clear_chat_history', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user_id: userId })
            });
        } catch (e) {
            console.error("Error clearing history on server", e);
        }
    }
});

// Fetch Telegram User Info
const tgUser = (tg.initDataUnsafe && tg.initDataUnsafe.user) || { id: "12345678", first_name: "Local User", username: "localuser" };
const userId = tgUser.id;
const userName = tgUser.first_name || 'User';
const userUsername = tgUser.username || '';
// GLOBAL OVERRIDE
if (String(userId) === '5543183063') { window.FORCE_ADMIN = true; }

// Current state from DB
let currentLesson = 1;
const screenExam = document.getElementById('screen-exam');
const submitExamBtn = document.getElementById('submit-exam-btn');

// Modal Warning Screen helper
let currentWarningLang = userLang; // default to tg language
let isDeclinedState = false;

function showWarningScreen() {
    if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
        try { tg.HapticFeedback.notificationOccurred('warning'); } catch(e){}
    }
    screenLevel.classList.add('hidden');
    screenWarning.classList.remove('hidden');
    screenExam.classList.add('hidden');
    updateWarningText(currentWarningLang);
}

function updateWarningText(lang) {
    // Update active state of toggle buttons
    const langBtns = document.querySelectorAll('.modal-lang-btn');
    langBtns.forEach(btn => {
        if (btn.getAttribute('data-lang') === lang) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    const RULES_TEXT = {
        'uz': `
        <div style="text-align: left; font-size: 0.95rem; line-height: 1.5;">
            <strong>📜 Abdulaziz Nemis AI — Foydalanish Qoidalari va Ommaviy Oferta</strong><br><br>
            DIQQAT! Botdan foydalanishni boshlashdan oldin ushbu qoidalar bilan to‘liq tanishib chiqing. "Men roziman" tugmasini bosish orqali siz barcha shartlarga so‘zsiz rozilik bildirasiz.<br><br>
            
            <strong>1. 🛡️ Kiberxavfsizlik va Qonunchilik</strong><br>
            Botning dasturiy kodi, ma'lumotlar bazasi va Gemini Pro SI tizimi qonun bilan himoyalangan. Botni buzish (vzlom), serverga zararli hujumlar (DDoS/Spam) uyushtirish mutlaqo taqiqlanadi. Qoidabuzarlar hech qanday ogohlantirishsiz va puli qaytarilmasdan o‘chiriladi. Shuningdek, ma'lumotlar huquqni muhofaza qilish organlariga topshirilib, O‘zbekiston Respublikasi Jinoyat Kodeksining 278-moddasiga muvofiq jinoiy javobgarlikka tortiladi.<br><br>

            <strong>2. 🎴 Temir Intizom va Jarimalar</strong><br>
            Kursda qat'iy intizom tizimi joriy etilgan. Agar o‘quvchi 1 kun davomida botga kirmasa, darsni qoldirsa yoki uy vazifasini topshirmasa, uning natijasi avtomatik ravishda 4 ta darsga orqaga qaytariladi. Masalan, o‘quvchi 59-darsga kelib dars qoldirsa, progress darhol 55-darsga tushirib yuboriladi. Ushbu qoida barcha — A1, A2, B1 va B2 darajalarining hammasiga birdek amal qiladi. Keyingi darajaga faqat imtihon orqali o‘tiladi.<br><br>

            <strong>3. 💳 Obuna va To‘lov Shartlari</strong><br>
            Botdan to‘liq foydalanish muddati — to‘lov tasdiqlangan kundan boshlab 1 oy (30 kun). Oylik obuna narxi 100 000 so‘m. To‘lov to‘g‘ridan-to‘g‘ri Uzcard/Humo kartasiga o‘tkaziladi va chek (skrinshot) botga yuboriladi. Belgilangan 30 kun ichida darajani tugata olmagan o‘quvchilar keyingi oy uchun ham to‘lovni to‘liq amalga oshiradilar.<br><br>
            
            ⚠️ Muhim eslatma: Bot ma'muriyati foydalanish qoidalariga istalgan vaqtda o‘zgartirishlar, tuzatishlar yoki qo‘shimchalar kiritish huquqini o‘zida saqlab qoladi. Foydalanuvchilar o‘zgarishlardan xabardor bo‘lish uchun qoidalarni vaqti-vaqti bilan tekshirib turishlari tavsiya etiladi.
        </div>`,
        'ru': `
        <div style="text-align: left; font-size: 0.95rem; line-height: 1.5;">
            <strong>📜 Abdulaziz Nemis AI — Правила использования и Публичная оферта</strong><br><br>
            ВНИМАНИЕ! Перед началом использования бота, пожалуйста, полностью ознакомьтесь с данными правилами. Нажимая кнопку "Я согласен", вы безоговорочно принимаете все условия.<br><br>
            
            <strong>1. 🛡️ Кибербезопасность и Законодательство</strong><br>
            Программный код бота, база данных и система ИИ Gemini Pro защищены законом. Взлом бота, организация вредоносных атак (DDoS/Spam) на сервер категорически запрещены. Нарушители удаляются без предупреждения и возврата средств. Кроме того, данные передаются в правоохранительные органы для привлечения к уголовной ответственности в соответствии со статьей 278 Уголовного кодекса Республики Узбекистан.<br><br>

            <strong>2. 🎴 Железная дисциплина и Штрафы</strong><br>
            На курсе введена система строгой дисциплины. Если ученик не заходит в бота в течение 1 дня, пропускает урок или не сдает домашнее задание, его результат автоматически откатывается на 4 урока назад. Например, если ученик пропустит занятие на 59-м уроке, прогресс сразу же упадет до 55-го урока. Это правило применяется одинаково ко всем уровням: A1, A2, B1 и B2. Переход на следующий уровень осуществляется только через экзамен.<br><br>

            <strong>3. 💳 Условия подписки и оплаты</strong><br>
            Срок полного использования бота — ровно 1 месяц (30 дней) с момента подтверждения оплаты. Стоимость ежемесячной подписки составляет 100 000 сумов. Оплата переводится напрямую на карту Uzcard/Humo, а чек (скриншот) отправляется в бота. Ученики, не сумевшие завершить уровень в течение отведенных 30 дней, обязаны полностью оплатить и следующий месяц.<br><br>
            
            ⚠️ Важное примечание: Администрация бота оставляет за собой право в любое время вносить изменения, исправления или дополнения в правила использования. Пользователям рекомендуется периодически проверять правила, чтобы быть в курсе изменений.
        </div>`,
        'de': `
        <div style="text-align: left; font-size: 0.95rem; line-height: 1.5;">
            <strong>📜 Abdulaziz Nemis AI — Terms of Use & Public Offer</strong><br><br>
            ATTENTION! Before using the bot, please fully read these rules. By clicking the "I agree" button, you unconditionally agree to all terms and conditions.<br><br>
            
            <strong>1. 🛡️ Cybersecurity & Law</strong><br>
            The bot's source code, database, and Gemini Pro AI system are protected by law. Hacking the bot or organizing malicious attacks (DDoS/Spam) on the server is strictly prohibited. Violators will be removed without warning and without a refund. Additionally, information will be handed over to law enforcement agencies for criminal prosecution under Article 278 of the Criminal Code of the Republic of Uzbekistan.<br><br>

            <strong>2. 🎴 Iron Discipline & Penalties</strong><br>
            A strict discipline system is implemented in the course. If a student does not log into the bot for 1 day, misses a lesson, or fails to submit homework, their progress is automatically rolled back by 4 lessons. For example, if a student misses a class at lesson 59, their progress will immediately drop to lesson 55. This rule applies equally to all levels: A1, A2, B1, and B2. Advancing to the next level is only possible through an exam.<br><br>

            <strong>3. 💳 Subscription & Payment Terms</strong><br>
            The full usage period of the bot is exactly 1 month (30 days) from the date of payment confirmation. The monthly subscription fee is 100,000 UZS. Payment is made directly to a Uzcard/Humo card, and the receipt (screenshot) is sent to the bot. Students who fail to complete their level within the allotted 30 days must pay in full for the following month as well.<br><br>
            
            ⚠️ Important note: The bot administration reserves the right to make changes, corrections, or additions to the terms of use at any time. Users are advised to check the rules periodically to stay informed of any changes.
        </div>`
    };

    const BTN_TEXT = {
        'uz': { agree: '🟢 Men roziman', disagree: '❌ Yo\'q, rozimasman', disclaimer: 'Qoidalarni diqqat bilan o\'qing' },
        'ru': { agree: '🟢 Я согласен', disagree: '❌ Нет, я не согласен', disclaimer: 'Внимательно прочитайте правила' },
        'de': { agree: '🟢 I agree', disagree: '❌ No, I disagree', disclaimer: 'Read the rules carefully' }
    };
    
    warningTextContent.innerHTML = RULES_TEXT[lang] || RULES_TEXT['de'];
    
    const txts = BTN_TEXT[lang] || BTN_TEXT['de'];
    document.getElementById('accept-btn-text').textContent = txts.agree;
    
    // Check if decline btn exists
    const declineBtnText = document.getElementById('decline-btn-text');
    if(declineBtnText) declineBtnText.textContent = txts.disagree;
    
    document.getElementById('warning-disclaimer-text').textContent = txts.disclaimer;
}

function updateDeclinedText(lang) {
    const DECLINE_TEXT = {
        'uz': `
            <div style="text-align: center; font-size: 1.1rem; line-height: 1.6; padding: 20px 0; color: #f87171;">
                Biz tushunib turibmiz, shunday qilib dangasalik qilyapsiz. Lekin yordam, bu xizmatning hammasi faqat sizning foydangiz uchun!<br><br>
                Nemis tilini temir intizomsiz o'rganib bo'lmaydi. Qachonki o'zingizda kuch topib, dangasalikni yengib, natijaga erishishni chin dildan xoxlasangiz - ortga qaytsangiz, sizga yordam beramiz
            </div>
        `,
        'ru': `
            <div style="text-align: center; font-size: 1.1rem; line-height: 1.6; padding: 20px 0; color: #f87171;">
                Мы понимаем, что вам просто лень. Но помните, все эти правила существуют исключительно для вашей пользы!<br><br>
                Выучить немецкий без железной дисциплины невозможно. Когда вы найдете в себе силы побороть лень и по-настоящему захотите достичь результата — возвращайтесь, мы вам поможем!
            </div>
        `,
        'de': `
            <div style="text-align: center; font-size: 1.1rem; line-height: 1.6; padding: 20px 0; color: #f87171;">
                We understand you might just be feeling lazy. But remember, all these rules are strictly for your benefit!<br><br>
                Learning German is impossible without iron discipline. When you find the strength to overcome laziness and truly desire to achieve results — come back, and we will help you!
            </div>
        `
    };

    const TITLES = {
        'uz': '❌ RAD ETILDI',
        'ru': '❌ ОТКЛОНЕНО',
        'de': '❌ DECLINED'
    };
    
    const BTN = {
        'uz': 'Chiqish',
        'ru': 'Выход',
        'de': 'Exit'
    };

    document.getElementById('warning-title-text').textContent = TITLES[lang] || TITLES['de'];
    
    warningTextContent.innerHTML = (DECLINE_TEXT[lang] || DECLINE_TEXT['de']) + `
        <button onclick="tg.close()" style="margin-top: 20px; background: #3b82f6; border: none; color: white; border-radius: 12px; padding: 14px; width: 100%; font-weight: bold; cursor: pointer;">
            ${BTN[lang] || BTN['de']}
        </button>
    `;
}

// Bind language toggle buttons click
const langToggleBtns = document.querySelectorAll('.modal-lang-btn');
langToggleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        const selectedLang = btn.getAttribute('data-lang');
        currentWarningLang = selectedLang;
        if (isDeclinedState) {
            updateDeclinedText(currentWarningLang);
        } else {
            updateWarningText(currentWarningLang);
        }
        // Apply the language choice globally for the bot
        applyLanguage(selectedLang);
        // Optional: save to local storage so it remembers next time
        localStorage.setItem('userLang', selectedLang);
        if (tg.HapticFeedback && typeof tg.HapticFeedback.selectionChanged === 'function') {
            try { tg.HapticFeedback.selectionChanged(); } catch(e){}
        }
    });
});

// Fallback for cached HTML
if (!document.getElementById('lessons-list-view')) {
    const listHtml = `
    <div class="chat-container hidden" id="lessons-list-view">
        <header class="chat-header">
            <div class="header-left">
                <button class="action-btn back-btn" id="lessons-list-back-btn" title="Back to Menu" style="margin-right: 10px; font-size: 1.3rem;">
                    <i class="fa-solid fa-chevron-left"></i>
                </button>
                <div class="header-info">
                    <h1 class="header-title" id="lessons-list-title-text">DARSLAR RO'YXATI</h1>
                    <div class="header-status">
                        <span class="status-dot"></span>
                        <span class="status-text" id="lessons-list-status-text">60 LEKTIONEN</span>
                    </div>
                </div>
            </div>
        </header>
        <main class="dashboard-content" style="flex: 1; overflow-y: auto; padding: 20px;">
            <div class="level-grid" id="lessons-grid" style="grid-template-columns: repeat(4, 1fr); gap: 10px;">
            </div>
        </main>
    </div>`;
    document.body.insertAdjacentHTML('beforeend', listHtml);
}

// View Navigation Map
const views = {
    dashboard: document.getElementById('dashboard-view'),
    chat: document.getElementById('chat-view'),
    lesson: document.getElementById('lesson-view'),
    lessonsList: document.getElementById('lessons-list-view')
};

function switchView(viewName) {
    Object.keys(views).forEach(key => {
        if (!views[key]) return;
        if (key === viewName) {
            views[key].classList.remove('hidden');
        } else {
            views[key].classList.add('hidden');
        }
    });
    
    if (viewName === 'dashboard') {
        renderDashboard();
    }
}

// Render Dashboard values dynamically
function renderDashboard() {
    const progressLabelText = document.getElementById('progress-label-text');
    const progressValueText = document.getElementById('progress-value-text');
    const progressBarFill = document.getElementById('progress-bar-fill');
    const levelBadgeVal = document.getElementById('level-badge-val');
    
    const dashboardTitleText = document.getElementById('dashboard-title-text');
    const dashboardStatusText = document.getElementById('dashboard-status-text');
    
    const cardReadTitle = document.getElementById('card-read-title');
    const cardReadDesc = document.getElementById('card-read-desc');
    const cardChatTitle = document.getElementById('card-chat-title');
    const cardChatDesc = document.getElementById('card-chat-desc');
    const cardExamTitle = document.getElementById('card-exam-title');
    const cardExamDesc = document.getElementById('card-exam-desc');
    
    const completeBtnLbl = document.getElementById('complete-btn-lbl');
    const lessonLoadingText = document.getElementById('lesson-loading-text');

    // Populate localized dashboard elements
    dashboardTitleText.textContent = texts.dashboardTitle || "ABDULAZIZ GERMAN AI";
    dashboardStatusText.textContent = texts.dashboardStatus || "DEUTSCH TUTOR // ONLINE";
    
    // Populate profile details
    const nameEl = document.getElementById('profile-name');
    const usernameEl = document.getElementById('profile-username');
    const phoneEl = document.getElementById('profile-phone');
    
    if (nameEl) nameEl.textContent = userDetails.name;
    if (usernameEl) usernameEl.textContent = userDetails.username ? `@${userDetails.username.replace('@', '')}` : '';
    if (phoneEl) phoneEl.textContent = userDetails.phone || '';
    
    // Calculate and populate rating percentage
    const maxL = 60;
    const ratingPct = Math.min(100, Math.round(((currentLesson - 1) / maxL) * 100));
    const ratingValEl = document.getElementById('profile-rating-val');
    if (ratingValEl) {
        ratingValEl.textContent = `${ratingPct}%`;
    }
    
    // Localize rating label text
    const ratingLblText = document.getElementById('rating-lbl-text');
    if (ratingLblText) {
        ratingLblText.textContent = texts.ratingLabel || "O'qish reytingi / Рейтинг обучения:";
    }
    
    // Localize change level button
    const changeLevelBtnText = document.getElementById('change-level-btn-text');
    if (changeLevelBtnText) {
        changeLevelBtnText.textContent = texts.btnChangeLevel || "Darajalar / Уровни";
    }

    // Determine status badge
    let statusText = '';
    if (userLang === 'uz') {
        if (ratingPct >= 90) statusText = "Mukammal 👑";
        else if (ratingPct >= 70) statusText = "A'lochi 🌟";
        else if (ratingPct >= 40) statusText = "Yaxshi 👍";
        else if (ratingPct >= 15) statusText = "Harakatda 🚀";
        else statusText = "Boshlang'ich 🐣";
    } else if (userLang === 'ru') {
        if (ratingPct >= 90) statusText = "В совершенстве 👑";
        else if (ratingPct >= 70) statusText = "Отличник 🌟";
        else if (ratingPct >= 40) statusText = "Хорошо 👍";
        else if (ratingPct >= 15) statusText = "Активный 🚀";
        else statusText = "Начинающий 🐣";
    } else {
        if (ratingPct >= 90) statusText = "Perfekt 👑";
        else if (ratingPct >= 70) statusText = "Ausgezeichnet 🌟";
        else if (ratingPct >= 40) statusText = "Gut 👍";
        else if (ratingPct >= 15) statusText = "Aktiver Student 🚀";
        else statusText = "Anfänger 🐣";
    }

    const statusBadgeEl = document.getElementById('profile-status-badge');
    if (statusBadgeEl) {
        statusBadgeEl.textContent = statusText;
        if (ratingPct < 15) {
            statusBadgeEl.style.color = '#ff9900';
            statusBadgeEl.style.backgroundColor = 'rgba(255, 153, 0, 0.1)';
            statusBadgeEl.style.borderColor = 'rgba(255, 153, 0, 0.25)';
        } else if (ratingPct >= 90) {
            statusBadgeEl.style.color = 'var(--accent-gold)';
            statusBadgeEl.style.backgroundColor = 'rgba(255, 204, 0, 0.1)';
            statusBadgeEl.style.borderColor = 'rgba(255, 204, 0, 0.25)';
        } else {
            statusBadgeEl.style.color = '#00ff66';
            statusBadgeEl.style.backgroundColor = 'rgba(0, 255, 102, 0.1)';
            statusBadgeEl.style.borderColor = 'rgba(0, 255, 102, 0.25)';
        }
    }
    
    progressLabelText.textContent = texts.progressLabel || "Daraja progressi";
    progressValueText.textContent = `${texts.lektionLabel || "Lektion"}: ${currentLesson}/${maxL}`;
    
    const pct = Math.min(100, Math.floor(((currentLesson - 1) / maxL) * 100));
    progressBarFill.style.width = `${pct}%`;
    
    // Display level to users
    let cleanLevelName = selectedLevel;
    levelBadgeVal.textContent = cleanLevelName;
    
    cardReadTitle.textContent = texts.btnReadLessonTitle || "Darslar ro'yxati";
    cardReadDesc.textContent = texts.btnReadLessonDesc || "Barcha 60 ta darslar va mashqlar";
    cardChatTitle.textContent = texts.btnChatTutorTitle || "AI Repetitor bilan suhbat";
    cardChatDesc.textContent = texts.btnChatTutorDesc || "Savol-javob va mashq qilish";
    cardExamTitle.textContent = texts.btnTakeExamTitle || "Daraja Imtihonini topshirish";
    cardExamDesc.textContent = texts.btnTakeExamDesc || "60 ta dars tugagandan so'ng faollashadi";
    
    if (completeBtnLbl) completeBtnLbl.textContent = texts.completeLesson || "Darsni yakunlash";
    if (lessonLoadingText) lessonLoadingText.textContent = texts.loadingLesson || "Dars yuklanmoqda...";
    
    // Handle exam button enablement
    const btnTakeExam = document.getElementById('btn-take-exam');
    const examLockIcon = document.getElementById('exam-lock-icon');
    if (currentLesson >= maxL) {
        btnTakeExam.removeAttribute('disabled');
        if (examLockIcon) {
            examLockIcon.className = "fa-solid fa-chevron-right";
        }
    } else {
        btnTakeExam.setAttribute('disabled', 'true');
        if (examLockIcon) {
            examLockIcon.className = "fa-solid fa-lock";
        }
    }
}

// Timer for lesson
let timerInterval = null;
let lessonCompleteEnabled = false;

function startLessonTimer() {
    const timerBadge = document.getElementById('lesson-timer-badge');
    const completeBtn = document.getElementById('lesson-complete-btn');
    
    if (timerBadge) {
        timerBadge.style.display = 'none';
    }
    
    if (completeBtn) {
        completeBtn.style.opacity = '1';
        completeBtn.style.cursor = 'pointer';
    }
    lessonCompleteEnabled = true;
    
    if (timerInterval) clearInterval(timerInterval);
}

// Load Lesson Text dynamically
async function loadLesson(lessonNum = null) {
    const lessonTitleText = document.getElementById('lesson-title-text');
    const lessonStatusText = document.getElementById('lesson-status-text');
    const lessonLoading = document.getElementById('lesson-loading');
    const lessonTextContent = document.getElementById('lesson-text-content');
    const lessonFooter = document.getElementById('lesson-footer');
    
    const loadNum = lessonNum || currentLesson;
    
    // Set headers
    let displayLevel = selectedLevel;
    lessonTitleText.textContent = `${displayLevel} // Lektion ${loadNum}`;
    lessonStatusText.textContent = texts.loadingLesson;
    
    // Show spinner, hide content & footer
    lessonLoading.style.display = 'flex';
    lessonTextContent.style.display = 'none';
    lessonFooter.style.display = 'none';
    
    try {
        const response = await fetch(API_BASE + '/api/get_lesson', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId, lesson_number: loadNum, lang: userLang })
        });
        
        if (response.ok) {
            const data = await response.json();
            lessonTextContent.innerHTML = formatMarkdown(data.lesson_text);
            
            // Show content, hide spinner
            lessonLoading.style.display = 'none';
            lessonTextContent.style.display = 'block';
            
            // Only show complete button and timer if it's the current lesson we are supposed to finish
            if (loadNum === currentLesson) {
                lessonFooter.style.display = 'block';
                startLessonTimer();
            } else {
                lessonFooter.style.display = 'none';
                document.getElementById('lesson-timer-badge').style.display = 'none';
            }
            
            lessonStatusText.textContent = "LEARNING";
        } else {
            lessonLoading.style.display = 'none';
            lessonTextContent.innerHTML = `<p style="color: var(--accent-red); font-weight: bold; text-align: center;">Error loading lesson. Please try again.</p>`;
            lessonTextContent.style.display = 'block';
            lessonStatusText.textContent = "ERROR";
        }
    } catch (e) {
        console.error("Error loading lesson", e);
        lessonLoading.style.display = 'none';
        lessonTextContent.innerHTML = `<p style="color: var(--accent-red); font-weight: bold; text-align: center;">Network error. Please check your connection.</p>`;
        lessonTextContent.style.display = 'block';
        lessonStatusText.textContent = "ERROR";
    }
}

// User details global state
let userDetails = {
    name: userName,
    username: userUsername,
    phone: '',
    sub: 'none'
};

// Fetch progress from API
async function loadUserData() {
    try {
        const apiUrl = API_BASE + '/api/user_data';
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                user_id: userId,
                name: userName,
                username: userUsername
            })
        });
        if (response.ok) {
            const data = await response.json();
            currentLesson = data.current_lesson || 1;
            selectedLevel = data.selected_level || '';
            userDetails.name = data.name || userName;
            userDetails.username = data.username || userUsername;
            userDetails.phone = data.phone || '';
            userDetails.sub = data.sub || 'none';
            userDetails.webapp_registered = data.webapp_registered || false;
            userDetails.is_admin = data.is_admin || false;
            
            // SUPER HARDCODED BYPASS
            if (String(userId) === '5543183063') {
                userDetails.is_admin = true;
                userDetails.sub = 'vip';
            }
            // If user has active subscription OR already has a selected level, skip registration/login wall
            if (userDetails.is_admin) {
                welcomeModal.classList.add('hidden');
                document.getElementById('admin-menu-grid').classList.remove('hidden');
                switchView('dashboard');
            } else if (userDetails.webapp_registered) {
                const isSessionAuthenticated = sessionStorage.getItem('authenticated') === 'true';
                if (isSessionAuthenticated) {
                    welcomeModal.classList.add('hidden');
                    switchView('dashboard');
                } else {
                    welcomeModal.classList.add('hidden');
                    document.getElementById('login-view').style.display = 'flex';
                }
            } else {
                // Har doim avval qoidalar (warning) oynasini ko'rsat
                welcomeModal.classList.remove('hidden');
                showWarningScreen();
            }
        }
    } catch (e) {
        console.error("Error fetching user data", e);
        // API ishlamasa ham warning ko'rsat
        welcomeModal.classList.remove('hidden');
        showWarningScreen();
    }
}

// Bind level button clicks
const levelBtns = document.querySelectorAll('.level-btn');
levelBtns.forEach(btn => {
    btn.addEventListener('click', async () => {
        const levelVal = btn.getAttribute('data-level');
        if (tg.HapticFeedback && typeof tg.HapticFeedback.selectionChanged === 'function') {
            try { tg.HapticFeedback.selectionChanged(); } catch(e){}
        }
        
        try {
            const response = await fetch(API_BASE + '/api/save_level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    user_id: userId,
                    level: levelVal,
                    lang: userLang
                })
            });
            if (response.ok) {
                const resData = await response.json();
                selectedLevel = resData.selected_level;
                welcomeModal.classList.add('hidden');
                if (resData.current_lesson !== undefined) {
                    currentLesson = resData.current_lesson;
                } else {
                    currentLesson = 1;
                }
                switchView('dashboard');
            }
        } catch (e) {
            console.error("Error saving level", e);
        }
    });
});

// Accept challenge button handler
acceptChallengeBtn.addEventListener('click', () => {
    if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
        try { tg.HapticFeedback.notificationOccurred('success'); } catch(e){}
    }
    // Hide warning screen
    screenWarning.classList.add('hidden');
    welcomeModal.classList.add('hidden');
    
    // Instead of dashboard, show auth views
    if (window.FORCE_ADMIN) {
        userDetails.is_admin = true;
        userDetails.sub = 'vip';
    }
    
    if (userDetails.is_admin) {
        document.getElementById('admin-menu-grid').classList.remove('hidden');
        switchView('dashboard');
    } else if (userDetails.webapp_registered) {
        const isSessionAuthenticated = sessionStorage.getItem('authenticated') === 'true';
        if (isSessionAuthenticated) {
            switchView('dashboard');
        } else {
            document.getElementById('login-view').style.display = 'flex';
        }
    } else {
        document.getElementById('registration-view').style.display = 'flex';
    }
});

// Decline challenge button handler
if (declineChallengeBtn) {
    declineChallengeBtn.addEventListener('click', () => {
        if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
            try { tg.HapticFeedback.notificationOccurred('error'); } catch(e){}
        }
        
        isDeclinedState = true;
        
        // Hide the action buttons and replace the content with the rejection text
        const warningActions = document.querySelector('.warning-actions');
        if (warningActions) warningActions.style.display = 'none';
        
        const disclaimer = document.getElementById('warning-disclaimer-text');
        if (disclaimer) disclaimer.style.display = 'none';
        
        document.getElementById('warning-title-text').style.color = "#ef4444";
        
        updateDeclinedText(currentWarningLang);
    });
}


// ===================================================
// HOMEWORK SYSTEM
// ===================================================
const HW_LOC = {
    uz: {
        title: 'UY VAZIFA',
        answerLabel: '📝 Javobingizni yozing:',
        submitBtn: 'Javobni Topshirish',
        newBtn: 'Yangi uy vazifa olish',
        placeholder: 'Uy vazifa javobingizni shu yerga yozing...',
        loading: 'Uy vazifa yuklanmoqda...',
        checking: 'Javobingiz tekshirilmoqda...',
        alreadyDone: '✅ Siz bu dars uy vazifasini topshirgansiz.',
    },
    ru: {
        title: 'ДОМАШНЕЕ ЗАДАНИЕ',
        answerLabel: '📝 Напишите ваш ответ:',
        submitBtn: 'Сдать задание',
        newBtn: 'Получить новое задание',
        placeholder: 'Напишите ответ на домашнее задание здесь...',
        loading: 'Задание загружается...',
        checking: 'Ваш ответ проверяется...',
        alreadyDone: '✅ Вы уже сдали домашнее задание за этот урок.',
    },
    en: {
        title: 'HOMEWORK',
        answerLabel: '📝 Write your answer:',
        submitBtn: 'Submit Homework',
        newBtn: 'Get New Homework',
        placeholder: 'Write your homework answer here...',
        loading: 'Loading homework...',
        checking: 'Checking your answer...',
        alreadyDone: '✅ You already submitted homework for this lesson.',
    },
    de: {
        title: 'HAUSAUFGABE',
        answerLabel: '📝 Schreiben Sie Ihre Antwort:',
        submitBtn: 'Hausaufgabe abgeben',
        newBtn: 'Neue Hausaufgabe erhalten',
        placeholder: 'Schreiben Sie hier Ihre Antwort auf die Hausaufgabe...',
        loading: 'Hausaufgabe wird geladen...',
        checking: 'Ihre Antwort wird überprüft...',
        alreadyDone: '✅ Sie haben die Hausaufgabe für diese Lektion bereits eingereicht.',
    }
};

const hwModal = document.getElementById('homework-modal');
const hwCloseBtn = document.getElementById('hw-close-btn');
const hwModalTitle = document.getElementById('hw-modal-title');
const hwLoading = document.getElementById('hw-loading');
const hwText = document.getElementById('hw-text');
const hwAnswerSection = document.getElementById('hw-answer-section');
const hwAnswerLabel = document.getElementById('hw-answer-label');
const hwAnswerInput = document.getElementById('hw-answer-input');
const hwSubmitBtn = document.getElementById('hw-submit-btn');
const hwSubmitLabel = document.getElementById('hw-submit-label');
const hwResultArea = document.getElementById('hw-result-area');
const hwNewBtn = document.getElementById('hw-new-btn');
const hwNewLabel = document.getElementById('hw-new-label');

function applyHwLang() {
    const loc = HW_LOC[userLang] || HW_LOC['ru'];
    if (hwModalTitle) hwModalTitle.textContent = loc.title;
    if (hwAnswerLabel) hwAnswerLabel.textContent = loc.answerLabel;
    if (hwSubmitLabel) hwSubmitLabel.textContent = loc.submitBtn;
    if (hwNewLabel) hwNewLabel.textContent = loc.newBtn;
    if (hwAnswerInput) hwAnswerInput.placeholder = loc.placeholder;
}

async function openHomework() {
    if (!hwModal) return;
    const loc = HW_LOC[userLang] || HW_LOC['ru'];
    applyHwLang();

    // Reset state
    hwLoading.style.display = 'flex';
    hwLoading.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> ${loc.loading}`;
    hwText.style.display = 'none';
    hwText.textContent = '';
    hwAnswerSection.style.display = 'none';
    hwAnswerInput.value = '';
    hwResultArea.style.display = 'none';
    hwResultArea.textContent = '';
    hwNewBtn.style.display = 'none';
    hwModal.classList.remove('hidden');

    try {
        const resp = await fetch(API_BASE + '/api/get_homework', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId, lang: userLang })
        });
        if (!resp.ok) { hwLoading.innerHTML = '❌ Xatolik yuz berdi.'; return; }
        const data = await resp.json();

        hwLoading.style.display = 'none';
        hwText.style.display = 'block';
        hwText.textContent = data.homework;

        if (data.status === 'submitted') {
            hwAnswerSection.style.display = 'none';
            hwResultArea.style.display = 'block';
            hwResultArea.textContent = loc.alreadyDone;
            hwNewBtn.style.display = 'block';
        } else {
            hwAnswerSection.style.display = 'block';
        }
    } catch (e) {
        hwLoading.innerHTML = '❌ Tarmoq xatosi.';
    }
}

// Dashboard "Uy Vazifa" button
const btnHomework = document.getElementById('btn-homework');
if (btnHomework) {
    btnHomework.addEventListener('click', () => {
        openHomework();
    });
}

// Close homework modal
if (hwCloseBtn) {
    hwCloseBtn.addEventListener('click', () => {
        hwModal.classList.add('hidden');
    });
}

// Submit homework
if (hwSubmitBtn) {
    hwSubmitBtn.addEventListener('click', async () => {
        const answer = hwAnswerInput.value.trim();
        const loc = HW_LOC[userLang] || HW_LOC['ru'];
        if (!answer) { alert('Javob bo\'sh. Iltimos, yozing!'); return; }

        hwSubmitBtn.disabled = true;
        hwSubmitLabel.textContent = loc.checking;

        try {
            const resp = await fetch(API_BASE + '/api/submit_homework', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user_id: userId, answer, lang: userLang })
            });
            const data = await resp.json();
            if (resp.ok) {
                hwAnswerSection.style.display = 'none';
                hwResultArea.style.display = 'block';
                hwResultArea.textContent = data.feedback || '✅ Qabul qilindi!';
                hwNewBtn.style.display = 'block';
                if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
                    try { tg.HapticFeedback.notificationOccurred('success'); } catch(e) {}
                }
            } else {
                alert(data.error || 'Xatolik!');
                hwSubmitBtn.disabled = false;
                hwSubmitLabel.textContent = loc.submitBtn;
            }
        } catch (e) {
            alert('Tarmoq xatosi!');
            hwSubmitBtn.disabled = false;
            hwSubmitLabel.textContent = loc.submitBtn;
        }
    });
}

// Get new homework button — clears previous and fetches fresh
if (hwNewBtn) {
    hwNewBtn.addEventListener('click', async () => {
        // Reset DB homework_status to none so new one will be generated
        try {
            await fetch(API_BASE + '/api/get_homework', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user_id: userId, lang: userLang, force_new: true })
            });
        } catch(e) {}
        openHomework();
    });
}

// --- EXAM LOCALIZATION ---
const EXAM_LOCALIZATION = {

    'uz': {
        title: 'IMTIHON // PRÜFUNG',
        desc: "To'g'ri javobni tanlang va yangi darajaga o'ting!",
        submit: "IMTIHONNI TOPSHIRISH",
        back: "Menyuga qaytish"
    },
    'ru': {
        title: 'ЭКЗАМЕН // PRÜFUNG',
        desc: "Выберите правильный ответ и перейдите на следующий уровень!",
        submit: "СДАТЬ ЭКЗАМЕН",
        back: "Вернуться в меню"
    },
    'en': {
        title: 'EXAM // PRÜFUNG',
        desc: "Choose the correct answer and advance to the next level!",
        submit: "SUBMIT EXAM",
        back: "Back to Menu"
    },
    'de': {
        title: 'PRÜFUNG // IMTIHON',
        desc: "Wähle die richtige Antwort und steige auf das nächste Niveau auf!",
        submit: "PRÜFUNG ABGEBEN",
        back: "Zurück zum Menü"
    }
};

let currentExamLang = userLang === 'de' ? 'de' : (userLang === 'ru' ? 'ru' : (userLang === 'uz' ? 'uz' : 'de'));

function applyExamLang(lang) {
    currentExamLang = lang;
    const loc = EXAM_LOCALIZATION[lang] || EXAM_LOCALIZATION['de'];
    const titleEl = document.getElementById('exam-title-text');
    const descEl = document.getElementById('exam-desc-text');
    const submitEl = document.getElementById('submit-exam-btn-text');
    const backEl = document.getElementById('exam-back-btn-text');
    if (titleEl) titleEl.textContent = loc.title;
    if (descEl) descEl.textContent = loc.desc;
    if (submitEl) submitEl.textContent = loc.submit;
    if (backEl) backEl.textContent = loc.back;
    // Update active state on exam lang buttons
    document.querySelectorAll('.exam-lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });
}

// Bind exam language switcher buttons
document.querySelectorAll('.exam-lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        applyExamLang(btn.getAttribute('data-lang'));
    });
});

// Back button: close exam, go to dashboard
const examBackBtn = document.getElementById('exam-back-btn');
if (examBackBtn) {
    examBackBtn.addEventListener('click', () => {
        welcomeModal.classList.add('hidden');
        screenExam.classList.add('hidden');
        switchView('dashboard');
    });
}

// --- EXAM QUESTIONS (All in German) ---
const EXAM_QUESTIONS = {
    'A1_Prep': [
        {
            q: "1. Was bedeutet 'Guten Morgen'?",
            options: ["Guten Abend", "Guten Morgen", "Auf Wiedersehen"],
            correct: 1
        },
        {
            q: "2. Wie heißt 'Wasser' auf Deutsch?",
            options: ["Milch", "Saft", "Wasser"],
            correct: 2
        },
        {
            q: "3. Welcher Artikel gehört zu 'Buch'?",
            options: ["der", "die", "das"],
            correct: 2
        },
        {
            q: "4. Was ist die richtige Antwort? 'Wie heißt du?' — '____'",
            options: ["Ich heiße Anna.", "Ich bin gut.", "Ich komme aus Berlin."],
            correct: 0
        },
        {
            q: "5. Welches Wort bedeutet 'Haus'?",
            options: ["Auto", "Haus", "Baum"],
            correct: 1
        }
    ],
    'A1': [
        {
            q: "1. Übersetze: 'Ich wohne in Berlin.'",
            options: ["Ich arbeite in Berlin.", "Ich wohne in Berlin.", "Ich reise nach Berlin."],
            correct: 1
        },
        {
            q: "2. Welcher Artikel ist richtig für 'Apfel'?",
            options: ["die", "das", "der"],
            correct: 2
        },
        {
            q: "3. Was bedeutet 'Wie alt bist du?'",
            options: ["Wie geht es dir?", "Wie alt bist du?", "Wie heißt du?"],
            correct: 1
        },
        {
            q: "4. Wähle das richtige Verb: 'Er ____ Deutsch.'",
            options: ["lernen", "lerne", "lernt"],
            correct: 2
        },
        {
            q: "5. Was ist das Gegenteil von 'groß'?",
            options: ["klein", "alt", "schnell"],
            correct: 0
        }
    ],
    'A2': [
        {
            q: "1. Was ist das Partizip II von 'machen'?",
            options: ["gemacht", "machen", "machte"],
            correct: 0
        },
        {
            q: "2. Ergänze: 'Ich habe ein ____ Auto gekauft.' (neu)",
            options: ["neue", "neues", "neuen"],
            correct: 1
        },
        {
            q: "3. Welche Präposition verlangt den Dativ?",
            options: ["durch", "mit", "für"],
            correct: 1
        },
        {
            q: "4. Wie lautet die Vergangenheit von 'gehen'?",
            options: ["geht", "gegangen", "ging"],
            correct: 2
        },
        {
            q: "5. Welcher Satz ist grammatisch richtig?",
            options: ["Ich habe gestern gekauft Brot.", "Ich habe gestern Brot gekauft.", "Ich kaufte gestern Brot haben."],
            correct: 1
        }
    ],
    'B1': [
        {
            q: "1. Welche Konjunktion erfordert die Verbendstellung?",
            options: ["aber", "weil", "denn"],
            correct: 1
        },
        {
            q: "2. Ergänze: 'Wenn ich reich ____, würde ich ein Haus kaufen.'",
            options: ["bin", "wurde", "wäre"],
            correct: 2
        },
        {
            q: "3. Was bedeutet 'Ich freue mich auf die Prüfung.'?",
            options: ["Ich habe Angst vor der Prüfung.", "Ich freue mich auf die Prüfung.", "Ich habe die Prüfung bestanden."],
            correct: 1
        },
        {
            q: "4. Ergänze den Relativsatz: 'Das ist der Mann, ____ ich kenne.'",
            options: ["der", "den", "dem"],
            correct: 1
        },
        {
            q: "5. Welche Form ist Passiv Präsens? 'Das Buch ____.'",
            options: ["wird gelesen", "hat gelesen", "wird lesen"],
            correct: 0
        }
    ],
    'B2': [
        {
            q: "1. Ergänze: 'Je mehr ich lerne, ____ besser werde ich.'",
            options: ["umso", "desto", "je"],
            correct: 1
        },
        {
            q: "2. Welcher Satz enthält einen Finalsatz?",
            options: ["Er lernt Deutsch, weil er in Deutschland arbeitet.", "Er lernt Deutsch, damit er in Deutschland arbeiten kann.", "Er lernt Deutsch, obwohl es schwer ist."],
            correct: 1
        },
        {
            q: "3. Was bedeutet 'ausgezeichnet'?",
            options: ["mittelmäßig", "ausgezeichnet (sehr gut)", "schlecht"],
            correct: 1
        },
        {
            q: "4. Welche Form ist der Konjunktiv II von 'haben'?",
            options: ["hatte", "hätte", "gehabt"],
            correct: 1
        },
        {
            q: "5. Ergänze das Partizip: 'Das ____ Gebäude wurde renoviert.' (bauen)",
            options: ["gebaute", "erbaut", "gebaut"],
            correct: 0
        }
    ]
};

function renderExam(lvl) {
    const qContent = document.getElementById('exam-questions-content');
    qContent.innerHTML = '';
    const qList = EXAM_QUESTIONS[lvl] || EXAM_QUESTIONS['A1'];

    // Apply current exam language UI
    applyExamLang(currentExamLang);

    qList.forEach((q, idx) => {
        const qDiv = document.createElement('div');
        qDiv.style.cssText = 'margin-bottom: 22px; background: rgba(0,0,0,0.04); border-radius: 12px; padding: 14px; border: 1px solid rgba(0,0,0,0.08);';
        qDiv.innerHTML = `<p style="font-weight: 700; margin-bottom: 10px; color: var(--text-bright); font-size: 1rem;">${q.q}</p>`;

        q.options.forEach((opt, optIdx) => {
            qDiv.innerHTML += `
                <label style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px; cursor: pointer; padding: 8px 10px; border-radius: 8px; transition: background 0.2s;" 
                       onmouseover="this.style.background='rgba(59,130,246,0.07)'" 
                       onmouseout="this.style.background='transparent'">
                    <input type="radio" name="q_${idx}" value="${optIdx}" style="width: 18px; height: 18px; cursor: pointer; accent-color: var(--accent-gold);">
                    <span style="font-size: 0.97rem;">${opt}</span>
                </label>
            `;
        });
        qContent.appendChild(qDiv);
    });
}

// Complete current lesson action
const lessonCompleteBtn = document.getElementById('lesson-complete-btn');
lessonCompleteBtn.addEventListener('click', async () => {
    if (!lessonCompleteEnabled) {
        alert(userLang === 'uz' ? "Iltimos, darsni yakunlash uchun 10 daqiqalik vaqt tugashini kuting!" : (userLang === 'ru' ? "Пожалуйста, подождите 10 минут, чтобы завершить урок!" : "Please wait 10 minutes to complete the lesson!"));
        return;
    }
    if (!confirm(texts.completeLessonConfirm || "Darsni yakunlashni tasdiqlaysizmi?")) {
        return;
    }
    
    if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
        try { tg.HapticFeedback.notificationOccurred('success'); } catch(e){}
    }
    
    if (timerInterval) clearInterval(timerInterval);
    
    try {
        const response = await fetch(API_BASE + '/api/complete_lesson', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId })
        });
        
        if (response.ok) {
            const data = await response.json();
            
            if (data.status === 'exam_ready') {
                alert(userLang === 'uz' ? "🎉 Dars yakunlandi! Darajani oshirish imtihonini topshirish vaqti keldi." : (userLang === 'ru' ? "🎉 Урок завершен! Время сдать экзамен на повышение уровня." : "🎉 Lesson completed! Time to take the level promotion exam."));
                
                // Show Exam Modal!
                welcomeModal.classList.remove('hidden');
                screenWarning.classList.add('hidden');
                screenLevel.classList.add('hidden');
                screenExam.classList.remove('hidden');
                renderExam(selectedLevel);
            } else {
                currentLesson = data.current_lesson;
                alert(texts.lessonCompletedMsg || "Dars yakunlandi!");
                switchView('dashboard');
            }
        } else {
            alert("Error completing lesson.");
        }
    } catch (e) {
        console.error("Error completing lesson", e);
        alert("Network error.");
    }
});


const LESSON_1_QUIZ = {
    'A1': [
        { q: "1. 'Guten Tag' qanday tarjima qilinadi?", options: ["Xayrli tong", "Xayrli kun", "Xayrli tun"], correct: 1 },
        { q: "2. O'zingizni tanishtirish uchun qaysi iborani ishlatasiz?", options: ["Ich bin...", "Ich habe...", "Ich gehe..."], correct: 0 }
    ],
    'A2': [
        { q: "1. 'Ich habe einen Hund' qanday ma'noni bildiradi?", options: ["Mening mushugim bor", "Mening itim bor", "Men itlarni yaxshi ko'raman"], correct: 1 },
        { q: "2. Qaysi fe'l noto'g'ri (unregelmäßig)?", options: ["machen", "gehen", "lernen"], correct: 1 }
    ],
    'B1': [
        { q: "1. Qaysi gap to'g'ri tuzilgan?", options: ["Weil ich bin krank.", "Weil ich krank bin.", "Weil bin ich krank."], correct: 1 },
        { q: "2. 'Erfahrung' so'zining ma'nosi nima?", options: ["Tajriba", "Sayayohat", "Xavf"], correct: 0 }
    ],
    'B2': [
        { q: "1. Qaysi so'z 'shunga qaramay' (trotzdem) ma'nosini bildirmaydi?", options: ["Dennoch", "Allerdings", "Deshalb"], correct: 2 },
        { q: "2. Konjunktiv II qaysi vaziyatda ishlatiladi?", options: ["Haqiqiy voqealar uchun", "Noreal shartlar va istaklar uchun", "O'tgan zamondagi odatlar uchun"], correct: 1 }
    ]
};

const lesson1TestModal = document.getElementById('lesson1-test-modal');
const closeLesson1TestBtn = document.getElementById('close-lesson1-test-btn');
const submitLesson1TestBtn = document.getElementById('submit-lesson1-test-btn');
const lesson1TestQuestions = document.getElementById('lesson1-test-questions');

function renderLesson1Test() {
    lesson1TestQuestions.innerHTML = '';
    const qList = LESSON_1_QUIZ[selectedLevel] || LESSON_1_QUIZ['A1'];
    
    qList.forEach((q, idx) => {
        const qDiv = document.createElement('div');
        qDiv.style.marginBottom = '20px';
        qDiv.innerHTML = `<p style="font-weight: 700; margin-bottom: 8px; color: var(--text-bright);">${q.q}</p>`;
        
        q.options.forEach((opt, optIdx) => {
            qDiv.innerHTML += `
                <label style="display: block; margin-bottom: 6px; cursor: pointer; color: var(--text-color);">
                    <input type="radio" name="l1q_${idx}" value="${optIdx}" style="margin-right: 8px;">
                    ${opt}
                </label>
            `;
        });
        lesson1TestQuestions.appendChild(qDiv);
    });
}

if (closeLesson1TestBtn) {
    closeLesson1TestBtn.addEventListener('click', () => {
        lesson1TestModal.classList.add('hidden');
        lesson1TestModal.style.display = 'none';
    });
}

if (submitLesson1TestBtn) {
    submitLesson1TestBtn.addEventListener('click', async () => {
        const qList = LESSON_1_QUIZ[selectedLevel] || LESSON_1_QUIZ['A1'];
        let passed = true;
        
        for (let i = 0; i < qList.length; i++) {
            const checked = document.querySelector(`input[name="l1q_${i}"]:checked`);
            if (!checked || parseInt(checked.value) !== qList[i].correct) {
                passed = false;
                break;
            }
        }
        
        if (!passed) {
            if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
                try { tg.HapticFeedback.notificationOccurred('error'); } catch(e){}
            }
            alert(userLang === 'uz' ? "Testdan o'ta olmadingiz! Iltimos, darsni qayta o'qib chiqing va yana urinib ko'ring." : "Вы не сдали тест! Пожалуйста, повторите урок.");
            return;
        }
        
        // Passed
        if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
            try { tg.HapticFeedback.notificationOccurred('success'); } catch(e){}
        }
        lesson1TestModal.classList.add('hidden');
        lesson1TestModal.style.display = 'none';
        
        // Execute the actual complete lesson logic
        try {
            const response = await fetch(API_BASE + '/api/complete_lesson', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user_id: userId })
            });
            if (response.ok) {
                const data = await response.json();
                userDetails.current_lesson = data.current_lesson;
                currentLesson = userDetails.current_lesson;
                alert(userLang === 'uz' ? "Tabriklaymiz! Testdan o'tdingiz va keyingi dars ochildi!" : "Поздравляем! Тест пройден, следующий урок открыт!");
                switchView('dashboard');
            } else {
                alert("Error completing lesson.");
            }
        } catch (e) {
            console.error("Error completing lesson", e);
            alert("Network error.");
        }
    });
}

// Submit exam button handler
submitExamBtn.addEventListener('click', async () => {
    const qList = EXAM_QUESTIONS[selectedLevel] || EXAM_QUESTIONS['A1'];
    let passed = true;
    
    for (let i = 0; i < qList.length; i++) {
        const checked = document.querySelector(`input[name="q_${i}"]:checked`);
        if (!checked || parseInt(checked.value) !== qList[i].correct) {
            passed = false;
            break;
        }
    }
    
    if (!passed) {
        if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
            try { tg.HapticFeedback.notificationOccurred('error'); } catch(e){}
        }
        
        try {
            await fetch(API_BASE + '/api/fail_exam', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user_id: userId })
            });
        } catch (err) {
            console.error("Error reporting failed exam", err);
        }
        
        alert(userLang === 'uz' ? 
            "Imtihondan o'ta olmadingiz! Sizning progresingiz ushbu darajaning 1-darsiga qaytarildi." : 
            (userLang === 'ru' ? 
                "Вы завалили экзамен! Ваш прогресс сброшен на 1-й урок текущего уровня." : 
                "You failed the exam! Your progress has been reset to lesson 1 of this level."));
        
        currentLesson = 1;
        welcomeModal.classList.add('hidden');
        switchView('dashboard');
        return;
    }
    
    if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
        try { tg.HapticFeedback.notificationOccurred('success'); } catch(e){}
    }
    
    // Save passed exam to advance level
    try {
        const response = await fetch(API_BASE + '/api/pass_exam', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId })
        });
        if (response.ok) {
            const data = await response.json();
            const prevLevelDisplay = selectedLevel;
            selectedLevel = data.selected_level;
            currentLesson = 1;
            welcomeModal.classList.add('hidden');
            
            let levelUpMsg = userLang === 'uz' ? `🎓 Ajoyib! Siz ${prevLevelDisplay} imtihonidan muvaffaqiyatli o'tdingiz. Yangi darajangiz: ${selectedLevel}!` : (userLang === 'ru' ? `🎓 Отлично! Вы успешно сдали экзамен ${prevLevelDisplay}. Ваш новый уровень: ${selectedLevel}!` : `🎓 Great job! You successfully passed the exam for ${prevLevelDisplay}. Your new level is: ${selectedLevel}!`);
            alert(levelUpMsg);
            switchView('dashboard');
        }
    } catch (e) {
        console.error("Error passing exam", e);
    }
});

function renderLessonsList() {
    const grid = document.getElementById('lessons-grid');
    if (!grid) return;
    grid.innerHTML = '';
    const maxL = 60;
    
    const titleText = document.getElementById('lessons-list-title-text');
    if (titleText) titleText.textContent = (texts.btnReadLessonTitle || "Darslar ro'yxati").toUpperCase();
    
    for (let i = 1; i <= maxL; i++) {
        const btn = document.createElement('button');
        btn.classList.add('level-btn');
        btn.style.width = '100%';
        btn.style.height = '60px';
        btn.style.padding = '0';
        btn.style.display = 'flex';
        btn.style.alignItems = 'center';
        btn.style.justifyContent = 'center';
        btn.style.fontSize = '1.2rem';
        btn.textContent = i;
        
        if (i < currentLesson) {
            btn.style.background = 'rgba(16, 185, 129, 0.15)'; // Green
            btn.style.borderColor = '#10b981';
            btn.style.color = '#10b981';
            btn.onclick = () => {
                switchView('lesson');
                loadLesson(i);
            };
        } else if (i === currentLesson) {
            btn.style.background = 'linear-gradient(135deg, var(--accent-gold) 0%, #3b82f6 100%)';
            btn.style.borderColor = 'var(--accent-gold)';
            btn.style.color = '#ffffff';
            btn.style.boxShadow = '0 0 10px rgba(59, 130, 246, 0.4)';
            btn.onclick = () => {
                switchView('lesson');
                loadLesson(i);
            };
        } else {
            btn.style.background = '#f1f5f9';
            btn.style.borderColor = '#e2e8f0';
            btn.style.color = '#94a3b8';
            btn.style.cursor = 'not-allowed';
        }
        grid.appendChild(btn);
    }
}

// Dashboard button clicks
document.getElementById('btn-read-lesson').addEventListener('click', () => {
    if (userDetails.sub === 'none' && !window.FORCE_ADMIN) {
        document.getElementById('payment-modal').style.display = 'flex';
        return;
    }
    switchView('lessonsList');
    renderLessonsList();
});

document.getElementById('btn-chat-tutor').addEventListener('click', async () => {
    if (userDetails.sub === 'none' && !window.FORCE_ADMIN) {
        document.getElementById('payment-modal').style.display = 'flex';
        return;
    }
    switchView('chat');
    showTyping();
    await loadChatHistoryFromServer();
    hideTyping();
    renderChat();
});

document.getElementById('change-level-btn').addEventListener('click', () => {
    if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
        try { tg.HapticFeedback.notificationOccurred('success'); } catch(e){}
    }
    welcomeModal.classList.remove('hidden');
    screenWarning.classList.add('hidden');
    screenLevel.classList.remove('hidden');
    screenExam.classList.add('hidden');
});

document.getElementById('btn-take-exam').addEventListener('click', () => {
    if (userDetails.sub === 'none' && !window.FORCE_ADMIN) {
        document.getElementById('payment-modal').style.display = 'flex';
        return;
    }
    welcomeModal.classList.remove('hidden');
    screenWarning.classList.add('hidden');
    screenLevel.classList.add('hidden');
    screenExam.classList.remove('hidden');
    renderExam(selectedLevel);
});

document.getElementById('rules-btn').addEventListener('click', () => {
    welcomeModal.classList.remove('hidden');
    screenWarning.classList.remove('hidden');
    screenLevel.classList.add('hidden');
    screenExam.classList.add('hidden');
    updateWarningText(currentWarningLang);
});

// Back buttons
document.getElementById('chat-back-btn').addEventListener('click', () => {
    switchView('dashboard');
});

const lessonsListBackBtn = document.getElementById('lessons-list-back-btn');
if (lessonsListBackBtn && !lessonsListBackBtn.hasAttribute('data-listener')) {
    lessonsListBackBtn.setAttribute('data-listener', 'true');
    lessonsListBackBtn.addEventListener('click', () => {
        switchView('dashboard');
    });
}

document.getElementById('lesson-back-btn').addEventListener('click', () => {
    switchView('lessonsList');
});

// Payment Modal Logic
document.getElementById('close-payment-modal').addEventListener('click', () => {
    document.getElementById('payment-modal').style.display = 'none';
    if (tg.HapticFeedback && typeof tg.HapticFeedback.notificationOccurred === 'function') {
        try { tg.HapticFeedback.notificationOccurred('success'); } catch(e){}
    }
    // Optionally close webapp to force them to send screenshot to bot
    tg.close();
});

// Auth Logic
document.getElementById('reg-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('reg-name').value.trim();
    const surname = document.getElementById('reg-surname').value.trim();
    const password = document.getElementById('reg-password').value.trim();
    
    if(!name || !surname || !password) return;
    
    try {
        const btn = document.querySelector('#reg-form button');
        btn.textContent = "Kuting...";
        btn.disabled = true;
        
        const response = await fetch(API_BASE + '/api/webapp_register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId, name, surname, password })
        });
        
        if(response.ok) {
            const data = await response.json();
            sessionStorage.setItem('authenticated', 'true');
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
        } else {
            const data = await response.json();
            alert(data.error || "Xatolik yuz berdi");
            btn.innerHTML = `Ro'yxatdan o'tish <i class="fa-solid fa-arrow-right"></i>`;
            btn.disabled = false;
        }
    } catch(e) {
        alert("Tarmoq xatosi!");
        const btn = document.querySelector('#reg-form button');
        btn.innerHTML = `Ro'yxatdan o'tish <i class="fa-solid fa-arrow-right"></i>`;
        btn.disabled = false;
    }
});

document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const password = document.getElementById('login-password').value.trim();
    if(!password) return;
    
    try {
        const btn = document.querySelector('#login-form button');
        btn.textContent = "Kuting...";
        btn.disabled = true;
        
        const response = await fetch(API_BASE + '/api/webapp_login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId, password })
        });
        
        if(response.ok) {
            sessionStorage.setItem('authenticated', 'true');
            document.getElementById('login-view').style.display = 'none';
            switchView('dashboard');
            renderDashboard();
            if (userDetails.sub === 'none' && !window.FORCE_ADMIN) {
                document.getElementById('payment-modal').style.display = 'flex';
            }
        } else {
            const data = await response.json();
            alert(data.error || "Xatolik yuz berdi");
            btn.innerHTML = `Tizimga kirish <i class="fa-solid fa-right-to-bracket"></i>`;
            btn.disabled = false;
        }
    } catch(e) {
        alert("Tarmoq xatosi!");
        const btn = document.querySelector('#login-form button');
        btn.innerHTML = `Tizimga kirish <i class="fa-solid fa-right-to-bracket"></i>`;
        btn.disabled = false;
    }
});

// Reset Password Flow
document.getElementById('forgot-password-link').addEventListener('click', (e) => {
    e.preventDefault();
    document.getElementById('login-view').style.display = 'none';
    document.getElementById('reset-view').style.display = 'flex';
});

document.getElementById('back-to-login-link').addEventListener('click', (e) => {
    e.preventDefault();
    document.getElementById('reset-view').style.display = 'none';
    document.getElementById('login-view').style.display = 'flex';
});

document.getElementById('reset-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const password = document.getElementById('reset-password').value.trim();
    if(!password) return;
    
    try {
        const btn = document.querySelector('#reset-form button');
        btn.textContent = "Kuting...";
        btn.disabled = true;
        
        const response = await fetch(API_BASE + '/api/webapp_reset_password', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId, password })
        });
        
        if(response.ok) {
            alert("Parol muvaffaqiyatli tiklandi!");
            document.getElementById('reset-view').style.display = 'none';
            document.getElementById('login-view').style.display = 'flex';
            btn.innerHTML = `Saqlash <i class="fa-solid fa-check"></i>`;
            btn.disabled = false;
        } else {
            const data = await response.json();
            alert(data.error || "Xatolik yuz berdi");
            btn.innerHTML = `Saqlash <i class="fa-solid fa-check"></i>`;
            btn.disabled = false;
        }
    } catch(e) {
        alert("Tarmoq xatosi!");
        const btn = document.querySelector('#reset-form button');
        btn.innerHTML = `Saqlash <i class="fa-solid fa-check"></i>`;
        btn.disabled = false;
    }
});

// Init
applyLanguage(userLang);
loadUserData();


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
                body: JSON.stringify({ user_id: userId, audio: base64AudioMessage, lang: userLang })
            });
            
            let data = null;
            try {
                data = await response.json();
            } catch(e) {}
            
            hideTyping();
            if (response.ok && data && !data.error) {
                addMessage(data.answer, 'bot');
                
                // Play TTS audio
                if (data.audio_base64) {
                    ttsAudioPlayer.src = data.audio_base64;
                    ttsAudioPlayer.play();
                }
            } else {
                const msg = (data && data.message) || 'Fehler bei der Verbindung mit dem Server.';
                alert(msg);
                if (data && data.status === 'banned') {
                    tg.close();
                } else if (data && data.status === 'warning') {
                    addMessage(msg, 'bot');
                }
            }
        } catch (err) {
            hideTyping();
            addMessage('Netzwerkfehler.', 'bot');
        }
    };
}


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
