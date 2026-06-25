import re

with open('website/app.py', 'r', encoding='utf-8') as f:
    code = f.read()

new_routes = '''

@app.route('/api/admin_stats', methods=['POST'])
def admin_stats():
    data = request.get_json(silent=True) or {}
    uid = str(data.get('user_id', '')).strip()
    admin_telegram_id = os.getenv('ADMIN_TELEGRAM_ID', '5543183063')
    if uid != admin_telegram_id:
        return {"error": "Unauthorized"}, 401
    
    conn = get_db_connection()
    all_users = conn.execute("SELECT id, name, username, current_lesson, sub, sub_expire, last_activity, selected_level FROM users").fetchall()
    
    users_list = []
    paid_users = []
    skipped_users = []
    
    import time
    now = time.time()
    
    for row in all_users:
        u_dict = dict(row)
        users_list.append(u_dict)
        
        if u_dict.get('sub') and u_dict['sub'] != 'none':
            paid_users.append(u_dict)
            
        if u_dict.get('last_activity'):
            try:
                last_act = time.mktime(time.strptime(u_dict['last_activity'], '%Y-%m-%d %H:%M:%S'))
                if now - last_act > 86400: # skipped lesson if > 24 hours
                    skipped_users.append(u_dict)
            except:
                pass
                
    conn.close()
    
    progress = {}
    for u in users_list:
        lvl = u.get('selected_level') or 'A1'
        les = u.get('current_lesson') or 1
        key = f"{lvl} - {les}"
        progress[key] = progress.get(key, 0) + 1
        
    return {
        "total_users": len(users_list),
        "total_paid": len(paid_users),
        "users": users_list,
        "paid": paid_users,
        "skipped": skipped_users,
        "progress": progress
    }

import base64
import tempfile
import os

@app.route('/assistant/query_voice', methods=['POST'])
def assistant_query_voice():
    try:
        from gtts import gTTS
        import google.generativeai as genai
    except ImportError:
        return {"error": "Dependencies missing"}, 500

    data = request.get_json(silent=True) or {}
    b64_audio = data.get('audio', '')
    lang = data.get('lang', 'ru')
    
    if not b64_audio:
        return {"error": "Empty audio"}, 400
        
    audio_bytes = base64.b64decode(b64_audio.split(',')[1]) if ',' in b64_audio else base64.b64decode(b64_audio)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name
        
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        sample_file = genai.upload_file(path=temp_audio_path)
        
        prompt = "Ты репетитор немецкого языка. Ученик отправил тебе голосовое сообщение. Ответь ему."
        if lang == 'uz': prompt = "Sen nemis tili repetitorisan. O'quvchining ovozli xabariga yordam berib javob qaytar."
        
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
        response = model.generate_content([prompt, sample_file])
        answer_text = response.text
        
        try:
            genai.delete_file(sample_file.name)
        except:
            pass
            
    except Exception as e:
        print("Gemini Voice Error:", e)
        answer_text = "Mening quloqlarim yaxshi eshitmadi. Iltimos, qayta gapiring." if lang == 'uz' else "Извините, я не расслышал. Повторите, пожалуйста."
    finally:
        try:
            os.remove(temp_audio_path)
        except:
            pass
        
    try:
        # Generate TTS
        tts_lang = 'de' if lang == 'de' else 'ru' # Fallback to ru for general
        tts = gTTS(text=answer_text, lang=tts_lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_mp3:
            tts.save(temp_mp3.name)
            with open(temp_mp3.name, 'rb') as f:
                mp3_data = f.read()
            tts_b64 = base64.b64encode(mp3_data).decode('utf-8')
        os.remove(temp_mp3.name)
        audio_url = f"data:audio/mp3;base64,{tts_b64}"
    except Exception as e:
        print("TTS Error:", e)
        audio_url = None
    
    return {
        "answer": answer_text,
        "audio_base64": audio_url
    }

'''

if '/api/admin_stats' not in code:
    code = code.replace("def keep_alive():", new_routes + "\ndef keep_alive():")
    with open('website/app.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print('Routes injected')
else:
    print('Already injected')
