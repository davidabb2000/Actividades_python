
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
op = input("Ingrese la operación (+, -, /, *): ")

if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == "*":
    resultado = num1 * num2
elif op == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: No se puede dividir entre 0."

else:
    resultado = "Operación no válida."


print(f"El cálculo: {num1} {op} {num2} es igual a: {resultado}")