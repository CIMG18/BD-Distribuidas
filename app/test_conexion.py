"""
Script de prueba de la capa de conexión.

Verifica que cada nodo responda correctamente y que el esquema esté aplicado.
Ejecutar desde la raíz del proyecto:
    python3 app/test_conexion.py
"""

from db.conexion import conectar, NODOS


def probar_nodo(nombre: str) -> None:
    print(f"\n{'─' * 40}")
    print(f"  Nodo: {nombre.upper()}")
    print(f"{'─' * 40}")
    try:
        conn = conectar(nombre)
        with conn.cursor() as cur:
            # Versión del servidor
            cur.execute("SELECT VERSION() AS version")
            row = cur.fetchone()
            print(f"  ✅ Conectado  →  MariaDB {row['version']}")

            # Tablas disponibles
            cur.execute("SHOW TABLES")
            tablas = [list(r.values())[0] for r in cur.fetchall()]
            print(f"  📋 Tablas     →  {', '.join(tablas) if tablas else '(ninguna)'}")

            # Conteo de registros
            for tabla in tablas:
                cur.execute(f"SELECT COUNT(*) AS total FROM `{tabla}`")
                total = cur.fetchone()["total"]
                print(f"  📊 {tabla:<15} →  {total} registros")

        conn.close()
    except Exception as e:
        print(f"  ❌ Error: {e}")


if __name__ == "__main__":
    print("\n════════════════════════════════════════")
    print("   PRUEBA DE CONEXIÓN — BD DISTRIBUIDA  ")
    print("════════════════════════════════════════")

    # Probamos solo morelia y patzcuaro (los nodos siempre activos)
    for nodo in ["morelia", "patzcuaro"]:
        probar_nodo(nodo)

    print(f"\n{'─' * 40}")
    print("  Prueba finalizada.\n")
