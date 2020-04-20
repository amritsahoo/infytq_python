'''
Created on Apr 20, 2020

@author: amrit
'''
def check_palindrome(word):
    for i in range(0,len(word)):
        if(len(word)<2):
            return 1
        else:
            if(word[0]!=word[-1]):
                return 0
    return check_palindrome(word[1:-1])
            

status=check_palindrome("malayalam")
if(status==1):
    print("word is palindrome")
else:
    print("word is not palindrome")
# Another Method   
def check_palindrome1(word):
    temp=word[::-1]
    if word==temp:
        return True
    else:
        return False

status=check_palindrome1("MAN")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
