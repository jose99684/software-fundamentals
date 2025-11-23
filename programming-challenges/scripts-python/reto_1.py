import random

def lanzar_dado_par_impar():
    """Función que lanza un dado y determina si es par o impar"""
    numero = random.randint(1, 6)
    print(f"Número generado: {numero}")
    
    if numero % 2 == 0:
        print(f"El número {numero} es PAR")
    else:
        print(f"El número {numero} es IMPAR")
    
    return numero

# Programa principal
if __name__ == "__main__":
    print("=== RETO 1: Lanzar dado Par/Impar ===")
    lanzar_dado_par_impar()
