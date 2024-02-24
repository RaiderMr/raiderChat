import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets.OpenAIAPI.openai_api_key)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "Piensa como un ingeniero de software"}
    ]

def communicate():
    messages = st.session_state["messages"]
    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    bot_message = response.choices[0].message
    messages.append(bot_message)

    st.session_state["user_input"] = ""

st.title("Desarrollador AI")
st.write("Utilizando la API chatGPT, este chatbot ofrece capacidades conversacionales avanzadas..")

user_input = st.text_input("por favor ingrese un mensaje aquí.", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        if isinstance(message, dict):
            speaker = '<img src="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png" width="50px">' if message["role"] == "user" else '<img src="https://example.com/bot-image.jpg" width="50px">'
            st.write(speaker + ": " + message["content"])
        else:
            st.write("🤖: " + message.content)
