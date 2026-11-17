import pymysql
import os
from pathlib import Path
from dotenv import load_dotenv
import json


ARCHIVO_NODOS = Path(__file__).resolve().parents[2] / "nodos.json"

NODOS_INICIALES = {"morelia", "patzcuaro"}

def cargar_nodos():
    if ARCHIVO_NODOS.exists():
        with open(ARCHIVO_NODOS, "r", encoding="utf-8") as archivo:
            nodos_guardados = json.load(archivo)

        for nombre, datos in nodos_guardados.items():
            variable = datos["password_env"]
            password = os.getenv(variable)

            if password is None:
                print(f"[!] Falta configurar {variable} en .env")
                continue

            NODOS[nombre] = {
                "host": datos["host"],
                "port": datos["port"],
                "user": datos["user"],
                "password": password,
                "database": datos["database"]
            }


def guardar_nodo(nombre, configuracion):
    NODOS[nombre] = configuracion

    nodos_adicionales = {}

    for nodo, datos in NODOS.items():
        if nodo not in NODOS_INICIALES:
            nodos_adicionales[nodo] = {
                "host": datos["host"],
                "port": datos["port"],
                "user": datos["user"],
                "database": datos["database"],
                "password_env": f"DB_PASSWORD_{nodo.upper()}"
            }

    with open(ARCHIVO_NODOS, "w", encoding="utf-8") as archivo:
        json.dump(nodos_adicionales, archivo, indent=4)

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

# Configuración de cada nodo: host, puerto, usuario y contraseña
NODOS = {
    "morelia": {
        "host":     "172.20.10.3",
        "port":     3307,
        "user":     "root",
        "password": os.getenv("DB_ROOT_PASSWORD"),
        "database": "sucursal",
    },
    "patzcuaro": {
        "host":     "172.20.10.2",
        "port":     3308,
        "user":     "root",
        "password": os.getenv("DB_ROOT_PASSWORD"),
        "database": "sucursal",
    },
    
}


def conectar(nodo):
    # Valida que el nodo exista antes de intentar conectar
    if nodo not in NODOS:
        raise KeyError(f"Nodo desconocido: '{nodo}'. Opciones: {list(NODOS.keys())}")

    cfg = NODOS[nodo]
    conn = pymysql.connect(
        host=cfg["host"],
        port=cfg["port"],
        user=cfg["user"],
        password=cfg["password"],
        database=cfg["database"],
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,  # resultados como diccionarios
    )
    return conn


def conectar_todos():
    # Intenta conectar a todos los nodos; omite los que no estén disponibles
    conexiones = {}
    for nombre in NODOS:
        try:
            conexiones[nombre] = conectar(nombre)
        except Exception as e:
            print(f"  [!] No se pudo conectar a '{nombre}': {e}")
    return conexiones

cargar_nodos()
