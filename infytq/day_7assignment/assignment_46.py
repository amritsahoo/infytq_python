'''
Created on Apr 22, 2020

@author: amrit
'''
def nearest_palindrome(number):
    rev=0
    temp=0
    dup_num=number
    while True:
        while number>0:
            temp=number%10
            rev=rev*10+temp
            number=number//10
        if dup_num==rev:
            break
        else:
            dup_num+=1
            number=dup_num
            temp=0
            rev=0
            continue
    return rev

number=12300
print(nearest_palindrome(number))