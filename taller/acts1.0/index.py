# Ejercicio 1.2 – Calculadora básica: Desarrollar una calculadora simple que solicite al usuario dos números y una operación matemática (+, -, *, /). El algoritmo debe realizar la operación correspondiente y mostrar el resultado. Incluir validación para evitar la división por cero, mostrando un mensaje de error en ese caso.

#Ejercicio 1.3 – Validación de correo electrónico: Crear un programa que pida al usuario ingresar un correo electrónico y verifique que contenga los caracteres "@" y "." en posiciones válidas. Mostrar mensajes apropiados indicando si el correo tiene un formato básico correcto o si presenta errores.

#Ejercicio 1.4 – Validador de contraseña segura: Implementar un sistema que valide la fortaleza de una contraseña. El usuario debe ingresar una contraseña y el algoritmo debe verificar que cumpla con los siguientes criterios: tener al menos 8 caracteres, contener al menos una letra mayúscula, un número y un carácter especial (!@#$%^&*). Informar específicamente qué criterios no se cumplen.

#Ejercicio 1.5 – Convertidor de unidades con menú: Desarrollar un convertidor de unidades con un menú interactivo que ofrezca tres opciones: 1. Convertir Celsius a Fahrenheit, 2. Convertir kilómetros a millas, 3. Convertir kilogramos a libras. El usuario debe seleccionar una opción, ingresar el valor a convertir y el programa mostrará el resultado con dos decimales.


#List
list = ["Manzana","Banano","Arandanos","Fresa","Cereza", "Uva"]
newlist = [x for x in list if "e" in x]
list.remove("Banano")
list.pop()
#for x in range(len(list)):
#    print(list[x])
print(newlist)


# Tuple
# tuple = ("Manzana","Banano","Arandanos","Fresa","Cereza")
# print(tuple[-4:-1])
# Set
# set = {"Manzana","Banano","Arandanos","Fresa","Cereza"}
# print("Fresa" not in set)
# Dictionaries



"""car = {
    "brand": "Toyota",
    "color": ["Gris","Rojo","Azul"],
    "model": 2024,
    "ref": "Yaris",
    "electric": True
}
print(len(car))"""