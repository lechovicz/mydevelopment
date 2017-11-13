################################
'''
find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
'''

list=[]
for i in range(2000, 3201):
    if(i%7==0 and i%5!=0):
        list.append(str(i))
print ','.join(list)

###########################################3

'''
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral 
number between 1 and n (both included). and then the program should print the dictionary.

'''

dict_input=raw_input('give me an integer:')
dictionary={}
for dict_input in range(1,int(dict_input)+1):
    dictionary[dict_input]=dict_input*dict_input
print dictionary

###############################

'''
Write a program which accepts a sequence of comma-separated numbers from console and generate
a list and a tuple which contains every number.
'''

input=raw_input()
list=input.split(',')
tpl=tuple(list)
print list
print tpl


################################3
'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

'''

import math
result=[]
C=50
H=30
D=raw_input('provide values of D:').split(',')
values=[i for i in D]
for D in values:
    result.append(int(round(math.sqrt((2*C*float(D))/H))))
print result

##########################################33333

'''
Write a program that accepts a comma separated sequence of words as input and prints the words
in a comma-separated sequence after sorting them alphabetically.
'''

words=[i for i in raw_input().split(",")]
words.sort()
print ",".join(words)

##############################################

'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
'''

capitalized=[]
while True:
    lines=raw_input()
    if lines:
        capitalized.append(lines.upper())
    else:
        break
for x in capitalized:
    print x

######################################################

'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and 
then check whether they are divisible by 5 or not.  
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
'''

numbers=[]
items=[i for i in raw_input().split(",")]
for x in items:
    intb2 = int(x,2)
    if intb2%5 == 0:
        numbers.append(x)

print ",".join(numbers

##########################################

'''
Write a program that accepts a sentence and calculate the number of letters and digits.
'''

count={'letters':0, 'digits':0 }
sentence = raw_input("Provide a sentence:")

for x in sentence:
    if x.isalpha():
        count['letters']+=1
    elif x.isdigit():

##########################################

'''
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
'''

import re
passinput=['123', '12345678', '12345678901112', 'Aa1$','Aaaaaaaaa1$','ABd1234@1', 'aaaaaaaa', 'Aaaaaaaaa']
#passinput=raw_input('enter your password:').split(',')
valid = []
passlist = [n for n in passinput]

for x in passlist:
    if len(x) < 6 or len(x) > 12:  # >6 and <12 req
        continue
    else:
        pass
    if not re.search("[0-9]",x):
        continue
    elif not re.search("[a-z]",x):
        continue
    elif not re.search("[A-Z]",x):
        continue
    elif not re.search("[$#@]",x):
        continue
    else:
        pass
    valid.append(x)
print ",".join(valid)