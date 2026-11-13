import pymysql
import os
from pathlib import Path
from dotenv import load_dotenv
import pymysql

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

# Configuración de cada nodo: host, puerto, usuario y contraseña
NODOS = {
    "morelia": {
        "host":     "127.0.0.1",
        "port":     3307,
        "user":     "root",
        "password": os.getenv("DB_ROOT_PASSWORD"),
        "database": "sucursal",
    },
    "patzcuaro": {
        "host":     "127.0.0.1",
        "port":     3308,
        "user":     "root",
        "password": os.getenv("DB_ROOT_PASSWORD"),
        "database": "sucursal",
    },
    # Nodo extra (solo disponible cuando se levanta con --profile extra)
    "uruapan": {
        "host":     "127.0.0.1",
        "port":     3309,
        "user":     "root",
        "password": "root",
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
