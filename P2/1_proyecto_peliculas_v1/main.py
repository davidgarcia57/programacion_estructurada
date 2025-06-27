'''
Crear un proyecto que permita gestionar (administra) peliculas Colocar un menu de opciones: Agregar, Borrar, 
Modificar, Mostrar, Buscar, Limpiar una lista de peliculas.

Notas:
1.- Utilizar funciones y mandar llamar desde el archivo (modulo)
2.- Utilizar una lista para almacenar los nombres de las peliculas
'''

import os
os.system('cls')

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t 1.- Agregar pelicula \n\t 2.- Borrar pelicula \n\t 3.- Modificar pelicula \n\t 4.- Mostrar peliculas " \
    "\n\t 5.- Buscar pelicula \n\t 6.- Limpiar lista de peliculas \n\t 7.- Salir")
    opcion=input("\n\t Selecciona una opcion: ").upper()
    
    match opcion:
        case "1":
            peliculas.agregarPelicula()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPelicula()
            peliculas.esperarTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPelicula()
            peliculas.esperarTecla()
        case "6":
            peliculas.LimpiarPelicula()
            peliculas.esperarTecla()
        case "7":
            print("\n\t Terminaste la ejecucion del programa gracias por usarlo")
            peliculas.borrarPantalla()
            opcion=False
        case _:
            print("\n\t Opcion no valida, por favor selecciona una opcion del menu")
            peliculas.esperarTecla()
            opcion=True