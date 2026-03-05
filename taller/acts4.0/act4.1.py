# Implementar un sistema de lista de compras que permita al usuario agregar productos, eliminar productos específicos y mostrar todos los productos actuales. Utilizar una lista para almacenar los elementos.

producto = ()
productos = []

while True:
    print("MENU PARA PRODUCTOS")
    print("----------------------------------------")
    print("1. Agregar Productos")
    print("2. Eliminar Productos")
    print("3. Mostrar productos actuales")
    print("4. Salir")
    print("----------------------------------------")
    opcion = int(input("Ingrese la opcion: "))
    print("----------------------------------------")

    if opcion == 1:
        producto = str(input("Ingrese el nombre del producto que desea agregar: "))
        productos.append(producto)
        print(f"*{producto}* ha sido agregado")
        
    elif opcion == 2:
        producto = str(input("Ingrese el nombre del producto que desea eliminar: "))
        productos.remove(producto)
        print(f"El producto: *{producto}* ha sido eliminado")
        
    elif opcion == 3:
        print("Lista de productos: ", productos)
    elif opcion == 4:
        break