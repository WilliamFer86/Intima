# Intima - Asistente de Salud Sexual con IA

Una aplicación web de chat especializada en salud sexual, construida con Flask y Gemini API.

## 🌟 Características

- Chat en tiempo real con IA especializada en salud sexual
- Diseño responsivo y accesible
- Interfaz limpia y profesional
- Seguridad y privacidad del usuario
- Historial de conversación por sesión

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/WilliamFer86/Intima.git
cd Intima
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura tu API key de Gemini:
```bash
cp .env.example .env
# Edita .env y agrega tu GEMINI_API_KEY
```

4. Inicia la aplicación:
```bash
python app.py
```

5. Abre http://localhost:5001 en tu navegador

## 🔧 Configuración

- Obtén tu API key en https://makersuite.google.com/app/apikey
- Configúrala en el archivo `.env`
- La aplicación usa el puerto 5001 para evitar conflictos con AirPlay

## 🛡️ Seguridad

- Las variables de entorno están en `.gitignore`
- No se almacenan mensajes sensibles
- Sesiones temporales que se limpian al cerrar

## 📁 Estructura del Proyecto

```
Intima/
├── app.py              # Backend Flask
├── templates/
│   └── index.html      # Frontend HTML
├── static/
│   └── style.css       # Estilos CSS
├── requirements.txt    # Dependencias
└── .env               # Variables de entorno (no subido a Git)
```

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para sugerencias o pull requests para mejoras.

## 📄 Licencia

Este proyecto es de código abierto con una licencia MIT.
