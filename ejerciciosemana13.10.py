
numeros = []
suma = 0


while suma <= 100:
    numero = float(input("Ingresa un número: "))
    
  
    if numero >= 0:
        numeros.append(numero)
        suma += numero
    else:
        print("Número negativo ignorado")


print("Números válidos ingresados:")
for num in numeros:
    print(num)

print(f"Suma total: {suma}")