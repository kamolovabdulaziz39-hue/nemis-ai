import os

js_path = 'website/assistant.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

quiz_code = """
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
"""

if 'LESSON_1_QUIZ' not in js:
    js = js.replace('// Submit exam button handler', quiz_code + '\n// Submit exam button handler')

    import re
    
    # Intercept complete lesson click
    target_click = """lessonCompleteBtn.addEventListener('click', async () => {
    if (!lessonCompleteEnabled) {
        alert(userLang === 'uz' ? "Iltimos, darsni yakunlash uchun 10 daqiqalik vaqt tugashini kuting!" : (userLang === 'ru' ? "Пожалуйста, подождите 10 минут, чтобы закончить урок!" : "Please wait 10 minutes to complete the lesson!"));
        return;
    }
    if (!confirm(texts.completeLessonConfirm || "Darsni yakunlashni tasdiqlaysizmi?")) {
        return;
    }"""
    
    replace_click = """lessonCompleteBtn.addEventListener('click', async () => {
    if (!lessonCompleteEnabled) {
        alert(userLang === 'uz' ? "Iltimos, darsni yakunlash uchun 10 daqiqalik vaqt tugashini kuting!" : (userLang === 'ru' ? "Пожалуйста, подождите 10 минут, чтобы закончить урок!" : "Please wait 10 minutes to complete the lesson!"));
        return;
    }
    
    // NEW: Intercept Lesson 1
    if (currentLesson === 1) {
        renderLesson1Test();
        lesson1TestModal.classList.remove('hidden');
        lesson1TestModal.style.display = 'flex';
        return;
    }
    
    if (!confirm(texts.completeLessonConfirm || "Darsni yakunlashni tasdiqlaysizmi?")) {
        return;
    }"""
    
    if "NEW: Intercept Lesson 1" not in js:
        js = js.replace(target_click, replace_click)

    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    
    print('Injected JS logic')
else:
    print('JS already injected')
