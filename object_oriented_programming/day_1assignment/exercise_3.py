'''
Created on Apr 20, 2020

@author: amrit
'''
class Employee:
    def __init__(self):
        self.name=None
        self.age=None
        self.salary=None
c1=Employee()
c1.name="Jill"
c1.salary=40000
c1.age=27
print(c1.name,c1.salary,c1.age)
c2=Employee()
c2.name="Jack"
c2.salary=30000
c2.age=24
print(c2.name,c2.salary,c2.age)