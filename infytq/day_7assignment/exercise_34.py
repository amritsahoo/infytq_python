'''
Created on Apr 22, 2020

@author: amrit
'''
import math
def find_number_of_combination(number_of_flavours):
    total_combination=0
    num=number_of_flavours
    result=0
    for i in range(num+1):
        a=math.factorial(num)
        b=math.factorial(i)
        c=math.factorial(num-i)
        result=a/(b*c)
        total_combination+=result
    return total_combination
number_of_combination=find_number_of_combination(4)
print(number_of_combination)
