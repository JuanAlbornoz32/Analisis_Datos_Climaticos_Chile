import requests
import pandas as pd
from funciones_extraccion import consulta_masiva, BASE_URL
from convertir_a_df import convertir_masivo_a_DataFrame

"""
    La consulta ha sido estructurada, para obtener en primera instancia los indices y atributos de la capa geográfica "comunas",
    y luego guardar estos indices en una lista, para que junto a una lista de los periodos de tiempo, pasarlos como parametros
    a las funciones 'consulta_masiva' y 'convertir_masivo_a_DataFrame', y así extraer los datos y guardarlos en un archivo CSV 

"""

# Se extraen los atributos de la capa geográfica comunas
url_atributos_comunas = BASE_URL + "datos/comunas/json/?attributes=NOM_COMUNA,NOM_PROVIN,NOM_REGION,REGION"
response_atributos_comunas = requests.get(url_atributos_comunas)

# Si la respuesta es positiva, se pasa a generar un dataframe con los datos y guardarlos en un archivo CSV.
if response_atributos_comunas.status_code == 200:
    datos_comunas = response_atributos_comunas.json()
    print(f"✅ Consulta de atributos de comunas ha sido exitosa")

    df_atributos_comunas = pd.DataFrame(
        datos_comunas["data"]["values"], 
        columns=datos_comunas["data"]["columns"], 
        index=datos_comunas["data"]["index"]
        )
    df_atributos_comunas.to_csv("Atributos comunas de Chile.csv" )

    # Se genera una lista con los códigos de las comunas para iterar en las consultas
    codigo_comunas = df_atributos_comunas.index.tolist()
    # Se genera una lista con los periodos de tiempo sobre los que se quiere iterar en las consultas
    meses = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dec"] 

    # Ejecución consulta de datos de temperaturas medias por comuna (mensual)
    temp_comunas = consulta_masiva("mean_temperature", "comunas", codigo_comunas, meses )
    df_temp_comunas = convertir_masivo_a_DataFrame(
        temp_comunas,
        ["years", "mean"],
        exportar=True,
        nombre_archivo="Datos temperaturas comunas.csv"
    )

    # Ejecución consulta de datos de precipitaciones acumuladas por comuna (mensual)
    pr_comunas = consulta_masiva("pr_sum", "comunas", codigo_comunas, meses )
    df_pr_comunas = convertir_masivo_a_DataFrame(
        pr_comunas,
        ["years", "mean"],
        exportar=True,
        nombre_archivo="Datos precipitaciones comunas.csv"
    )   

else:
    print(f"❗ Error en la consulta de los atributos de comunas. Código de estado: {response_atributos_comunas.status_code}")