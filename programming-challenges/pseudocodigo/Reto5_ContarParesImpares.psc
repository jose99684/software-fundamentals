Algoritmo Reto5_ContarParesImpares
    Definir cantidad, pares, impares, numero, i Como Entero

// Programa principal
contarParesImpares(x)
FinAlgoritmo
Funcion contarParesImpares(x)
	Escribir "¿Cuántos lanzamientos desea efectuar?"
	Leer cantidad
	
	pares <- 0
	impares <- 0
	
	Para i <- 1 Hasta cantidad Hacer
		numero <- Aleatorio(1,6)
		Escribir "Lanzamiento ", i, ": ", numero
		
		Si numero MOD 2 = 0 Entonces
			pares <- pares + 1
		SiNo
			impares <- impares + 1
		FinSi
	FinPara
	
	Escribir "=== RESULTADOS ==="
	Escribir "Total de PARES: ", pares
	Escribir "Total de IMPARES: ", impares
FinFuncion