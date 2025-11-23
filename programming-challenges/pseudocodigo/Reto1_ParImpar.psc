Algoritmo Reto1_ParImpar
    Definir numero Como Entero
    
// Programa principal
resultado <- lanzarDado(x)
FinAlgoritmo

Funcion resultado <- lanzarDado(x)
	numero <- Aleatorio(1,6)
	Escribir "Número generado: ", numero
	
	Si numero MOD 2 = 0 Entonces
		Escribir "El número es PAR"
	SiNo
		Escribir "El número es IMPAR"
	FinSi
	
	Mostrar  numero
FinFuncion