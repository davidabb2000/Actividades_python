# Crear una función llamada es_palindromo que reciba un texto como parámetro y retorne True si es un palíndromo (se lee igual al derecho y al revés) o False en caso contrario. La función debe ignorar espacios, mayúsculas/minúsculas y signos de puntuación.

import string

def es_palindromo(texto):
    limpio = ""
    for c in texto.lower():
        if c not in string.punctuation and c != " ":
            limpio += c
    return limpio == limpio[::-1]

texto = input("Ingrese un texto: ")
if es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")