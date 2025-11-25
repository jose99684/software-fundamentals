import os
import datetime
os.system("cls")
print("Document (CC, PS, CE, CI)")
id = input("Type document: ")
firstName = input("First Name: ")
lastName = input("Last Name: ")
gender = input("Gender (mujer/hombre): ")
birth = input("Year of birth: dd/mm/yyyy")
address = input("Address: ")
phone = int(input("Phone: "))
salary = int(input("Salary: "))

def calculate_increase(salary, percentage):
    return salary * percentage / 100

if salary <= 1200000:
    increase = calculate_increase(salary, 3 if gender == "mujer" else 8)
elif salary > 12000000 and salary < 20000000:
    increase = calculate_increase(salary, 5)
else:
    increase = calculate_increase(salary, 3 if gender == "mujer" else 2.5)

new_salary = salary + increase
print(f"Hola {firstName} {lastName}, su salario aumentó en {increase / salary * 100}%, su salario es: {new_salary}")