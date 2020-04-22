'''
Created on Apr 22, 2020

@author: amrit
'''
def find_correct(word_dict):
    #start writing your code here
    wrong_count=0
    correct_count=0
    almost_count=0
    result_list=[]
    letter_count=0
    for x,y in word_dict.items():
        if len(y)!=len(x):
            wrong_count+=1
        else:
            i=0
            while i<len(y):
                if y[i]!=x[i]:
                    letter_count+=1
                    i+=1
                else:
                    i+=1
                    continue
                
            if letter_count>0 and letter_count<=2:
                almost_count+=1
            elif letter_count>2:
                wrong_count+=1
            else:
                correct_count+=1
            letter_count=0
    result_list=[correct_count,almost_count,wrong_count]
    return result_list
                

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))

