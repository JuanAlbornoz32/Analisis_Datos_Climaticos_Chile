import requests
import pandas as pd

# Extracción de capas geograficas disponibles por la api
url_capas = "https://arclim.mma.gob.cl/api/capas"
response_capas = requests.get(url_capas)
capas = response_capas.json()

df_capas = pd.DataFrame(capas)
df_capas.to_csv("capas_api_arclim.csv", index=False)

# Extracción de los indicadores disponibles por la api

url_indicadores = "https://arclim.mma.gob.cl/api/indicadores_climaticos"
response_indicadores = requests.get(url_indicadores)
indicadores = response_indicadores.json()

df_indicadores = pd.DataFrame(indicadores)
df_indicadores.to_csv("indicadores_api_arclim.csv", index=False)

# Extracción de atributos para la capa geografica "comunas"
url_atributos_comunas = "https://arclim.mma.gob.cl/api/attributos/comunas/"
response_atributos_comunas = requests.get(url_atributos_comunas)
atributos_comunas = response_atributos_comunas.json()

df_atributos_comunas = pd.DataFrame(atributos_comunas)
df_atributos_comunas.to_csv("atributos_comunas_api_arclim.csv", index=False)

