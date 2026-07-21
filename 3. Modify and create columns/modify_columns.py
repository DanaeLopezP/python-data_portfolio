# Author: Paola Danae López Pérez

import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Carlos", "María", "José"],
    "Edad": [24, 17, 31, 28, 19],
    "Ciudad": ["CDMX", "Monterrey", "Guadalajara", "Puebla", "Monterrey"],
    "Salario": [18000, 12000, 25000, 21000, 15000]
}

df = pd.DataFrame(datos)

#CREATE COLUMNS
df["Pais"] = "México" #Create a new column all rows w Mexico
df["Edad en 10 años"] = df["Edad"] + 10 # Create a new column from an existing
df["Mayor_de_edad"] = (df["Edad"] >= 18).astype(int) # Create a new column w conditions
df['Salario Mensual'] = df['Salario'] # Create a new column w the same data as an existing
df['Salario Anual'] = df["Salario"] * 12 
df['Impuesto'] = df["Salario"] * 0.16

#MODIFY COLUMNS
df["Salario"] = df["Salario"] * 1.10 # To modify just replace the column 
df["Edad"] = df["Edad"] + 1 

#MODIFY FORMAT
df["Ciudad"] = df["Ciudad"].str.upper()
df["Ciudad"] = df["Ciudad"].str.lower()
df["Ciudad"] = df["Ciudad"].str.capitalize()

#REPLACE MULTIPLE VALUES
df["Ciudad"] = df["Ciudad"].replace("Monterrey","Chiapa de Corzo") #replace all values in the column
df["Ciudad"] = df["Ciudad"].replace("Cdmx","CDMX") # replace a value misstyped
df["Ciudad"] = df["Ciudad"].replace({
    "CDMX": "Ciudad de México",
    "Puebla": "Puebla, Pue.",
    "Guadalajara": "Guadalajara, Jal."
})

#DROP COLUMNS
df = df.drop(columns=["Impuesto"]) #drop one column
df = df.drop(columns=["Edad", "Ciudad"]) #drop multiple columns
df = df.drop(index=2) # drop an especific row


print(df.head())
