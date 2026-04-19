nota = int(input("ingrese la Nota que desea revisar="))


if nota >= 9 and nota <10:
    print("Excelente")  
elif nota >= 7 and nota <= 8:
    print("Bueno")
elif nota == 6:
    print("Arobado")
elif nota <= 5 and nota >= 0:
    print("Reprobado")
else:    print("nota no valida")