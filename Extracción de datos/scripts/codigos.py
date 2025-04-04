import requests
import pandas as pd

BASE_URL = "https://arclim.mma.gob.cl/api/"

# Extracción de codigos de las capas geograficas disponibles por la api
url_capas = BASE_URL + "capas"
response_capas = requests.get(url_capas)
capas = response_capas.json()

df_capas = pd.DataFrame(capas)
df_capas.to_csv("capas_api_arclim.csv", index=False)

# Extracción codigos de los indicadores disponibles por la api
url_indicadores = BASE_URL + "indicadores_climaticos"
response_indicadores = requests.get(url_indicadores)
indicadores = response_indicadores.json()

df_indicadores = pd.DataFrame(indicadores)
df_indicadores.to_csv("indicadores_api_arclim.csv", index=False)

# Extracción de codigos de los atributos disponibles para la capa geografica "comunas"
url_atributos_comunas = BASE_URL + "attributos/comunas/"
response_atributos_comunas = requests.get(url_atributos_comunas)
atributos_comunas = response_atributos_comunas.json()

df_atributos_comunas = pd.DataFrame(atributos_comunas)
df_atributos_comunas.to_csv("atributos_comunas_api_arclim.csv", index=False)

