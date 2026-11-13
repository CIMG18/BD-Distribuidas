# Sistema de Bases de Datos Distribuidas

Proyecto académico que implementa un sistema de bases de datos distribuidas utilizando **Python, MariaDB y Docker**.

Autores: Christian Morales y Grecia Arias

## Objetivo

Desarrollar un sistema que permita administrar información de clientes y direcciones en diferentes sucursales, utilizando fragmentación horizontal y ofreciendo una interfaz unificada para realizar operaciones sobre los datos.

## Arquitectura

El sistema utiliza dos nodos principales:

| Nodo | Puerto | Base de datos |
|---|---|---|
| Morelia | 3307 | sucursal |
| Pátzcuaro | 3308 | sucursal |

Cada nodo cuenta con las tablas `Clientes` y `Direcciones`.

Los datos se distribuyen horizontalmente según la sucursal a la que pertenecen.

Existe un tercer nodo opcional, Uruapan, configurado para realizar pruebas de expansión.

## Tecnologías utilizadas

- Python
- MariaDB 11
- Docker y Docker Compose
- PyMySQL

## Funcionalidades

- Insertar clientes y direcciones en su sucursal correspondiente.
- Consultar clientes de todas las sucursales desde una sola interfaz.
- Buscar clientes por nombre, RFC o domicilio.
- Actualizar información de clientes y direcciones.
- Eliminar clientes y sus direcciones asociadas.
- Utilizar transacciones para mantener la integridad de los datos.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/CIMG18/BD-Distribuidas.git
cd BD-Distribuidas
```

### 2. Configurar la contraseña

Crear un archivo `.env` en la raíz del proyecto:

```env
DB_ROOT_PASSWORD=root
```

La contraseña debe coincidir con la que utiliza la aplicación Python.

### 3. Iniciar las bases de datos

```bash
docker compose up -d
```

En una instalación nueva, Docker inicializa las tablas y carga los datos de ejemplo desde los archivos SQL.

### 4. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 5. Verificar las conexiones

```bash
python app/test_conexion.py
```

### 6. Ejecutar la aplicación

```bash
python app/main.py
```

## Fragmentación horizontal

La información se almacena según la sucursal seleccionada.

- Los clientes de Morelia se almacenan en el nodo Morelia.
- Los clientes de Pátzcuaro se almacenan en el nodo Pátzcuaro.

El archivo `app/db/particion.py` define la correspondencia entre sucursales y nodos.

## Consultas distribuidas

La aplicación consulta los nodos configurados y reúne sus resultados para presentar una vista global.

De esta manera, el usuario puede buscar clientes sin tener que conectarse manualmente a cada base de datos.

## Integridad de datos

Las tablas utilizan llaves primarias UUID y una relación de llave foránea entre clientes y direcciones.

Las operaciones de actualización y eliminación utilizan transacciones para evitar cambios parciales.

## Limitaciones

- Las conexiones están configuradas para ejecutarse localmente.
- La incorporación de nuevos nodos requiere actualizar la configuración.
- No se implementa replicación automática entre nodos.
- Los archivos SQL inicializan instalaciones nuevas; no sincronizan bases de datos existentes.

## Proyecto académico

Sistema desarrollado como práctica de Bases de Datos Distribuidas.