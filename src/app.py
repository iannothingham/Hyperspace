import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parent))

from hyperspace.data_loader import load_planets_data
from hyperspace.calculator import hyperspace_time


st.title("🚀 Star Wars Hyperspace Calculator")

df = load_planets_data()

planets = sorted(df["Planet"].dropna().unique())

departure = st.selectbox("Planète de départ", planets)
arrival = st.selectbox("Planète d'arrivée", planets)
hyperdrive = st.selectbox("Multiplicateur d'hyperespace", [0.5, 1, 2], index=1)

if st.button("Calculer le trajet"):
    result = hyperspace_time(df, departure, arrival, hyperdrive)

    st.subheader("Résultat")
    st.write(f"**Départ :** {result['departure']}")
    st.write(f"**Destination :** {result['arrival']}")
    st.write(f"**Hyperdrive :** {result['hyperdrive_multiplier']}")
    st.write(f"**Distance :** {result['distance_cases']} cases")
    st.write(f"**Temps de trajet :** {result['travel_time_hours']} heures")
    st.write(f"**Soit :** {result['travel_time_days']} jours")
