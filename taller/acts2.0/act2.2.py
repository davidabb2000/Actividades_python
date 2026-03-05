# Implementar un menú interactivo con tres opciones: 1. Saludar, 2. Despedirse, 3. Salir. El programa debe mostrar el menú, leer la opción seleccionada y ejecutar la acción correspondiente utilizando estructuras condicionales if-elif-else.
while True:
    print("1. Saludar      |  2. Despedirse     |  3. Salir")
    opcion = input("Ingrese la opcion: ")

    if opcion == "1":
        print("Holas")
        
    elif opcion == "2":
        print("xao")
        
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida, intente de nuevo")
        
    print()