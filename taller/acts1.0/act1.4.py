#Ejercicio 1.4 – Validador de contraseña segura: Implementar un sistema que valide la fortaleza de una contraseña. El usuario debe ingresar una contraseña y el algoritmo debe verificar que cumpla con los siguientes criterios: tener al menos 8 caracteres, contener al menos una letra mayúscula, un número y un carácter especial (!@#$%^&*). Informar específicamente qué criterios no se cumplen.

passw = input("Ingrese su contraseña: ")
caract = ["!","@","#","$","%","^","&","*"]
num = ["1","2","3","4","5","6","7","8"]

if 8 > len(passw):
    print("La contraseña debe tener al menos 8 caracteres")
elif not any(x in passw for x in caract):
    print("La contraseña debe tener un caracter especial")
elif not any(c in passw for c in num):
    print("La contraseña debe tener un numero")
else:
    print("La contraseña es segura")