Este script analiza archivos TXT, CSV, JSON y XML de un proyecto.
Genera un informe en JSON con estadísticas como número de líneas, palabras, filas, columnas y elementos.
El resultado se guarda en informe_resultados.json en la carpeta del proyecto.
He utilizado los archivos: alumnos_ejemplo_grande.json    animales_mundo_grande.csv         calendario_festivos_grande.xml       estadisticas_partidos_grande.txt
El programa se ejecuta poniendo en la barra inferior de visual studio code "python .\leer_archivos"
El informe informe_resultados.json contiene:
TXT: número de líneas y palabras.
CSV: número de filas, columnas y nombres de las columnas.
JSON: número de elementos y "apartados" de la lista (nombre, edad, grado...).
XML: etiqueta raíz y número de elementos <pais> (u otros nodos relevantes) 
