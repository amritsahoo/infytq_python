'''
Created on Apr 20, 2020

@author: amrit
'''
class Instructor:
    def __init__(self):
        self.__instructor_name=None
        self.__experience=None
        self.__technology_skill=None
        self.__avg_feedback=None
    def set_instructor_name(self,instructor_name):
        self.__instructor_name=instructor_name
    def get_instructor_name(self):
        return self.__instructor_name
    def set_experience(self,experience):
        self.__experience=experience
    def get_experience(self):
        return self.__experience
    def set_technology_skill(self,technology_skill):
        self.__technology_skill=technology_skill
    def get_technology_skill(self):
        return self.__technology_skill
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback=avg_feedback
    def get_avg_feedback(self):
        return self.__avg_feedback
    def check_eligibility(self):
        if(self.__experience>=3 and self.__avg_feedback>=4.5):
            return True
        elif(self.__experience<=3 and self.__avg_feedback>=4):
            return True
        else:
            return False
    def allocate_course(self,technology):
        #print(self.__technolofy_skill)
        if(self.check_eligibility()):
            if(technology in self.__technology_skill):
                return True
            else:
                return False
        else:
            return False
i1=Instructor()
i1.set_instructor_name("Priya")
#i1.get_instructor_name()
i1.set_experience(4)
#i1.get_experience()
i1.set_technology_skill(["Java","C","Python"])
#i1.get_technolofy_skill()
i1.set_avg_feedback(4.5)
#i1.get_avg_feedback())
i1.check_eligibility()
print(i1.allocate_course("Java"))