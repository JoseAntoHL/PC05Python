import pandas as pd

df = pd.read_csv('./data/winemag-data-130k-v2.csv') #Carga el archivo

#Explore el dataframe según lo visto en clase

print(df.head())  #Muestra las primeras filas
print(df.info())  #Muestra info
print(df.describe())  #Muestra estadistica

#Realice al menos 4 renombre de columna y 3 creación de nuevas columnas según criterio. 
#Deberá crear las columnas que crea conveniente. Ejemplo: Según el país etiquetelos según continente.

df.rename(columns={'designation': 'designation_name', 'point': 'wine_rating', 'variety': 'grape_variety'}, inplace=True)

#Genere 4 reportes por agrupamiento de datos. Deberá elegir que reportes realizar

