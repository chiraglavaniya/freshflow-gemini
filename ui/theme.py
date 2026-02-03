import streamlit as st

def apply_theme():
    st.markdown("""
        <style>
        body {
            background: radial-gradient(circle at top, #0f2027, #203a43, #2c5364);
            color: #ffffff;
        }
        .stButton>button {
            border-radius: 12px;
            background: linear-gradient(90deg,#00c6ff,#0072ff);
            color: white;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)
