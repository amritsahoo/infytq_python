'''
Created on Apr 22, 2020

@author: amrit
'''
import random
i=0
head_count=0
tail_count=0
def biasedcoin():
    return random.choice(['H','T','H','H','H','H','H','T','T','H'])
    
while i<1000:
    a=biasedcoin()
    if a=='H':
        head_count+=1
    else:
        tail_count+=1
    i+=1
print("Head-count:",head_count)
print("Tail_count:",tail_count)
