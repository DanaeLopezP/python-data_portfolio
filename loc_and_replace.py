# Author: Paola Danae López Pérez

import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Carlos", "María", "José"],
    "Edad": [24, 17, 31, 28, 19],
    "Ciudad": ["CDMX", "Monterrey", "Guadalajara", "Puebla", "Monterrey"],
    "Salario": [18000, 12000, 25000, 21000, 15000]
}

df = pd.DataFrame(datos)

#REPLACE ONE SPECIFIC VALUE 
df.loc[df["Nombre"] == "Luis", "Ciudad"] = "Chiapa de Corzo"

#REPLACE ONE VALUE FOR ALL THE COLUMN
df["Ciudad"] = df["Ciudad"].replace(
    "Monterrey",
    "Chiapa de Corzo"
)

#REPLACE A VALUE KNOWING THE ROW
df.loc[3, "Ciudad"] = "Zapopan"

df.loc[df["Nombre"] == "Ana", "Salario"] = 20000

df.loc[df["Nombre"] == "María", "Ciudad"] = 'Toluca'

df["Ciudad"] = df["Ciudad"].replace(
    "Chiapa de Corzo",
    "San Cristobal de las Casas"
)

df.loc[df["Nombre"] == "José", "Salario"] = 18000

print(df.head())
