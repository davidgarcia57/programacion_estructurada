def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("Presiona Enter para continuar...")

def menu_principal():
    print("📝 Sistema de Calificaciones")
    print("\n\t1.- ✅ Agregar Calificación")
    print("\t2.- 📂 Mostrar Calificaciones")
    print("\t3.- 🕒 Calcular Promedio")
    print("\t4.- 🚪 Salir\n")
    opcion = input("🔍 Selecciona una opción de 1-4: ")
    return opcion

def agregar_calificacion(lista):
    borrarPantalla()
    print("✅ Agregar Calificaciones\n")
    nombre = input("👤 Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 3 + 1):
        continua= True
        while continua:
            try:
                cal = float(input(f"📝 Ingrese la calificación {i} de {nombre}: "))
                if cal >= 0 and cal <= 10:
                    calificaciones.append(cal)
                    continua = False
                else:
                    print("⚠️ La calificación debe estar entre 0 y 10.\n")
            except ValueError:
                print("❌ Entrada inválida. Por favor, ingrese un valor número.\n")
    lista.append([nombre] + calificaciones)
    print("\n🎉 Acción realizada con éxito\n")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("📂 Mostrar Calificaciones\n")
    if len(lista) > 0:
        print(f" {'👤 Nombre':<15}{'📝 Calif. 1':<10}{'📝 Calif. 2':<10}{'📝 Calif. 3':<10}")
        print("-" * 50)
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:10}{fila[2]:10}{fila[3]:<10}")
            print("-" * 50)
        cuantos = len(lista)
        print(f"\nSon {cuantos} alumnos\n")
    else:
        print("⚠️ No hay calificaciones registradas.\n")

def calcular_promedio(lista):
    borrarPantalla()
    print("🕒 Promedio de nuevos alumnos\n")
    if len(lista) > 0:
        print(f" {'👤 Nombre':<15}{'🧮 Promedio':<10}")
        print("-" * 40)
        promedio_grupal = 0
        for fila in lista:
            nombre = fila[0]
            promedio = sum(fila[1:]) / 3
            print(f"{nombre:<15}{promedio:<10.2f}")
            promedio_grupal += promedio
        print("-" * 40)
        promedio_grupal = promedio_grupal/ len(lista)
        print(f"\n🎉 Promedio grupal: {promedio_grupal:.2f}\n")
    else:
        print("⚠️ No hay calificaciones registradas.\n")