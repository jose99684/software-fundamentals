ALGORITMO Reto_condicional5
	
	//INICIO
    // Declaración de variables
    Definir  id, firstName, lastName, gender, birth, adress Como Caracter
	Definir phone, salary COMO ENTERO 
    Definir increase  COMO   REAL 
    
    // Entrada de datos
    ESCRIBIR "Document (CC, PS, CE, CI)"
    ESCRIBIR "Type document: "
    LEER id
    
    ESCRIBIR "First Name: "
    LEER firstName
    
    ESCRIBIR "Last Name: "
    LEER lastName
    
    ESCRIBIR "Gender: "
    LEER gender
    
    ESCRIBIR "Year of birth: "
    LEER birth
    
    ESCRIBIR "Adress: "
    LEER adress
    
    ESCRIBIR "Phone: "
    LEER phone
    
    ESCRIBIR "Salary: "
    LEER salary


    // Proceso de cálculo de aumento
    SI salary <= 1200000 ENTONCES
        SI gender = "mujer" ENTONCES
            increase = (salary * 3) / 100
            ESCRIBIR "hola ", firstName, " ", lastName, " su salario aumento el 3%, su salario es: ", (salary + increase)
        SINO
            increase = (salary * 8) / 100
            ESCRIBIR "hola ", firstName, " ", lastName, " su salario aumento el 8%, su salario es: ", (salary + increase)
		FinSi
		
		SINO
			SI salary > 1200000 Y salary < 2000000 ENTONCES
				increase = (salary * 5) / 100
				ESCRIBIR "hola ", firstName, " ", lastName, " su salario aumento el 5%, su salario es: ", (salary + increase)
			SINO
				SI gender = "mujer" ENTONCES
					increase = (salary * 3) / 100
					ESCRIBIR "hola ", firstName, " ", lastName, " su salario aumento el 3%, su salario es: ", (salary + increase)
				SINO
					increase = (salary * 2.5) / 100
					ESCRIBIR "hola ", firstName, " ", lastName, " su salario aumento el 2.5%, su salario es: ", (salary + increase)
				FinSi
				
			FinSi
			
		FinSi
		
FinAlgoritmo

		
					

	
