import streamlit as st
from openai import OpenAI

class Bot:
    def __init__(self, name, api_key):
        self.name = name
        self.client = OpenAI(api_key=api_key)

    def communicate(self, user_input):
        messages_key = f"messages_{self.name.lower()}"
        messages = st.session_state.get(messages_key, [])
        messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        bot_message = response.choices[0].message
        messages.append({"role": "bot", "content": bot_message})

        st.session_state[messages_key] = messages

    def show_bot(self):
        st.title(f"Bot {self.name}")
        st.write(f"Este es el Bot {self.name}.")

        user_input_key = f"entrada_usuario_{self.name.lower()}"
        user_input = st.text_input(f"Por favor, ingrese un mensaje para Bot {self.name}.", key=user_input_key)
        if user_input:
            self.communicate(user_input)

        messages_key = f"messages_{self.name.lower()}"
        if st.session_state.get(messages_key):
            messages = st.session_state[messages_key]

            for message in reversed(messages):
                speaker = "😎" if message["role"] == "user" else "🤖"
                st.write(f"{speaker}: {message['content']}")

# Define tus claves API para los bots
api_key_panadero = st.secrets["OpenAIAPI"]["openai_api_key_panadero"]
api_key_desarrollador = st.secrets["OpenAIAPI"]["openai_api_key_desarrollador"]

# Crea instancias de los bots
bot_panadero = Bot("Panadero", api_key_panadero)
bot_desarrollador = Bot("Desarrollador", api_key_desarrollador)

# Muestra los bots
bot_panadero.show_bot()
bot_desarrollador.show_bot()
