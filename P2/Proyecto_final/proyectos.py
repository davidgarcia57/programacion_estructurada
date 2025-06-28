# Sistema de Gestión para Ingeniero Civil
# Programación Estructurada con Listas y Diccionarios

def mostrar_menu():
    print("\n=== Sistema de Gestión para Ingeniero Civil ===")
    print("1. Agregar Proyecto")
    print("2. Ver Todos los Proyectos")
    print("3. Actualizar Proyecto")
    print("4. Eliminar Proyecto")
    print("5. Salir")
    return input("Seleccione una opción (1-5): ")

def agregar_proyecto(proyectos):
    id_proyecto = input("Ingrese el ID del Proyecto: ")
    if id_proyecto in proyectos:
        print("¡El ID del proyecto ya existe!")
        return
    nombre = input("Ingrese el Nombre del Proyecto: ")
    ubicacion = input("Ingrese la Ubicación del Proyecto: ")
    presupuesto = float(input("Ingrese el Presupuesto del Proyecto: "))
    materiales = input("Ingrese los Materiales (separados por comas): ").split(",")
    tareas = input("Ingrese las Tareas (separadas por comas): ").split(",")
    proyectos[id_proyecto] = {
        "nombre": nombre,
        "ubicacion": ubicacion,
        "presupuesto": presupuesto,
        "materiales": [m.strip() for m in materiales],
        "tareas": [t.strip() for t in tareas]
    }
    print(f"¡Proyecto {nombre} agregado exitosamente!")

def ver_proyectos(proyectos):
    if not proyectos:
        print("No hay proyectos disponibles.")
        return
    for pid, detalles in proyectos.items():
        print(f"\nID del Proyecto: {pid}")
        print(f"Nombre: {detalles['nombre']}")
        print(f"Ubicación: {detalles['ubicacion']}")
        print(f"Presupuesto: ${detalles['presupuesto']:.2f}")
        print(f"Materiales: {', '.join(detalles['materiales'])}")
        print(f"Tareas: {', '.join(detalles['tareas'])}")

def actualizar_proyecto(proyectos):
    id_proyecto = input("Ingrese el ID del Proyecto a actualizar: ")
    if id_proyecto not in proyectos:
        print("¡Proyecto no encontrado!")
        return
    print("Deje en blanco para mantener el valor actual.")
    nombre = input(f"Ingrese nuevo Nombre ({proyectos[id_proyecto]['nombre']}): ") or proyectos[id_proyecto]['nombre']
    ubicacion = input(f"Ingrese nueva Ubicación ({proyectos[id_proyecto]['ubicacion']}): ") or proyectos[id_proyecto]['ubicacion']
    presupuesto = input(f"Ingrese nuevo Presupuesto ({proyectos[id_proyecto]['presupuesto']}): ")
    presupuesto = float(presupuesto) if presupuesto else proyectos[id_proyecto]['presupuesto']
    materiales = input(f"Ingrese nuevos Materiales (separados por comas, actuales: {', '.join(proyectos[id_proyecto]['materiales'])}): ")
    materiales = materiales.split(",") if materiales else proyectos[id_proyecto]['materiales']
    tareas = input(f"Ingrese nuevas Tareas (separados por comas, actuales: {', '.join(proyectos[id_proyecto]['tareas'])}): ")
    tareas = tareas.split(",") if tareas else proyectos[id_proyecto]['tareas']
    proyectos[id_proyecto] = {
        "nombre": nombre,
        "ubicacion": ubicacion,
        "presupuesto": presupuesto,
        "materiales": [m.strip() for m in materiales],
        "tareas": [t.strip() for t in tareas]
    }
    print(f"¡Proyecto {id_proyecto} actualizado exitosamente!")

def eliminar_proyecto(proyectos):
    id_proyecto = input("Ingrese el ID del Proyecto a eliminar: ")
    if id_proyecto in proyectos:
        del proyectos[id_proyecto]
        print(f"¡Proyecto {id_proyecto} eliminado exitosamente!")
    else:
        print("¡Proyecto no encontrado!")

def main():
    proyectos = {}  # Diccionario para almacenar proyectos
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            agregar_proyecto(proyectos)
        elif opcion == "2":
            ver_proyectos(proyectos)
        elif opcion == "3":
            actualizar_proyecto(proyectos)
        elif opcion == "4":
            eliminar_proyecto(proyectos)
        elif opcion == "5":
            print("Saliendo del sistema. ¡Adiós!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()