#Dict u objeto que permita almacenar los siguientes atributos: (nombre, categoria, clasificacion, genero, idioma)

#pelicula = {
#    "nombre": "",
#    "categoria": "",
#    "clasificacion": "",
#    "genero": "",
#    "idioma": ""

pelicula={}

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n\t Presiona una tecla para continuar...")

def crearPeliculas():
    borrarPantalla()
    print("\n\t\t\t\tCrear Pelicula")
    pelicula.update(input("\n\t Nombre de la pelicula: ").strip().upper())
    print("\n\t Pelicula creada exitosamente!")
    esperarTecla()

