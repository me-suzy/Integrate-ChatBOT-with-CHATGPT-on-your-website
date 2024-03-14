import streamlit as st
import os
from embedchain import App

def main():
    # Inițializează componentele UI și CSS-ul
    initialize_ui()

    # Setează cheia API ca variabilă de mediu
    # https://platform.openai.com/api-keys
    os.environ["OPENAI_API_KEY"] = "YOUR-API-KEY"

    # Crează instanța botului
    elon_bot = App()

    # Adaugă resurse la bot
    add_resources_to_bot(elon_bot)

    # Preia interogarea utilizatorului și afișează răspunsul
    query_user_and_display_response(elon_bot)

def initialize_ui():
    # CSS-ul personalizat
    custom_css = """
    <style>
      html, body, .stApp {
        height: 100%;
      }
      .stTextInput {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        z-index: 99;
      }
      .stTextInput .st-dg {
        background-color: #f1f1f1; /* culoarea fundalului input-ului */
      }
      .stTextInput input {
        padding: 10px; /* spațierea din interiorul input-ului */
        border: none;
        border-radius: 5px; /* colțurile rotunjite ale input-ului */
      }
      .stButton > button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 99;
      }
      .chat-messages {
        margin-bottom: 70px; /* spațiu la partea de jos pentru input */
      }
      .css-12oz5g7 {
        overflow-y: auto;
        height: calc(100% - 75px); /* ajustează înălțimea containerului de mesaje */
        padding: 0 20px 20px;
      }
      header {
        display: none;
      }
      /* Stilul pentru bară despărțitoare la mesajele de la bot */
      .bot-message {
        border-top: 2px solid #cccccc; /* Culoarea și grosimea barei */
        padding-top: 10px; /* Spațiul deasupra textului */
        margin-top: 10px; /* Spațiul deasupra barei */
      }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Set viewport meta tag for responsiveness
    st.markdown(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        unsafe_allow_html=True
    )

    # Titlul aplicației
    st.title("Support Bot")

def add_resources_to_bot(bot):
    # Citește resursele din fișierul text
    with open('resources.txt', 'r') as file:
        for url in file:
            bot.add(url.strip())


def query_user_and_display_response(bot):
    if 'responses' not in st.session_state:
        st.session_state.responses = []

    # Definește o funcție pentru a interoga botul și a afișa răspunsul
    def get_answer(query):
        query += " Explain in detail the above question based on context provided. Be like a teacher explaining to student"
        ans = bot.query(query)
        return ans

    query = st.text_input("", key="input_text", on_change=lambda: setattr(st.session_state, 'submitted', True))

    # Dacă există o interogare și starea 'submitted' este True, afișează răspunsul
    if query and st.session_state.submitted:
        response = get_answer(query)
        st.session_state.responses.append(response)
        for idx, resp in enumerate(st.session_state.responses):
            if idx > 0:  # Adaugă o bară despărțitoare între mesaje, dar nu înaintea primului mesaj
                st.markdown("")
            st.markdown(f'<div class="bot-message">{resp}</div>', unsafe_allow_html=True)
        st.session_state.submitted = False  # Resetăm starea pentru următoarea interogare

if __name__ == "__main__":
    main()


