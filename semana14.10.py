def orden(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = input("Ingrese 6 números separados por espacios: ").split()
numeros = [int(x) for x in numeros[:6]]

numerosorden = orden(numeros)
print(numerosorden)

   
  