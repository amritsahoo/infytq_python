'''
Created on Apr 20, 2020

@author: amrit
'''
#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if food_type=='V':
        if quantity_ordered>0:
            if distance_in_kms>6:
                bill_amount=quantity_ordered*120+((distance_in_kms-6)*6)+9
            elif distance_in_kms>3:
                bill_amount=quantity_ordered*120+((distance_in_kms-3)*3)
            elif distance_in_kms>0:
                bill_amount=quantity_ordered*120
            else:
                bill_amount=-1
        else:
            bill_amount=-1
    elif food_type=='N':
        if quantity_ordered>0:
            if distance_in_kms>6:
                bill_amount=quantity_ordered*150+((distance_in_kms-6)*6)+9
            elif distance_in_kms>3:
                bill_amount=quantity_ordered*150+((distance_in_kms-3)*3)
            elif distance_in_kms>0:
                bill_amount=quantity_ordered*150
            else:
                bill_amount=-1
        else:
            bill_amount=-1
    else:
        bill_amount=-1
                
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",1,7)
print(bill_amount)
