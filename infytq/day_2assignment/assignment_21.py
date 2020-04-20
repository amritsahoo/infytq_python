'''
Created on Apr 20, 2020

@author: amrit
'''
def generate_next_date(day,month,year):
   
    if((year%4==0 and year%100!=0) or year%400==0):
        
            
        if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10):
            if(day==31):
                print("1-",month+1,"-",year)
            elif(day>=1 and day<=30):
                print(day+1,"-",month,"-",year)
                    
            else:
                print("Invalid")
        elif(month==4 or month==6 or month==9 or month==11):
            if(day==30):
                print("1-",month+1,"-",year)
            elif(day>=1 and day<=29):
                print(day+1,"-",month,"-",year)
            else:
                print("Invalid")
        elif(month==2):
            if(day==29):
                print("1-",month+1,"-",year)
            elif(day>=1 and day<=28):
                print(day+1,"-",month,"-",year)
            else:
                print("Invalid")
        elif(month==12):
            if(day==31):
                print("1-1-",year+1)
            elif(day>=1 and day<=30):
                print(day+1,"-",month,"-",year)
                    
            else:
                print("Invalid")
                    
        else:
            print("Invalid")
    else:
        if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10):
            if(day==31):
                print("1-",month+1,"-",year)
            elif(day>=1 and day<=30):
                print(day+1,"-",month,"-",year)
            else:
                print ("Invalid")
        elif(month==4 or month==6 or month==9 or month==11):
            if(day==30):
                print("1-",month+1,"-",year)
            elif(day>=1 and day<=29):
                print(day+1,"-",month,"-",year)
            else:
                print("Invalid")
        elif(month==2):
            if(day==28):
                print("1-",month+1,"-",year)
            elif(day>=1 and day<=27):
                print(day+1,"-",month,"-",year)
            else:
                print("Invalid")
        elif(month==12):
            if(day==31):
                print("1-1-",year+1)
            elif(day>=1 and day<=30):
                print(day+1,"-",month,"-",year)
            else:
                print("Invalid")
        else:
            print("Invalid")
        
#day=int(input("Enter the day"))
#month=int(input("Enter the month"))
#year=int(input("Enter the year"))

#generate_next_date(day,month,year)


generate_next_date(30,6,2015)