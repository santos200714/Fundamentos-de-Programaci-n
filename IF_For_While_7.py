monto = float(input("Ingrese el monto de la compra: "))

if monto > 100:
    descuento = 0.20
elif monto >= 50 and monto <= 100:
    descuento = 0.10
elif monto < 50:
    descuento = 0.10
else:
    descuento = 0.0

montofinal = monto * (1 - descuento)

print(f"El descuento aplicado es del {descuento * 100:.0f}%.")
print(f"El monto final a pagar es: {montofinal:.2f}")