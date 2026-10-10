import json
import os

from src.inventario import cargar_equipos, guardar_equipos


def registrar_ingreso_mantenimiento(codigo):
    """Marca un equipo como en mantenimiento si existe en el inventario."""
    equipos = cargar_equipos()

    if not codigo:
        print("Error: el código no puede estar vacío.")
        return False

    for equipo in equipos:
        if equipo.get("codigo") == codigo:
            if equipo.get("estado") == "en mantenimiento":
                print(f"El equipo '{codigo}' ya se encuentra en mantenimiento.")
                return True

            equipo["estado"] = "en mantenimiento"
            guardar_equipos(equipos)
            print(f"El equipo '{codigo}' fue registrado como en mantenimiento.")
            return True

    print(f"Error: no se encontró ningún equipo con el código '{codigo}'.")
    return False


def listar_en_mantenimiento():
    """Muestra todos los equipos cuyo estado es en mantenimiento."""
    equipos = cargar_equipos()
    equipos_en_mantenimiento = [equipo for equipo in equipos if equipo.get("estado") == "en mantenimiento"]

    if not equipos_en_mantenimiento:
        print("No hay equipos en mantenimiento.")
        return

    print("Equipos en mantenimiento:")
    for equipo in equipos_en_mantenimiento:
        print(f"- Código: {equipo.get('codigo')} | Nombre: {equipo.get('nombre')} | Ubicación: {equipo.get('ubicacion')}")
