import streamlit as st
from styles import load_css

load_css()

st.title("Dashboard")

burnout_score = 62

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown(f"<div class='score'>{burnout_score}</div>", unsafe_allow_html=True)
st.markdown("**Burnout Risk Score**")
st.markdown("<p class='muted'>Moderate risk — rising slowly</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.metric("Sleep", "6.2 hrs", "-0.8")
col2.metric("Screen Time", "7.1 hrs", "+1.2")
col3.metric("Workload", "High", "+2 deadlines")

st.markdown("<div class='recommend'>", unsafe_allow_html=True)
st.markdown("### 🎯 Today’s Focus")
st.write("Stop screen usage **45 minutes earlier tonight** to recover cognitive energy.")
st.markdown("</div>", unsafe_allow_html=True)
