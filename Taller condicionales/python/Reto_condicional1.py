import random
import os

os.system("cls")



#initialize dices
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

#show dices
print('''Rolling the dices...
        \n''')
print(f"Die one → {die1}")
print(f"Die two → {die2}\n")
#check win condition


if die1 == die2:
    print("YOU WIN")
else:
    print("GAME OVER")



    