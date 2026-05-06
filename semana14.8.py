def buscar(productos, nombre):
    for producto in productos:
        if producto.lower() == nombre.lower():
            return True
    return False

productos = [
    "Leche",
    "Pan",
    "Huevos",
    "Arroz",
    "Azúcar"
]

nombrebuscar = input("Ingrese el nombre del producto: ")

if buscar(productos, nombrebuscar):
    print(f"El producto '{nombrebuscar}' se encontró en la lista.")
else:
    print(f"El producto '{nombrebuscar}' no se encontró en la lista.")