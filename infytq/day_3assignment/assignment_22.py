'''
Created on Apr 5, 2020

@author: amrit
'''
def next_15_leapyear(year):
    arr=[]
    count=0
    temp_year=year
    while(temp_year>=year):
        if(temp_year%4==0 and temp_year%100!=0 or temp_year%400==0):
            arr.append(temp_year)
            count+=1
        if(count==15):
            break
        temp_year+=1
    return arr
year=int(input("Enter the year"))
res=next_15_leapyear(year)
print(res)
    
while(5>4):
    query=input("Do you want to give another input:[Y/N]")
    if(query.upper()=="Y"):
        year=int(input("Enter the year"))
        res=next_15_leapyear(year)
        print(res)
    else:
        break
        
    