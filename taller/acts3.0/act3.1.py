# Crear un programa que solicite al usuario un número entero positivo N y muestre todos los números pares desde 1 hasta N utilizando un ciclo for.

num = int(input("Ingrese un número entero positivo: "))

if num > 0:
    print(f"Números pares desde 1 hasta {num}:")
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)
else:
    print("El número ingresado no es positivo. Intente de nuevo.")