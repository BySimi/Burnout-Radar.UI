# styles.py
import streamlit as st

def load_css():
    st.markdown(
        """
        <style>
        /* Import font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        /* Global */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #F9FAFB;
            color: #111827;
        }

        /* Titles */
        h1, h2, h3 {
            font-weight: 700;
            color: #111827;
        }

        /* Muted text */
        .muted {
            color: #6B7280;
            font-size: 0.9rem;
        }

        /* Card container */
        .card {
            background: #F1F5F9;
            padding: 1.2rem 1.4rem;
            border-radius: 18px;
            margin-bottom: 1rem;
        }

        /* Burnout score */
        .score {
            font-size: 3.5rem;
            font-weight: 700;
            color: #4F46E5;
            line-height: 1;
        }

        /* Recommendation box */
        .recommend {
            background: #ECFEFF;
            border-left: 6px solid #14B8A6;
            padding: 1rem 1.2rem;
            border-radius: 14px;
            margin-top: 1rem;
        }

        /* Buttons */
        button {
            border-radius: 12px !important;
            font-weight: 600 !important;
        }

        /* Metrics */
        [data-testid="stMetricValue"] {
            font-size: 1.4rem;
            font-weight: 600;
        }

        /* Mobile spacing */
        @media (max-width: 768px) {
            .score {
                font-size: 2.6rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
