while True:
    notas = int(input("¿Cuántas notas vas a ingresar? (0 para salir): "))
    if notas == 0:
        break

    notas_validas = [] 

    for i in range(1, notas + 1):
        nota = float(input(f"Ingresa la nota {i}: "))
        
       
        if 0 <= nota <= 10:
            notas_validas.append(nota)
        
    if len(notas_validas) > 0:
        suma = 0
        for nota in notas_validas:
            suma += nota
        
        promedio = suma / len(notas_validas)
        print(f"Promedio de notas válidas: {promedio:.2f}")
    else:
        print("No se ingresaron notas válidas.")