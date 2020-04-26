'''
Created on Apr 26, 2020

@author: amrit
'''
'''
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15
'''
def find_sum(num):
    summ=0
    for n in num:
        summ+=int(n)
    return summ 
def find_substr(arr,sum):
    length=len(arr)
    for i in range(2,length):
        last_index=length-i+1
        for j in range(0,last_index):
            if(find_sum(arr[j:j+i:1])==sum):
                print(j+1,j+i)         
n=int(input("Enter the number of test cases"))
i=0
while(i<n):
    temp=input("Enter the number of element and the sum")
    data=temp.split(" ")
    no_of_digits=data[0]
    sum=int(data[1])
    temp=input("Enter the digits")
    arr=temp.split(" ")
    find_substr(arr,sum)
    i+=1
        