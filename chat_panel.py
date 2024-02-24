import streamlit as st
from openai import OpenAI

class BotPanadero:
    def __init__(self):
        self.client = OpenAI(api_key=st.secrets["OpenAIAPI"]["openai_api_key"])

    # Función para manejar la entrada del usuario y generar la respuesta del bot
    def communicate(self, user_input):
        messages = st.session_state.get("messages_botPanadero", [])
        messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        bot_message = response.choices[0].message
        messages.append({"role": "bot", "content": bot_message})

        st.session_state["messages_botPanadero"] = messages

    # Mostrar el bot Panadero
    def show_bot(self):
        st.title("Bot Panadero")
        st.write("Este es el Bot Panadero.")
        
        user_input = st.text_input("Por favor, ingrese un mensaje para Bot Panadero.", key="entrada_usuario_botPanadero")
        if user_input:
            self.communicate(user_input)
        
        if st.session_state.get("messages_botPanadero"):
            messages = st.session_state["messages_botPanadero"]
            
            for message in reversed(messages):
                speaker = "😎" if message["role"] == "user" else "🤖"
                st.write(f"{speaker}: {message['content']}")

class BotDesarrollador:
    def __init__(self):
        self.client = OpenAI(api_key=st.secrets["OpenAIAPI"]["openai_api_key"])

    # Función para manejar la entrada del usuario y generar la respuesta del bot
    def communicate(self, user_input):
        messages = st.session_state.get("messages_botDesarrollador", [])
        messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        bot_message = response.choices[0].message
        messages.append({"role": "bot", "content": bot_message})

        st.session_state["messages_botDesarrollador"] = messages

    # Mostrar el bot Desarrollador
    def show_bot(self):
        st.title("Bot Desarrollador")
        st.write("Este es el Bot Desarrollador.")
        
        user_input = st.text_input("Por favor, ingrese un mensaje para Bot Desarrollador.", key="entrada_usuario_botDesarrollador")
        if user_input:
            self.communicate(user_input)
        
        if st.session_state.get("messages_botDesarrollador"):
            messages = st.session_state["messages_botDesarrollador"]
            
            for message in reversed(messages):
                speaker = "😎" if message["role"] == "user" else "🤖"
                st.write(f"{speaker}: {message['content']}")
