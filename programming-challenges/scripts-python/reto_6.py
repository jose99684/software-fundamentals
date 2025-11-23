import random

def jugar_con_opcion():
    """Función que permite lanzar dados con opción de continuar"""
    total_tiros = 0
    suma = 0
    pares = 0
    impares = 0
    continuar = 'S'
    
    print("=== Juego de dados con opción de continuar ===")
    
    while continuar.upper() == 'S':
        total_tiros += 1
        numero = random.randint(1, 6)
        suma += numero
        
        print(f"\nLanzamiento {total_tiros}: {numero}")
        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        continuar = input("¿Desea volver a lanzar? (S/N): ")
    
    # Mostrar reporte final
    print("\n" + "="*30)
    print("=== REPORTE FINAL ===")
    print("="*30)
    print(f"Total de tiros efectuados: {total_tiros}")
    print(f"Suma total de los tiros: {suma}")
    print(f"Total de pares generados: {pares}")
    print(f"Total de impares generados: {impares}")
    
    return {
        'total_tiros': total_tiros,
        'suma': suma,
        'pares': pares,
        'impares': impares
    }

# Programa principal
if __name__ == "__main__":
    print("=== RETO 6: Lanzamientos con opción ===")
    jugar_con_opcion()
