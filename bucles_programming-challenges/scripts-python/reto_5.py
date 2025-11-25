import random

def contar_pares_impares():
    """Función que cuenta pares e impares en N lanzamientos"""
    cantidad = int(input("¿Cuántos lanzamientos desea efectuar? "))
    
    pares = 0
    impares = 0
    
    for i in range(1, cantidad + 1):
        numero = random.randint(1, 6)
        print(f"Lanzamiento {i}: {numero}")
        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print("\n=== RESULTADOS ===")
    print(f"Total de PARES: {pares}")
    print(f"Total de IMPARES: {impares}")
    
    return pares, impares

# Programa principal
if __name__ == "__main__":
    print("=== RETO 5: Contar pares e impares ===")
    contar_pares_impares()
