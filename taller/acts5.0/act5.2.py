# Implementar una función llamada calcular_promedio que reciba una lista de números como parámetro y retorne el promedio de esos números. Incluir validación para listas vacías.

def calcular_promedio(numeros):
    if not numeros:
        return "Error: la lista está vacía."
    return sum(numeros) / len(numeros)

entrada = input("Ingrese números separados por comas: ")
numeros = [float(n.strip()) for n in entrada.split(",")]
resultado = calcular_promedio(numeros)
print(f"Promedio: {resultado:.2f}")