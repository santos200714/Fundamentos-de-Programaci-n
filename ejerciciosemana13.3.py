while True:
    numero = int(input("Escribe un número (-1 para salir): "))

    if numero == -1:
        break

    for i in range(1, 11):
        producto = numero * i
        if producto > 20:
            print(f"{numero} x {i} = {producto}")