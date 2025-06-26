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
    print("\n\t\t\t\tAgregar Peliculas")
    pelicula.update({"nombre": input("\n\t Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria": input("\n\t Ingresa la categoria: ").upper().strip()})
    pelicula.update({"clasificacion": input("\n\t Ingresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero": input("\n\t Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma": input("\n\t Ingresa el idioma: ").upper().strip()})
    print("\n\t LA OPERACION SE REALIZO CON EXITO")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t\t\t\tMostrar Peliculas")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\n\t {i}: {pelicula[i]}")
    else:
        print("\n\t No hay peliculas registradas")

def borrarPelicula():
    borrarPantalla()
    print("\n\t\t\t\tBorrar o Quitar la Pelicula")
    if len(pelicula) > 0:
        resp= input("\n\t Deseas borrar la pelicula? (S/N): ").upper().strip()
        if resp == "S":
            pelicula.clear()
            print("\n\t La pelicula se ha borrado con exito")
    else:
        print("\n\t No hay peliculas registradas")

            
def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t\tAgregar Caracteristica a la Pelicula")
    if len(pelicula) > 0:
        atributo = input("\n\t Ingresa el nombre de la caracteristica quedeseas agregar: ").lower().strip()
        valor_atributo = input(f"\n\t Ingresa el valor para {atributo}: ").upper().strip()
        pelicula[atributo] = valor_atributo
        print("\n\t La caracteristica se ha agregado con exito")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t\tModificar Caracteristica de la Pelicula")
    if len(pelicula) > 0:
        resp="SI"
        while resp=="SI":
            for i in pelicula:
                resp= input(f"\n\t Deseas modificar el valor de {i}: {pelicula[i]}? (Si/No): ").upper().strip()
                if resp == "SI":
                    nuevo_valor = input(f"\n\t Ingresa el nuevo valor para {i}: ").upper().strip()
                    pelicula[i] = nuevo_valor
                    print("\n\t El valor se ha modificado con exito")
                    esperarTecla()
    else:
        print("\n\t No hay caracteristicas de las peliculas a mostrar")
    
def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t\tBorrar Caracteristica de la Pelicula")
    if len(pelicula) > 0:
        print("Valores actuales:")
        for i in pelicula:
            print(f"\n\t {i}: {pelicula[i]}")
        resp = input("\n\t ¿Deseas borrar alguna caracteristica? (Si/No): ").upper().strip()
        if resp == "SI":
            atributo = input("\n\t Ingresa el nombre de la caracteristica que deseas borrar o quitar: ").lower().strip()
            if atributo in pelicula:
                del pelicula[atributo]
                print("\n\t La caracteristica se ha borrado con exito")
            else:
                print("\n\t La caracteristica no existe, por favor ingresa otra")
    else:
        print("\n\t No hay caracteristicas de las peliculas a mostrar")