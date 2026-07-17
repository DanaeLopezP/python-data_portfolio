# Author: Paola Danae López Pérez

import pandas as pd # pd is an alias for our library
#using pd we can use and refer library's methods quickly

# DATA LOAD
# Pandas allows you to read different types of archives

#df1 = pd.read_excel('data.xls')

df2 = pd.read_csv('dataCGP.csv')

#DATA INSPECTION
#print(df2.dtypes)
#print(df2.describe())
#print(df2.head())
#print(df2.tail())
#df2.info()

#DATA CLEANING
#print(df2.isnull().sum())
df2.rename(columns={'Precio Unitario': 'PRECIO'}, inplace = True)
# df2 = df2.drop(columns=['Cantidad'])

# MULTIPLE COLUMN SELECTION
df2 [['Producto','Origen' ]] #Syntaxis: double brackets for column selection
#print(df2 [['Producto','Origen' ]])

#CREATE NEW DF FROM AN EXISTING
df3 = df2 [['Cliente','Total','Origen' ]]
#print(df3.head())

#SELECTION BY POSITION
#print(df3.iloc[0:5]) # Brings from 0 to position minus 1 
#print(df3.loc[25]) # Brings from 0 to position

#SELECTION BY CONDITION
selection = df3[df3['Total'] > 40] #brings all rows where total is upper than 40
print (selection)
#print(df3)