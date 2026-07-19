# Author: Paola Lopez

import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Carlos", "María", "José", "Luis"],
    "Edad": [24, 17, 31, 28, 19, 17],
    "Ciudad": ["CDMX", "Monterrey", "Guadalajara", "Puebla", "Monterrey", "Monterrey"],
    "Salario": [18000, 12000, 25000, 21000, 15000, 12000]
}

df = pd.DataFrame(datos)

#EXPLORE DATA FRAME
df.info() #Remember methods info ad describe don't need print()

#CREATE NEW COLUMNS
df['Mayor_de_edad'] = (df["Edad"] >= 18).astype(int)
df['Salario_Anual'] = df['Salario'] * 12

#MODIFY COLUMNS
df["Salario"] *= 1.10
df['Salario_Anual'] = df['Salario'] * 12
df["Ciudad"] = df["Ciudad"].replace("CDMX","Ciudad de México")
df.loc[df["Nombre"] == "José", "Ciudad"] = "Querétaro" #Locate an specific cell and modify
df = df.drop(columns=["Edad"])

print(df.head(6))
