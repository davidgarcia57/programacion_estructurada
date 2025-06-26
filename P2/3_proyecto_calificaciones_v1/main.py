import os
os.system('cls')

import calificaciones

opcion=True

while opcion:
    calificaciones.borrarPantalla()
    print("\n\t 1.- Agregar \n\t 2.- Mostrar \n\t 3.- Calcular \n\t 4.- Salir ")
    opcion=input("\n\t Selecciona una opcion: ").upper()
    
    match opcion:
        case "1":
            calificaciones.AgregarCalificacion()
            calificaciones.esperarTecla()
        case "2":
            calificaciones.borrarPelicula()
            calificaciones.esperarTecla()
        case "3":
            calificaciones.mostrarPeliculas()
            calificaciones.esperarTecla()
        case "4":
            opcion=False
            print("\n\t Terminaste la ejecucion del programa gracias por usarlo")
            calificaciones.borrarPantalla()
        case _:
            print("\n\t Opcion no valida, por favor selecciona una opcion del menu")
            calificaciones.esperarTecla()
            opcion=True