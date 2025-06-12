peliculas=[]

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n\t Presiona una tecla para continuar...")

def agregarPelicula():
    borrarPantalla()
    print("\n\t .::Agregar Películas::.\n")
    peliculas.append(input("Ingrese el nombre: ").upper().strip())
    print("\n\t\t:::La operación se realizó con exito")

def mostrarPeliculas():
    borrarPantalla()
    print(".::Mostrar todas las Peliculas::.")
    if len(peliculas)>0:
        for i in range (0,len(peliculas)):
            print(f"{i+1} : {peliculas[i]}")
    else:
        print("No hay peliculas en este momento en el sistema::.")