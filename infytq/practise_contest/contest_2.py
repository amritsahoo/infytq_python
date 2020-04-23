5,'''
Created on Apr 22, 2020

@author: amrit
'''
import math
def max_digit(inarr):
    length=len(inarr)
    largest_num=""
    combinations=(math.factorial(length)//(math.factorial(length-3)))
    inarr.sort(reverse=True)
    for i in inarr:
        largest_num+=str(i)
    print(int(largest_num[:3]), end="")
    print(",",end="")
    print(combinations)
temp=input("Enter the digits separated by comma")
digits=temp.split(",")
max_digit(digits)