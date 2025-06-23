"""
CCC '10 J1 - What Is N, Daddy?

Natalie is learning to count on her fingers. When her Daddy tells her the number n (1≤n≤10) she asks "What is n, Daddy?", by which she means "How many fingers should I hold up on each hand so that the total is n?"To make matters simple, her Daddy gives her the correct finger representation according to the following rules:
the number may be represented on one or two hands;
if the number is represented on two hands, the larger number is given first.
For example, if Natalie asks "What is 4, Daddy?", her Dad may reply:
4 is 4.
4 is 3 and 1.
4 is 2 and 2..
Your job is to make sure that Natalie's Daddy gives the correct number of answers.
Input Specification
The input will be a single integer i such that 1≤i≤10.
Output Specification
The output is the number of ways of producing that number on two hands, subject to the rules outlined above.
"""

# Taking user input 
num = int(input())

# Determining possible combinations 
if num == 10:
    print(1)
elif num == 9:
    print(1)
elif num == 8:
    print(2)
elif num == 7:
    print(2) 
elif num == 6:
    print(3)
elif num == 5:
    print(3)
elif num == 4:
    print(3)
elif num == 3:
    print(2)
elif num == 2:
    print(2)
elif num == 1:
    print(1)