
from hyperspace.data_loader import load_planets_data
from hyperspace.calculator import hyperspace_time


def ask_hyperdrive_multiplier():
    hyperdrive = input("Multiplicateur d'hyperespace (0.5, 1 ou 2) [1] : ")

    if hyperdrive == "":
        return 1

    return float(hyperdrive)


def display_result(result):
    if isinstance(result, dict):
        print("\n==============================")
        print(" STAR WARS HYPERSPACE CALCULATOR")
        print("==============================")
        print(f"Départ           : {result['departure']}")
        print(f"Destination      : {result['arrival']}")
        print(f"Hyperdrive       : {result['hyperdrive_multiplier']}")
        print(f"Distance         : {result['distance_cases']} cases")
        print(f"Temps de trajet  : {result['travel_time_hours']} heures")
        print(f"                 : {result['travel_time_days']} jours")
    else:
        print(result)


def main():
    df = load_planets_data()

    departure = input("Planète de départ : ")
    arrival = input("Planète d'arrivée : ")
    hyperdrive = ask_hyperdrive_multiplier()

    result = hyperspace_time(df, departure, arrival, hyperdrive)
    display_result(result)


if __name__ == "__main__":
    main()
