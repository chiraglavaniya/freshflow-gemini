import bootstrap  # ⬅️ CRITICAL

import streamlit as st
import plotly.express as px
import os
from dotenv import load_dotenv

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="FreshFlow AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- ENV ----------------
load_dotenv()

# ---------------- UI ----------------
from ui.theme import apply_theme
from ui.animations import hero_animation

apply_theme()
hero_animation()

# ---------------- DATA ----------------
from live_api.mandi_api import fetch_mandi_data
from analytics.anomaly import detect_anomaly
from analytics.forecast import forecast_price

# ---------------- AI ----------------
from gemini.gemini_client import generate_insight

# ---------------- AGENTS ----------------
from agents.farmer_agent import farmer_view
from agents.trader_agent import trader_view
from agents.analyst_agent import analyst_view

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Controls")
limit = st.sidebar.slider("Records", 50, 500, 200)
alert_price = st.sidebar.number_input("Alert if price >", 1000, 10000, 3000)

# ---------------- DATA FETCH ----------------
api_key = os.getenv("DATA_GOV_API_KEY")
df = fetch_mandi_data(api_key, limit)

avg_price = df["modal_price"].mean()
forecast = forecast_price(df["modal_price"].values, steps=1)[0]
anomalies = detect_anomaly(df["modal_price"].values)

# ---------------- HEADER ----------------
st.title("🌾 FreshFlow Gemini AI Market Dashboard")
st.caption("AI-powered mandi intelligence")

# ---------------- METRICS ----------------
c1, c2, c3 = st.columns(3)
c1.metric("Average Price", f"₹{avg_price:.2f}")
c2.metric("Forecast Price", f"₹{forecast:.2f}")
c3.metric("Anomalies", len(anomalies))

# ---------------- CHART ----------------
fig = px.line(df, y="modal_price", title="📈 Price Movement")
st.plotly_chart(fig, use_container_width=True)

# ---------------- AGENTS ----------------
st.subheader("🧠 Multi-Agent Reasoning")

col1, col2, col3 = st.columns(3)
col1.info(f"👨‍🌾 Farmer: {farmer_view(avg_price)}")
col2.info(f"📦 Trader: {trader_view(df['modal_price'].std()/avg_price)}")
col3.info(f"📊 Analyst: {analyst_view('Uptrend')}")

# ---------------- GEMINI ----------------
st.subheader("🤖 Gemini AI Commentary")

if st.button("Generate Market Insight"):
    summary = df["modal_price"].describe().to_string()
    insight = generate_insight(summary)
    st.success(insight)
