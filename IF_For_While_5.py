
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")
    
if operacion == "+":
    resultado = numero1 + numero2
    print("Resultado:", resultado)
elif operacion == "-":
    resultado = numero1 - numero2
    print("Resultado:", resultado)
elif operacion == "*":
    resultado = numero1 * numero2
    print("Resultado:", resultado)
elif operacion == "/":
    
    resultado = numero1 / numero2
    print("Resultado:", resultado)
else:
    print("Operación no válida.")