from typing import Any, Optional
from cola import queue
from lista import List
from pila import Stack
from datos_superheroes import superheroes
from pprint import pprint



superheroes1 = [
    {"name": "Spider-Man", "alias": "Peter Parker"},
    {"name": "Iron Man", "alias": "Tony Stark"},
    {"name": "Captain America", "alias": "Steve Rogers"},
    {"name": "Thor", "alias": "Thor Odinson"},
    {"name": "Hulk", "alias": "Bruce Banner"},
    {"name": "Black Widow", "alias": "Natasha Romanoff"},
    {"name": "Hawkeye", "alias": "Clint Barton"},
    {"name": "Black Panther", "alias": "T'Challa"},
    {"name": "Doctor Strange", "alias": "Stephen Strange"},
    {"name": "Scarlet Witch", "alias": "Wanda Maximoff"},
    {"name": "Vision", "alias": "Vision"},
    {"name": "Ant-Man", "alias": "Scott Lang"},
    {"name": "Wasp", "alias": "Hope van Dyne"},
    {"name": "Falcon", "alias": "Sam Wilson"},
    {"name": "Winter Soldier", "alias": "Bucky Barnes"}
]



# ejercicio 1 recursividad - buscar a capitan america

def buscar_capitan_america(superheroes1, pos= 0):
    if pos >= len(superheroes1):
        return False
    
    if superheroes1[pos]["name"].lower() == "captain america":
        return True
    
    return buscar_capitan_america(superheroes1, pos + 1)


if buscar_capitan_america(superheroes1):
    print(f"capitan america se encuentra en la lista")
else:
    print(f"capitan america no se encuentra en la lista ")


#ejercicio 2 recursividad - listar superheroes
print("\n")
print("Listado de super heroes: ")
def listar (superheroes1, pos=0):
    if pos >= len(superheroes1):
     return 
    print(superheroes1[pos])
    listar(superheroes1, pos + 1)

listar(superheroes1)



#EJERCICIO 2 


#Listado ordenado de manera ascendente por nombre de los personajes.
superheroes2 = List()

for heroe in superheroes:
    superheroes2.append(heroe)


print("\n")
print("Listado por nombre")
def order_by_name(item):
    return item["name"]

superheroes2.add_criterion("nombre", order_by_name)

superheroes2.sort_by_criterion("nombre")

superheroes2.show()


#Determinar en que posicion esta The Thing y Rocket Raccoon.

def order_by_alias(item):
    return item["alias"]

superheroes2.add_criterion("alias", order_by_alias)

superheroes2.sort_by_criterion("alias")


print("\n")
print("Las posiciones de los buscados son: ")
pos_heroe = superheroes2.search("The Thing", "alias")
if pos_heroe is not None:
    print(f"The Thing se encuentra en la posicion {pos_heroe} de la lista")
else:
    print("The Thing no esta en la lista")

pos_heroe = superheroes2.search("Rocket Raccoon", "alias")
if pos_heroe is not None:
    print(f"Rocket Raccoon se encuentra en la posicion {pos_heroe} de la lista")
else:
    print("Rocket Raccoon no esta en la lista")




#Listar todos los villanos de la lista
print ("\n")
print("Listado de villanos ")
for heroe in superheroes2:
    if heroe["is_villain"] == True:
        pprint(heroe["name"])


#Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
print("\n")
print("cola villanos")
cola_villanos = queue()
for heroe in superheroes2:
    if heroe["is_villain"] == True:
        cola_villanos.arrive(heroe)
        
cola_villanos.show()

print("\n")
print("Villanos que aparecieron antes de 1980: ")
while cola_villanos.size() > 0:
    heroe = cola_villanos.atenttion()
    if heroe["first_appearance"] < 1980:
        print(f"{heroe["name"]}, {heroe["first_appearance"]}")


#Listar los superheores que comienzan con  Bl, G, My, y W
print("\n")
print("Los super heroes cuyos nombres empiezan con Bl, G, My, y W, son:  ")
letras = ("Bl", "G", "My","W")
for heroe in superheroes:
    if heroe["alias"].startswith(letras):
        print(f"{heroe["alias"]}")


#Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
print("\n")
print("Listado ordenado por nomnbre real")

def order_by_real_name(item):
    return item["real_name"]

superheroes2.add_criterion("real_name", order_by_real_name)

superheroes2.sort_by_criterion("real_name")
print()

superheroes2.show()


#Listado de superheroes ordenados por fecha de aparación.
print("\n")
print("Listado por anio de aparicion")
def order_by_anio_aparicion(item):
    return item["first_appearance"]

superheroes2.add_criterion("aparicion", order_by_anio_aparicion)

superheroes2.sort_by_criterion("aparicion")

superheroes2.show()


#Modificar el nombre real de Ant Man a Scott Lang.
print("\n")
print("cambio de nombre ")

def order_by_alias(item):
    return item["alias"]

superheroes2.add_criterion("alias", order_by_alias)

pos_antman = superheroes2.search("Ant Man", "alias")

if pos_antman is not None:
    superheroes[pos_antman]["real_name"] = "Scott Lang"
    print(f"Nombre actualizado a {superheroes[pos_antman]}")
else:
    print("Ant Man no se encuentra en la lista.")


#Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
print("\n")
print("Los superheroes que en su biografia incluyen la palabra time-traveling o suit, son :")
buscadas = ["time-traveling", "suit"]

for heroe in superheroes:
    bio_lower = heroe["short_bio"].lower()
    if any(buscada in bio_lower for buscada in buscadas):
        print(f" {heroe["alias"]}")

#Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista
print("\n")
print("eliminar a Electro")
eliminado = superheroes2.delete_value("Electro", "alias")
print(f"el eliminado es: {eliminado}")

print("\n")
print("eliminar a Baron Zemo")
eliminado = superheroes2.delete_value("Baron Zemo", "alias")
print(f"el eliminado es: {eliminado}")

