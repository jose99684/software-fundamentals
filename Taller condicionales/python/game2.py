##lANZAR DOS DADOS, CUANDO TIRE EL DADO VA ACOMPARAR Y SUMAR, DE ENTReDA 3 VIDAAS, suma de los dos dadoe
#par+1 vida
#impar-1 vida
#igual game over

import os
import random #para numeros enteros
from random import randint #randint
#unifor numeros flotantes
#con funcion que permita generar el numero

lives = 3
status = True

def roll_dices():

    print("lance el dado:")
    dice1=randint(1,6)
    dice2=randint(1,6)
    return dice1,dice2



    
######main
#print (roll_dices())

while True:
        key =(input("Please any key to roll dice: "))
        dices=roll_dices()
        print(f"die1:{dices[0]}")
        print(f"die2:{dices[1]}")
        
    
        if (dices[0] + dices[1])%2==0:
            print("sus vidas son",lives)
            lives+=1
        else:
            print("sus vidas son",lives)
            lives-=1
        if dices[0] =="6" and dices[1] =="6":
            os.system("cls")
            print("YOU WIN")
            
            break
        if lives == 0:
            print("YOU LOSE")
        
            break









