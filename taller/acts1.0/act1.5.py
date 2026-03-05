#Ejercicio 1.5 – Convertidor de unidades con menú: Desarrollar un convertidor de unidades con un menú interactivo que ofrezca tres opciones: 1. Convertir Celsius a Fahrenheit, 2. Convertir kilómetros a millas, 3. Convertir kilogramos a libras. El usuario debe seleccionar una opción, ingresar el valor a convertir y el programa mostrará el resultado con dos decimales.

opcion = int(input("Elija la opcion: 1. C a F   |       2. Km a Millas          |          3. Kg a Lb:   "))


if opcion == 1:
    cels = float(input("Ingrese los grados Celsius: "))
    
    cels = (9/5 * cels) + 32
    
    print("El resultado es: ", cels)
    
elif opcion == 2:
    km = float(input("Ingrese los Kilometros: "))
    
    km = km * 0.621371
    
    print("El resultado es: ", km)
elif opcion == 3:
    kg = float(input("Ingrese los Kilogramos: "))
    
    kg = kg * 2.20462
    
    print("El resultado es: ", kg)
else:
    print("La opcion es incorrecta")