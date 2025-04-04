# 📌 **Análisis de Tendencias Climáticas en Chile**


## 🌍 Descripción General

Este proyecto tiene como objetivo analizar **tendencias climáticas** en las distintas zonas geográficas de Chile. Para ello, se implementará un proceso **ETL** que iniciará con la extracción de datos climáticos desde la **API Arclim** del Ministerio del Medio Ambiente de Chile, desde donde se recopilarán medidas de diversos **indicadores climáticos** a nivel nacional, desagregados por distintas **capas geográficas**.

Los datos proporcionados por **Arclim** se generan a partir de **simulaciones climáticas** basadas en modelos GCM (Modelos de Circulación General). Esto permite obtener tanto **proyecciones futuras** como reconstrucciones de **medidas históricas** para diversos indicadores climáticos con base en estos modelos.

Tras la **extracción, limpieza y transformación** de los datos, se procederá a realizar un **análisis exploratorio y estadístico** para identificar patrones y variaciones en los indicadores climáticos a lo largo del tiempo. Finalmente, se creará un **visualizador de datos** dentro de una app, que permita explorar la información de manera interactiva.

## 🏷️ Etapas del Proyecto

1️⃣ **Extracción de Datos ✅**  

  •	Obtención de datos climáticos desde la **API Arclim**.

  •	Conversión de datos a formatos estructurados (**CSV, DataFrames**).

2️⃣ **Limpieza y Transformación de los Datos (Etapa actual)** 

•	Eliminación de **inconsistencias** y **valores faltantes**.

•	**Estandarización y estructuración** de los datos para su análisis.

3️⃣ **Almacenamiento en Base de Datos**  

•	Diseño e implementación de una **base de datos** para almacenar y gestionar los datos transformados.

•	Carga eficiente de los datos en el sistema de almacenamiento.

4️⃣ **Análisis exploratorio y Modelado**  

•	Identificación de **patrones y tendencias climáticas** a lo largo del tiempo.

•	Aplicación de **análisis estadísticos y visualización** de distribuciones.

5️⃣ **Creación de un Visualizador de Datos**  

•	Creación de una **aplicación** para explorar los datos de manera dinámica.

•	Implementación de **gráficos y filtros** para el análisis visual.


## 💾 1. Extracción de Datos (Etapa Actual)

La API Arclim permite acceder a **series de tiempo (1970-2070)** de diversos indicadores climáticos, como temperatura media, precipitación acumulada y olas de calor, entre otros. Estos datos están desagregados por distintas **capas geográficas** (comunas, regiones, caletas, áreas protegidas, etc.) y las **entidades** que conforman cada una de ellas.

Para **automatizar** el proceso de extracción, se desarrolló un conjunto de **scripts en Python** que facilitan la consulta de datos en la API, su conversión a DataFrames y su exportación a archivos CSV.

**📝 Documentación de la API:** [Arclim API](#)

### 📚 Estructura de la Extracción (Scripts)

**📌 codigos.py**  
- Descarga los **códigos** de las **capas geográficas** y los **indicadores climáticos** disponibles, los cuales son necesarios para estructurar las consultas.  
- Obtiene los **atributos** y entidades de la capa **"comunas"**.  

**📌 funciones_extraccion.py**  
- Contiene funciones para realizar consultas a la API de manera flexible, pudiendo especificar **entidad**, **capa geográfica**, **indicador climático** y **periodo de tiempo** del cual se necesite información.
- Las funciones permiten realizar tanto **consultas individuales** como para **multiples entidades** de una capa geográfica. 
- Las funciones retornan diccionarios, con los **metadatos** de la consulta y el **archivo JSON** con la información obtenida de la API.  

**📌 convertir_a_df.py**  
- Contiene funciones para convertir los datos obtenidos por las funciones de extracción en **DataFrames de Pandas** y exportarlos a archivos **CSV**.
- Las funciones permiten seleccionar los **campos de información** que se requieren extraer de la **respuesta JSON**.  

**📌 consultas.py**  
- Ejecuta la extracción de datos específicos: **temperatura media** y **precipitación acumulada** para las distintas comunas de Chile.  

## 📊 Datos Extraídos

✅ **Códigos de referencia**  
- 📋 Listado de códigos de **capas geográficas** e **indicadores climáticos** disponibles.  

✅ **Datos por comuna (desagregados por mes y año)**  
- 🌡️ **Temperatura media**  
- 🌧️ **Precipitación acumulada**  

✅ **Atributos de la capa "comunas"**  
- 📍 **Nombre de la comuna**  
- 🏛️ **Provincia a la que pertenece**  
- 🌎 **Región a la que pertenece**  

## 🛠️ Herramientas Utilizadas

- **Lenguaje:** Python  
- **Librerías:** requests, pandas  
- **Instalación de dependencias:**  

```bash
pip install -r requirements.txt
```

## 🔜 Próximo Paso

La siguiente etapa del proyecto se centrará en la limpieza y transformación de los datos, preparando la información para su posterior almacenamiento en una base de datos.

## ✨ Autor

📌 [Juan Albornoz](https://www.linkedin.com/in/juan-albornoz-carrillo/)

🚀 ¡Si tienes comentarios o sugerencias, no dudes en contribuir o abrir una issue!


