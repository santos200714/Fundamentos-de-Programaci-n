
numerosecreto = 6
intentos = 0
adivinado = False
historial = []

while not adivinado:
    numero = int(input("Adivina el número (1-10): "))
    intentos += 1
    historial.append(numero)
    
    if numero == numerosecreto:
        adivinado = True
        print(f"¡Correcto! Adivinaste en {intentos} intento")
    elif numero < numerosecreto:
        print("El número secreto es MAYOR")
    else:
        print("El número secreto es MENOR")

print("Historial de intentos:")
for i in range(1, intentos + 1):
    print(f"Intento {i}: {historial[i-1]}")