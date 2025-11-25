Algoritmo nomina
	date_empleados(x)
FinAlgoritmo
SubProceso date_empleados(x)
    Escribir "Ingrese sus nombres completos: "
    Leer nombres
    Escribir "Ingrese su número móvil: "
    Leer movil
	
    // Validar género
    Repetir
        Escribir "Ingrese su género (M/F/O): "
        Leer genero
        Si genero <> "M" Y genero <> "F" Y genero <> "O" Entonces
            Escribir "Género inválido, intente de nuevo."
        FinSi
    Hasta Que genero = "M" O genero = "F" O genero = "O"
	
    Si genero = "M" Entonces
        acum_m <- acum_m + 1
    SiNo
        Si genero = "F" Entonces
            acum_f <- acum_f + 1
        SiNo
            acum_o <- acum_o + 1
        FinSi
    FinSi
	
    Escribir "Ingrese su salario: "
    Leer salario
    acum_salarios <- acum_salarios + salario
	
    // Validar año de nacimiento
    Repetir
        Escribir "Ingrese su año de nacimiento (AAAA): "
        Leer año_nacimiento
        Si año_nacimiento < 1900 O año_nacimiento > 2024 Entonces
            Escribir "Año inválido, intente de nuevo."
        FinSi
    Hasta Que año_nacimiento >= 1900 Y año_nacimiento <= 2024
	
    edad <- 2024 - año_nacimiento
    totaledades <- totaledades + edad
    acum_empleados <- acum_empleados + 1
	
    // Registrar otro empleado
    Repetir
        Escribir "¿Desea ingresar los datos de otro empleado? (S/s/N/n): "
        Leer registrar_otro
        Si registrar_otro = "S" o registrar_otro = "s" Entonces
            date_empleados(x)
        FinSi
    Hasta Que registrar_otro = "N" O registrar_otro = "n"
FinSubProceso



