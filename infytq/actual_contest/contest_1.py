'''
Created on Apr 23, 2020

@author: amrit
'''
str=input()
list_sample=list(str)
i=0
j=len(list_sample)-1
while i<j:
    if not list_sample[i].isalpha():
        i+=1
    elif not list_sample[j].isalpha():
        j-=1
    else:
        list_sample[i],list_sample[j]=list_sample[j],list_sample[i]
        i+=1
        j-=1
outputstr="".join(list_sample)
print(outputstr)