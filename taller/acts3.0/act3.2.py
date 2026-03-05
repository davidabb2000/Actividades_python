# Implementar un algoritmo que permita al usuario ingresar números de manera continua. El programa debe sumar todos los números ingresados hasta que el usuario ingrese el valor 0, momento en el cual mostrará la suma total acumulada.

suma_total = 0

while True:
    numero = float(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma_total += numero

print(f"La suma total acumulada es: {suma_total}")