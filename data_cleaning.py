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
df2 = df2.drop(columns=['Cantidad'])
print(df2.head())