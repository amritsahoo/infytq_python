'''
Created on Apr 22, 2020

@author: amrit
'''
def sms_encoding(data):
    vowel_set = set("aeiouAEIOU")
    final_list=[]
    word=data.split()
    temp_string=""
    for w in word:
        temp_word=[]
        for letter in w:
            if letter.lower() not in vowel_set:
                temp_word.append(letter)
        if len(temp_word)==0:
            temp_word.append(w)
        final_list.append("".join(temp_word))
    return " ".join(final_list)

data="I will not repeat mistakes"
print(sms_encoding(data))