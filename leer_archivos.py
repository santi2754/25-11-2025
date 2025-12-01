import json
import csv
import xml.etree.ElementTree as ET
from pathlib import Path

# FUNCIONES DE LECTURA DE ARCHIVOS

def analizar_txt(ruta: Path):
    """Lee un archivo TXT y devuelve estadísticas básicas."""
    if not ruta.exists():
        return {
            "archivo": ruta.name,
            "error": True,
            "detalle": "El archivo no existe en la carpeta del proyecto."
        }

    try:
        contenido = ruta.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        contenido = ruta.read_text(encoding="latin-1")

    lineas = contenido.strip().splitlines()

    return {
        "archivo": ruta.name,
        "num_lineas": len(lineas),
        "num_palabras": len(contenido.split())
    }


def analizar_csv(ruta: Path):
    """Lee un archivo CSV y devuelve información básica."""
    try:
        with ruta.open("r", encoding="utf-8") as f:
            reader = csv.reader(f)
            filas = list(reader)

        if filas:
            header = filas[0]
            num_columnas = len(header)
            num_filas = len(filas) - 1
        else:
            header = []
            num_columnas = 0
            num_filas = 0

        return {
            "archivo": ruta.as_posix(),
            "num_filas": num_filas,
            "num_columnas": num_columnas,
            "columnas": header
        }

    except Exception as e:
        return {
            "archivo": ruta.as_posix(),
            "procesado_correctamente": False,
            "detalle": str(e)
        }


def analizar_json(ruta: Path):
    """Lee un archivo JSON y devuelve estadísticas básicas."""
    try:
        with ruta.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            num_elementos = len(data)
            claves_primer_elemento = list(data[0].keys()) if num_elementos > 0 else []
        elif isinstance(data, dict):
            num_elementos = 1
            claves_primer_elemento = list(data.keys())
        else:
            num_elementos = 0
            claves_primer_elemento = []

        return {
            "archivo": ruta.as_posix(),
            "num_elementos": num_elementos,
            "claves_primer_elemento": claves_primer_elemento
        }

    except Exception as e:
        return {
            "archivo": ruta.as_posix(),
            "procesado_correctamente": False,
            "detalle": str(e)
        } 


def analizar_xml(ruta: Path):
    """Lee un archivo XML y devuelve información del nodo raíz y número de países."""
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()

        lista_paises = root.findall("pais")

        return {
            "archivo": ruta.as_posix(),
            "procesado_correctamente": True,
            "etiqueta_raiz": root.tag,
            "num_paises": len(lista_paises)
        }

    except Exception as e:
        return {
            "archivo": ruta.as_posix(),
            "procesado_correctamente": False,
            "detalle": str(e)
        }

# PROCESAMIENTO PRINCIPAL

ruta_txt = Path("estadisticas_partidos_grande.txt")
ruta_csv = Path("animales_mundo_grande.csv")
ruta_json = Path("alumnos_ejemplo_grande.json")
ruta_xml = Path("calendario_festivos_grande.xml")

resultado = {
    "txt": analizar_txt(ruta_txt),
    "csv": analizar_csv(ruta_csv),
    "json": analizar_json(ruta_json),
    "xml": analizar_xml(ruta_xml)
}

# ESCRIBIR ARCHIVO DE RESULTADOS

with open("informe_resultados.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, indent=4, ensure_ascii=False)

print("✔ Informe generado correctamente: informe_resultados.json")