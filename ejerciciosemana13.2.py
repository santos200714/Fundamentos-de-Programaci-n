positivo = 0
negativo = 0

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    
    if numero == 0:
        break
    
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
        
resumen = [("positivos", positivo), ("negativos", negativo)]
for etiqueta, valor in resumen:
            print(f"{etiqueta}: {valor}")

    
 