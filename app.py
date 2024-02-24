import streamlit as st
from chat_panel import BotPanadero, BotDesarrollador

# Página de inicio con la selección de bots
def pagina_inicio():
    st.title("Seleccione un bot")
    bot_seleccionado = st.selectbox("Seleccione un bot", ["Bot Panadero", "Bot Desarrolladore"])
    
    if bot_seleccionado == "Bot Panadero":
        bot = BotPanadero()
    else:
        bot = BotDesarrollador()

    # Mostrar el bot seleccionado
    bot.show_bot()

# Mostrar la página de inicio
pagina_inicio()
