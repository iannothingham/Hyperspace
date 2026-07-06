from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "Data" / "Processed" / "planets_clean.csv"

def load_planets_data(filepath=DATA_PATH):
    df = pd.read_csv(filepath)

    df["Grid X"] = df["Grid Letter"].str.upper().apply(
        lambda letter: ord(letter) - ord("A") + 1
    )

    df["Grid Number"] = pd.to_numeric(df["Grid Number"])

    return df
