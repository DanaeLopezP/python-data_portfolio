# Author: Paola Danae López Pérez

import pandas as pd 

datos = {
    "Nombre": ["Ana", "Luis", "Carlos", "María", "José", "Elena", "Pedro", "Laura"],
    "Edad": [24, 17, 31, 28, 19, 35, 16, 42],
    "Ciudad": ["CDMX", "Monterrey", "Guadalajara", "Puebla",
               "Monterrey", "CDMX", "Puebla", "Guadalajara"],
    "Salario": [18000, 12000, 25000, 21000, 15000, 32000, 9000, 45000]
}

df = pd.DataFrame(datos)

#ONE CONDITION

#Only +18
df1 = df[df['Edad'] > 17]
#print(df1)
#Only younger than 25
df2 = df[df['Edad'] < 25 ]
#print(df2)
#Only people who lives in CDMX
df3 = df[df['Ciudad']== 'CDMX']
#print(df3)
#Only salary upper than 20,000
df4 = df[df['Salario'] > 20000]
#print(df4)
#Only Marias
df5 = df[df['Nombre'] == 'María']
print(df.loc[df['Nombre'] == 'María']) #Useful way

#TWO CONDITIONS W AND

#Only +18 and Monterrey
print(df.loc[(df['Edad'] > 18) & (df['Ciudad']== 'Monterrey')])
#Only +30 and Salary upper 30000
print(df.loc[(df['Edad'] > 30) & (df['Salario'] > 30000 )])
#Only -18 and Puebla
print(df.loc[(df['Edad'] < 18) & (df['Ciudad'] == 'Puebla' )])
#Only Guadalajara and salari lower than 30000
print(df.loc[(df['Ciudad'] == 'Guadalajara') & (df['Salario'] < 30000 )])

#TWO CONDITIONS W OR

#City CDMX or Guadalajara
print(df.loc[(df['Ciudad'] == 'CDMX') | (df["Ciudad"] == 'Guadalajara')])
#Only -18 or salary lower than 10000
print(df.loc[(df['Edad'] < 18) | (df["Salario"] < 10000)])
#Name is Ana or Maria
print(df.loc[(df['Nombre'] == 'Ana') | (df["Nombre"] == 'María')])

#NEGATION

#No living in Monterrey
print(df.loc[~(df["Ciudad"] == "CDMX")])
#No +18 and no Monterrey
print(df.loc[~(df["Edad"] > 17) & ~(df["Ciudad"] == 'Monterrey')])
#No salary upper than 20000
print(df.loc[~(df["Salario"] > 20000)])

#MULTIPLE SELECTION COLUMN W CONDITION
print(df.loc[df['Salario'] > 20000, ['Nombre', 'Salario']])

#MULTIPLE CONDITIONS
print(df.loc[(df['Edad'] > 18) & (df['Ciudad'] == 'CDMX') | (df['Ciudad'] == 'Puebla') & (df['Salario'] > 15000)])

#CHALLENGE
print(df.loc[(df['Edad'] >= 25) & (df['Salario'] < 30000) & ~(df["Ciudad"] == "Monterrey"), ['Nombre', 'Ciudad', 'Salario']])
