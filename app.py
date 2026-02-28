from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
import os
import google.generativeai as genai
import json

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clave secreta para sesiones

# Configurar Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    """Página principal del chat"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint para procesar mensajes del chat"""
    try:
        # Obtener mensaje del usuario
        user_message = request.json.get('message', '')
        
        if not user_message.strip():
            return jsonify({'error': 'El mensaje no puede estar vacío'}), 400
        
        # Inicializar historial si no existe
        if 'chat_history' not in session:
            session['chat_history'] = []
        
        # Agregar mensaje del usuario al historial
        session['chat_history'].append({'role': 'user', 'content': user_message})
        
        # Preparar el contexto para Gemini
        system_prompt = """Eres Intima, un asistente de IA especializado en salud sexual. 
        Tu propósito es proporcionar información precisa, respetuosa y confidencial sobre salud sexual.
        Siempre mantén un tono profesional, empático y educativo.
        No proporciones diagnósticos médicos y recomienda consultar profesionales de la salud cuando sea necesario."""
        
        # Crear conversación con Gemini
        full_prompt = f"{system_prompt}\n\nUsuario: {user_message}\n\nIntima:"
        
        # Llamar a Gemini API
        response = model.generate_content(full_prompt)
        ai_response = response.text
        
        # Agregar respuesta de la IA al historial
        session['chat_history'].append({'role': 'assistant', 'content': ai_response})
        
        return jsonify({
            'response': ai_response,
            'history': session['chat_history']
        })
        
    except Exception as e:
        print(f"Error en chat: {str(e)}")
        return jsonify({'error': 'Lo siento, hubo un error al procesar tu mensaje'}), 500

@app.route('/clear_history', methods=['POST'])
def clear_history():
    """Limpiar historial de chat"""
    session.pop('chat_history', None)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
