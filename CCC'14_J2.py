"""
A vote is held after singer A and singer B compete in the final round of a singing competition. Your job is to count the votes and determine the outcome.
Input Specification
The input will be two lines. The first line will contain V(1≤V≤15), the total number of votes. The second line of input will be a sequence of V characters, each of which will be A or B, representing the votes for a particular singer.
Output Specification
The output will be one of three possibilities:
A, if there are more A votes than B votes;
B, if there are more B votes than A votes;
Tie, if there are an equal number of A votes and B votes.
"""

# Taking user inputs 
num_votes = int(input())
outcome = input()

# Listifying string
outcome = list(outcome)

# Running through each character 
a = 0 
b = 0 
for letter in outcome:
    if letter == "A":
        a += 1
    else:
        b += 1 
if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("Tie")