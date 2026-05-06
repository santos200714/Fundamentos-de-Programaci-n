edades = [int(edad) for edad in input("Ingrese las edades separadas por espacios: ").split()]
mayor = 0
def validos(edades):
    global mayor
    for edad in edades:
        if edad >= 18:
            mayor += 1

validos(edades)
print(f"Cantidad de personas mayores de edad: {mayor}")