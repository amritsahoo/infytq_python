'''
Created on Apr 20, 2020

@author: amrit
'''
class Customer:
    def __init__(self):
        self.customer_name=None
        self.bill_amount=None
    def purchase(self):
        self.bill_amount-=self.bill_amount*(5/100)
        self.pays_bill(self.bill_amount)
    def pays_bill(self,amount):
        print(self.customer_name+" pays bill amount of Rs."+str(self.bill_amount))
c1=Customer()
c1.customer_name="Amrit"
c1.bill_amount=500
c1.purchase()