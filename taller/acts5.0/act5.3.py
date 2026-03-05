# Tomar el menú de calculadora desarrollado en ejercicios anteriores y refactorizarlo, convirtiendo cada operación matemática en una función separada. El menú principal debe llamar a estas funciones según la opción seleccionada.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero."
    return a / b

while True:
    print("\n--- Calculadora ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    op = input("Elige una opción: ")

    if op == "5":
        print("Saliendo...")
        break

    if op in ["1", "2", "3", "4"]:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        match op:
            case "1": print(f"Resultado: {sumar(a, b)}")
            case "2": print(f"Resultado: {restar(a, b)}")
            case "3": print(f"Resultado: {multiplicar(a, b)}")
            case "4": print(f"Resultado: {dividir(a, b)}")
    else:
        print("Opción no válida.")