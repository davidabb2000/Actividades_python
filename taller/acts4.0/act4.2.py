contact = {}

while True:
    print("\n--- Directorio de contactos ---")
    print("1. Agregar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Salir")
    op = input("Elige la opcion: ")
    
    match op:
        case "1":
            name= input("Ingrese el nombre: ")
            cel= input("Ingrese el Telefono: ")
            contact[name] = cel
            print("Contacto agregado")
        
        case "2":
            name= input("Digite Nombre a buscar: ")
            if name in contact:
                print(f"Contacto encontrado: {name}", contact[name])
            else:
                print("Contacto no encontrado")
                
        case "3":
            name= input("Digite nombre a eliminar: ")
            if name in contact:
                del contact[name]
                print("Contacto eliminado")
            else:
                print("Contacto no existe")
        
        case "4":
            if not contact:
                print("Contactos vacios")
            else:
                for name, t in contact.items():
                    print(f"{name}: {t}")
                contact[name] = cel
        
        case "5":
            break