peliculas=[]

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n\t Presiona una tecla para continuar...")

def agregarPelicula():
    borrarPantalla()
    pelicula = input("\n\t Ingresa el nombre de la pelicula a agregar: ")
    if pelicula:
        peliculas.append(pelicula)
        print(f"\n\t Pelicula '{pelicula}' agregada exitosamente.")
    else:
        print("\n\t No se ingresó un nombre válido.")

