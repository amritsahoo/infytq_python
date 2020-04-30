'''
Created on Apr 30, 2020

@author: amrit
'''

def calculate(arr):
    length=len(arr)
    arr3=[]
    for i in range(length):
        arr2=arr[i].split(" ")
        num1=int(arr2[0])
        arr3.append(num1)
        num2=int(arr2[1])
        arr3.append(num2)
        i+=1
    num1=0
    num2=0
    for i in range(len(arr3)):
        if(i%2!=0):
            num1+=arr3[i]
        else:
            num2+=arr3[i]
    product=num1*num2
    return product

if __name__=="__main__":
    no_row_column=input("Enter the no of rows and column")
    arr=no_row_column.split(" ")
    n=int(arr[0])
    m=arr[1]
    i=0
    arr1=[]
    while(i<n):
        arr_element=input("Enter the array element")
        arr1.append(arr_element)
        i+=1
    res=calculate(arr1)
    print(res)
