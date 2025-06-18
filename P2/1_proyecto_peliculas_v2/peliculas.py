peliculas=[]

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n\t Presiona una tecla para continuar...")

def agregarPelicula():

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


