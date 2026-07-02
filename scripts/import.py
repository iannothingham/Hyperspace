import pandas as pd

# Lire le fichier CSV
df = pd.read_csv("/Users/thomasmoreau/code/iannothingham/Hyperspace/Data/planets.csv")

# Afficher les 5 premières lignes
print(df.head())
