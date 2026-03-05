# Crear un algoritmo que solicite la edad de una persona y la clasifique en una de las siguientes categorías: niño (0-12 años), adolescente (13-17 años), adulto (18-64 años) o adulto mayor (65 años o más). Mostrar la categoría correspondiente.

edad = int(input("Ingrese su edad: "))

if 0 <= edad <= 12:
    categoria = "niño"
elif 13 <= edad <= 17:
    categoria = "adolescente"
elif 18 <= edad <= 64:
    categoria = "adulto"
elif edad >= 65:
    categoria = "adulto mayor"
else:
    categoria = "Edad no válida"

print(f"La categoría correspondiente es: {categoria}")