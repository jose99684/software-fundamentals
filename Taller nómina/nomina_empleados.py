import os
from datetime import datetime
os.system("cls")

acum_empleados = 0
acum_f = 0
acum_m = 0
acum_o = 0
acum_salarios = 0
edad = 0
prom_edades = 0
edad=0
totaledades= 0

def date_empleados():
    nombres=input("Ingrese sus Nombres completos: ")
    movil=input("Ingrese su numero movill: ")
    
    while True:
        genero=input("Ingrese su Genero (M/F/O): ")
        if genero == "M" or genero == "F" or genero == "O":
            break
            
        else:
            print("Género inválido, intente de nuevo.")
####suma generos
    global acum_m
    global acum_f
    global acum_o

    if genero == "M":
        acum_m+=1
    elif genero == "F":
        acum_f+=1
    else:
        acum_o+=1
            
            
    salario=int(input("Ingrese su salario: "))
#####Total salarios   
    global acum_salarios
    acum_salarios+=salario 

    while True:
        año_nacimiento= int(input("Ingrese su año de nacimiento (AAAA): "))
        if año_nacimiento >=1900 and año_nacimiento <= datetime.now().year:
            break
        else:
            print("Año inválido, intente de nuevo.")
            año_nacimiento = False
###### promedio edades
    global prom_edades
    global totaledades
    edad = datetime.now().year-año_nacimiento
    totaledades+=edad
  


######  global acum_empleados
    global acum_empleados
    acum_empleados += 1




####bucle para registrar otro empleado    
    while True:
        registrar_otro=input("¿Desea ingresar los datos de otro empleado? (S/s/N/n): ")
        
        if registrar_otro  == "S" or registrar_otro == "s":
            date_empleados()
            
            break
            
        elif registrar_otro == "N" or registrar_otro == "n":
            break
    


def print_total():
    print("Total empleados: ",acum_empleados)
    print("Total hombres: ", acum_m)
    print("Total mujeres: ",acum_f)
    print("Total otro: ", acum_o)
    print("Total salarios: ", acum_salarios)
    print("promedio edades: ", totaledades/acum_empleados)



#####main

date_empleados()
print_total()

