contador = 0

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    if numero % 2 != 0:
        contador += 1

print("La cantidad de números impares ingresados es:", contador)