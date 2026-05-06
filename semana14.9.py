numbers = list(map(int, input("Ingrese los numeros : ").split()))


def lista(numbers):
    suma = 0
    for num in numbers:
        if num % 2 == 0:
            suma += num
    return suma

suma = lista(numbers)
print(f"la suma de los numeros pares: {suma}")
