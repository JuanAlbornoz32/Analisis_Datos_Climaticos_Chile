import pandas as pd

def convertir_a_DataFrame(datos, campos, guardar_csv=False, nombre_csv="datos.csv"):
    """
    Convierte un diccionario con archivo JSON y metadatos en un DataFrame.

    Parameters
    ----------
    datos : dict 
        Diccionario con metadatos y el archivo JSON extraído de la API.
    campos : list
        Lista de campos a extraer del JSON (Consultar en documentación campos disponible).
    guardar_csv : bool, optional
        Si True, guarda el DataFrame en un archivo CSV (por defecto es False).
    nombre_csv : str, optional
        Nombre del archivo CSV a guardar (por defecto "datos.csv").

    Returns
    -------
    pd.DataFrame
        DataFrame con los datos estructurados.
    """
    
    # Verifica que 'datos' sea un diccionario 
    if not isinstance(datos, dict):
        raise ValueError("Parametro 'datos' debe ser un diccionario")

    # Extrae metadatos y archivo JSON del diccionario
    entidad_id = datos.get("entidad_id", None)
    periodo = datos.get("periodo", None)
    capa = datos.get("capa", None)
    indicador = datos.get("indicador", None)  
    json_data = datos.get("json_data")
    
    # Verifica que 'json_data' sea un diccionario 
    if not isinstance(json_data, dict):  
        raise ValueError("Error en la extracción, 'json_data' debe ser un diccionario")
    
    # Extrae los valores de los campos pasados por parametro dentro de 'json_data' y los guarda en un diccionario
    extracted = {campo: json_data.get(campo, []) for campo in campos}

    # Si todos los campos extraídos son listas vacías, muestra una advertencia y devuelve un DataFrame vacío
    if all(len(valores) == 0 for valores in extracted.values()):
        print("⚠ Advertencia: Ninguno de los campos especificados está presente en el JSON.")
        return pd.DataFrame()

    # Determina la longitud máxima de las listas extraídas
    max_len = max((len(valores) for valores in extracted.values()), default=0)

    # Construye una lista de diccionarios representando cada fila del DataFrame 
    filas = []
    for i in range(max_len):
        # Agrega los campos estáticos al diccionario 'fila'
        fila = {
            "ID_Entidad": entidad_id,
            "Periodo": periodo,
            "Capa_Geografica": capa,
            "Indicador": indicador
        }
        # Itera sobre los campos especificados y agrega sus valores a 'fila'
        for campo in campos:
            valores = extracted.get(campo, [])
            fila[campo] = valores[i] if i < len(valores) else None
        filas.append(fila)

    # Convierte 'filas' en un DataFrame
    df = pd.DataFrame(filas)
    
    # Guardar en CSV si el parámetro está activado
    if guardar_csv:
        df.to_csv(nombre_csv, index=False, encoding="utf-8")
        print(f"📁 Archivo guardado: {nombre_csv}")

    return df

def convertir_masivo_a_DataFrame(lista_datos, campos, guardar_csv=False, nombre_csv="datos_masivos.csv"):
    """
    Convierte una lista de diccionarios con metadatos y datos JSON en un único DataFrame.

    Parameters
    ----------
    lista_datos : list
        Lista de diccionarios, donde cada diccionario contiene metadatos y datos JSON extraídos de la API.
    campos : list
        Lista de campos a extraer del JSON (Consultar en documentación campos disponible).
    guardar_csv : bool, optional
        Si True, guarda el DataFrame en un archivo CSV (por defecto es False).
    nombre_csv : str, optional
        Nombre del archivo CSV a guardar (por defecto "datos_masivos.csv").    

    Returns
    -------
    pd.DataFrame
        DataFrame combinado con los datos estructurados.
    """
    
    if not isinstance(lista_datos, list):
        raise ValueError("lista_datos debe ser una lista de diccionarios.")
    
    dataframes = []  # Lista para almacenar los DataFrames individuales
    
    # Itera sobre cada diccionario de la lista, llamando a la funcion convertir_a_DataFrame
    for datos in lista_datos:
        df = convertir_a_DataFrame(datos, campos)  
        dataframes.append(df)
    
    # Concatenamos todos la lista de diccionarios en un DataFrame
    df_final = pd.concat(dataframes, ignore_index=True)    

    # Guardar en CSV si el parámetro está activado
    if guardar_csv:
        df_final.to_csv(nombre_csv, index=False, encoding="utf-8")
        print(f"📁 Archivo guardado: {nombre_csv}")
    
    return df_final
