Proceso Reto3_ContadorFrecuencias
    contarFrecuencias(x)
FinProceso


SubProceso contarFrecuencias(x)
    Definir cantidad, i, numero Como Entero
    Definir contador Como Entero
    Dimension contador[6]
    
    // Inicializar contadores
    Para i <- 1 Hasta 6 Hacer
        contador[i] <- 0
    FinPara
    
    Escribir "¿Cuántas veces desea lanzar el dado?"
    Leer cantidad
    
    // Lanzar el dado y contar frecuencias
    Para i <- 1 Hasta cantidad Hacer
        numero <- Aleatorio(1,6)
        contador[numero] <- contador[numero] + 1
        Escribir "Lanzamiento ", i, ": ", numero
    FinPara
    
    // Mostrar resultados
    Escribir "=== FRECUENCIAS ==="
    Para i <- 1 Hasta 6 Hacer
        Escribir "Número ", i, ": ", contador[i], " veces"
    FinPara
FinSubProceso
