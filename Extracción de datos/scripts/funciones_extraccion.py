import requests
import time

# Base URL de la API
BASE_URL = "https://arclim.mma.gob.cl/api/"

def consulta_de_indicador(indicador, capa, id_entidad, periodo):
    """
    Extrae series de tiempo (1970-1969) de un indicador climático para una entidad geográfica específica desde la API de ARClim.

    Parameters
    ----------
    indicador : str
        Código del indicador climático (por ejemplo, 'mean_temperature', 'pr_sum').
    capa : str
        Código de la capa geográfica ('comunas', 'regiones', etc.).
    id_entidad : int or str
        Código de la entidad (comuna o región) de la cual se quiere extraer información.
    periodo : str
        Código del período de tiempo (por ejemplo, 'annual', 'jan', 'feb').

    Returns
    -------
    dict
        Diccionario con metadatos y la respuesta JSON si la consulta fue exitosa.
    None
        En caso de error en la consulta.

    Examples
    --------
    >>> consulta_de_indicador('mean_temperature', 'comunas', 1101, 'annual')
    {"indicador": "mean_temperature", "capa": "comunas", "entidad_id": "1101", "periodo": "annual", "json_data": {...}}

    """

    id_entidad = str(id_entidad)  # Asegurar que sea string
    url = f"{BASE_URL}series/{indicador}/{capa}/{id_entidad}/{periodo}/" # Se genera la url para realizar la consulta
    response = requests.get(url)

    # Si la respuesta es positiva se guarda el archivo extraido en un diccionario junto con sus metadatos
    if response.status_code == 200:
        data = {
        "indicador": indicador,
        "capa": capa,
        "entidad_id": id_entidad,
        "periodo": periodo,
        "json_data": response.json()
    }
        print(f"✅ Consulta exitosa para entidad {id_entidad}, periodo {periodo}")
        return data
    
    # Si la consulta es erronea se retorna None
    else:
        print(f"❗ Error en la consulta: entidad {id_entidad} - periodo {periodo}")
        return None

def consulta_masiva(indicador, capa, entidades, periodos, delay=0.3):
    """
    
    Realiza consultas de un indicador climático para múltiples entidades y/o periodos de tiempo desde la API de ARClim.

    Parameters
    ----------
    indicador : str
        Código del indicador climático.
    capa : str
        Código de la capa geográfica.
    entidades : list, str or int
        Lista de códigos de entidades o un único código (se convierte a lista).
    periodos : list or str
        Lista de periodos o un único periodo (se convierte a lista).
    delay : float, optional
        Tiempo de espera entre consultas, por defecto 0.3 segundos.

    Returns
    -------
    list
        Lista de diccionarios con los datos y metadatos de cada consulta exitosa.

    Examples
    --------
    >>> consulta_masiva('mean_temperature', 'comunas', [1101, 1102], ['annual', 'jan'])
    [{"indicador": "mean_temperature", "capa": "comunas", "entidad_id": "1101", "periodo": "annual", "json_data": {...}}, {...}]

    """

    if isinstance(entidades, (str, int)):
        entidades = [entidades]
    
    if isinstance(periodos, str):
        periodos = [periodos]   

    resultados = []
    for entidad_id in entidades:
        for periodo in periodos:
            instancia = consulta_de_indicador(indicador, capa, entidad_id, periodo)
            if instancia is not None:
                resultados.append(instancia)            
            time.sleep(delay)          
    
    return resultados


