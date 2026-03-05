from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

SYSTEM_PROMPT = """Eres Intima, una asistente de salud sexual empática y profesional.
Tu rol es actuar como un primer punto de contacto para personas que enfrentan dificultades en su vida sexual o íntima.
Eres cálida, cercana y sin juicios de valor. Profesional sin ser fría.
Valida las emociones antes de dar información.
Nunca realizas diagnósticos médicos ni prescribes medicamentos.
Responde en el idioma en que el usuario te escribe."""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        if not user_message:
            return jsonify({'error': 'Mensaje vacío'}), 400
        if 'history' not in session:
            session['history'] = []
        session['history'].append({"role": "user", "content": user_message})
        
        contents = []
        for msg in session['history']:
            role = "user" if msg['role'] == "user" else "model"
            contents.append({"role": role, "parts": [{"text": msg['content']}]})
        
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}",
            headers={"Content-Type": "application/json"},
            json={
                "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
                "contents": contents
            }
        )
        print(f"Status: {response.status_code}")
        print(f"Respuesta: {response.text[:200]}")
        ai_response = response.json()['candidates'][0]['content']['parts'][0]['text']
        session['history'].append({"role": "assistant", "content": ai_response})
        session.modified = True
        return jsonify({'response': ai_response})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Lo siento, hubo un error. Por favor intenta de nuevo.'}), 500

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session.pop('history', None)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)