import random

numeros = [random.randint(0, 100) for _ in range(10)]

mayor = 0
def mayores50(numeros):
    global mayor
    for numero in numeros:
        if numero > 50:
            mayor += 1

mayores50(numeros)

print("Números generados:", numeros)
print(f"Cantidad de números mayores a 50: {mayor}")

