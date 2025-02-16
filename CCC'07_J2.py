"""
Text messaging using a cell phone is popular among teenagers. The messages can appear peculiar because short forms and symbols are used to abbreviate messages and hence reduce typing.
For example, LOL means "laughing out loud" and :-) is called an emoticon which looks like a happy face (on its side) and it indicates chuckling. This is all quite a mystery to some adults.
Write a program that will continually input a short form and output the translation for an adult using the following translation table:
Short Form
Translation
CU
see you
:-)
I'm happy
:-(
I'm unhappy
;-)
wink
:-P
stick out my tongue
(~.~)
sleepy
TA
totally awesome
CCC
Canadian Computing Competition
CUZ
because
TY
thank-you
YW
you're welcome
TTYL
talk to you later

Input Specification
The user will enter text to be translated one line at a time. When the short form TTYL is entered, the program ends. Users may enter text that is found in the translation table, or they may enter other words. All entered text will be symbols or uppercase letters. There will be no spaces and no quotation marks.
Output Specification
The program will output text immediately after each line of input. If the input is one of the phrases in the translation table, the output will be the translation; if the input does not appear in the table, the output will be the original word. The translation of the last short form entered TTYL should be output.
"""

# Creating a dictionary 
txt_diction = {'CU': 'see you',
     ':-)': "I'm happy",
     ':-(': "I'm unhappy",
     ';-)': 'wink',
     ':-P': 'stick out my tongue',
     '(~.~)': 'sleepy',
     'TA': 'totally awesome',
     'CCC': 'Canadian Computing Competition',
     'CUZ': 'because',
     'TY': 'thank-you',
     "YW": "you're welcome",
     'TTYL': 'talk to you later'} 

# Loops till user is done entering all inputs
while True:
    # Taking user input 
    user = input()
    
    # Mapping key to value and printing its full form out 
    if user in txt_diction:
        print(txt_diction[user])
        if user == "TTYL":
            break
    else:
        print(user)