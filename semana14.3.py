notas = [int(x) for x in input("Ingrese las notas del 1 al 10 separadas por espacios: ").split()]

promedio = sum(notas) / len(notas)
print(f"El promedio  es: {promedio:.2f}")

if promedio >= 6:
    print("Aprueba")
else:
    print("Reprueba")