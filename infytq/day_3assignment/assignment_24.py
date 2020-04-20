'''
Created on Apr 5, 2020

@author: amrit
'''
def is_tringle(num1,num2,num3):
    if(num1+num2>num3 and num1+num3>num2 and num2+num3>num1):
        return 1
    else:
        return 0
num1=int(input("Enter the first side of the tringle:"))
num2=int(input("Enter the second side of the tringle:"))
num3=int(input("Enter the third side of the tringle:"))
res=is_tringle(num1,num2,num3)
if(res==1):
    print("Tringle is possible")
else:
    print("Tringle is not possible")