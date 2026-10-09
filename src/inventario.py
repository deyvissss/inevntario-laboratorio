import json
import os


def registrar_equipo():
    """Registra un nuevo equipo en el archivo JSON del inventario."""
    ruta_base = os.path.dirname(os.path.dirname(__file__))
    ruta_archivo = os.path.join(ruta_base, "data", "equipos.json")

    try:
        if os.path.exists(ruta_archivo) and os.path.getsize(ruta_archivo) > 0:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                equipos = json.load(archivo)
        else:
            equipos = []
    except (FileNotFoundError, json.JSONDecodeError):
        equipos = []

    codigo = input("Ingrese el código del equipo: ").strip()
    if not codigo:
        print("Error: el código no puede estar vacío.")
        return

    for equipo in equipos:
        if equipo.get("codigo") == codigo:
            print(f"Error: el código '{codigo}' ya existe en el inventario.")
            return

    nombre = input("Ingrese el nombre del equipo: ").strip()
    if not nombre:
        print("Error: el nombre no puede estar vacío.")
        return

    tipo = input("Ingrese el tipo del equipo: ").strip()
    if not tipo:
        print("Error: el tipo no puede estar vacío.")
        return

    estado = input("Ingrese el estado del equipo (disponible, en uso, en mantenimiento, dado de baja): ").strip().lower()
    estados_permitidos = ["disponible", "en uso", "en mantenimiento", "dado de baja"]
    if estado not in estados_permitidos:
        print("Error: el estado ingresado no es válido.")
        return

    ubicacion = input("Ingrese la ubicación del equipo: ").strip()
    if not ubicacion:
        print("Error: la ubicación no puede estar vacía.")
        return

    nuevo_equipo = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado,
        "ubicacion": ubicacion,
    }

    equipos.append(nuevo_equipo)

    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(equipos, archivo, ensure_ascii=False, indent=2)

    print(f"Equipo '{nombre}' registrado correctamente.")
