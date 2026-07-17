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
#df1 = df[df['Edad'] > 17]
#print(df1)
#Only younger than 25
#df2 = df[df['Edad'] < 25 ]
#print(df2)
#Only people who lives in CDMX
#df3 = df[df['Ciudad']== 'CDMX']
#print(df3)
#Only salary upper than 20,000
#df4 = df[df['Salario'] > 20000]
#print(df4)
#Only Marias
#df5 = df[df['Nombre'] == 'María']

print(df.loc[df['Nombre'] == 'María'])


