'''
Created on Apr 22, 2020

@author: amrit
'''
import math
def max_digit(inarr):
    length=len(inarr)
    largest_num=""
    combinations=(math.factorial(length)//(6*math.factorial(length-3)))*3
    inarr.sort(reverse=True)
    for i in inarr:
        largest_num+=str(i)
    print(int(largest_num[:3]), end="")
    print(",",end="")
    print(combinations)
max_digit([1,2,1,4,7])