email = input("Ingrese su correo electrónico: ")
dig1 = "@"
dig2 = "."

if dig1 in email and dig2 in email:
    position1 = email.find(dig1)  # Encuentra la posición del @
    position2 = email.rfind(dig2)  # Encuentra la última posición del punto

    # Verificar que el @ está antes del punto y que hay texto antes y después de ambos
    if position1 > 0 and position2 > position1 + 1 and position2 < len(email) - 1:
        print("El correo es válido.")
    else:
        print("El correo no tiene el @ y el punto en las posiciones correctas.")
else:
    print("El correo debe contener un '@' y un '.'.")