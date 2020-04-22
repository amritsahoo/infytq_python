'''
Created on Apr 22, 2020

@author: amrit
'''
def encrypt_sentence(sentence):
    vowel_set = set("aeiouAEIOU")
    final_list=[]
    word=sentence.split()
    final_sent=""
    p=0
    for i in range(0,len(word)):
        if((i%2)==0):
            final_list.append(word[i][::-1])
        else:  # do rearrangement
            vowels = list()
            consonants = list()
            for letter in word[i]:
                if letter in vowel_set:
                    vowels.append(letter)
                else:
                    consonants.append(letter)
            new_string = "".join(consonants) + "".join(vowels)
            final_list.append(new_string)
    while p<len(final_list):
        final_sent=final_sent+" "+final_list[p]
        p+=1
    return final_sent
    

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)