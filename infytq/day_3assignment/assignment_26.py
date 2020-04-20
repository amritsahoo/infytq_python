'''
Created on Apr 20, 2020

@author: amrit
'''
def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    if(legs%2!=0 or heads==0 or heads>legs):
        print(error_msg)
        
    else:
        chicken_count=int((2*heads)-(legs/2))
        
        rabbit_count=int((legs-(2*heads))/2)
        print(chicken_count,rabbit_count)
result=solve(35,94)