# Implementar una función llamada factorial que calcule el factorial de un número usando recursión. La función debe recibir un número entero positivo y retornar su factorial. Incluir validación para números negativos.

def factorial(n):
    if n < 0:
        return "Error: no existe factorial de números negativos."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

numero = int(input("Ingrese un número entero positivo: "))
print(f"Factorial de {numero}: {factorial(numero)}")