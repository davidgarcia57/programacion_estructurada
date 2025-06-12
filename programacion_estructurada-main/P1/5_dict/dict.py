"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("clear")

paises=["México","Brasil","Canada","España"]

pais1={"nombre":"México"
       "capital":"CDMX",
       "poblacion":12000000,
       "idioma":"español",
       "status":True
       }

pais2={"nombre":"Brasil"
       "capital":"Brasilia",
       "poblacion":14000000,
       "idioma":"portugues",
       "status":True
       }

pais3={"nombre":"Canada"
       "capital":"Otawa",
       "poblacion":10000000,
       "idioma":["ingles","frances"],
       "status":True
       }

print(pais1)

for i in pais 1:
   print(f"{i}= {pais1[i]}")

#Agregar un atributo a un objeto
pais1.["altitud"]=3000
for i in pais 1:
   print(f"{i}= {pais1[i]}")

#Modificar un valor o item que ya existe
pais1.update("altitud":2500)
for i in pais 1:
   print(f"{i}= {pais1[i]}")

#Eliminar el ultimo atributo de un objeto
pais1.popitem()
for i in pais 1:
   print(f"{i}= {pais1[i]}")

"Eliminar un atributo a eleccion
pais1.pop("status")
for i in pais 1:
   print(f"{i}= {pais1[i]}")
