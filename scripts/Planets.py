import pandas as pd

df = pd.read_csv("/Users/thomasmoreau/code/iannothingham/Hyperspace/Data/Raw/planets.csv")

#Ajout d'un Identificateur unique pour chaque planète

df["ID"] = range(1, len(df)+1)

# Réorganisation des colonnes pour que l'ID soit la première colonne

id_col = df.pop("ID")
df.insert(0, "ID", id_col)

# Renommer la colonne "Name" en "Planet"

df = df.rename(columns={
    "Name": "Planet"
})
# Remplir les valeurs manquantes avec "Unknown"

df = df.fillna("Unknown")

# Extraire les coordonnées de la grille à partir de la colonne "Grid Coordinates" et les ajouter comme nouvelles colonnes

coords = df["Grid Coordinates"].str.extract(r"([A-Z])-(\d+)")

df["Grid Letter"] = coords[0]
df["Grid Number"] = coords[1]

# Supprimer les lignes où la colonne "Grid Coordinates" est égale à "Unknown"

df = df[df["Grid Coordinates"] != "Unknown"]

# Supprimer les lignes où la colonne "Grid Letter" ou "Grid Number" est vide

df = df.dropna(subset=["Grid Letter", "Grid Number"])

# Sauvegarder le DataFrame nettoyé dans un nouveau fichier CSV

df.to_csv("Data/Processed/planets_clean.csv", index=False)
