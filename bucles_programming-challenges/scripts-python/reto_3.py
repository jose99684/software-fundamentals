import random

def contar_frecuencias():
    """Función que cuenta la frecuencia de cada número en N lanzamientos"""
    cantidad = int(input("¿Cuántas veces desea lanzar el dado? "))
    
    # Inicializar contador para cada número del 1 al 6
    contador = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    for i in range(1, cantidad + 1):
        numero = random.randint(1, 6)
        contador[numero] += 1
        print(f"Lanzamiento {i}: {numero}")
    
    print("\n=== FRECUENCIAS ===")
    for num in range(1, 7):
        print(f"Número {num}: {contador[num]} veces")
    
    return contador

# Programa principal
if __name__ == "__main__":
    print("=== RETO 3: Contador de frecuencias ===")
    contar_frecuencias()
