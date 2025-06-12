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

def LimpiarPelicula():
    borrarPantalla()
    print(".::Limpiar todas las Peliculas::.")
    resp=input("¿Deseas borrar todas las peliculas del sistema? (Si/No)").lower().strip()
    if resp=="si":
        peliculas.clear()
        print("\n\t\t:::La operación se realizó con exito")

def buscarPelicula():
    borrarPantalla()
    print(".::Buscar Peliculas::.")
    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t.::Esta pelicula a buscar no existe en el sistema::.")
    else:
        encontro=0
        for i in range(0, len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"\n\tLa pelicula{pelicula_buscar}se encontro en el casillero: {i+1}")
                encontro+=1
            print(f"\nTenemos{encontro} pelicula(s) con este titulo")
            print("\n\t.::Esta pelicula a buscar no existe en el sistema::.")

def modificarPeliculas():
    borrarPantalla()
    print(".::Modificar Peliculas::.")
    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t.::Esta pelicula a buscar no existe en el sistema::.")
    else:
        encontro=0
        for i in range(0, len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                resp=input("Deseas actualizar la pelicula (Si/No)").lower()
                if resp=="si":
                    peliculas[i]=input("\n Introduce el nuevo nombre de la pelicula").upper().strip()
                    encontro+=1
                    print("\n\t.::Esta pelicula a buscar no existe en el sistema::.")
            print(f"\nSe modifico{encontro} pelicula(s) con este titulo")