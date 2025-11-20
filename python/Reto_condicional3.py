import os

os.system('cls')
def number__classification(number):

    if number >=0:
       if abs(number)%2==0:
        return "your number is even positive\n"
       else:
        return "your number is odd positive\n"
            
    elif  abs(number)%2==0:
        return "your number is even negative\n"
    else:
        return "your number is odd negative\n"
    
    
    
number=int(input("Enter a number: "))
print(number__classification(number))