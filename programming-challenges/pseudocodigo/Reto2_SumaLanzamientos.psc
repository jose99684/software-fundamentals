Algoritmo Reto2_SumaLanzamientos
    Definir cantidad, suma, contador, numero Como Entero
    


// Programa principal
	total <- sumarLanzamientos(x)
FinAlgoritmo
Funcion total <- sumarLanzamientos(x)
	Escribir "¿Cuántas veces desea lanzar el dado?"
	Leer cantidad
	
	suma <- 0
	
	Para contador <- 1 Hasta cantidad Hacer
		numero <- Aleatorio(1,6)
		Escribir "Lanzamiento ", contador, ": ", numero
		suma <- suma + numero
	FinPara
	
	Escribir "Suma total de los valores: ", suma
	Mostrar  suma
FinFuncion