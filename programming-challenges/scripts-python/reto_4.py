import random

def lanzar_hasta_doble_seis():
    """Función que lanza dados hasta obtener doble seis"""
    intentos = 0
    continuar = True
    
    print("Lanzando dados hasta obtener doble seis...")
    
    while continuar:
        intentos += 1
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        
        print(f"Intento {intentos}: Dado1={dado1}, Dado2={dado2}")
        
        if dado1 == 6 and dado2 == 6:
            continuar = False
            print(f"\n¡DOBLE SEIS! Conseguido en {intentos} intentos")
    
    return intentos

# Programa principal
if __name__ == "__main__":
    print("=== RETO 4: Lanzar hasta doble seis ===")
    lanzar_hasta_doble_seis()
