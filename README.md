📌 Proyecto Datos Climáticos de Chile

🌍 Descripción General
Este proyecto tiene como objetivo la extracción, limpieza, análisis y visualización de datos climáticos de Chile, los cuales serán obtenidos desde la API Arclim del Ministerio del Medio Ambiente de Chile.
La API permite acceder a datos de diferentes indicadores climáticos como temperaturas medias, precipitaciones acumuladas, olas de calor, entre otros, los cuales han sido calculados a partir de distintas simulaciones climáticas. Esta información puede ser desagregada para diferentes capas geográficas (comunas, regiones, caletas, áreas protegidas, etc.), y distintas entidades de cada una de estas capas.

📄 Documentación de la API: Arclim API
________________________________________
🏗️ Etapas del Proyecto
1️⃣ Extracción de Datos (Etapa actual) ✅
2️⃣ Limpieza y Transformación de los Datos
3️⃣ Migración a una Base de Datos
4️⃣ Análisis Estadístico y Modelado
5️⃣ Creación de un Visualizador de Datos
________________________________________
📥 1. Extracción de Datos (Etapa Actual)

La API permite realizar consultas para series climáticas que van de 1970 hasta 2070, para localidades específicas, por lo que se opto por este tipo de consultas para extraer información de dos indicadores climáticos, para las distintas comunas de Chile.  
✅ Temperatura media
✅ Precipitación acumulada

Para automatizar este proceso, se estructuró una serie de scripts en Python que facilitan las consultas a la API, la conversión de los datos a DataFrames de Pandas y su exportación a archivos CSV.

📂 Estructura de la Extracción

🔹 Scripts Principales
📌 codigos.py
•	Descarga los códigos de las capas geográficas y los indicadores climáticos disponibles, los cuales son necesarios para estructurar las consultas.
•	Obtiene los atributos y entidades de la capa "comunas".
📌 funciones_extraccion.py
•	Contiene dos funciones para realizar consultas a la API y obtener datos climáticos de una entidad de alguna capa geográfica especificada, para un periodo de tiempo (año, estación, meses).
•	Las funciones retornan diccionarios con los metadatos de la consulta y un archivo json con su información.
📌 convertir_a_df.py
•	Convierte los datos extraídos por las funciones de extracción, en DataFrames de Pandas y los exporta a archivos CSV.
📌 consultas.py
•	Ejecuta la extracción de datos específicos, la temperatura media y precipitación acumulada, para las distintas comunas de Chile.
________________________________________
📊 Datos Extraídos

✅ Códigos de referencia
•	Listado de códigos de capas geográficas e indicadores climáticos disponibles.
✅ Datos por comuna (desagregados por mes y año)
•	🌡️ Temperatura media
•	🌧️ Precipitación acumulada
✅ Atributos de la capa "comunas"
•	Nombre de la comuna
•	Provincia a la que pertenece
•	Región a la que pertenece
________________________________________
🛠️ Herramientas Utilizadas
•	Lenguaje: Python
•	Librerías: requests, pandas
•	Instalación de dependencias: pip install -r requirements.txt
________________________________________
🔜 Próximo Paso
La siguiente etapa del proyecto se centrará en la limpieza y transformación de los datos, preparando la información para su posterior almacenamiento en una base de datos.
________________________________________
✨ Autor
📌 Juan Albornoz
🚀 ¡Si tienes comentarios o sugerencias, no dudes en contribuir o abrir una issue!
