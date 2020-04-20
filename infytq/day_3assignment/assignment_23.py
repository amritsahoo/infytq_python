'''
Created on Apr 5, 2020

@author: amrit
'''
def calculate_bill_amount(gem_list,price_list,reqd_gems,reqd_quantity):
    bill_amount=0
    for i in range(0,len(reqd_gems)):
        if(reqd_gems[i] in gem_list):
            indx=gem_list.index(reqd_gems[i])
            bill_amount=bill_amount+price_list[indx]*reqd_quantity[i]
        else:
            bill_amount=-1
    if(bill_amount>30000):
        bill_amount=bill_amount*(1-0.05)
    return bill_amount

gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
price_list=[1760,2119,1599,3920,3999]
reqd_gems=["Ivory","Emerald","Garnet"]
reqd_quantity=[3,10,12]
bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)