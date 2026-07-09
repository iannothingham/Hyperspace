import pandas as pd

# Charger les fichiers
planets = pd.read_csv("data/Processed/planets_clean.csv")
hyperlanes = pd.read_csv("data/Processed/hyperlanes.csv")

# Normaliser les noms de colonnes si besoin
planets.columns = planets.columns.str.strip()
hyperlanes.columns = hyperlanes.columns.str.strip()

# Table des planètes présentes dans une hyperlane
# On récupère les planètes présentes en From et en To
from_planets = hyperlanes[["Route", "From"]].rename(columns={"From": "Planet"})
to_planets = hyperlanes[["Route", "To"]].rename(columns={"To": "Planet"})

hyperlane_planets = pd.concat([from_planets, to_planets], ignore_index=True)

# Si une planète apparaît dans plusieurs routes, on les regroupe
hyperlane_planets = (
    hyperlane_planets
    .groupby("Planet", as_index=False)["Route"]
    .apply(lambda routes: ", ".join(sorted(set(routes))))
)

# Jointure avec les planètes
galaxy_map = planets.merge(
    hyperlane_planets,
    on="Planet",
    how="left"
)

# Ajouter une colonne booléenne
galaxy_map["Is Hyperlane Planet"] = galaxy_map["Route"].notna()

# Renommer Route pour être plus clair
galaxy_map = galaxy_map.rename(columns={
    "Route": "Hyperlane"
})

# Sauvegarder le résultat
galaxy_map.to_csv("data/Processed/galaxy_map.csv", index=False)

print("✅ galaxy_map.csv créé dans data/Processed/")
print(galaxy_map.head())
