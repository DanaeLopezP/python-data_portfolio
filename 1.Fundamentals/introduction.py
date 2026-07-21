# Author: Paola Danae López Pérez

import pandas as pd # pd is an alias for our library
#using pd we can use and refer to the library's methods quickly

# DATA LOAD

datas = {
    "Nombre": ["Ana", "Luis", "Carlos","Joan", "Jewel", "Katrina"],
    "Edad": [24, 31, 27, 23, 14, 56],
    "Ciudad": ["CDMX", "Monterrey", "Guadalajara", "CDMX", "Monterrey", "Guadalajara"]
}

df = pd.DataFrame(datas) # This method transforms the dictionary to a table, our df

#print(df) #prints our table in console

# USEFUL PRINT METHODS

# print(df.head()) # prints the very first 5 rows
# print(df.tail()) # prints the last rows
# print(df.columns) # prints column names
# print(df.shape) # prints how many rows, columns we have in our df
# print(df.info()) # prints how many rows, how many columns, if there's any null, each column data type
# print(df.describe()) # prints an statistic resume of numeric columns in this case 'Edad'

#ACCESS TO COLUMMS 
# print(df["Nombre"]) # Prints just all th info in column Nombre
# print(df[["Nombre", "Edad"]]) # Prints all info in columns Nombre and Edad

#ADD ROWS
df.loc[len(df)] = ["María", 22, "Puebla"]
df.loc[len(df)] = ["José", 29, "Querétaro"]
#Add new registers at the final of our df. Use loc to say where use len(df) to know the final
#You also can replace a register choosing an specific number 

#ADD COLUMNS
df["País"] = "México" # Create a new column with all rows w Mexico
df["Edad en 5 años"] = df["Edad"] + 5 #Create a new columns w Edad plus five for all rows
df["Profesión"] = "Doctora", "Niñero", "Secretario", "Ingeniero","Doctora", "Ingeniera","Karateka","Judoca"
#Create a whole new column w specific info for each row
df.loc[5, "Ciudad"] = "Chiapa de Corzo" # Replace info in a specific location
df ["Mayor de edad"] = df["Edad"] >= 18 #Create a new column evaluating if info in Edad is upper than 18 
#If is true row will have true in the register, if is false will have false in the rgister

print(df)