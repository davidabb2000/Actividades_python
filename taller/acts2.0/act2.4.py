#Desarrollar un sistema que convierta una calificación numérica (0-100) a su equivalente en letras según la siguiente escala: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59). Validar que la nota ingresada esté dentro del rango permitido.

num = int(input("Ingrese un numero para calificar: "))

if 0 <= num <= 59:
    calificacion = "F"
elif 60 <= num <= 69:
    calificacion = "D"
elif 70 <= num <= 79:
    calificacion = "C"
elif 80 <= num <= 89:
    calificacion = "B"
elif 90 <= num <= 100:
    calificacion = "A"
else:
    print("Numero no valido.")
    
print("Su calificacion de *",num,"* se encuentra en la categoria: ", calificacion)