import streamlit as st
from styles import load_css

load_css()

st.title("Insights & Patterns")
st.markdown("<p class='muted'>Understand what drives your burnout</p>", unsafe_allow_html=True)

st.line_chart({
    "Sleep vs Burnout": [30, 40, 50, 60],
    "Screen Time vs Burnout": [35, 45, 55, 65]
})
