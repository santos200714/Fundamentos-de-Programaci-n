Algoritmo Ejemplo2
	Definir cajero, cuentaDeAhorro, numeroDeCuenta, CantidafSaliente, saldo Como Entero
	cuentaDeAhorro =1000
	numeroDeCuenta = 12345
	
	Escribir "bienvenido"
	Escribir "Actividad que desea realizar"
	Escribir "1 para consulta"
	Escribir "2 para extraer dinero de la cuenta de ahorro"
	
	escribir "escriba el numero de cuenta a operar"
	leer preguntar
	
	si  preguntar == 1
		Escribir "escriba el numero de cuenta a operar"
		leer preguntar //es valor del numero  de cuentas
		
		si preguntar == numeroDeCuenta
	    Escribir  "su saldo es " ,cuentaDeAhorro
		FinSi
	FinSi
	
	
	
	
		
		si  preguntar == 2
			Escribir  " Escriba el nunero de cuenta a operar"
			Leer preguntar // es valor den numero de cuentas
			si preguntar == numeroDeCuenta
				Escribir  " Escriba el monto a extraer"
				Leer preguntar // es la cantidad a extraer
				// < =
				si preguntar <= cuentaDeAhorro
					Saldo = cuentaDeAhorro - preguntar
					Escribir  "Procesando"
					Escribir  "Su saldo actual es de " , Saldo
				FinSi
			FinSi
		FinSi
		
		// or  o pues llevar 
		// panes con cafe o chocolate
		
		// and  puedes llevar carne y jamon
		
		// not mejor no 
		
		
		// == si es igual 
		//<>  diferente <> ! =  
		
		
		//no pueden comenzar con 
		// numero 
		// signos a manenos que sea _
		// no teben llevar espacio 
		// Si es una calse simpre inicia con Mayusculas
		// es evitar el codigo espagueti
FinAlgoritmo
