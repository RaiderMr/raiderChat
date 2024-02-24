import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
  {"role": "system", "content": "Piensa como un ingenierio de software"}
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

st.markdown(
    """
    <style>
    body {
        background-image: url('https://c8.alamy.com/compes/mbwhc7/futurista-con-fondo-blanco-hexagonal-de-forma-abstracta-ilustracion-3d-mbwhc7.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title ("Desarrollador AI")
st.write ("Utilizando la API chatGPT, este chatbot ofrece capacidades conversacionales avanzadas..")

user_input = st.text_input("por favor ingrese un mensaje aquí.", key = "user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        if isinstance(message, dict):
            speaker = "😎" if message["role"] == "user" else "ðŸ¤–"
            st.write (speaker + ": " + message["content"])
        else:
            st.write("🤖: " + message.content)
