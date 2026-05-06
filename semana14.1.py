numbers = list(map(int, input("Ingrese los numeros : ").split()))
pares = 0
impares = 0
def lista(numbers):
    global pares, impares
    for num in numbers:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
   
lista(numbers)
print(f"Cantidad de numeros pares: {pares}")
print(f"Cantidad de numeros impares: {impares}")    
