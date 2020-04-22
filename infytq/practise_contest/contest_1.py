'''
Created on Apr 22, 2020

@author: amrit
'''
def reverse(num):
    temp=0
    while(num>0):
        reminder=num%10
        temp=temp*10+reminder
        num=num//10
    return temp
def add(num1,num2):
    res=num1+num2
    return res
def isPallindrome(num):
    num=str(num)
    if(num==num[::-1]):
        return True
    else:
        return False
num=int(input("Enter the number")) 
rev=reverse(num)
sum=add(num,rev)
res=isPallindrome(sum)
while(res==False):
    num=sum
    rev=reverse(num)
    sum=add(num,rev)
    res=isPallindrome(sum)
print(sum)