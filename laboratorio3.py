import random
while True: 
    puntaje = 0 
    intentos = 0 
    
    for i in range(1, 11):
        numero1 = random.randint(1, 15)
        numero2 = random.randint(1, 15)
        operador = random.choice(['+', '-', '*'])

        match operador:
            case '+': resultado = numero1 + numero2
            case '-': resultado = numero1 - numero2
            case '*': resultado = numero1 * numero2

        print(f"Pregunta {i}: ¿Cuánto es {numero1} {operador} {numero2}?")
        respuesta = input("Ingrese su respuesta: ")

        if respuesta.lower() == "salir":
            break 

        intentos += 1
        if float(respuesta) == resultado:
            print(f"Pregunta {i}: ¡Respuesta correcta!")
            puntaje += 1
        else:
            print(f"Pregunta {i}: Respuesta incorrecta. Era {resultado}")

   
    if respuesta.lower() == "salir":
        break

    print("juego terminado")
    print(f"Su puntaje final es: {puntaje}")
    print("¡Iniciando nueva ronda")
   