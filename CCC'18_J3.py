"""
Canadian Computing Competition: 2018 Stage 1, Junior #3
You decide to go for a very long drive on a very straight road. Along this road are five cities. 
As you travel, you record the distance between each pair of consecutive cities.

You would like to calculate a distance table that indicates the distance between any two of the cities you have encountered.

Input Specification
The first line contains positive integers less than, each representing the distances 
between consecutive pairs of consecutive cities: specifically, the ith integer represents the distance between city i
and city i + 1.

Output Specification
The output should be 5 lines, with the 
ith line (1 <= i <= 5) containing the distance from city i to cities 1, 2, 3, 4, 5 in order, separated by one space.
"""

# Taking user input 
I = input().split()

# Convering the input to integers
I = [int(i) for i in I]
print(I)

# Creating a list to store the distances