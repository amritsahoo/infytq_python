'''
Created on Apr 20, 2020

@author: amrit
'''
def factor_count(num):
    count=0
    for n in range(1,num+1):
        if(num%n==0):
            count+=1
    return count
def find_smallest_number(num):
    number=1
    while(number>0):
        if (factor_count(number)==num):
            break
        else:
            number+=1
    return number
    

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)