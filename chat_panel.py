import streamlit as st
from openai import OpenAI

# Credenciales de la API de OpenAI
api_key = st.secrets["OpenAIAPI"]["openai_api_key"]
openai = OpenAI(api_key=api_key)

# Texto del prompt para el panadero
panadero_prompt = "Eres un panadero y estás buscando nuevas recetas de pan. ¿Puedes darme algunas ideas?"

# Texto del prompt para el ingeniero de sistemas
ingeniero_prompt = "Eres un ingeniero de sistemas y estás desarrollando un nuevo software. ¿Qué características debería tener?"

# Función para obtener la respuesta del chatbot
def get_response(prompt):
    response = openai.Completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a customer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50
    )
    return response["choices"][0]["message"]["content"]

# Sidebar para seleccionar la vist
vista = st.sidebar.radio("Selecciona una vista", ["Chatbot", "Prompts"])

# Mostrar la vista seleccionada
if vista == "Chatbot":
    st.title("Chatbot GPT-3.5-turbo")
    st.write("¡Hola! Soy un chatbot GPT-3.5-turbo. ¿En qué puedo ayudarte?")
    user_input = st.text_input("Escribe tu mensaje")
    if user_input:
        st.write("Usuario:", user_input)
        response = get_response(user_input)
        st.write("Chatbot:", response)
elif vista == "Prompts":
    st.title("Prompts")
    st.write("Selecciona un prompt:")
    prompt_seleccionado = st.selectbox("Selecciona un prompt", ["Panadero", "Ingeniero de sistemas"])
    if prompt_seleccionado == "Panadero":
        st.write("Prompt para el panadero:")
        st.code(panadero_prompt, language="text")
    elif prompt_seleccionado == "Ingeniero de sistemas":
        st.write("Prompt para el ingeniero de sistemas:")
        st.code(ingeniero_prompt, language="text")
