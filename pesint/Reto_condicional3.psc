Algoritmo Reto_condicional3
	
	Definir number Como Entero
	
	Escribir "Please enter your number: "
	Leer number
	
	si number >= 0
		Entonces
		si Abs(number)%2=0
			Entonces
			Mostrar  "Your number ", number, " es PAR POSITIVO"
		SiNo
			Mostrar  "Your number ", number, " es IMPAR POSITIVO"
			
		FinSi
	SiNo si Abs(number)%2=0
			Entonces
			
			Mostrar  "Your number ", number, " es PAR NEGATIVO"
		SiNo
			Mostrar  "Your number ", number, " es IMPAR NEGATIVO"
		FinSi
		
		
	FinSi
	
	
	
FinAlgoritmo
