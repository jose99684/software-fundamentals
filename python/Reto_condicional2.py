import os

os.system("cls")
number = int(input("Enter value for number1: "))


if abs(number) % 2 == 0:
    print(f"\n The number {number} is even")
else:
    print(f"\n The number {number} is odd")