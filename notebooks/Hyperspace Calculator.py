# 1. Charger le fichier
import pandas as pd
import math

df = pd.read_csv("Data/Processed/planets_clean.csv")

df["Grid X"] = df["Grid Letter"].str.upper().apply(

    lambda letter: ord(letter) - ord("A") + 1

)

df["Grid Number"] = pd.to_numeric(df["Grid Number"])

def hyperspace_time(departure_planet, arrival_planet, hyperdrive_multiplier=1):

    allowed_hyperdrive_multipliers = [0.5, 1, 2]

    if hyperdrive_multiplier not in allowed_hyperdrive_multipliers:

        return f"Multiplicateur invalide : {hyperdrive_multiplier}. Valeurs autorisées : 0.5, 1, 2"

    start = df[df["Planet"].str.lower() == departure_planet.lower()]

    end = df[df["Planet"].str.lower() == arrival_planet.lower()]

    if start.empty:

        return f"Planète de départ introuvable : {departure_planet}"

    if end.empty:

        return f"Planète d'arrivée introuvable : {arrival_planet}"

    x1 = start.iloc[0]["Grid X"]

    y1 = start.iloc[0]["Grid Number"]

    x2 = end.iloc[0]["Grid X"]

    y2 = end.iloc[0]["Grid Number"]

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    hours = distance * 8 * hyperdrive_multiplier

    return {

        "departure": departure_planet,

        "arrival": arrival_planet,

        "hyperdrive_multiplier": f"x{hyperdrive_multiplier}",

        "distance_cases": round(distance, 2),

        "travel_time_hours": round(hours, 2),

        "travel_time_days": round(hours / 24, 2)

    }

result = hyperspace_time("Tatooine", "Coruscant")

print(result)
