Algoritmo Reto6_LanzamientosConOpcion
    Definir total_tiros, suma, pares, impares, numero Como Entero
    Definir continuar Como Caracter
    

// Programa principal
	jugarConOpcion(x)
	
FinAlgoritmo
Funcion jugarConOpcion(x)
	total_tiros <- 0
	suma <- 0
	pares <- 0
	impares <- 0
	continuar <- "S"
	
	Mientras continuar = "S" o continuar = "s" Hacer
		total_tiros <- total_tiros + 1
		numero <- Aleatorio(1,6)
		suma <- suma + numero
		
		Escribir "Lanzamiento ", total_tiros, ": ", numero
		
		Si numero MOD 2 = 0 Entonces
			pares <- pares + 1
		SiNo
			impares <- impares + 1
		FinSi
		
		Escribir "¿Desea volver a lanzar? (S/N)"
		Leer continuar
	FinMientras
	
	Escribir "=== REPORTE FINAL ==="
	Escribir "Total de tiros efectuados: ", total_tiros
	Escribir "Suma total de los tiros: ", suma
	Escribir "Total de pares generados: ", pares
	Escribir "Total de impares generados: ", impares
FinFuncion