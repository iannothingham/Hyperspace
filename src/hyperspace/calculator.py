import math

ALLOWED_HYPERDRIVE_MULTIPLIERS = [0.5, 1, 2]
BASE_HOURS_PER_GRID_UNIT = 8

def hyperspace_time(df, departure_planet, arrival_planet, hyperdrive_multiplier=1):
    if hyperdrive_multiplier not in ALLOWED_HYPERDRIVE_MULTIPLIERS:
        raise ValueError("Invalid hyperdrive multiplier")

    departure_row = df[df["Planet Name"] == departure_planet]
    arrival_row = df[df["Planet Name"] == arrival_planet]

    if departure_row.empty or arrival_row.empty:
        raise ValueError("One or both planets not found")

    departure_x = departure_row["Grid X"].iloc[0]
    departure_y = departure_row["Grid Number"].iloc[0]
    arrival_x = arrival_row["Grid X"].iloc[0]
    arrival_y = arrival_row["Grid Number"].iloc[0]

    distance = math.hypot(arrival_x - departure_x, arrival_y - departure_y)
    time = distance * BASE_HOURS_PER_GRID_UNIT / hyperdrive_multiplier

    return time
