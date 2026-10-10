import json
import os


RUTA_DATOS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "equipos.json")
ESTADOS_PERMITIDOS = ["disponible", "en uso", "en mantenimiento", "dado de baja"]


def cargar_equipos():
    """Carga la lista de equipos desde el archivo JSON."""
    try:
        if not os.path.exists(RUTA_DATOS) or os.path.getsize(RUTA_DATOS) == 0:
            return []
        with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
            equipos = json.load(archivo)
        return equipos if isinstance(equipos, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_equipos(equipos):
    """Guarda la lista de equipos en el archivo JSON."""
    os.makedirs(os.path.dirname(RUTA_DATOS), exist_ok=True)
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(equipos, archivo, ensure_ascii=False, indent=2)


def registrar_equipo():
    """Registra un nuevo equipo en el archivo JSON del inventario."""
    equipos = cargar_equipos()

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
    if estado not in ESTADOS_PERMITIDOS:
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
    guardar_equipos(equipos)
    print(f"Equipo '{nombre}' registrado correctamente.")


def listar_equipos():
    """Lista todos los equipos registrados en el inventario."""
    equipos = cargar_equipos()

    if not equipos:
        print("No hay equipos registrados.")
        return

    print("Listado de equipos:")
    for equipo in equipos:
        print(f"- Código: {equipo.get('codigo')} | Nombre: {equipo.get('nombre')} | Tipo: {equipo.get('tipo')} | Estado: {equipo.get('estado')} | Ubicación: {equipo.get('ubicacion')}")


def buscar_equipo():
    """Busca un equipo por su código y muestra sus datos si existe."""
    equipos = cargar_equipos()
    codigo = input("Ingrese el código del equipo a buscar: ").strip()

    if not codigo:
        print("Error: el código no puede estar vacío.")
        return

    for equipo in equipos:
        if equipo.get("codigo") == codigo:
            print("Equipo encontrado:")
            print(f"Código: {equipo.get('codigo')}")
            print(f"Nombre: {equipo.get('nombre')}")
            print(f"Tipo: {equipo.get('tipo')}")
            print(f"Estado: {equipo.get('estado')}")
            print(f"Ubicación: {equipo.get('ubicacion')}")
            return

    print(f"Error: no se encontró ningún equipo con el código '{codigo}'.")


def modificar_estado():
    """Modifica el estado de un equipo registrado."""
    equipos = cargar_equipos()
    codigo = input("Ingrese el código del equipo: ").strip()

    if not codigo:
        print("Error: el código no puede estar vacío.")
        return None

    for equipo in equipos:
        if equipo.get("codigo") == codigo:
            nuevo_estado = input("Ingrese el nuevo estado (disponible, en uso, en mantenimiento, dado de baja): ").strip().lower()
            if nuevo_estado not in ESTADOS_PERMITIDOS:
                print("Error: el estado ingresado no es válido.")
                return None

            equipo["estado"] = nuevo_estado
            guardar_equipos(equipos)
            print(f"Estado actualizado correctamente para el equipo '{codigo}'.")
            return equipo

    print(f"Error: no se encontró ningún equipo con el código '{codigo}'.")
    return None


def eliminar_equipo():
    """Elimina un equipo del inventario por su código."""
    equipos = cargar_equipos()
    codigo = input("Ingrese el código del equipo a eliminar: ").strip()

    if not codigo:
        print("Error: el código no puede estar vacío.")
        return

    equipo_encontrado = None
    for equipo in equipos:
        if equipo.get("codigo") == codigo:
            equipo_encontrado = equipo
            break

    if equipo_encontrado is None:
        print(f"Error: no se encontró ningún equipo con el código '{codigo}'.")
        return

    equipos.remove(equipo_encontrado)
    guardar_equipos(equipos)
    print(f"Equipo '{codigo}' eliminado correctamente.")
