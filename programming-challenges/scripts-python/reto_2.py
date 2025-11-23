import random

def sumar_lanzamientos():
    """Función que suma N lanzamientos de dados"""
    cantidad = int(input("¿Cuántas veces desea lanzar el dado? "))
    suma = 0
    
    for i in range(1, cantidad + 1):
        numero = random.randint(1, 6)
        print(f"Lanzamiento {i}: {numero}")
        suma += numero
    
    print(f"\nSuma total de los valores: {suma}")
    return suma


# Programa principal
if __name__ == "__main__":
    print("=== RETO 2: Suma de N lanzamientos ===")
    sumar_lanzamientos()
