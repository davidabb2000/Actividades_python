# Desarrollar un programa que solicite al usuario ingresar una lista de números separados por comas. El algoritmo debe calcular y mostrar: el valor máximo, el valor mínimo, el promedio y la suma total de todos los números.

entrada = input("Ingrese números separados por comas: ")
numeros = [float(n.strip()) for n in entrada.split(",")]

maximo = numeros[0]
minimo = numeros[0]
suma = 0

for n in numeros:
    if n > maximo:
        maximo = n
    if n < minimo:
        minimo = n
    suma += n

promedio = suma / len(numeros)

print(f"\nMáximo  : {maximo}")
print(f"Mínimo  : {minimo}")
print(f"Promedio: {promedio:.2f}")
print(f"Suma    : {suma}")