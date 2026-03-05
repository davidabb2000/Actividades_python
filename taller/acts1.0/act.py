while True:

    name = str(input("Ingrese su nombre: "))
    age = int(input("Ingrese su edad: "))
    city = str(input("Ingrese su ciudad de residencia: "))

    if age > 0:
        print("Hola ",name, ",tienes ",age, " y vives en ",city)
        print("La edad es un numero positivo")
        break
    elif age == 0:
        print("Tiene 0 años??? XD")
    else:
        print("La edad es un numero negativo")
