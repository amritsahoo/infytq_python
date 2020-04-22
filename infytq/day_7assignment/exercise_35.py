'''
Created on Apr 22, 2020

@author: amrit
'''
def count_names(name_list):
    count1=0
    count2=0
    
    #start writing your code here
    #Populate the variables: count1 and count2
    for i in name_list:
        if len(i)>2 and i.endswith('at'):
            count1+=1
        if i.count('at'):
            count2+=1
            
    print("_at -> ",count1)
    print("%at% -> ",count2)
name_list=["Hat","Cat","rabbit","matter","at"]
count_names(name_list)
