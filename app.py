import streamlit as st
from styles import load_css

st.set_page_config(
    page_title="Burnout Radar",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css()

st.title("🧠 Burnout Radar")
st.markdown("### Predict burnout before it hits you")
st.markdown("<p class='muted'>Built for college students under academic pressure</p>", unsafe_allow_html=True)

user = st.text_input("College Email / Username")
anon = st.checkbox("Continue anonymously")

if st.button("Continue"):
    st.session_state.logged_in = True
if "logged_in" not in st.session_state:
    st.stop()
