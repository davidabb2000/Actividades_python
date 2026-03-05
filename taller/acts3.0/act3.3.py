# Dada una lista predefinida de nombres, crear un programa que permita al usuario buscar un nombre específico. El algoritmo debe recorrer la lista e indicar si el nombre se encuentra o no en ella, mostrando su posición en caso afirmativo.

nombre = str(input("Ingrese el nombre que busca: ")).upper()

lista = ("Juan", "Pedro", "Ernesto")
lista = [x.upper() for x in lista]


if nombre in lista:
    posicion = lista.index(nombre)
    print(f"*{nombre}* se encuentra en la lista, su posicion es: *{posicion}*")
else:
    print(f"*{nombre}* no se encuentra en la lista")