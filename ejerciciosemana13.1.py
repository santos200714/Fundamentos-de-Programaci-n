
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print("Pares=")
    for i in range(1, numero + 1):
        if i % 2 == 0:
            print(i)
   
   
