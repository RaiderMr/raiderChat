import streamlit as st
from openai import OpenAI

class BotPanadero:
    def __init__(self):
        self.client = OpenAI(api_key=st.secrets["OpenAIAPI"]["openai_api_key"])

    def communicate(self, user_input):
        messages = [{"role": "system", "content": "Piensa como un panadero"}]
        messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        bot_message = response.choices[0].message
        messages.append({"role": "bot", "content": bot_message})

        return messages

    def show_bot(self):
        st.title("Bot Panadero")

        user_input = st.text_input("Por favor, ingrese un mensaje aquí.", key="user_input_botPanadero")
        if user_input:
            messages = self.communicate(user_input)
            for message in reversed(messages):
                speaker = "😎" if message["role"] == "user" else "🤖"
                st.write(f"{speaker}: {message['content']}")

class BotDesarrollador:
    def __init__(self):
        self.client = OpenAI(api_key=st.secrets["OpenAIAPI"]["openai_api_key"])

    def communicate(self, user_input):
        messages = [{"role": "system", "content": "Piensa como un ingeniero de software"}]
        messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        bot_message = response.choices[0].message
        messages.append({"role": "bot", "content": bot_message})

        return messages

    def show_bot(self):
        st.title("Bot Desarrollador")

        user_input = st.text_input("Por favor, ingrese un mensaje aquí.", key="user_input_botDesarrollador")
        if user_input:
            messages = self.communicate(user_input)
            for message in reversed(messages):
                speaker = "😎" if message["role"] == "user" else "🤖"
                st.write(f"{speaker}: {message['content']}")

