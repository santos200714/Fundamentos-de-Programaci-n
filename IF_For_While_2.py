edad = int(input("ingrese la edad que desea revisar="))


if edad < 18 and edad >= 0:
    print("es menor de edad")  
elif edad >= 18 and edad <= 60:
    print("es mayor de edad")
elif edad > 60:
    print("es un adulto mayor")
else:    print("edad no valida")