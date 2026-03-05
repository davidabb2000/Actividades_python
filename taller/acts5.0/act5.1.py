# Crear una función llamada saludar que reciba dos parámetros: nombre y hora del día. La función debe retornar un saludo apropiado según la hora: "Buenos días [nombre]" (5-12), "Buenas tardes [nombre]" (13-19), "Buenas noches [nombre]" (20-4).

def saludar(nombre, hora):
    if 5 <= hora <= 12:
        return f"Buenos días {nombre}"
    elif 13 <= hora <= 19:
        return f"Buenas tardes {nombre}"
    else:
        return f"Buenas noches {nombre}"

nombre = input("Ingrese su nombre: ")
hora = int(input("Ingrese la hora (0-23): "))
print(saludar(nombre, hora))