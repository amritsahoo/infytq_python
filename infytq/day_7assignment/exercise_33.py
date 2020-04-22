'''
Created on Apr 22, 2020

@author: amrit
'''
import random
def guess_number(number_in_mind):
    x=random.randrange(1,10)
    if x>number_in_mind:
        print('Number is high')
    elif x<number_in_mind:
        print('Number is low')
    else:
        print('You have got it right!!!')
guess_number(5)