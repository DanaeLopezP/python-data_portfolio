# Author: Paola Lopez

import pandas as pd

datos = {
    "ID": [101,102,103,104,105,106,107,108,109,110],
    "Nombre": ["Ana","Luis","Carlos","María","José","Laura","Pedro","Sofía","Carlos","Luis"],
    "Edad": [24,17,31,None,19,45,28,22,31,17],
    "Ciudad": [
        "CDMX",
        "Monterrey",
        "Guadalajara",
        "Puebla",
        "monterrey",
        "CDMX",
        "Puebla",
        "Guadalajara",
        "Guadalajara",
        "Monterrey"
    ],
    "Departamento": [
        "Ventas",
        "Ventas",
        "TI",
        "RH",
        "Ventas",
        "TI",
        "RH",
        "Ventas",
        "TI",
        "Ventas"
    ],
    "Salario": [
        18000,
        12000,
        25000,
        21000,
        None,
        38000,
        19500,
        17000,
        25000,
        12000
    ]
}

df = pd.DataFrame(datos)

#EXPLORATION
#df.info() #6 columns and 10 rows
#print(df.describe()) #Terminal didn't show me the statistic resume without the print

#CLEANING
#print(df.head())
#Repairing misstyped cities
df["Ciudad"] = df["Ciudad"].str.upper()
df["Ciudad"] = df["Ciudad"].str.lower()
df["Ciudad"] = df["Ciudad"].str.capitalize()

#Detecting duplicates
#print(df.loc[df['Nombre'] == 'Luis'])
#print(df.loc[df['Nombre'] == 'Carlos'])
df.loc[df.duplicated()]
df = df.drop(index=8)
df = df.drop(index=9)
#df = df.drop_duplicates()

#NaN


#CREATE NEW COLUMNS
df['Mayor_de_edad'] = (df["Edad"] >= 18).astype(int)
df['Salario_Anual'] = df['Salario'] * 12
df['Bono'] = df['Salario'].apply(lambda x: x * 0.05 if x > 20000 else 0)
df['Nivel_salarial'] = df['Salario'].apply(
    lambda x: 'Bajo' if x < 15000 else ('Medio' if x <= 30000 else 'Alto')
)

#MODIFY
df["Ciudad"] = df["Ciudad"].replace("Cdmx","Ciudad de México")
df.loc[df["Departamento"] == "TI", "Salario"] = df["Salario"] * 1.15
df.loc[df["Departamento"] == "RH", "Salario"] = df["Salario"] * 1.08
df['Salario_Anual'] = df['Salario'] * 12
#print(df.head(8))

#DROP
df = df.drop(columns=["Edad"])

#QUERYS
print(df.loc[df["Departamento"] == "TI", ["Nombre", "Departamento"]])
print(df.loc[df["Salario"] > 20000, ["Nombre", "Salario"]])
print(df.loc[(df["Departamento"] == "Ventas")  & (df["Ciudad"] == "Ciudad de México"), ["Nombre", "Departamento", "Ciudad"]])
print(df.loc[df["Salario"] > 25000, ["Nombre", "Salario"]])
print(df.loc[~(df["Departamento"] == "Ventas"), ["Nombre", "Salario"]])