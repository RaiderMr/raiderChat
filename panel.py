import streamlit as st
from chat_panel import show_chat_panel

# Página de inicio con opciones de redirección
def pagina_inicio():
    st.title("Bienvenido al Chatbot")
    st.write("Por favor, selecciona una opción para continuar:")
    opcion = st.selectbox("Selecciona una opción", ["Iniciar Chat", "Otra opción"])
    
    if opcion == "Iniciar Chat":
        st.session_state["redireccion"] = True
    else:
        st.session_state["redireccion"] = False

# Verificar si se debe redirigir
if "redireccion" not in st.session_state or st.session_state["redireccion"]:
    pagina_inicio()
else:
    show_chat_panel()
