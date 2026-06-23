Línea 3: Detección y análisis de eventos meteorológicos extremos
Desarrollo de un sistema automático de detección de eventos extremos (olas de calor, olas
de frío, episodios de precipitación intensa/DANA) a partir de datos observacionales. El alumno
definirá criterios cuantitativos para cada tipo de evento (basados en percentiles o umbrales
absolutos), aplicará estos criterios sobre décadas de datos, y analizará si hay cambios en la
frecuencia, duración e intensidad de estos eventos a lo largo del tiempo.
Objetivos específicos:
● Definir e implementar criterios de detección para al menos 3 tipos de eventos extremos
● Procesar datos diarios de todas las estaciones disponibles en paralelo (dask/polars)
● Construir un catálogo de eventos extremos con metadatos (inicio, fin, duración, intensidad,
extensión espacial)
● Analizar tendencias temporales en la frecuencia e intensidad de cada tipo de evento
● Crear visualizaciones interactivas de los eventos detectados (mapas animados, timelines)
Fuentes de datos recomendadas: AEMET OpenData, ECA&D (índices precalculados como
referencia)
Reto Big Data: Procesamiento paralelo de miles de series diarias, definición robusta de umbrales
(percentiles locales vs globales), manejo de datos faltantes.