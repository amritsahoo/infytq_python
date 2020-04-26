'''
Created on Apr 26, 2020

@author: amrit
'''
'''
def reverse_word(list):
    arr=[]
    for word in list:
        rev=word[::-1]
        arr.append(rev)
    str=' '.join(arr)
    return str
line=input("Enter the string")
list=line.split(" ")
res=reverse_word(list)
print(res)
'''
'''
def reverse_arrange(list):
    list.reverse()
    str=' '.join(list)
    return str
line=input("Enter the string")
list=line.split(" ")
res=reverse_arrange(list)
print(res)
'''
'''
def reverse_arrange(list):
    rev=reversed(list)
    str=' '.join(rev)
    return str
line=input("Enter the string")
list=line.split(" ")
res=reverse_arrange(list)
print(res)
'''
def reverse_word_arrange(list):
    rev=reversed(list)
    arr=[]
    for word in rev:
        rev_word=word[::-1]
        arr.append(rev_word)
    res=' '.join(arr)
    return res
line=input("Enter the string")
list=line.split(" ")
res=reverse_word_arrange(list)
print(res)
