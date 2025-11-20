Algoritmo Reto_condicional1
	
	Definir die1 Como Entero
	Definir die2 Como Entero
	
	die1 <- Aleatorio(1,6)
	die2 <- Aleatorio(1,6)
	
	Mostrar "Die 1: " , die1
	Mostrar "Die 2: " , die2
	
	si die1 = die2
		Entonces
		Mostrar "YOU WIN"
	SiNo
		Mostrar "GAME OVER"
	FinSi
	
	
	
FinAlgoritmo
