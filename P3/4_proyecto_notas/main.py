import funciones
from notas import nota
from usuarios import usuario
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            # password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\tSe registro el usuario {nombre} {apellidos} correctamente")
            else:
                print(f"\n\t..No fue posible registrar el usuario en este momento, intentalo mas tarde ...")    
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            lista_usuarios=usuario.inicio_sesion(email,password)
            if len(lista_usuarios)>0:
              menu_notas(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2])
            else:
              print(f"\n\tE-mail y/o contraseña incorrectas por favor verifique ....")
              funciones.esperarTecla()    
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            respuesta = nota.crear(usuario_id, titulo, descripcion)
            if respuesta:
                print(f"\n\t Se creo la nota {titulo} con exito.")
            else:
                print(f"\n\t No fue posible crear la nota en este momento, intentalo mas tarde...")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo
            lista_notas = nota.mostrar(usuario_id)
            if len(lista_notas) > 0:    
                print(f"\n\t Mostrar las Notas")
                print(f"{'ID':<5} {'Titulo':<20} {'Descripción':<30} {'Fecha':<20}")
                print("-" * 80)
                for fila in lista_notas:
                    print(f"\n\t ID: {fila[0]<5} Titulo: {fila[2]:<20} Descripción: {fila[3]:<30} Fecha: {fila[4]}")
                print("-" * 80)
            else:
                print("\n\t No hay notas para este usuario.")
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            lista_notas = nota.mostrar(usuario_id)
            if len(lista_notas) > 0:    
                print(f"\n\t Mostrar las Notas")
                print(f"{'ID':<5} {'Titulo':<20} {'Descripción':<30} {'Fecha':<20}")
                print("-" * 80)
                respuesta=input("\t \t ¿Deseas actualizar una nota? (Si/No): ").strip().upper()
                if respuesta != 'SI':
                    for fila in lista_notas:
                        print(f"\n\t ID: {fila[0]<5} Titulo: {fila[2]:<20} Descripción: {fila[3]:<30} Fecha: {fila[4]}")
                    print("-" * 80)
                    print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar una Nota ::. \n")
                    id = input("\t \t ID de la nota a actualizar: ")
                    titulo = input("\t Nuevo título: ")
                    descripcion = input("\t Nueva descripción: ")
                    respuesta = nota.cambiar(id, titulo, descripcion)
                    if respuesta:
                        print(f"\n\t Se actualizó la nota {titulo} correctamente.")
                    else:
                        print(f"\n\t No fue posible actualizar la nota en este momento, intentalo mas tarde ...")
            else:
                print("\n\t No hay notas para este usuario.")

            funciones.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            lista_notas = nota.mostrar(usuario_id)
            if len(lista_notas) > 0:    
                print(f"\n\t Mostrar las Notas")
                print(f"{'ID':<5} {'Titulo':<20} {'Descripción':<30} {'Fecha':<20}")
                print("-" * 80)
                respuesta=input("\t \t ¿Deseas borrar alguna una nota? (Si/No): ").strip().upper()
                if respuesta == 'SI':
                    print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
                    id = input("\t \t ID de la nota a eliminar: ")
                    resultado = nota.borrar(id)
                    if resultado:
                        print(f"\n\t Se borro la nota con ID {id} correctamente.")
                    else:
                        print(f"\n\t No fue posible borrar la nota en este momento, intentalo mas tarde ...")
                else:
                    print(f"\n\t No se realizó ninguna acción.")
            funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()


