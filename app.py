from src.inventario import eliminar_equipo, buscar_equipo, listar_equipos, modificar_estado, registrar_equipo
from src.mantenimiento import listar_en_mantenimiento, registrar_ingreso_mantenimiento


def mostrar_menu():
    """Muestra el menú principal del sistema en consola."""
    print("=======================================")
    print("   SISTEMA DE INVENTARIO DE LABORATÓRIO")
    print("=======================================")
    print("1. Registrar equipo")
    print("2. Listar equipos")
    print("3. Buscar equipo")
    print("4. Modificar estado")
    print("5. Eliminar equipo")
    print("0. Salir")
    print("=======================================")
    return input("Seleccione una opción: ").strip()


def main():
    """Ejecuta la aplicación principal del inventario."""
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            buscar_equipo()
        elif opcion == "4":
            equipo_actualizado = modificar_estado()
            if equipo_actualizado is not None and equipo_actualizado.get("estado") == "en mantenimiento":
                registrar_ingreso_mantenimiento(equipo_actualizado.get("codigo"))
        elif opcion == "5":
            eliminar_equipo()
        elif opcion == "0":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
