import requests
import pandas as pd
from funciones_extraccion import consulta_de_indicador, consulta_masiva, BASE_URL
from convertir_a_df import convertir_a_DataFrame, convertir_masivo_a_DataFrame


# Se extrae los datos de las comunas 
url_datos_comunas = BASE_URL + "datos/comunas/json/?attributes=NOM_COMUNA,NOM_PROVIN,NOM_REGION,REGION"
response_datos_comunas = requests.get(url_datos_comunas)
datos_comunas = response_datos_comunas.json()

# Se convierten los datos extraidos de las comunas en un dataframe
df_atributos_comunas = pd.DataFrame(datos_comunas["data"]["values"], columns=datos_comunas["data"]["columns"], index=datos_comunas["data"]["index"])
df_atributos_comunas.to_csv("Atributos comunas de Chile.csv" )

# Se genera una lista con los codigos de las comunas 
codigo_comunas = df_atributos_comunas.index.tolist()
meses = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dec"] 


pr_comunas = consulta_masiva("pr_sum", "comunas", codigo_comunas, meses )
df_pr_comunas = convertir_masivo_a_DataFrame(pr_comunas, ["years", "mean"], True, "Datos precipitaciones comunas.csv")

