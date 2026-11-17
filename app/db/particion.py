"""
Lógica de partición: cada sucursal almacena
sus datos en su nodo correspondiente.
"""

from db.conexion import NODOS

# Crear automáticamente el mapa sucursal → nodo
PARTICION = {
    nombre: nombre
    for nombre in NODOS
}


def nodo_para(sucursal):
    sucursal = sucursal.lower().strip()

    if sucursal not in PARTICION:
        raise ValueError(
            f"Sucursal desconocida: '{sucursal}'. "
            f"Opciones: {list(PARTICION.keys())}"
        )

    return PARTICION[sucursal]