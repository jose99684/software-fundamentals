Algoritmo Reto4_DobleSeis
    Definir dado1, dado2, intentos Como Entero
    Definir continuar Como Logico
    


// Programa principal
	resultado <- lanzarHastaDobleSeis(x)
FinAlgoritmo
Funcion resultado <- lanzarHastaDobleSeis(x)
	intentos <- 0
	continuar <- Verdadero
	
	Mientras continuar Hacer
		intentos <- intentos + 1
		dado1 <- Aleatorio(1,6)
		dado2 <- Aleatorio(1,6)
		
		Escribir "Intento ", intentos, ": Dado1=", dado1, " Dado2=", dado2
		
		Si dado1 = 6 Y dado2 = 6 Entonces
			continuar <- Falso
			Escribir "¡DOBLE SEIS! Conseguido en ", intentos, " intentos"
		FinSi
	FinMientras
	
	Mostrar  intentos
FinFuncion