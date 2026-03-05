# Implementar un programa que permita al usuario ingresar dos listas de elementos. El algoritmo debe mostrar: los elementos comunes a ambas listas, los elementos únicos de la primera lista y los elementos únicos de la segunda lista, implementando esta lógica con ciclos sin usar funciones de conjuntos.

entrada1 = input("Ingrese elementos de la lista 1 separados por comas: ")
entrada2 = input("Ingrese elementos de la lista 2 separados por comas: ")

lista1 = [e.strip() for e in entrada1.split(",")]
lista2 = [e.strip() for e in entrada2.split(",")]

comunes = []
unicos1 = []
unicos2 = []

for elemento in lista1:
    encontrado = False
    for e2 in lista2:
        if elemento == e2:
            encontrado = True
            break
    if encontrado:
        ya_esta = False
        for c in comunes:
            if c == elemento:
                ya_esta = True
                break
        if not ya_esta:
            comunes.append(elemento)
    else:
        unicos1.append(elemento)

for elemento in lista2:
    encontrado = False
    for e1 in lista1:
        if elemento == e1:
            encontrado = True
            break
    if not encontrado:
        unicos2.append(elemento)

print(f"\nElementos comunes    : {comunes}")
print(f"Únicos de la lista 1 : {unicos1}")
print(f"Únicos de la lista 2 : {unicos2}")