numeros = list(map(int, input("Ingrese los numeros con un espacio: ").split()))

def positivos(lista):
    solopositivos = [] 
    for numero in lista:
        if numero > 0:
            solopositivos.append(numero) 
    return solopositivos

resultado = positivos(numeros)
print("positivos:", resultado)