import streamlit as st
from openai import OpenAI

# Inicializar el cliente de OpenAI
cliente = OpenAI(api_key=st.secrets["OpenAIAPI"]["openai_api_key"])

# Inicializar el estado de la sesión
if "mensajes" not in st.session_state:
    st.session_state["mensajes"] = [{"rol": "sistema", "contenido": "Piensa como un panadero"}]

# Función para manejar la entrada del usuario y generar la respuesta del bot
def comunicar():
    # Obtener los mensajes actuales
    mensajes = st.session_state["mensajes"]
    
    # Agregar el mensaje del usuario a los mensajes
    mensaje_usuario = {"rol": "usuario", "contenido": st.session_state["entrada_usuario"]}
    mensajes.append(mensaje_usuario)
    
    # Generar la respuesta del bot
    respuesta = cliente.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=mensajes
    )
    mensaje_bot = respuesta.choices[0].message
    mensajes.append({"rol": "bot", "contenido": mensaje_bot})
    
    # Actualizar el estado de la sesión
    st.session_state["mensajes"] = mensajes
    st.session_state["entrada_usuario"] = ""

# Interfaz de Streamlit
st.title("Desarrollador AI")
st.write("Utilizando la API chatGPT, este chatbot ofrece capacidades conversacionales avanzadas..")

# Cuadro de texto para la entrada del usuario
entrada_usuario = st.text_input("Por favor, ingrese un mensaje aquí.", key="entrada_usuario", on_change=comunicar)

# Mostrar los mensajes del chat
if st.session_state["mensajes"]:
    mensajes = st.session_state["mensajes"]
    
    for mensaje in reversed(mensajes):
        emisor = "😎" if mensaje["rol"] == "usuario" else "🤖"
        st.write(f"{emisor}: {mensaje['contenido']}")
