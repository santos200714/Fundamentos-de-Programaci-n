nombres = input("Ingrese los 10 nombres dejando espacio entre cada uno : ").split()

def validos(nombres):
    for nombre in nombres:
        if len(nombre) > 5:
            print(nombre)

validos(nombres)