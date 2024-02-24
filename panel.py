import streamlit as st
from openai import OpenAI

class BotPanadero:
    def __init__(self):
        self.client = OpenAI(api_key=st.secrets["OpenAIAPI"]["openai_api_key"])

    # Función para manejar la entrada del usuario y generar la respuesta del bot
    def communicate(self):
        # Lógica de comunicación con OpenAI para Bot Panadero
        pass

    # Mostrar el bot Panadero
    def show_bot(self):
        st.title("Bot Panadero")
        st.write("Este es el Bot Panadero.")
        
        # Aquí va la interfaz de usuario específica del Bot Panadero
        user_input = st.text_input("Por favor, ingrese un mensaje para Bot Panadero.", key="entrada_usuario_botPanadero", on_change=self.communicate)
        
        # Mostrar mensajes de Bot Panadero
        if st.session_state.get("messages_botPanadero"):
            messages = st.session_state["messages_botPanadero"]
            
            for message in reversed(messages):
                speaker = "😎" if message["role"] == "user" else "🤖"
                st.write(f"{speaker}: {message['content']}")

class BotDesarrollador:
    def __init__(self):
        self.client = OpenAI(api_key=st.secrets["OpenAIAPI"]["openai_api_key"])

    # Función para manejar la entrada del usuario y generar la respuesta del bot
    def communicate(self):
        # Lógica de comunicación con OpenAI para Bot Desarrollador
        pass

    # Mostrar el bot Desarrollador
    def show_bot(self):
        st.title("Bot Desarrollador")
        st.write("Este es el Bot Desarrollador.")
        
        # Aquí va la interfaz de usuario específica del Bot Desarrollador
        user_input = st.text_input("Por favor, ingrese un mensaje para Bot Desarrollador.", key="entrada_usuario_botDesarrollador", on_change=self.communicate)
        
        # Mostrar mensajes de Bot Desarrollador
        if st.session_state.get("messages_botDesarrollador"):
            messages = st.session_state["messages_botDesarrollador"]
            
            for message in reversed(messages):
                speaker = "😎" if message["role"] == "user" else "🤖"
                st.write(f"{speaker}: {message['content']}")
