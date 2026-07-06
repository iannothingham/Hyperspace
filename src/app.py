import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parent))

from hyperspace.data_loader import load_planets_data
from hyperspace.calculator import hyperspace_time


st.set_page_config(
    page_title="Hyperspace Calculator",
    page_icon="🚀",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top, #1f2937 0%, #020617 55%, #000000 100%);
        color: #f8fafc;
    }

    h1, h2, h3 {
        color: #facc15;
    }

    .subtitle {
        font-size: 1.1rem;
        color: #cbd5e1;
        margin-bottom: 2rem;
    }

    .result-card {
        background: rgba(15, 23, 42, 0.88);
        border: 1px solid rgba(250, 204, 21, 0.35);
        border-radius: 16px;
        padding: 1.2rem;
        margin-top: 1rem;
        box-shadow: 0 0 24px rgba(250, 204, 21, 0.12);
    }

    .metric-label {
        color: #94a3b8;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .metric-value {
        color: #f8fafc;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 999px;
        border: 1px solid #facc15;
        background: #facc15;
        color: #020617;
        font-weight: 700;
    }

    div.stButton > button:hover {
        border: 1px solid #fde68a;
        background: #fde68a;
        color: #020617;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🚀 Star Wars Hyperspace Calculator")
st.markdown(
    '<p class="subtitle">Calcule rapidement le temps de trajet entre deux planètes de la galaxie.</p>',
    unsafe_allow_html=True,
)

df = load_planets_data()
planets = sorted(df["Planet"].dropna().unique())

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        departure = st.selectbox("Planète de départ", planets)

    with col2:
        arrival = st.selectbox("Planète d'arrivée", planets)

    hyperdrive = st.select_slider(
        "Multiplicateur d'hyperespace",
        options=[0.5, 1, 2],
        value=1,
    )

    calculate = st.button("Calculer le trajet")

if calculate:
    result = hyperspace_time(df, departure, arrival, hyperdrive)

    st.markdown("### Résultat")

    st.markdown(
        f"""
        <div class="result-card">
            <div class="metric-label">Route</div>
            <div class="metric-value">{result['departure']} → {result['arrival']}</div>

            <div class="metric-label">Hyperdrive</div>
            <div class="metric-value">{result['hyperdrive_multiplier']}</div>

            <div class="metric-label">Distance</div>
            <div class="metric-value">{result['distance_cases']} cases</div>

            <div class="metric-label">Temps de trajet</div>
            <div class="metric-value">{result['travel_time_hours']} heures · {result['travel_time_days']} jours</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
