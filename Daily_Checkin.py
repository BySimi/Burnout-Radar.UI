import streamlit as st
from styles import load_css

load_css()

st.title("Daily Check-In")
st.markdown("<p class='muted'>Takes less than 10 seconds</p>", unsafe_allow_html=True)

mood = st.radio("How do you feel today?", ["😞", "😐", "🙂", "😄", "🤩"], horizontal=True)
sleep = st.slider("Sleep (hours)", 0, 10, 7)
screen = st.slider("Screen Time (hours)", 0, 16, 6)

note = st.text_input("Optional note (1 line)")

if st.button("Save"):
    st.success("Check-in saved. You’re doing fine.")
