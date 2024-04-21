import pandas as pd

df = pd.read_csv('./data/airbnb.csv') #Carga el archivo airbnb.csv

# Filtrar las propiedades de Roberto y Clara
roberto_id = 97503
clara_id = 90387
roberto_property = df[df['room_id'] == roberto_id]
clara_property = df[df['room_id'] == clara_id]
roberto_reviews = roberto_property['reviews'].values[0] #Criticas de roberto
clara_reviews = clara_property['reviews'].values[0] #Criticas de clara

data = {'Property': ['Roberto', 'Clara'],
        'Property ID': [roberto_id, clara_id],
        'Reviews': [roberto_reviews, clara_reviews]}
comparison_df = pd.DataFrame(data)

comparison_df.to_excel('roberto.xlsx', index=False) #Guardar .xls
