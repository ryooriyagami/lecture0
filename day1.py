#this program is for password generator and minimum password is 7
import random as r#import from random
from string import ascii_letters, digits

print ("\nHello world, this is my password generator password project for day 1") #print
print ("\nHow many numbers of alphabets do you want: ", end = " ") # for alphabets
alphabets = int(input()) #take numbers of alphabets only

print("\nHow many numbers of digits:", end = " ") # for number
numbers = int(input())

print("\nHow many special characters: ", end = " ") # for special character $,#,@, ! and etc
specialCharacters = int(input())

#checking minimum number for random generator password > 6
if alphabets+numbers+specialCharacters > 6:
    RL = RD = RS = ''
    Letters = ascii_letters #sets of alphabets A-Z
    Digits = digits #set of digits 1-10+++

    for i in range(alphabets):  #random letters for how many users input
        RL = RL + r.choice(Letters)
    for i in range(numbers):
        RD = RD + r.choice(Digits)
    for i in range(specialCharacters):
        RS = RS + r.choice('!@#$%^&*()_+')

    password = RD + RL + RS
    password = list(password)
    r.shuffle(password)
    generatedPass = ''.join(password)
    print("generated password for u: ", generatedPass)
else:
    print("Your minimum number for password generator is atleast 7 ")
