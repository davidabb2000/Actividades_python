# Expandir la calculadora básica del ejercicio 1.2 agregando un menú que permita al usuario realizar múltiples operaciones sin salir del programa. El menú debe incluir las cuatro operaciones básicas y una opción para salir.

while True:

    print("MENU DE INTERACCION")
    print("---------------------------")
    print("Ingrese la tecla especifica para cada operacion")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    print("---------------------------")
    op = input("Ingrese la operacion: ")
    
    if op=="5":
        print("Saliendo del programa...")
        break
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if op == "1":
        resultado = num1 + num2
        print(f"El cálculo: {num1} + {num2} es igual a: {resultado}")
    elif op == "2":
        resultado = num1 - num2
        print(f"El cálculo: {num1} - {num2} es igual a: {resultado}")
    elif op == "3":
        resultado = num1 * num2
        print(f"El cálculo: {num1} * {num2} es igual a: {resultado}")
    elif op == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"El cálculo: {num1} / {num2} es igual a: {resultado}")
            
        else:
            resultado = "Error: No se puede dividir entre 0."
    else:
        resultado = "Operación no válida."
    
print()