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
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────

if __name__ == "__main__":
    while True:
        print("\n════════════════════════════════════════")
        print("   BD DISTRIBUIDA — Morelia / Pátzcuaro  ")
        print("════════════════════════════════════════")
        print("  1. Insertar cliente nuevo")
        print("  2. Ver todos los clientes")
        print("  0. Salir")
        print("────────────────────────────────────────")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            insertar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "0":
            print("\n  Hasta luego.\n")
            break
        else:
            print("  [!] Opción no válida.")
