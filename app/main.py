"""
Programa principal del sistema de BD distribuida.

Permite insertar clientes nuevos (se guardan en el nodo de su sucursal)
y consultar todos los clientes de ambos nodos como si fueran una sola BD.

Ejecutar desde la raíz del proyecto:
    python3 app/main.py
"""

import uuid
import pymysql

from db.conexion import conectar
from db.particion import nodo_para, PARTICION


# ─────────────────────────────────────────────
#  INSERTAR UN CLIENTE NUEVO
# ─────────────────────────────────────────────

def insertar_cliente():
    print("\n── Insertar cliente nuevo ──")

    # Elegir sucursal
    opciones = list(PARTICION.keys())
    print("Sucursales disponibles:", ", ".join(opciones))
    sucursal = input("Sucursal: ").strip().lower()

    try:
        nodo = nodo_para(sucursal)
    except ValueError as e:
        print(f"  [!] {e}")
        return

    # Datos del cliente
    nombre   = input("Nombre: ").strip()
    ap_pat   = input("Apellido paterno: ").strip()
    ap_mat   = input("Apellido materno (Enter para omitir): ").strip() or None
    rfc      = input("RFC: ").strip().upper()

    # Datos de dirección
    print("\n── Dirección ──")
    calle   = input("Calle: ").strip()
    numero  = input("Número: ").strip()
    colonia = input("Colonia: ").strip()
    estado  = input("Estado: ").strip()
    cp      = input("CP (5 dígitos): ").strip()

    # Generar UUIDs
    id_cliente   = str(uuid.uuid4())
    id_direccion = str(uuid.uuid4())

    try:
        conn = conectar(nodo)
        conn.begin()

        with conn.cursor() as cur:
            # Insertar cliente
            cur.execute(
                """
                INSERT INTO Clientes (Id, Nombre, ApellidoPaterno, ApellidoMaterno, RFC)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (id_cliente, nombre, ap_pat, ap_mat, rfc)
            )

            # Insertar dirección
            cur.execute(
                """
                INSERT INTO Direcciones (Id, Calle, Numero, Colonia, Estado, CP, idCliente)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (id_direccion, calle, numero, colonia, estado, cp, id_cliente)
            )

        conn.commit()
        conn.close()
        print(f"\n  ✅ Cliente guardado en el nodo '{nodo}' correctamente.")

    except Exception as e:
        conn.rollback()
        conn.close()
        print(f"\n  ❌ Error al guardar: {e}")


# ─────────────────────────────────────────────
#  CONSULTAR TODOS LOS CLIENTES (VISTA GLOBAL)
# ─────────────────────────────────────────────

def listar_clientes():
    print("\n── Clientes en toda la red (todos los nodos) ──\n")

    todos = []

    for sucursal, nodo in PARTICION.items():
        try:
            conn = conectar(nodo)
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT c.Nombre, c.ApellidoPaterno, c.ApellidoMaterno, c.RFC,
                           d.Calle, d.Numero, d.Colonia, d.Estado, d.CP
                    FROM Clientes c
                    LEFT JOIN Direcciones d ON d.idCliente = c.Id
                    ORDER BY c.ApellidoPaterno, c.Nombre
                    """
                )
                filas = cur.fetchall()
            conn.close()

            for fila in filas:
                fila["_sucursal"] = sucursal
                todos.append(fila)

        except Exception as e:
            print(f"  [!] No se pudo consultar el nodo '{nodo}': {e}")

    if not todos:
        print("  (Sin registros en ningún nodo)")
        return

    print(f"  {'SUCURSAL':<12} {'NOMBRE':<30} {'RFC':<14} {'DIRECCIÓN'}")
    print(f"  {'─'*12} {'─'*30} {'─'*14} {'─'*40}")

    for r in todos:
        nombre_completo = f"{r['Nombre']} {r['ApellidoPaterno']}"
        if r['ApellidoMaterno']:
            nombre_completo += f" {r['ApellidoMaterno']}"

        direccion = "—"
        if r['Calle']:
            direccion = f"{r['Calle']} {r['Numero']}, {r['Colonia']}, {r['Estado']} {r['CP']}"

        print(f"  {r['_sucursal']:<12} {nombre_completo:<30} {r['RFC']:<14} {direccion}")

    print(f"\n  Total: {len(todos)} cliente(s) en la red.")


# ─────────────────────────────────────────────
#  ACTUALIZAR UN CLIENTE
# ─────────────────────────────────────────────


def actualizar_cliente():
    print("\n── Actualizar cliente ──")

    print("Sucursales disponibles:", ", ".join(PARTICION))
    sucursal = input("Sucursal: ").strip().lower()

    try:
        nodo = nodo_para(sucursal)
    except ValueError as e:
        print(f"[!] {e}")
        return

    rfc = input("RFC del cliente a actualizar: ").strip().upper()
    conn = None

    try:
        conn = conectar(nodo)

        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM Clientes WHERE RFC = %s",
                (rfc,)
            )
            cliente = cur.fetchone()

            if not cliente:
                print("No se encontró el cliente.")
                return

            cur.execute(
                "SELECT * FROM Direcciones WHERE idCliente = %s",
                (cliente["Id"],)
            )
            direcciones = cur.fetchall()

        print(f"\nCliente: {cliente['Nombre']} {cliente['ApellidoPaterno']}")
        print("Deja vacío cualquier campo que no quieras modificar.")

        campos_cliente = {
            "Nombre": "Nombre",
            "ApellidoPaterno": "Apellido paterno",
            "ApellidoMaterno": "Apellido materno",
            "RFC": "RFC"
        }

        cambios_cliente = {}

        for campo, etiqueta in campos_cliente.items():
            valor = input(f"{etiqueta} [{cliente[campo] or ''}]: ").strip()

            if valor:
                cambios_cliente[campo] = (
                    valor.upper() if campo == "RFC" else valor
                )

        cambios_direccion = {}
        direccion_elegida = None

        if direcciones:
            print("\nDirecciones del cliente:")

            for i, d in enumerate(direcciones, 1):
                print(
                    f"{i}. {d['Calle']} {d['Numero']}, "
                    f"{d['Colonia']}, {d['Estado']} {d['CP']}"
                )

            seleccion = input(
                "Número de dirección a modificar "
                "(Enter para omitir): "
            ).strip()

            if seleccion:
                if not seleccion.isdigit() or not (
                    1 <= int(seleccion) <= len(direcciones)
                ):
                    print("Dirección no válida.")
                    return

                direccion_elegida = direcciones[int(seleccion) - 1]

                for campo in ("Calle", "Numero", "Colonia", "Estado", "CP"):
                    valor = input(
                        f"{campo} [{direccion_elegida[campo]}]: "
                    ).strip()

                    if valor:
                        if campo == "CP" and (
                            len(valor) != 5 or not valor.isdigit()
                        ):
                            print("El CP debe contener exactamente 5 dígitos.")
                            return

                        cambios_direccion[campo] = valor

        if not cambios_cliente and not cambios_direccion:
            print("No se realizaron cambios.")
            return

        print("\nSe actualizarán los datos seleccionados.")
        confirmar = input("¿Confirmas? (s/n): ").strip().lower()

        if confirmar != "s":
            print("Operación cancelada.")
            return

        conn.begin()

        with conn.cursor() as cur:
            if cambios_cliente:
                campos = ", ".join(
                    f"{campo} = %s" for campo in cambios_cliente
                )
                valores = list(cambios_cliente.values())

                cur.execute(
                    f"UPDATE Clientes SET {campos} WHERE Id = %s",
                    valores + [cliente["Id"]]
                )

            if cambios_direccion:
                campos = ", ".join(
                    f"{campo} = %s" for campo in cambios_direccion
                )
                valores = list(cambios_direccion.values())

                cur.execute(
                    f"UPDATE Direcciones SET {campos} WHERE Id = %s",
                    valores + [direccion_elegida["Id"]]
                )

        conn.commit()
        print("\n✅ Datos actualizados correctamente.")

    except Exception as e:
        if conn is not None:
            conn.rollback()
        print(f"\n❌ Error al actualizar: {e}")

    finally:
        if conn is not None:
            conn.close()


# ─────────────────────────────────────────────
#  ELIMINAR UN CLIENTE
# ─────────────────────────────────────────────


def eliminar_cliente():
    print("\n── Eliminar cliente ──")

    print("Sucursales disponibles:", ", ".join(PARTICION))
    sucursal = input("Sucursal: ").strip().lower()

    try:
        nodo = nodo_para(sucursal)
    except ValueError as e:
        print(f"[!] {e}")
        return

    rfc = input("RFC del cliente: ").strip().upper()

    if not rfc:
        print("[!] Debes ingresar un RFC.")
        return

    conn = None

    try:
        conn = conectar(nodo)

        with conn.cursor() as cur:
            cur.execute(
                "SELECT Id, Nombre, ApellidoPaterno FROM Clientes WHERE RFC = %s",
                (rfc,)
            )
            clientes = cur.fetchall()

        if not clientes:
            print("No se encontró ningún cliente con ese RFC.")
            return

        if len(clientes) > 1:
            print("Hay varios clientes con ese RFC. Operación cancelada.")
            return

        cliente = clientes[0]
        print(f"Cliente: {cliente['Nombre']} {cliente['ApellidoPaterno']}")

        confirmar = input("¿Confirmas la eliminación? (s/n): ").strip().lower()

        if confirmar != "s":
            print("Operación cancelada.")
            return

        conn.begin()

        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM Direcciones WHERE idCliente = %s",
                (cliente["Id"],)
            )

            cur.execute(
                "DELETE FROM Clientes WHERE Id = %s",
                (cliente["Id"],)
            )

        conn.commit()
        print("✅ Cliente y sus direcciones eliminados correctamente.")

    except Exception as e:
        if conn is not None:
            conn.rollback()
        print(f"❌ Error al eliminar: {e}")

    finally:
        if conn is not None:
            conn.close()


def buscar_clientes():
    print("\n── Búsqueda global de clientes ──")
    print("1. Buscar por nombre")
    print("2. Buscar por RFC")
    print("3. Buscar por domicilio")

    opcion = input("Elige una opción: ").strip()

    columnas = {
        "1": "CONCAT_WS(' ', c.Nombre, c.ApellidoPaterno, c.ApellidoMaterno)",
        "2": "c.RFC",
        "3": "CONCAT_WS(' ', d.Calle, d.Numero, d.Colonia, d.Estado, d.CP)"
    }

    if opcion not in columnas:
        print("Opción no válida.")
        return

    busqueda = input("¿Qué deseas buscar?: ").strip()

    if not busqueda:
        print("Debes escribir un valor.")
        return

    resultados = []
    errores = []

    for sucursal, nodo in PARTICION.items():
        try:
            conn = conectar(nodo)

            try:
                with conn.cursor() as cur:
                    sql = f"""
                        SELECT c.Nombre, c.ApellidoPaterno,
                               c.ApellidoMaterno, c.RFC,
                               d.Calle, d.Numero, d.Colonia,
                               d.Estado, d.CP
                        FROM Clientes c
                        LEFT JOIN Direcciones d
                            ON d.idCliente = c.Id
                        WHERE {columnas[opcion]} LIKE %s
                    """

                    cur.execute(sql, (f"%{busqueda}%",))
                    filas = cur.fetchall()

                    for fila in filas:
                        fila["Sucursal"] = sucursal
                        resultados.append(fila)
            finally:
                conn.close()

        except Exception as e:
            errores.append(sucursal)
            print(f"Error al consultar {sucursal}: {e}")

    if not resultados:
        if errores:
            print("\nNo se encontraron coincidencias en los nodos consultados.")
            print("La búsqueda está incompleta porque algunos nodos fallaron.")
        else:
            print("\nNo se encontraron coincidencias.")
        return

    print(f"\nSe encontraron {len(resultados)} resultado(s):\n")

    for cliente in resultados:
        print(f"Sucursal: {cliente['Sucursal']}")
        print(
            f"Nombre: {cliente['Nombre']} "
            f"{cliente['ApellidoPaterno']} "
            f"{cliente['ApellidoMaterno'] or ''}"
        )
        print(f"RFC: {cliente['RFC']}")
        print(
            f"Dirección: {cliente['Calle']} "
            f"{cliente['Numero']}, "
            f"{cliente['Colonia']}, "
            f"{cliente['Estado']} "
            f"{cliente['CP']}"
        )
        print("-" * 40)

    if errores:
        print("Advertencia: resultados parciales; hubo nodos no disponibles.")


# ─────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────

if __name__ == "__main__":
    while True:
        print("\n════════════════════════════════════════")
        print("   BD DISTRIBUIDA — Morelia / Pátzcuaro  ")
        print("════════════════════════════════════════")
        print("  1. Insertar cliente nuevo")
        print("  2. Ver todos los clientes")
        print("  3. Actualizar cliente")
        print("  4. Eliminar cliente")
        print("  5. Buscar clientes")
        print("  0. Salir")
        print("────────────────────────────────────────")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            insertar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            actualizar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            buscar_clientes()
        elif opcion == "0":
            print("\n  Hasta luego.\n")
            break
        else:
            print("  [!] Opción no válida.")
