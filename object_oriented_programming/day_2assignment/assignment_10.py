'''
Created on Apr 20, 2020

@author: amrit
'''
class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.phoneno=phoneno
        self.called_no=called_no
        self.duration=duration
        self.call_type=call_type

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        l2=[]
        for i in list_of_call_string:
            l1=i.split(",")
            
            l2.append(CallDetail(l1[0],l1[1],l1[2],l1[3]))
            print(l2)
        self.list_of_call_objects=l2
            

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)