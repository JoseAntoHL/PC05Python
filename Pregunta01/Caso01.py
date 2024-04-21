import pandas as pd

#Carga el archivo airbnb.csv

filtered_df = df[(df['reviews'] > 10) & (df['overall_satisfaction'] > 4)] #Filtrar las habitaciones

sorted_df = filtered_df.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False]) #Ordenar las habitaciones

top_3_options = sorted_df.head(3) # 3 mejores

print(top_3_options[['room_id', 'neighborhood', 'overall_satisfaction', 'reviews']]) #Mostrar
