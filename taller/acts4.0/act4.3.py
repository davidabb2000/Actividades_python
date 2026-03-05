# Dada una lista de diccionarios donde cada diccionario representa un producto con las claves "nombre", "precio" y "stock", crear un programa que permita actualizar el precio de un producto específico buscándolo por su nombre.

products = []

while True:
    print("\n--- Directorio de productos ---")
    print("1. Agregar")
    print("2. Actualizar precio")
    print("3. Mostrar")
    print("4. Buscar")
    print("5. Salir")
    op = input("Elige la opción: ")

    match op:
        case "1":
            name = input("Ingrese el nombre del producto: ")
            price = float(input("Ingrese el precio: "))
            stock = int(input("Ingrese la cantidad de stock: "))


            products.append({"nombre": name, "precio": price, "stock": stock})
            print(f"Producto '{name}' agregado correctamente.")

        case "2":
            name = input("Ingrese el nombre del producto a actualizar: ")
            found = False

            for product in products:
                if product["nombre"].lower() == name.lower():
                    new_price = float(input(f"Ingrese el nuevo precio para '{name}': "))
                    product["precio"] = new_price
                    print(f"Precio de '{name}' actualizado a ${new_price:.2f}")
                    found = True
                    break

            if not found:
                print(f"Producto '{name}' no encontrado.")

        case "3":
            if not products:
                print("No hay productos registrados.")
            else:
                print(f"\n{'Nombre':<20} {'Precio':>10} {'Stock':>8}")
                print("-" * 40)
                for product in products:
                    print(f"{product['nombre']:<20} ${product['precio']:>9.2f} {product['stock']:>8}")

        case "4":
            name = input("Ingrese el nombre del producto a buscar: ")
            found = False

            for product in products:
                if product["nombre"].lower() == name.lower():
                    print(f"\nProducto encontrado:")
                    print(f"  Nombre : {product['nombre']}")
                    print(f"  Precio : ${product['precio']:.2f}")
                    print(f"  Stock  : {product['stock']}")
                    found = True
                    break

            if not found:
                print(f"Producto '{name}' no encontrado.")

        case "5":
            print("Saliendo...")
            break

        case _:
            print("Opción no válida.")