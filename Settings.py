import streamlit as st
import pandas as pd
from styles import load_css

load_css()

st.title("Settings & Privacy")
st.markdown("<p class='muted'>You are always in control of your data</p>", unsafe_allow_html=True)

# -------------------------
# Initialize settings state
# -------------------------
if "settings" not in st.session_state:
    st.session_state.settings = {
        "track_sleep": True,
        "track_screen": True,
        "track_calendar": False
    }

# -------------------------
# Data Tracking Controls
# -------------------------
st.subheader("Data Collection")

st.session_state.settings["track_sleep"] = st.checkbox(
    "Track sleep duration",
    value=st.session_state.settings["track_sleep"]
)

st.session_state.settings["track_screen"] = st.checkbox(
    "Track screen time",
    value=st.session_state.settings["track_screen"]
)

st.session_state.settings["track_calendar"] = st.checkbox(
    "Use calendar workload (deadlines, classes)",
    value=st.session_state.settings["track_calendar"]
)

st.info("Burnout Radar never reads messages, content, or notifications.")

# -------------------------
# Data Export
# -------------------------
st.subheader("Your Data")

# Mock user data (replace later with real DB)
sample_data = pd.DataFrame({
    "date": ["2026-01-08", "2026-01-09", "2026-01-10"],
    "sleep_hours": [6.5, 5.8, 7.2],
    "screen_time": [7.1, 8.0, 6.2],
    "mood": ["🙂", "😐", "😄"],
    "burnout_score": [58, 62, 55]
})

csv = sample_data.to_csv(index=False)

st.download_button(
    label="⬇️ Export my data (CSV)",
    data=csv,
    file_name="burnout_radar_data.csv",
    mime="text/csv"
)

# -------------------------
# Danger Zone
# -------------------------
st.subheader("Danger Zone")

st.warning("Deleting your data is permanent and cannot be undone.")

confirm = st.checkbox("I understand and want to delete all my data")

if st.button("Delete all my data", disabled=not confirm):
    st.session_state.clear()
    st.success("All your data has been deleted successfully.")
    st.stop()
