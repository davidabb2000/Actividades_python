# Crear un simulador de descuentos que solicite al usuario su categoría (A, B, C) y el monto de compra. Aplicar los siguientes descuentos según categoría: A=20%, B=15%, C=10%. Para cualquier otra categoría no aplicar descuento. Mostrar el monto final a pagar y la cantidad ahorrada.


# Crear un simulador de descuentos que solicite al usuario su categoría (A, B, C) y el monto de compra. Aplicar los siguientes descuentos según categoría: A=20%, B=15%, C=10%. Para cualquier otra categoría no aplicar descuento. Mostrar el monto final a pagar y la cantidad ahorrada.


categoria = input("Ingrese su categoría (A, B, C): ").upper()
monto_compra = float(input("Ingrese el monto de su compra: "))

if categoria == "A":
    descuento = 0.20
elif categoria == "B":
    descuento = 0.15
elif categoria == "C":
    descuento = 0.10
else:
    descuento = 0.0

cantidad_ahorrada = monto_compra * descuento
monto_final = monto_compra - cantidad_ahorrada

print(f"Ahorrado: ${cantidad_ahorrada}")
print(f"Pago final: ${monto_final}")