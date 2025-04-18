import pandas as pd

# Relativer Pfad zur Datei im data-Ordner
file_path = "data/retail_sales_dataset.csv"

# CSV-Datei einlesen
df = pd.read_csv(file_path)

# Zeige die ersten 5 Zeilen
print(df.head())

