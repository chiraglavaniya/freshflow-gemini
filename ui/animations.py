import streamlit as st
from streamlit_lottie import st_lottie
import json
from pathlib import Path


def load_lottie(path: str):
    with open(path, "r") as f:
        return json.load(f)


def hero_animation():
    st.markdown(
        """
        <div style="text-align:center; padding:20px;">
            <h1 style="font-size:48px;">🌾 FreshFlow AI</h1>
            <p style="font-size:18px; opacity:0.8;">
                Multi-Agent Intelligence for Agricultural Markets
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
