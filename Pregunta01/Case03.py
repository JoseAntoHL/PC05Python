import pandas as pd

df = pd.read_csv('./data/airbnb.csv') #Carga el archivo airbnb.csv

filtered_df = df[(df['price'] <= 50) & (df['room_type'] == 'Shared room')]
sorted_df = filtered_df.sort_values(by=['price', 'overall_satisfaction'], ascending=[True, False])

top_10_properties = sorted_df.head(10) #top 10

print(top_10_properties[['room_id', 'neighborhood', 'price', 'overall_satisfaction']])
