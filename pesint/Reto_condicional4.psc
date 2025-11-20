ALGORITMO reto_condicional
	
	//INICIO
    // Declarar variables o constantes
    Definir  num1, num2, res COMO REAL
    Definir  opt  COMO ENTERO// Variable para asignar valor de opción (Entre 1 y 5)
    
    // Inicializar variables o constantes
    num1 = 0
    num2 = 0
    
    // Obtener número 1
    ESCRIBIR "Enter value to number 1: "
    LEER num1
    
    // Obtener número 2
    ESCRIBIR "Enter value to number 2: "
    LEER num2
    
    // Imprimir menú matemático
    ESCRIBIR "Math menu: [1]. Add - [2]. Subs - [3]. Mult - [4]. Div - [5]. All"
    ESCRIBIR "Press any option [1 - 5]"
    LEER opt
    
    // Procesar según la opción seleccionada
    SI opt = 1 ENTONCES
        res = num1 + num2
        ESCRIBIR "Addition: ", res
    SINO
        SI opt = 2 ENTONCES
            res = num1 - num2
            ESCRIBIR "Substraction: ", res
        SINO
            SI opt = 3 ENTONCES
                res = num1 * num2
                ESCRIBIR "Multiplication: ", res
            SINO
                SI opt = 4 ENTONCES
                    res = num1 / num2
                    ESCRIBIR "Division: ", res
                SINO
                    SI opt = 5 ENTONCES
                        ESCRIBIR "Add: ", num1 + num2
                        ESCRIBIR "Subs: ", num1 - num2
                        ESCRIBIR "Mult: ", num1 * num2
                        ESCRIBIR "Div: ", num1 / num2
                    SINO
                        ESCRIBIR "Invalid option"
						FINSI
						FINSI
						FINSI
						FINSI
						FINSI
						
FinAlgoritmo
