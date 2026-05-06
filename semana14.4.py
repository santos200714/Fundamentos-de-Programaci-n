def encontrarmayor(lista):
  
    mayor = max(lista)
    return mayor

entrada = input("Ingrese 8 números separados por espacios: ").split()
numeros = [int(x) for x in entrada[:8]]


if len(numeros) < 8:
    print("Error: Debes ingresar  8 números.")
else:
   
    resultado = encontrarmayor(numeros)
    print(f"La lista es: {numeros}")
    print(f"El número mayor es: {resultado}")