contador = 0

while True:
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == "12345pl":
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta, intente de nuevo")
        contador += 1
        
        
    for i in range(contador):
     print(f"Intento fallido {i + 1}")