###
import os

###

status = True
acum = 0
count= 0


while status:
    print("Please any number(cero to exit): ")
    num = int(input())
    acum+=num
    
    if num %2==0:
        break ## status = False
    count  +=1 
            
print("The total is: ", acum)
print("The total even: ", count)


