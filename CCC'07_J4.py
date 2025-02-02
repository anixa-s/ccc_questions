"""
An anagram is a word or a phrase formed by rearranging the letters of another phrase such as ITEM and TIME. 
Anagrams may be several words long such as CS AT WATERLOO and COOL AS WET ART. 
Note that two phrases may be anagrams of each other even if each phrase has a different number of words (as in the previous example). 
Write a program to determine if two phrases are anagrams of each other.

Input Specification
The program should take two phrases, each on a separate line. You may assume that the input only contains uppercase letters and spaces.

Output Specification
The program will print out one of two statements: Is an anagram. or Is not an anagram.
"""

# Taking user inputs 
first = input()
second = input()

# Listfying to check each letter in the string 
first = list(first)
second = list(second) 

# Checking if the two words are anagrams 
index_counter = 0 
for element in first:
    if element in second:
        index_counter += 1 
if index_counter == len(first):
    print("Is an anagram.")
else: 
    print("Is not an anagram.")