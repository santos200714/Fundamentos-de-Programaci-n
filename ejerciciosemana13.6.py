while True:
    numero = int(input("Ingresa un número n (0 para salir): "))
    if numero == 0:
        break
        
    for numero in range(1, numero + 1):
        if numero < 2:
            print(numero, "no es primo")
        else:
            es_primo = True  
            for i in range(2, numero):
                if numero % i == 0:
                    es_primo = False 
                    break 
            
            
            if es_primo:
                print(numero, "es primo")
            else:
                print(numero, "no es primo")