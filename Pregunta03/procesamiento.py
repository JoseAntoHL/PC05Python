#Cree un archivo llamado procesamiento .py
import pandas as pd
import requests

df = pd.read_excel('./data/reactiva.xlsx')

def obtener_tipo_cambio():
    try:
        url = "https://api.apis.net.pe/v2/sunat/tipo-cambio?date=2023-05-01"
        response = requests.get(url)
        data = response.json()
        if 'result' in data and 'venta' in data['result']:
            return data['result']['venta']
        else:
            print("No se encontró el tipo de cambio en la respuesta:", data)
            return None
    except Exception as e:
        print("Error al obtener el tipo de cambio:", e)
        return None

#Genere una función de limpieza que permita el renombre de las columnas eliminando espacios, tildes y convirtiendo los nombres de columna a minúscula. 
#De ser necesario cambie el nombre de columna a uno que le sea de más ayuda.

def limpieza(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

#Elimine la columna ID y TipoMoneda que se encuentre repetida.
    if 'id' in df.columns:
        df.drop('id', axis=1, inplace=True) 
    if 'tipomoneda' in df.columns:
        df.drop('tipo_moneda', axis=1, inplace=True) 

#De la columna “DISPOSITIVO LEGAL” elimine el carácter coma ‘,’ del texto.
    if 'dispositivo_legal' in df.columns:
        df['dispositivo_legal'] = df['dispositivo_legal'].str.replace(',', '') 

#Empleando el api de sunat de la pc4. Dolarice los valores de montos de inversión y montos de transferencia de acuerdo con el valor actual del dólar. 
#Deberá mostrar estos montos en dos nuevas columnas.
    tipo_cambio = obtener_tipo_cambio()['result']['venta']
    if tipo_cambio:
        df['monto_inversion_usd'] = df['monto_de_inversion'] / tipo_cambio
        df['monto_transferencia_usd'] = df['monto_de_transferencia_2020'] / tipo_cambio

#Para la columna “Estado” cambie los valores a: Actos Previos, Concluido, Resuelto y Ejecucion
    df['estado'] = df['estado'].replace({'Actos Previos': 'ActosPrevios', 'Resuelto': 'Resuelto', 'Ejecucion': 'Ejecución'}, regex=True)

#Cree una nueva columna que puntue el estado según: ActosPrevios -> 1, Resuelto->0, Ejecución 2 y Concluido 3
    df['estado_puntuado'] = df['estado'].map({'ActosPrevios': 1, 'Resuelto': 0, 'Ejecución': 2, 'Concluido': 3})
    return df

df_limpiado = limpieza(df)

#Genere los siguientes reportes
#Almacene en una base de datos una tabla de ubigeos a partir de los datos sin duplicados de las columnas “ubigeo”, “Region”, “Provincia”, “Distrito”
ubigeos = df_limpiado[['ubigeo', 'region', 'provincia', 'distrito']].drop_duplicates()

#Por cada región genere un Excel con el top 5 costo inversión de las obras de tipo Urbano en estado 1,2,3. 
#En caso no haber datos en alguna de las regiones, no se generará el reporte
for region, datos_region in df_limpiado.groupby('region'):
    top_inversiones = datos_region[datos_region['tipoologia'] == 'Urbano'].sort_values(by='monto_de_inversion_dolar', ascending=False).head(5)
    for estado in [1, 2, 3]:
        top_inversiones_estado = top_inversiones[top_inversiones['puntaje_estado'] == estado]
        if not top_inversiones_estado.empty:
            top_inversiones_estado.to_excel(f'top_inversiones_{region}_estado_{estado}.xlsx', index=False)
