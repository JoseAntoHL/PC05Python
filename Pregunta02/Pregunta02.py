import pandas as pd

df = pd.read_csv('./data/winemag-data-130k-v2.csv') #Carga el archivo

#Explore el dataframe según lo visto en clase

print(df.head())  #Muestra las primeras filas
print(df.info())  #Muestra info
print(df.describe())  #Muestra estadistica

#Realice al menos 4 renombre de columna y 3 creación de nuevas columnas según criterio. 
#Deberá crear las columnas que crea conveniente. Ejemplo: Según el país etiquetelos según continente.

df.rename(columns={'designation': 'denomination', 'taster_name': 'taster_in_name', 'point': 'value', 'variety': 'diversity'}, inplace=True)

df['high_price'] = df['price'].apply(lambda x: 'Yes' if x > 100 else 'No')
df['wine_full_name'] = df['title'] + ' - ' + df['winery']
df['has_twitter_handle'] = df['taster_twitter_handle'].apply(lambda x: 'Yes' if pd.notnull(x) else 'No')

#Genere 4 reportes por agrupamiento de datos. Deberá elegir que reportes realizar

reporte_puntaje_por_pais = df.groupby('country')['value'].mean().reset_index().sort_values(by='value', ascending=False)

reporte_vinos_por_provincia = df.groupby('province').size().reset_index(name='num_wines').sort_values(by='num_wines', ascending=False)

reporte_precio_por_pais = df.groupby('country').agg({'price': 'mean', 'description': 'count'}).reset_index()
reporte_precio_por_pais.rename(columns={'description': 'num_reviews'}, inplace=True)
reporte_precio_por_pais = reporte_precio_por_pais.sort_values(by='num_reviews', ascending=False)

reporte_precio_variedad_uva = df.groupby('diversity').agg({'price': ['max', 'min']}).reset_index()

#Al menos uno de estos datos agrupados deberán ser almacenados en excel o csv

reporte_puntaje_por_pais.to_excel('reporte_puntaje_por_pais.xlsx', index=False)

print(reporte_puntaje_por_pais.head())
