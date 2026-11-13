"""
Lógica de partición: decide qué nodo almacena los datos de cada sucursal.

Regla: cada sucursal es dueña de sus propios datos.
El nodo al que pertenece una sucursal es el único que guarda y consulta sus registros.
"""

# Mapa sucursal → nodo
# Si se agrega una nueva sucursal, solo hay que añadirla aquí.
PARTICION = {
    "morelia":   "morelia",
    "patzcuaro": "patzcuaro",
}


def nodo_para(sucursal):
    # Devuelve el nombre del nodo que le corresponde a la sucursal indicada
    sucursal = sucursal.lower().strip()

    if sucursal not in PARTICION:
        raise ValueError(
            f"Sucursal desconocida: '{sucursal}'. "
            f"Opciones: {list(PARTICION.keys())}"
        )

    return PARTICION[sucursal]
