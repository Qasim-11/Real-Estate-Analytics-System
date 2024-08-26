import streamlit as st
from streamlit_navigation_bar import st_navbar
from news import news
from interface_ar import home_ar
from interface_en import home_en
from chat import chat
st.set_page_config(initial_sidebar_state="collapsed", layout="wide")


pages = ["Dashboard", "News", "Chatbot", "Real-Time Dashboard"]
styles = {
    "nav": {
        "background-color": "#FBF9F1",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },


}





page = st_navbar(pages, styles=styles)





# lang = st.toggle("en", "ar", key="lang")
lang = "en" # if lang else "ar"


if page == "Dashboard":
    if lang == "ar":
        home_ar()
    elif lang == "en":
        home_en()

elif page == "News":
    news()
    # if lang == "ar":
    #     news_ar()
    # elif lang == "en":
    #     news_en()
elif page == "Chatbot":
    chat()
elif page == "Real-Time Dashboard":
    st.title("Coming Soon")
